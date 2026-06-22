# Parse, don’t validate

## Metadata
- Author: [[lexi-lambda.github.io]]
- Full Title: Parse, don’t validate
- Category: #articles
- Summary: In Haskell, it is better to parse inputs upfront than to validate them later, as parsing catches errors early and keeps the code safe. Strengthening types helps avoid runtime errors and makes programs clearer. People have mixed feelings about Haskell, finding it either powerful and elegant or complex and hard to learn.
- URL: https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate/

## Full Document
Historically, I’ve struggled to find a concise, simple way to explain what it means to practice type-driven design. Too often, when someone asks me “How did you come up with this approach?” I find I can’t give them a satisfying answer. I know it didn’t just come to me in a vision—I have an iterative design process that doesn’t require plucking the “right” approach out of thin air—yet I haven’t been very successful in communicating that process to others.

However, about a month ago, [I was reflecting on Twitter](https://twitter.com/lexi_lambda/status/1182242561655746560) about the differences I experienced parsing JSON in statically- and dynamically-typed languages, and finally, I realized what I was looking for. Now I have a single, snappy slogan that encapsulates what type-driven design means to me, and better yet, it’s only three words long:

**Parse, don’t validate.**

#### The essence of type-driven design

Alright, I’ll confess: unless you already know what type-driven design is, my catchy slogan probably doesn’t mean all that much to you. Fortunately, that’s what the remainder of this blog post is for. I’m going to explain precisely what I mean in gory detail—but first, we need to practice a little wishful thinking.

##### The realm of possibility

One of the wonderful things about static type systems is that they can make it possible, and sometimes even easy, to answer questions like “is it possible to write this function?” For an extreme example, consider the following Haskell type signature:

```
foo :: Integer -> Void
```

Is it possible to implement `foo`? Trivially, the answer is *no*, as `Void` is a type that contains no values, so it’s impossible for *any* function to produce a value of type `Void`.[1](https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate/) That example is pretty boring, but the question gets much more interesting if we choose a more realistic example:

```
head :: [a] -> a
```

This function returns the first element from a list. Is it possible to implement? It certainly doesn’t sound like it does anything very complicated, but if we attempt to implement it, the compiler won’t be satisfied:

```
head :: [a] -> a
head (x:_) = x
```

```
warning: [-Wincomplete-patterns]
    Pattern match(es) are non-exhaustive
    In an equation for ‘head’: Patterns not matched: []

```

This message is helpfully pointing out that our function is *partial*, which is to say it is not defined for all possible inputs. Specifically, it is not defined when the input is `[]`, the empty list. This makes sense, as it isn’t possible to return the first element of a list if the list is empty—there’s no element to return! So, remarkably, we learn this function isn’t possible to implement, either.

##### Turning partial functions total

To someone coming from a dynamically-typed background, this might seem perplexing. If we have a list, we might very well want to get the first element in it. And indeed, the operation of “getting the first element of a list” isn’t impossible in Haskell, it just requires a little extra ceremony. There are two different ways to fix the `head` function, and we’ll start with the simplest one.

###### Managing expectations

As established, `head` is partial because there is no element to return if the list is empty: we’ve made a promise we cannot possibly fulfill. Fortunately, there’s an easy solution to that dilemma: we can weaken our promise. Since we cannot guarantee the caller an element of the list, we’ll have to practice a little expectation management: we’ll do our best return an element if we can, but we reserve the right to return nothing at all. In Haskell, we express this possibility using the `Maybe` type:

```
head :: [a] -> Maybe a
```

This buys us the freedom we need to implement `head`—it allows us to return `Nothing` when we discover we can’t produce a value of type `a` after all:

```
head :: [a] -> Maybe a
head (x:_) = Just x
head []    = Nothing
```

Problem solved, right? For the moment, yes… but this solution has a hidden cost.

Returning `Maybe` is undoubtably convenient when we’re *implementing* `head`. However, it becomes significantly less convenient when we want to actually use it! Since `head` always has the potential to return `Nothing`, the burden falls upon its callers to handle that possibility, and sometimes that passing of the buck can be incredibly frustrating. To see why, consider the following code:

```
getConfigurationDirectories :: IO [FilePath]
getConfigurationDirectories = do
  configDirsString <- getEnv "CONFIG_DIRS"
  let configDirsList = split ',' configDirsString
  when (null configDirsList) $
    throwIO $ userError "CONFIG_DIRS cannot be empty"
  pure configDirsList

main :: IO ()
main = do
  configDirs <- getConfigurationDirectories
  case head configDirs of
    Just cacheDir -> initializeCache cacheDir
    Nothing -> error "should never happen; already checked configDirs is non-empty"
```

When `getConfigurationDirectories` retrieves a list of file paths from the environment, it proactively checks that the list is non-empty. However, when we use `head` in `main` to get the first element of the list, the `Maybe FilePath` result still requires us to handle a `Nothing` case that we know will never happen! This is terribly bad for several reasons:

1. First, it’s just annoying. We already checked that the list is non-empty, why do we have to clutter our code with another redundant check?
2. Second, it has a potential performance cost. Although the cost of the redundant check is trivial in this particular example, one could imagine a more complex scenario where the redundant checks could add up, such as if they were happening in a tight loop.
3. Finally, and worst of all, this code is a bug waiting to happen! What if `getConfigurationDirectories` were modified to stop checking that the list is empty, intentionally or unintentionally? The programmer might not remember to update `main`, and suddenly the “impossible” error becomes not only possible, but probable.

The need for this redundant check has essentially forced us to punch a hole in our type system. If we could statically *prove* the `Nothing` case impossible, then a modification to `getConfigurationDirectories` that stopped checking if the list was empty would invalidate the proof and trigger a compile-time failure. However, as-written, we’re forced to rely on a test suite or manual inspection to catch the bug.

###### Paying it forward

Clearly, our modified version of `head` leaves some things to be desired. Somehow, we’d like it to be smarter: if we already checked that the list was non-empty, `head` should unconditionally return the first element without forcing us to handle the case we know is impossible. How can we do that?

Let’s look at the original (partial) type signature for `head` again:

```
head :: [a] -> a
```

The previous section illustrated that we can turn that partial type signature into a total one by weakening the promise made in the return type. However, since we don’t want to do that, there’s only one thing left that can be changed: the argument type (in this case, `[a]`). Instead of weakening the return type, we can *strengthen* the argument type, eliminating the possibility of `head` ever being called on an empty list in the first place.

To do this, we need a type that represents non-empty lists. Fortunately, the existing `NonEmpty` type from `Data.List.NonEmpty` is exactly that. It has the following definition:

```
data NonEmpty a = a :| [a]
```

Note that `NonEmpty a` is really just a tuple of an `a` and an ordinary, possibly-empty `[a]`. This conveniently models a non-empty list by storing the first element of the list separately from the list’s tail: even if the `[a]` component is `[]`, the `a` component must always be present. This makes `head` completely trivial to implement:[2](https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate/)

```
head :: NonEmpty a -> a
head (x:|_) = x
```

Unlike before, GHC accepts this definition without complaint—this definition is *total*, not partial. We can update our program to use the new implementation:

```
getConfigurationDirectories :: IO (NonEmpty FilePath)
getConfigurationDirectories = do
  configDirsString <- getEnv "CONFIG_DIRS"
  let configDirsList = split ',' configDirsString
  case nonEmpty configDirsList of
    Just nonEmptyConfigDirsList -> pure nonEmptyConfigDirsList
    Nothing -> throwIO $ userError "CONFIG_DIRS cannot be empty"

main :: IO ()
main = do
  configDirs <- getConfigurationDirectories
  initializeCache (head configDirs)
```

Note that the redundant check in `main` is now completely gone! Instead, we perform the check exactly once, in `getConfigurationDirectories`. It constructs a `NonEmpty a` from a `[a]` using the `nonEmpty` function from `Data.List.NonEmpty`, which has the following type:

```
nonEmpty :: [a] -> Maybe (NonEmpty a)
```

The `Maybe` is still there, but this time, we handle the `Nothing` case very early in our program: right in the same place we were already doing the input validation. Once that check has passed, we now have a `NonEmpty FilePath` value, which preserves (in the type system!) the knowledge that the list really is non-empty. Put another way, you can think of a value of type `NonEmpty a` as being like a value of type `[a]`, plus a *proof* that the list is non-empty.

By strengthening the type of the argument to `head` instead of weakening the type of its result, we’ve completely eliminated all the problems from the previous section:

* The code has no redundant checks, so there can’t be any performance overhead.
* Furthermore, if `getConfigurationDirectories` changes to stop checking that the list is non-empty, its return type must change, too. Consequently, `main` will fail to typecheck, alerting us to the problem before we even run the program!

What’s more, it’s trivial to recover the old behavior of `head` from the new one by composing `head` with `nonEmpty`:

```
head' :: [a] -> Maybe a
head' = fmap head . nonEmpty
```

Note that the inverse is *not* true: there is no way to obtain the new version of `head` from the old one. All in all, the second approach is superior on all axes.

##### The power of parsing

You may be wondering what the above example has to do with the title of this blog post. After all, we only examined two different ways to validate that a list was non-empty—no parsing in sight. That interpretation isn’t wrong, but I’d like to propose another perspective: in my mind, the difference between validation and parsing lies almost entirely in how information is preserved. Consider the following pair of functions:

```
validateNonEmpty :: [a] -> IO ()
validateNonEmpty (_:_) = pure ()
validateNonEmpty [] = throwIO $ userError "list cannot be empty"

parseNonEmpty :: [a] -> IO (NonEmpty a)
parseNonEmpty (x:xs) = pure (x:|xs)
parseNonEmpty [] = throwIO $ userError "list cannot be empty"
```

These two functions are nearly identical: they check if the provided list is empty, and if it is, they abort the program with an error message. The difference lies entirely in the return type: `validateNonEmpty` always returns `()`, the type that contains no information, but `parseNonEmpty` returns `NonEmpty a`, a refinement of the input type that preserves the knowledge gained in the type system. Both of these functions check the same thing, but `parseNonEmpty` gives the caller access to the information it learned, while `validateNonEmpty` just throws it away.

These two functions elegantly illustrate two different perspectives on the role of a static type system: `validateNonEmpty` obeys the typechecker well enough, but only `parseNonEmpty` takes full advantage of it. If you see why `parseNonEmpty` is preferable, you understand what I mean by the mantra “parse, don’t validate.” Still, perhaps you are skeptical of `parseNonEmpty`’s name. Is it really *parsing* anything, or is it merely validating its input and returning a result? While the precise definition of what it means to parse or validate something is debatable, I believe `parseNonEmpty` is a bona-fide parser (albeit a particularly simple one).

Consider: what is a parser? Really, a parser is just a function that consumes less-structured input and produces more-structured output. By its very nature, a parser is a partial function—some values in the domain do not correspond to any value in the range—so all parsers must have some notion of failure. Often, the input to a parser is text, but this is by no means a requirement, and `parseNonEmpty` is a perfectly cromulent parser: it parses lists into non-empty lists, signaling failure by terminating the program with an error message.

Under this flexible definition, parsers are an incredibly powerful tool: they allow discharging checks on input up-front, right on the boundary between a program and the outside world, and once those checks have been performed, they never need to be checked again! Haskellers are well-aware of this power, and they use many different types of parsers on a regular basis:

* The [aeson](https://hackage.haskell.org/package/aeson) library provides a `Parser` type that can be used to parse JSON data into domain types.
* Likewise, [optparse-applicative](https://hackage.haskell.org/package/optparse-applicative) provides a set of parser combinators for parsing command-line arguments.
* Database libraries like [persistent](https://hackage.haskell.org/package/persistent) and [postgresql-simple](https://hackage.haskell.org/package/postgresql-simple) have a mechanism for parsing values held in an external data store.
* The [servant](https://hackage.haskell.org/package/servant) ecosystem is built around parsing Haskell datatypes from path components, query parameters, HTTP headers, and more.

The common theme between all these libraries is that they sit on the boundary between your Haskell application and the external world. That world doesn’t speak in product and sum types, but in streams of bytes, so there’s no getting around a need to do some parsing. Doing that parsing up front, before acting on the data, can go a long way toward avoiding many classes of bugs, some of which might even be security vulnerabilities.

One drawback to this approach of parsing everything up front is that it sometimes requires values be parsed long before they are actually used. In a dynamically-typed language, this can make keeping the parsing and processing logic in sync a little tricky without extensive test coverage, much of which can be laborious to maintain. However, with a static type system, the problem becomes marvelously simple, as demonstrated by the `NonEmpty` example above: if the parsing and processing logic go out of sync, the program will fail to even compile.

##### The danger of validation

Hopefully, by this point, you are at least somewhat sold on the idea that parsing is preferable to validation, but you may have lingering doubts. Is validation really so bad if the type system is going to force you to do the necessary checks eventually anyway? Maybe the error reporting will be a little bit worse, but a bit of redundant checking can’t hurt, right?

Unfortunately, it isn’t so simple. Ad-hoc validation leads to a phenomenon that the [language-theoretic security](http://langsec.org) field calls *shotgun parsing*. In the 2016 paper, [The Seven Turrets of Babel: A Taxonomy of LangSec Errors and How to Expunge Them](http://langsec.org/papers/langsec-cwes-secdev2016.pdf), its authors provide the following definition:

> Shotgun parsing is a programming antipattern whereby parsing and input-validating code is mixed with and spread across processing code—throwing a cloud of checks at the input, and hoping, without any systematic justification, that one or another would catch all the “bad” cases. 
> 
> 

They go on to explain the problems inherent to such validation techniques:

> Shotgun parsing necessarily deprives the program of the ability to reject invalid input instead of processing it. Late-discovered errors in an input stream will result in some portion of invalid input having been processed, with the consequence that program state is difficult to accurately predict. 
> 
> 

In other words, a program that does not parse all of its input up front runs the risk of acting upon a valid portion of the input, discovering a different portion is invalid, and suddenly needing to roll back whatever modifications it already executed in order to maintain consistency. Sometimes this is possible—such as rolling back a transaction in an RDBMS—but in general it may not be.

It may not be immediately apparent what shotgun parsing has to do with validation—after all, if you do all your validation up front, you mitigate the risk of shotgun parsing. The problem is that validation-based approaches make it extremely difficult or impossible to determine if everything was actually validated up front or if some of those so-called “impossible” cases might actually happen. The entire program must assume that raising an exception anywhere is not only possible, it’s regularly necessary.

Parsing avoids this problem by stratifying the program into two phases—parsing and execution—where failure due to invalid input can only happen in the first phase. The set of remaining failure modes during execution is minimal by comparison, and they can be handled with the tender care they require.

#### Parsing, not validating, in practice

So far, this blog post has been something of a sales pitch. “You, dear reader, ought to be parsing!” it says, and if I’ve done my job properly, at least some of you are sold. However, even if you understand the “what” and the “why,” you might not feel especially confident about the “how.”

My advice: focus on the datatypes.

Suppose you are writing a function that accepts a list of tuples representing key-value pairs, and you suddenly realize you aren’t sure what to do if the list has duplicate keys. One solution would be to write a function that asserts there aren’t any duplicates in the list:

```
checkNoDuplicateKeys :: (MonadError AppError m, Eq k) => [(k, v)] -> m ()
```

However, this check is fragile: it’s extremely easy to forget. Because its return value is unused, it can always be omitted, and the code that needs it would still typecheck. A better solution is to choose a data structure that disallows duplicate keys by construction, such as a `Map`. Adjust your function’s type signature to accept a `Map` instead of a list of tuples, and implement it as you normally would.

Once you’ve done that, the call site of your new function will likely fail to typecheck, since it is still being passed a list of tuples. If the caller was given the value via one of its arguments, or if it received it from the result of some other function, you can continue updating the type from list to `Map`, all the way up the call chain. Eventually, you will either reach the location the value is created, or you’ll find a place where duplicates actually ought to be allowed. At that point, you can insert a call to a modified version of `checkNoDuplicateKeys`:

```
checkNoDuplicateKeys :: (MonadError AppError m, Eq k) => [(k, v)] -> m (Map k v)
```

Now the check *cannot* be omitted, since its result is actually necessary for the program to proceed!

This hypothetical scenario highlights two simple ideas:

1. **Use a data structure that makes illegal states unrepresentable.** Model your data using the most precise data structure you reasonably can. If ruling out a particular possibility is too hard using the encoding you are currently using, consider alternate encodings that can express the property you care about more easily. Don’t be afraid to refactor.
2. **Push the burden of proof upward as far as possible, but no further.** Get your data into the most precise representation you need as quickly as you can. Ideally, this should happen at the boundary of your system, before *any* of the data is acted upon.[3](https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate/) 

If one particular code branch eventually requires a more precise representation of a piece of data, parse the data into the more precise representation as soon as the branch is selected. Use sum types judiciously to allow your datatypes to reflect and adapt to control flow.

In other words, write functions on the data representation you *wish* you had, not the data representation you are given. The design process then becomes an exercise in bridging the gap, often by working from both ends until they meet somewhere in the middle. Don’t be afraid to iteratively adjust parts of the design as you go, since you may learn something new during the refactoring process!

Here are a handful of additional points of advice, arranged in no particular order:

* **Let your datatypes inform your code, don’t let your code control your datatypes.** Avoid the temptation to just stick a `Bool` in a record somewhere because it’s needed by the function you’re currently writing. Don’t be afraid to refactor code to use the right data representation—the type system will ensure you’ve covered all the places that need changing, and it will likely save you a headache later.
* **Treat functions that return `m ()` with deep suspicion.** Sometimes these are genuinely necessary, as they may perform an imperative effect with no meaningful result, but if the primary purpose of that effect is raising an error, it’s likely there’s a better way.
* **Don’t be afraid to parse data in multiple passes.** Avoiding shotgun parsing just means you shouldn’t act on the input data before it’s fully parsed, not that you can’t use some of the input data to decide how to parse other input data. Plenty of useful parsers are context-sensitive.
* **Avoid denormalized representations of data, *especially* if it’s mutable.** Duplicating the same data in multiple places introduces a trivially representable illegal state: the places getting out of sync. Strive for a single source of truth. 

	+ **Keep denormalized representations of data behind abstraction boundaries.** If denormalization is absolutely necessary, use encapsulation to ensure a small, trusted module holds sole responsibility for keeping the representations in sync.
* **Use abstract datatypes to make validators “look like” parsers.** Sometimes, making an illegal state truly unrepresentable is just plain impractical given the tools Haskell provides, such as ensuring an integer is in a particular range. In that case, use an abstract `newtype` with a smart constructor to “fake” a parser from a validator.

As always, use your best judgement. It probably isn’t worth breaking out [singletons](https://hackage.haskell.org/package/singletons) and refactoring your entire application just to get rid of a single `error "impossible"` call somewhere—just make sure to treat those situations like the radioactive substance they are, and handle them with the appropriate care. If all else fails, at least leave a comment to document the invariant for whoever needs to modify the code next.

#### Recap, reflection, and related reading

That’s all, really. Hopefully this blog post proves that taking advantage of the Haskell type system doesn’t require a PhD, and it doesn’t even require using the latest and greatest of GHC’s shiny new language extensions—though they can certainly sometimes help! Sometimes the biggest obstacle to using Haskell to its fullest is simply being aware what options are available, and unfortunately, one downside of Haskell’s small community is a relative dearth of resources that document design patterns and techniques that have become tribal knowledge.

None of the ideas in this blog post are new. In fact, the core idea—“write total functions”—is conceptually quite simple. Despite that, I find it remarkably challenging to communicate actionable, practicable details about the way I write Haskell code. It’s easy to spend lots of time talking about abstract concepts—many of which are quite valuable!—without communicating anything useful about *process*. My hope is that this is a small step in that direction.

Sadly, I don’t know very many other resources on this particular topic, but I do know of one: I never hesitate to recommend Matt Parson’s fantastic blog post [Type Safety Back and Forth](https://www.parsonsmatt.org/2017/10/11/type_safety_back_and_forth.html). If you want another accessible perspective on these ideas, including another worked example, I’d highly encourage giving it a read. For a significantly more advanced take on many of these ideas, I can also recommend Matt Noonan’s 2018 paper [Ghosts of Departed Proofs](https://kataskeue.com/gdp.pdf), which outlines a handful of techniques for capturing more complex invariants in the type system than I have described here.

As a closing note, I want to say that doing the kind of refactoring described in this blog post is not always easy. The examples I’ve given are simple, but real life is often much less straightforward. Even for those experienced in type-driven design, it can be genuinely difficult to capture certain invariants in the type system, so do not consider it a personal failing if you cannot solve something the way you’d like! Consider the principles in this blog post ideals to strive for, not strict requirements to meet. All that matters is to try.

1. Technically, in Haskell, this ignores “bottoms,” constructions that can inhabit *any* value. These aren’t “real” values (unlike `null` in some other languages)—they’re things like infinite loops or computations that raise exceptions—and in idiomatic Haskell, we usually try to avoid them, so reasoning that pretends they don’t exist still has value. But don’t take my word for it—I’ll let Danielsson et al. convince you that [Fast and Loose Reasoning is Morally Correct](https://www.cs.ox.ac.uk/jeremy.gibbons/publications/fast+loose.pdf). [↩](https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate/)
2. In fact, `Data.List.NonEmpty` already provides a `head` function with this type, but just for the sake of illustration, we’ll reimplement it ourselves. [↩](https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate/)
3. Sometimes it is necessary to perform some kind of authorization before parsing user input to avoid denial of service attacks, but that’s okay: authorization should have a relatively small surface area, and it shouldn’t cause any significant modifications to the state of your system. [↩](https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate/)

  
A stereotype about programmers is that they like to think in black and white. Programmers like things to be good or bad, moral or immoral, responsible or irresponsible. Perhaps there is something romantic in the idea that programmers like to be as binary as the computers they program. Reductionist? Almost certainly, but hey, laugh at yourself a bit: we probably deserve to be made fun of from time to time.

Personally, I have no idea if the trope of the nuance-challenged programmer is accurate, but whether it’s a property of programmers or just humans behind a keyboard, the intensity with which we disagree with one another never ceases to amaze. Ask any group of working programmers what their least favorite programming language is, and there’s a pretty good chance things are going to get heated real fast. Why? What is it about programming that makes us feel so strongly that we are right and others are wrong, even when our experiences contradict those of tens or hundreds of thousands of others?

I think about that question a lot.

#### 2015 called, and they want their dress back

Humans have a knack for caring intensely about the most trivial of things. Name almost anything—cats versus dogs, the appropriate way to fasten a necktie, or even which day of the week comes first—and someone somewhere has probably written an essay about it on an internet forum. It would be easy to throw up our hands and give up trying to understand our peers, as sometimes they seem like aliens from another planet.

However, what interests me is how the littlest things seem to get people the most upset. Few people have shouting matches over the best interpretation of quantum mechanics, but friendships will be tested when someone says they just aren’t that into *Star Wars*. One explanation for this phenomenon is simple accessibility: most people aren’t equipped to understand quantum mechanics well enough to argue about it, but almost anyone can have an opinion on which direction the toilet paper is supposed to go.[1](https://lexi-lambda.github.io/blog/2019/10/19/empathy-and-subjective-experience-in-programming-languages/)

There is truth in that explanation, but personally, I don’t think it’s the whole story. Rather, I think we grow so used to the idea that our experiences are universal that discovering someone else experienced the exact same thing we did yet came to a different conclusion is not just frustrating: it’s incomprehensible.

Take 2015’s phenomenon of “[the dress](https://en.wikipedia.org/wiki/The_dress)” as an example. Some people see black and blue, others white and gold, and frankly, whether you see one or the other has no impact on anything remotely meaningful. How did *this*—something so completely irrelevant—become a cross-cultural phenomenon reported on by major news outlets? My guess: people just aren’t used to the idea that vision—the primary way we sense the world—does not provide us with an objective, universal understanding of reality.

##### When something objective isn’t

Our culture and society works because, in spite of our differences, we’re still all humans. We eat food, we sleep, we like spending time with each other, and we like feeling connected to those around us. So when we watch a movie, and it tickles us in a way that makes us feel good, we can have an awfully hard time understanding how our best friend—who we largely agree with about everything—didn’t like it at all.

The truth, of course, is that very little of what we experience is in any way objective. Yes, we can be pretty confident that basic arithmetic is true anywhere in the universe, and that if we all agree a table is brown it probably is. There are even things we accept as subjective without a second thought, such as the kinds of food people like or the fashions they find attractive. It’s all the in-betweens that are so pernicious! “The dress” was so unbelievable to most people because, nine hundred and ninety nine times out of of a thousand, when two humans look at a picture, they at least mostly agree on the colors contained within. We do not consider that we are seeing different lenses into the same objective reality, we simply think we are perceiving objective truths directly.

In the case of the dress, whether you [heard “yanny” or “laurel,”](https://en.wikipedia.org/wiki/Yanny_or_Laurel) or whether you believe the *Sonic* games were ever any good, subjective disagreement is essentially harmless. But what about when it isn’t? Might incorrect beliefs that our experiences are universal cause genuine harm?

I think the answer is absolutely, unequivocally *yes*.

#### Subjectivity in programming, and in programming languages specifically

Quick question: which is better, functional or imperative programming?

My guess, given the usual subject of my blog, most of my readers would pick the former. However, the actual answer you chose doesn’t matter: my guess is you feel like you have a pretty rational argument to back it up. It certainly isn’t simply a matter of taste… right?

Well, no, I hope not. I don’t think the world is so subjective that we cannot ever advocate for one thing over another—we tried that whole “everything is XML” thing for a while, and I think we agreed it really wasn’t a good idea. But if you truly believe your answer to the above question can be completely objectively justified (as many do), how does one explain the average Hacker News comment thread on just about any post about Haskell?

I generally try not to read Hacker News if I can help it, as I find doing it mostly just makes me angry,[2](https://lexi-lambda.github.io/blog/2019/10/19/empathy-and-subjective-experience-in-programming-languages/) but I did happen to find a link to [a recent discussion](https://news.ycombinator.com/item?id=21282647) on a blog post about using Haskell in production. Let’s take a look at a few comments, shall we?

In a [branch of the discussion](https://news.ycombinator.com/item?id=21284383), one user writes:

> 
> > Haskell is great for business and great in production 
> > 
> > 
> 
> I disagree. It's a beautiful language but it lacks a lot of features to make it useable at scale. And in my experience Haskell engineers are extremely smart but the environment/culture they create makes it difficult to foster team spirit. 
> 
> I've been in 2 companies in the last 4 years who initially used Haskell in production. One has transitioned to Go and the other is rewriting the codebase in Rust. 
> 
> 

The first paragraph is an assertion without many specifics, but it does sound like it could be reasonable. And although the last two sentences are entirely anecdotal, anecdotes are still better than hunches. Let’s see what someone else has to say in response:

> I’ve met some pretty damn solid engineers who started on Haskell and, even at a junior level in other languages, produce an elegant solution far more easily than a senior engineer in that language. You probably wouldn’t put the code in production verbatim but you can very easily see what’s going on and it isn’t haunted by spectre of early abstraction, which IMO is the biggest flaw of OOP at scale. 
> 
> From my naive perspective it’s easy to make classes out of everything, and to hold state and put side-effects everywhere, but you don’t want to deal with the trouble of a monad until you need it. So you have an automatic inclination towards cleaner code when you start functional and move on. 
> 
> 

Also pretty vague and high-level, but also sounds reasonable. If you read either of these comments, and your first inclination was to grow frustrated and start crafting counter-arguments in your head, I encourage you to step outside your feelings momentarily (rational as they may be!) and try your very hardest to interpret them charitably. The discussion continues:

> Haskell gives one plenty of rope to hang himself on complexity. 
> 
> So much that developers develop an aversion to it as deep as fear. It's unavoidable, the ones that didn't develop it are still buried at the working of their first Rube Goldberg machine and unavailable. 
> 
> 

Whether you think it’s accurate or not, there is definitely a perception held by a great many people that Haskell is a very complicated language. Surely at least some of them must have given it an honest shot, so have they just not “seen the light” yet? What do you think they’re missing? Perhaps a followup commenter can help elucidate things:

> Hi, I find that everything people here are complaining about (and they're valid complaints) has also been true of C++. C++ developed a lot of its complexity (particularly 15-20 yrs ago in the template space) after it got popular, so people were already wed to it. 
> 
> […] 
> 
> The C++ community's really gotten good in the last 5 years or so about reigning in the bad impulses and getting people to write clean, clear, efficient code that has reasonable expressiveness. 
> 
> Coming into Haskell from C++, I have the same instincts. Haskell's been a pure pleasure. The benefits are really there, and they're easy to get. You just have to think of the trade-offs. 
> 
> 

That argument seems reasonable, too. Everything in moderation, right? If you disagree, and you think Haskell is just not worth it, what does this person value that you don’t? What are they missing that you see?

##### The unsatisfying subjective reality of programming languages

You can probably see where I’m going with all this. These arguments are not built on hard, refutable facts or rigorous real-world evidence, they’re based in gut feelings and personal preferences. Does that mean they’re wrong, invalid, and worthless, and we should do studies to determine which language allows programmers to ship features the fastest and with the fewest bugs, then all agree to use that?

***No!***

These conversations are subjective because, for better or for worse, humans think in different ways and value different things, and programming languages are the medium in which we express ourselves. To many people who write Haskell (myself included), there is an effervescent joy in modeling a problem with the type system—like capturing something in amber—that others just don’t care about. What’s more, some people clearly loathe Haskell’s significant whitespace and plethora of infix operators, but I’ve never really minded. Is one of us wrong? If so, *why?* Talk about reliability all you want, but the few rigorous numbers we have don’t provide much evidence one way or the other.

While [one commenter](https://news.ycombinator.com/item?id=21284317) in the aforementioned Hacker News thread described Haskell as nothing less than “pain and torture,” [another](https://news.ycombinator.com/item?id=21284540) says they “did some Haskell in production and it was delightful.” People push excuses and rationalizations for these differences constantly—they point out that most people are exposed to imperative programming first, while others retort that Haskell is clearly not very widely used despite being around for an awfully long time—but none of their arguments ever seem to change people’s minds.

Often, people walk away from these conversations confused and incensed. To them, their point of view is so obviously apparent that it is hard to fathom anyone else seeing things differently. They rack their brains trying to figure out why their opponents just don’t *get it.* There must be some key point they’ve misunderstood, some joy they haven’t experienced, some sharp edge they haven’t yet been cut by. But no matter how much time they spend trying to reach these people, somehow, it’s never enough.

##### Empathy, and how bad results come from good intentions

I’ll admit that these kinds of discussions aren’t *always* fruitless; sometimes they really do manage to change people’s minds or help them see some new idea they had not been able to grasp. When people manage to keep their cool and acknowledge the differences in their mindsets while still helping people learn, everyone benefits.

Sadly, in my experience, this rarely happens. We have a natural tendency to become angry if people don’t see things the way we do; it’s confusing and disorienting, and it can even disgust us. None of those emotions are conducive to empathy. When we fail to account for the ways in which others might think differently, we voluntarily reject any insights we might have otherwise gained from the conversation because we did not allow ourselves to embrace, even just temporarily, someone else’s strange and perhaps uncomfortable set of values and experiences. We refuse to accept that our perception of color might not be as universal as we thought, and we miss out on the amazing insights we could learn about the nature of light, color, and human vision.

Although failing to empathize with those we are arguing with is bad enough, in my mind, this failure to accept the potential subjectivity of one’s own views has even worse, indirect effects. Take this comment for example, again from the same thread:

> Sounds like you've barely programmed in Haskell and don't know what you're talking about. Haskell was the first language I learned. I didn't think this at all and I still don't. It doesn't strike me as any more difficult than learning Java or something. 
> 
> 

I have no doubts that this commenter meant what they said: they didn’t find Haskell difficult to learn. The comment they were replying to was vitriolic and combative, so one could almost feel they had a smackdown coming to them… but this isn’t a private conversation. How do you think someone feels when they are learning Haskell, scroll through this thread, and find a comment that tells them they ought to find it easy? If they’ve been struggling, even a little bit, what do you think they might think?

If I were in their place, I might feel a little stupid. I might wonder if I’m really cut out for Haskell or if I should just give up. I definitely wouldn’t feel encouraged and excited to keep trying.

Who knows why this commenter found Haskell straightforward. Maybe they were exposed to certain concepts already, maybe it just fit their style of thinking, perhaps they’re even exceptionally smart. I don’t know. But no matter what the answer is, insulting the intelligence of others, even indirectly in this way, belies a lack of empathy in the face of frustration, and although the intent may not have been to hurt, it can still be seriously harmful.

To be clear, I’m not saying the commenter should have pretended their experiences were different or even kept them to themselves. I don’t believe in being “fake nice”—in my experience, I am best equipped to reach people when speaking genuinely, from the heart. What I would have done is tell my story in a different way, perhaps by writing something like this:

> It’s true that a lot of people find Haskell challenging, and I totally accept that some people just don’t think it’s worth it. It’s fine if you don’t want to write Haskell. But personally, I really enjoy writing it, as do the people I work with, and I think we ship great software with it because it aligns naturally—even joyfully!—with the way we like to think about program construction. 
> 
> Personally, I didn’t find Haskell as challenging to learn as I think some people have, but it was still work, and in some ways I was just exposed to it at the right time. Other people I know have struggled quite a lot at first, and reasonably so, but they’ve still managed to become great Haskell programmers, and they found it worthwhile. Our team dynamic just wouldn’t be the same in any other language. 
> 
> 

When I respond to comments I disagree with, I try to tell a personal story that provides a different perspective **without** invalidating their experiences. Sometimes the result is ungrateful snark anyway (or just no response at all), but you might be surprised how often talking from an emotional place about *your own* experiences—while being neither aggressive nor especially defensive—can go a long way. Perhaps you can even learn something if they return the favor and explain what they find frustrating, beyond the fundamental, subjective disagreements.

It’s okay to have opinions. It’s okay to like and dislike things. It’s okay to be frustrated that others don’t see things the way you do, and to advocate for the technologies and values you believe in. It’s just not okay to tell someone else their reality is wrong.

Learn to embrace the subjective differences between us all, and you won’t just be kinder. You’ll be *happier.*

1. This is where I’m supposed to put a snarky footnote saying something like “obviously, the correct way is *blah*,” but you deserve better. So you, uh, get a *meta* snarky footnote instead. [↩](https://lexi-lambda.github.io/blog/2019/10/19/empathy-and-subjective-experience-in-programming-languages/)
2. Which, to be entirely fair, may well be as subjective as anything else in this blog post. [↩](https://lexi-lambda.github.io/blog/2019/10/19/empathy-and-subjective-experience-in-programming-languages/)
