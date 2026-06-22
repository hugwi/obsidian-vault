---
title: "Yann LeCun's Billion Dollar Bet"
source: "https://m.youtube.com/watch?v=kYkIdXwW2AE"
author: "Welch Labs"
published: 2026-05-01
created: 2026-05-03
description: "Apply to join Hudson River Trading: https://www.hudsonrivertrading.com/welchlabs"
tags:
  - to-process
  - llm-foundations
---

Okay, then let me make a controversial statement that again is going to get me a lot of friends in SQL. Um, >> AI legend Yan Lun has raised a billion dollars to pursue an alternative approach to AI. Unlike large language models, Lacun's approach is not rooted in language and is not generative. By design, it does not spit out text, images or videos. Instead, Lacun has proposed Jeepa. Jeppa is not a single AI model, but instead an alternative 

architecture or framework for training AI models. Many successful approaches in AI and machine learning train models to predict some output Y given some input X. Large language models are given some input text X and trained to predict the text Y that comes next. Image classifier models are given an input image X and trained to predict the corresponding label Y. Jeepa does not work like this. Instead, our inputs X and outputs Y are each passed into models known as 

encoders. These encoders return a vector or matrix of numbers, often referred to as an embedding. From here, a third model known as a predictor is trained to predict the embedding of Y given the embedding of X. Why might this be a better way to build AI systems? Do you think that Jeepa or world model based approaches, do you think they'll replace LLMs one day or are they kind of solving different problems? Initially they'll solve different problems. >> Eventually they're replaced LLM okay 

because you know LLMs are really good at manipulating language but basically nothing else. >> They're really good in domains where the language itself is the substrate of reasoning >> compared to the mainline generative language approach to AI. Jeepa lives on an alternative path of joint embedding architectures. Interestingly, Lacun played a significant role at the outset of both paths. In part one of this two-part series, we'll explore this alternative 

path to Jeepa. We'll dig into why Yan moved away from generative architectures just as they were gaining traction in language and explore Yan's epiphany for a new solution to the representation collapse problem that plagued joint embedding architectures for years. Finally, we'll dig into the Jeepa architecture itself. In part two, we'll dive into JEPA implementations and see exactly how these models stack up against LLM driven approaches. 

Yan Lun saw the revolution coming in the 1980s. While most of the AI field was busy building expert systems that were explicitly programmed instead of learned from data, Jan pioneered the convolutional neural network. 25 years later, when deep learning began its rise to its now dominant position in AI, the breakthrough deep learning model AlexNet turned out to be uncannily similar to Lacun's convolutional nets from the 1990s. 

However, as deep learning continued to pick up steam through the 2010s, Lacun and other researchers became increasingly concerned by just how much this approach to AI depended on labeled training data. AlexNet was trained on the enormous and meticulously labeled imageet data set using supervised learning where AlexNet was trained to match the labels assigned to each image by human annotators. In contrast, children are able to learn very general representations for concepts like dog with very few explicitly labeled examples. 

As manually labeled data became a bottleneck for supervised learning, interest grew in alternative approaches. Reinforcement learning, where models learn from interacting with their environments instead of from labeled data, experienced a many renaissance in the mid2010s, highlighted by Google DeepMind's breakthrough performance on Atari games and the highly complex board game Go. Concurrently, Lacun and others explored unsupervised methods that learn from 

data without labels, including a variant called self-supervised learning, where the labels are taken from the data itself. Starting in 2015 or so, I started showing a slide that has become a bit of a meme in the machine learning community where I said like, you know, if it's the cake slide, right? So, if uh intelligence is a cake, the bulk of the cake is self-s supervised learning, the icing on the cake, supervised learning, and the chair on the cake, reinforcement learning. At the time, people were kind of crazy about reinforcement learning. So I was trying to tell them like this 

is not never going to you know take us to you know anywhere close to human or animal intelligence because it's too inefficient. Um and uh turns out the success of self-s supervised learning uh you know happened in in text and and language much faster than it did in sort of more uh you know natural uh modalities like uh like vision. Here Jan is referring to the success of next token prediction for training large 

language models. OpenAI was founded in 2015 and initially focused their efforts on reinforcement learning creating OpenAI Gym and Universe and showing very impressive performance on complex video games. While much of the company was focused on reinforcement learning, Ilia Sutskever, Alec Radford and others became interested in a new neural network architecture from Google, the transformer. Initially designed for language translation, while experimenting, Radford tried an 

interesting modification. Instead of having the transformer translate from a block of text in one language to a block of text in another language, he switched to a simpler self-supervised approach where training text is broken into sequences and the transformer is given all but the last little piece of text known as a token in each sequence and trained to predict what this final token will be. Ratford and his OpenAI colleagues trained their transformer on a fairly large internal OpenAI data set of 7,000 

books. Note that we now call this phase pre-training and then further train their model using standard supervised learning from human generated labels on specific language tasks. Their two-stage training approach worked well, setting new state-of-the-art results on nine language benchmarks, including tasks like high school level reading comprehension questions, outperforming architectures and methods that were individually designed and trained for each individual task. Radford's model is now known as 

generative pre-trained transformer 1 or GPT1. GPT1 didn't receive much public attention at the time, but was a huge unlock, breaking models free from their dependence on humanlabeled data and opening up unprecedented levels of scale. Other researchers at OpenAI quickly grasp the significance of Radford's results and the team went allin on this approach, aggressively scaling up to GPT2 in 2019, GPT3 in 2020, and Chat GPT 

in 2022. In 2012, AlexNet was trained on around a million examples. In 2020, GPT3 was trained on hundreds of billions of examples. And interestingly, the new training paradigm that emerged exactly matched Yon Lacun's predictions from a few years earlier. An extensive self-supervised pre-training phase followed by supervised learning and finally reinforcement learning to shape the raw next token predictor model into 

a helpful AI assistant. However, while these self-supervised generative approaches clearly broke through in language, the picture was much fuzzier for image and video data. But I I I kept working on vision and then initially uh the the uh idea was to use um so to train a system to predict what happens in video but to use uh generative architectures. Um so basically train at a pixel level what's going to happen in the video. Years 

before the success of GPT1, researchers including Lacun had tried to apply the same self-supervised generative approach to video. In the most straightforward implementation, we configure our neural network to take in the RGB pixel values from a sequence of video frames and then predict the pixel values in the next frame just as the GPT models are trained to predict the next token in language. However, when we use these models to predict the next frame, the results are blurry. And this blurriness compounds 

dramatically in longer horizon predictions. Large language models are auto reggressive. When chat GPT answers a question, it generates one token at a time. At each step, feeding its latest generated token back into its input to create the next output. If we try this auto reggressive approach with a next frame video prediction model, the results quickly devolve into blurry nothingness. Before we see exactly how JEA is able to get around this blurry prediction problem, let's look at another 

fascinating application of transformers beyond language models. This video is sponsored by Hudson River Trading, and this is an order book. The left column shows all the bids to buy Nvidia stock ranked by bid price, and the right column shows all the current offers to sell Nvidia stock ranked by asking price. On a busy trading day, on the order of 1,000 new buy and sell orders like this come in every second. This deluge of orders is an incredibly rich 

information source. Is it possible to train a transformer like the ones used in VJA to find patterns in this data and use these patterns to predict future prices? Hudson River Trading has trillions of tokens of historical data. This is the same order of magnitude of training data used to train Frontier LLMs. and their researchers are working to push the frontiers of machine learning on this data. The VJEPA model we'll see later in the video maps patches of videos to 

individual embedding vectors. We could take a similar approach with order book data tokenizing groups of orders using some financial intuition. However, this naive approach does not work well in practice, and the Hudson River trading team has developed some really interesting approaches to adapt cutting edge transformer architectures to the complexities and constraints of trading data. And all of this is happening in a setting where speed is everything. Models have to run under incredibly tight latency constraints. 

These fascinating and highly complex research and engineering challenges combined with the resources to actually tackle them and an open, highly collaborative environment make Hudson River Trading an incredibly unique place to work. I hear a lot from potential sponsors these days and have been seriously impressed in my interactions with the Hudson River Trading team. The level of technical discussion and enthusiasm for these deep and interesting problems is unparalleled in my experience. If this sounds interesting, Hudson River Trading is 

currently hiring for AI researchers, algorithm developers, and software engineers. They're hiring globally, and you don't need a finance background. You can learn more at hudson rivertrading.com/welchlabs. Now, back to Jeepa. Now, the blurry frames produced by our generative video prediction approach are not some huge mystery. Language is complex and unpredictable, but it's nothing compared to video. Language models use fixedsiz vocabularies. 

GPT2 has 50,257 discrete outputs, one for each token that the model could say next. This complete enumeration approach is hopeless in video. For full HD video, in the most general case, each pixel can take on 256 discrete values. And we have 1920 \* 1080 \* 3 color pixels. Meaning there are something like 10 to the power of 15 million possible next video frames 

dwarfing the number of atoms in the observable universe. So there's no way our video prediction model can have a discrete output for each possible next video frame as our language model has a discrete output for each next possible token. Instead, many generative video approaches of this era had the network directly output pixel intensity values. The big challenge with this approach is how the model learns to handle uncertainty. If we compare an LLM learning to complete the sentence, the ball bounced 

to the and a neural network predicting the next frame of a video of a ball actually bouncing, we can see exactly what goes wrong. In the LLM training case, the model will see various examples in its training set of the ball bouncing left and right. And since the model has separate outputs for each of these tokens, it can essentially independently update these probabilities. Our video model doesn't have it so easy. If our data set includes videos of the ball starting down the same path and 

then bouncing in various directions, since our model is forced to directly predict a single output frame for a given input, the best it can do in the face of this ambiguity is to predict the average of these outcomes. When we average the pixel values of our videos, we end up with a blurry, washed out mess. Now, this is only the most naive approach, and there have been many, many interesting video and image prediction strategies tried with various degrees of success over the last couple decades. 

However, the challenges that naturally arise led Lun and other researchers to ask an interesting question. Do our models really need to be generative? In our GPT example, during the crucial pre-training phase, it really doesn't matter that our model is generative. After pre-training on next token prediction, we're left with a model that's essentially a really good autocomplete. But this is not the point. What actually matters are the internal representations 

and features that the model learns to solve the next token prediction task. These learned internal representations are what allows pre-trained models to be quickly adapted into powerful AI assistance. Next token prediction on language is a proxy for intelligence that has turned out to work shockingly well. But are there other signals and methods that we can use to learn these powerful internal representations that we need to build intelligent systems? 

Simultaneously we started realizing in the you know around 2017 18 that uh the the best system to learn representations of images are systems that do not are not generative. They don't reconstruct they they you know you you you get an image and you run it to an encoder and then you try to kind of coers this encoder to extract as much information as possible with certain properties. So for example, you 

take two images of the same scene or you take an image and you corrupt it or transform it in some ways. You run them both through encoders and you tell the system the representation whatever you extract to really be the same for those two images because they semantically represent the same thing. Um and I've been working on things like this since the '9s. So this is not a new idea. This this idea joint embedding we used to call this Siamese neural net. The method Yan is referring to here, Siamese networks, was created by Yan and his collaborators at Bell Labs in the early 

1990s when developing systems to detect fraudulent signatures. The system worked by passing a pair of signature images into two copies of the same neural network. The network copies were not trained to generate any kind of data. Instead, they output vectors of numbers, often referred to as embedding vectors. These network copies were trained on two types of examples. Positive examples that contain a reference signature and a nonfraudulent signature. So these are by the same 

person. And negative examples that contain a reference signature and a fraudulent signature. For fraudulent examples, the network copies are trained to produce embedding vectors that are maximally different. And for positive examples, produce embedding vectors that are maximally similar. When a new signature comes along, we can pass it into our network to comput an embedding vector and compare it to the embedding vector produced from our reference signature. If the resulting embedding vectors are not similar 

enough, the signature is detected as fraudulent. By jointly embedding our signatures, our Siamese network learns a very useful internal representation of the images of our signatures, notably without learning to predict or generate any actual signature images. As a GPT-based approach would joint embeddings offer a potentially viable solution to our blurry video problem. As Yan explains, >> you you get an image and you run it to an encoder and then you try to kind of 

coers this encoder to extract as much information as possible with certain properties. So for example, you take two images of the same scene or you take an image and you corrupt it or transform it in some ways. You run them both through encoders and you tell the system the representation whatever you extract should really be the same for those two images because they semantically represent the same thing. So the idea here is that we sidestep the blurry video problem we saw with generative models by using a joint embedding architecture to map copies of images or 

videos with one or both corrupted or transformed to similar embedding vectors. This trained model will ideally learn a useful internal representation of images or video that we can repurpose for other tasks just as GPT models learn internal representations during pre-training that can be adapted into AI assistant behaviors. However, this joint embedding strategy has a huge problem. Since we're training our network to make the embeddings of 

our original and corrupted images or videos as similar as possible, the network can find a trivial solution where it simply returns the same embedding vector for any input that we pass in. If our network learns to output, for example, a vector of all ones for any input, then the network will return all ones for a corrupted and non-corrupted view of the same image, maximizing the resulting similarity, but without actually learning anything useful. This problem is known as representation 

collapse. In Lacun's original Siamese network approach, the team used what's now known as contrastive learning to avoid representation collapse, giving the network both positive and negative examples. It turns out we can apply the same contrastive approach to images and video, training our network to output similar embeddings for views of the same underlying images or videos and dissimilar embeddings for different images or video. These contrastive methods have been successfully implemented on images and videos, but 

can run into issues when they're scaled up, requiring large amounts of computation and many negative examples to learn meaningful representations. and Lacun has argued that in the worst case, the number of contrastive samples may grow exponentially with the dimension of the representation. By the end of the 2010s, it was clear to Lun and others that using generative models to fully reconstruct images and video was not a good strategy for self-supervised learning. But there 

wasn't a straightforward solution to the representation collapse problem that would allow joint embedding architectures to learn the same level of powerful and general internal representations that large language models were enjoying. >> And so it was pretty clear that reconstruction was a bad idea for uh signals like like images and >> a fortory for video. And I had a bit of an epiphany because uh the uh the the methods that we were 

using to train those joint emitting architectures were kind of hacks a little bit until um I did some work with a couple postocs at at Meta particular guy called Stefan Deni who uh came up with a technique called Ballot twin. So it it's based on an old idea in uh in computational noise science in machine learning that Jeffington also played on with similar ideas which is that you you should have time to have some measure of information content and try to maximize 

that and there's some real world work by uh by Barlo about is a famous computational neuroscientist and right >> theoretical neuroscientist >> here Jan is referencing the work of Horus Barlo who hypothesized in 1961 one that the neurons in animal and human vision systems operate by reducing redundant information between neurons. Stefan Deni a postto lacun was working with in 2020 was familiar with Barlo's 

work and proposed that one way to avoid representation collapse could be to apply Barlo's idea to the outputs of their networks. In the joint embedding architectures we've been considering, our embedding vectors are produced by a final layer of artificial neurons in our embedding networks. So if our embedding vectors are of length 128, then the output layer of each of our networks contains 128 neurons. If we pass in a batch of various images into each of our networks and plot the 

output activation of the first neuron as we step through our images, we can see that this neuron fires strongly on this first picture of a dog, not so much on this cat picture, and so on. Following our joint embedding approach, our network takes in a distorted view of the same batch of images. The whole point of our joint embedding architecture is to make the resulting embeddings of the same underlying images or videos similar. So we want the output of our first neuron in our second 

network to be similar to the output of our first neuron in our first network. In a standard joint embedding architecture, we would simply measure and maximize the similarity between these two vectors. However, as we've seen, this approach is susceptible to representation collapse. With the network simply learning to output the same values for any input image. But now applying Barllo's hypothesis as proposed by Stefan Deni, we should reduce the redundancy between the outputs of different neurons. 

We have a bit of a choice to make here. We could compare the output of the first neuron in our first network to the output of our second neuron in our first network or to the output of the second neuron in our second network. The team chose to compare to the output of the second network. As we'll see, this results in a simpler implementation and the team further notes in the appendex of their paper that in practice they didn't see much difference between these alternatives. Here's the output of the second neuron in our second model. To measure the 

redundancy between neuron outputs, the team computed the crossorrelation between these output vectors. This computation consists of scaling each vector and taking the dotproduct resulting in a single number, the correlation or more precisely the Pearson correlation coefficient between our vectors. To reduce the redundancy between our neurons as proposed by Barlo, we want this correlation to be close to zero. If we arrange the neuron outputs of our first encoder vertically 

and the outputs of our second encoder horizontally, we can compute and place the correlations between all pairs of neurons into a single matrix. This crossorrelation matrix has one row for each output neuron in our first encoder and one column for each output neuron in our second encoder. The elements along the diagonal capture the correlations between corresponding neurons. Since the whole idea here of this joint embedding architecture is to produce similar outputs for distorted versions of the same image, we want the 

corresponding neurons in our two encoders to have high correlations. Alternatively, all of the off diagonal entries in our crossorrelation matrix correspond to different neurons in our two encoders. And following Barlo's hypothesis, we want to reduce the redundancy between these neurons. So we want these correlations to be zero. So ideally our crossorrelation matrix looks like the identity matrix. Deni lacun and their collaborators 

designed a new loss function for their joint embedding architecture that measured the deviation of their crossorrelation matrix from the identity matrix. Their new method which they called barlo twins worked surprisingly well avoiding representation collapse while learning a powerful internal representation of the images that it was trained on. The team used a few different methods to measure the quality of these internal representations. Earlier, we saw how by using 

self-supervised pre-training, GPT1 was able to outperform purely supervised models that had been adapted to specific language tasks. For vision tasks, one of the most important benchmarks at the time was accuracy on the imageet data set. This is the same image classification data set that the AlexNet model had shown breakthrough performance on back in 2012. The original AlexNet paper achieved an accuracy of 59.3% on the imagenet validation set. To compare the 

self-supervised Barlo twins approach to fully supervised models like AlexNet, the team used a common approach known as a linear probe where a single layer of neurons are tacked onto the output of the Barllo twins trained encoder model and trained using supervised learning to classify the imageet data set. Importantly, the main encoder model is frozen during this training process. So the simple linear probe is effectively adapting the Barlo twins 

encoders learned representation to solve the imageet classification task. Impressively, the frozen Barlo twins encoder with a linear probe achieved an imageet accuracy of 73.2%. Outperforming the original fully supervised AlexNet model by over 10 percentage points. However, in the nine years from the AlexNet paper in 2012 to the Barlo twins paper in 2021, fully supervised approaches had made significant improvements over AlexNet. 

In 2020, a team at Google applied the transformer architecture to image classification, achieving a new state-of-the-art imageet accuracy of 88.6%. So by 2021, thanks to the Barlo twins epiphany and other joint embedding approaches, self-supervised learning was advancing rapidly for vision tasks, but was still inferior to fully supervised methods. The general and clearly superior self-supervised generative pre-training methods in language that 

were fueling the rapid advancement of LLMs were still out of reach for image and video applications. And so it became clear that this really was the the right way to go. So we kind of uh after that published another version a simplified version basically of battle twins called vicrag which turned out to be quite good. uh and then simultaneously another group some of our colleagues at fair paris were working on uh uh similar methods which eventually came to be 

known as dino uh dino v1 v2 v3 now have a new version which is not called dino anymore uh and and this is also a jetting uh technique so so it's really clear john embedding was better for represent learning you know right >> self-supervised learning to to represent images. >> The Dino V3 paper released in August 2025 marked an important turning point 

achieving a very near state-of-the-art image at accuracy of 88.4% using a joint embedding architecture. As the authors say in their paper, all in all, this is the first time that a self-supervised model has reached comparable results to weekly and supervised models on image classification. The quality of representations that Dino V3 is able to learn without access to any human generated labels is astounding. Dino outputs an embedding vector for each patch of image that it 

analyzes. If I take this image of myself and take Dino's embedding vector from this image patch on my hand and compare this embedding vector to the rest of the patches in the image, visualizing how similar each patch is to the hand patch using a color map. Dino does a remarkably good job segmenting my hand from the background. Here's the same approach applied to a ball, a cat, and a book. Following the success of Barlo twins 

Vicreg and Dinov1, in 2022, Lun brought these and many other threads together into a 60-page position paper called a path towards autonomous machine intelligence. Unlike the great majority of Lun's papers where he works on specific and technical pieces of machine learning theory or practice, a path towards autonomous machine intelligence takes a holistic first principles approach to how we should build intelligent machines. Lun begins by arguing that our current approaches to 

AI are nowhere near the capabilities of human learning, giving the example of a teenager that can learn to drive a car in around 20 hours of practice. How is it that we have those millions of hours of training data where we have we can train kind of level two system with it which is what Tesla is doing basically. >> Yeah. >> Um but >> nowhere near level three, four, five. Okay. Uh yet a 17-year-old can learn to drive in a few hours of practice. Like how does that happen, right? Shouldn't 

we figure out what the what's the secret there? >> And my guess about it is the secret is role models. Lacun's billion-dollar bet is that the missing piece of modern AI is world models. Models that make predictions about the physical world. As he says in his 2022 position paper, common sense can be seen as a collection of models of the world that can tell an agent what is likely, what is plausible, and what is impossible. Using such world models, animals can learn new skills 

with very few trials. They can predict the consequences of their actions. They can reason, plan, explore, and imagine new solutions to problems. Lun goes on to argue that joint embedding architectures offer the right foundation to build world models on top of. >> So, JPA means joint embedding predictive architecture and it's you you take an observation in the world and then the next observation in the world. Uh you run them through encoders. So this is like a joint embedding type architecture 

and then you have a predictor that tries to predict that the state at time t plus one from the state at time t and you might condition this on an action and now you have a world model >> as a concrete example instead of using a generative architecture to predict the pixel values in the next frame of video. We can map the video and next frame to embeddings and then train a predictor model to predict the embedding of the next frame given the embedding of the video. In this implementation, the JEPA architecture frees the model of the 

intractable task of predicting every pixel in the next frame of video and theoretically allows the predictor to focus on predicting only the salient features of the scene that make it through the encoder. Jan gives a nice example here. If you train a geology model, you know, to predict what's going to happen in a dash cam video, uh, it will spend most of its resources predicting the random motion of the leaves on the trees that bord bordering the road and and those are things that are essentially not predictable, but they have a lot of pixels, you know, 

that move around. >> As Jan mentioned earlier, we can take Jeepo one step further by conditioning on actions. In the VJEPA 2 paper, which we'll dig into in part two, the team conditions a JEPA model on the action signals sent to a robot arm. So, the JEPA model sees a sequence of images of the robot's arm and environment and then is trained to predict the embedding of the next video frame, but is also given the control signals that are sent to the robot arm. This allows the predictor to 

learn to predict how various control signals will change the robot arm's position in the embedded image. This learned world model can then be used for robot planning and control. Given an image of some goal state, for example, moving a cup off of a platform, this image is passed into the next frame encoder, resulting in an embedding of the goal state of the robot. From here, a controls algorithm can be used to explore the world model's predictions given various hypothetical actions and 

find a set of actions that will lead the model's predicted future state to match its goal state. As Jan says, this is really a new twist on an old idea. >> You build a model that gives you the state of the world at time t plus one as a function of the state of the world at time t and an action you imagine taking or intervention or control, right? And then if you have this you can uh predict the outcome of a sequence of actions and you can by optimization you can figure out an optimal sequence of actions to 

arrive at a particular um outcome. Right? This is classical optimal control. This is you know this is going back to the late 50s in the Soviet Union early 60s in the in the west. >> Very classical stuff. >> Yeah. >> What is not classical is you learn the model. You use machine learning to learn the model. >> Right. Yeah, >> what is even less classical is you learn a representation of the input that computes a state an abstract state representation and you learn the you 

know the the model in that uh in that state and that's JPA but will Jeepa or other world model based approaches really overtake large language models since lacun first proposed Jeppa in 2022 the architecture has been applied by various teams to a wide range of problems. How exactly do these models stack up? In part two, we'll dive deeper into VJeppa 2 to get a sense for what's really 

happening inside the models embedding space and see how VJA 2 fares as a robotics control algorithm against rapidly advancing VLA approaches. We'll also explore VLJA which solves many of the same vision language problems we solve today with multimodal LLMs but in a very different way and with impressive results. Finally, we'll spend some time on an implementation of Jeepa called layworld model. Layworld model gives perhaps the most complete 

albeit early picture of what Jeepa based systems can do. Until next time, I'll leave you with Yan's take. Okay, then let me make a controversial statement that again is going to get me a lot of friends in Silicon Valley. Um, I do not understand how you can even think of building an agentic system without a agentic system having the ability of predicting the consequences of its actions. >> Okay? And a VA doesn't doesn't do that. 

>> Sure. >> Right. Airlines do not have world models. They cannot predict the consequences of their actions beforehand. they just take the action and then deluj as uh you know as some famous French kings said. So uh if you really want to build reliable agentic systems, they absolutely have to be able to predict the consequences of their actions so that they can plan a sequence of actions to do something first of all to uh fulfill the task that they are 

being asked to fulfill but also uh perhaps to you know guarantee some safety guard rails. Sure. >> Right. >> And the inference process now becomes a search as opposed to just an autogressive prediction. >> Right. Uh, so that's a world model. That the whole idea of a world model. >> If you enjoyed this video, check out the Welch Labs illustrated guide to AI. Its cover produces highly consistent Dino representations, so you know it has to be good. The book is beautifully 

illustrated and is a great way to dig deeper into many of the topics we touched on in this video. Chapter 5 on Alexnet is a great way to learn more about embedding vectors and the rise of deep learning. Chapter six on neural scaling laws takes a deeper look at the fascinating buildup from GPT1 to GPT3 at OpenAI. Chapter 9 covers diffusion models which are able to reconstruct highly accurate pixel level representations of images and video but with some notable 

trade-offs. Chapters 1 through 4 give some great background on all these topics covering the fundamentals of neural networks back propagation and deep learning. Each chapter includes thought-provoking exercises and supporting code. The book is now shipping to 24 countries. You can pick up a copy today at welchlabs.com. 

<p>
 <span data-rw-start="0.24" data-rw-transcript-version="2">
 Okay, then let me make a controversial
 </span>
 <span data-rw-start="2.72" data-rw-transcript-version="2">
 statement that again is going to get me
 </span>
 <span data-rw-start="4.72" data-rw-transcript-version="2">
 a lot of friends in SQL. Um,
 </span>
 <span data-rw-start="6.879" data-rw-transcript-version="2">
 &gt;&gt; AI legend Yan Lun has raised a billion
 </span>
 <span data-rw-start="9.519" data-rw-transcript-version="2">
 dollars to pursue an alternative
 </span>
 <span data-rw-start="11.519" data-rw-transcript-version="2">
 approach to AI. Unlike large language
 </span>
 <span data-rw-start="14.559" data-rw-transcript-version="2">
 models, Lacun's approach is not rooted
 </span>
 <span data-rw-start="17.279" data-rw-transcript-version="2">
 in language and is not generative. By
 </span>
 <span data-rw-start="20.56" data-rw-transcript-version="2">
 design, it does not spit out text,
 </span>
 <span data-rw-start="22.24" data-rw-transcript-version="2">
 images or videos. Instead, Lacun has
 </span>
 <span data-rw-start="25.279" data-rw-transcript-version="2">
 proposed Jeepa. Jeppa is not a single AI
 </span>
 <span data-rw-start="28.8" data-rw-transcript-version="2">
 model, but instead an alternative
 </span>
 <span data-rw-start="30.64" data-rw-transcript-version="2">
 architecture or framework for training
 </span>
 <span data-rw-start="32.559" data-rw-transcript-version="2">
 AI models. Many successful approaches in
 </span>
</p>
<p>
 <span data-rw-start="35.68" data-rw-transcript-version="2">
 AI and machine learning train models to
 </span>
 <span data-rw-start="37.6" data-rw-transcript-version="2">
 predict some output Y given some input
 </span>
 <span data-rw-start="39.84" data-rw-transcript-version="2">
 X. Large language models are given some
 </span>
 <span data-rw-start="42.399" data-rw-transcript-version="2">
 input text X and trained to predict the
 </span>
 <span data-rw-start="44.8" data-rw-transcript-version="2">
 text Y that comes next. Image classifier
 </span>
 <span data-rw-start="48.079" data-rw-transcript-version="2">
 models are given an input image X and
 </span>
 <span data-rw-start="50.32" data-rw-transcript-version="2">
 trained to predict the corresponding
 </span>
 <span data-rw-start="51.68" data-rw-transcript-version="2">
 label Y. Jeepa does not work like this.
 </span>
 <span data-rw-start="56.079" data-rw-transcript-version="2">
 Instead, our inputs X and outputs Y are
 </span>
 <span data-rw-start="58.399" data-rw-transcript-version="2">
 each passed into models known as
 </span>
 <span data-rw-start="60.079" data-rw-transcript-version="2">
 encoders. These encoders return a vector
 </span>
 <span data-rw-start="62.8" data-rw-transcript-version="2">
 Or matrix of numbers, often referred to
 </span>
 <span data-rw-start="65.519" data-rw-transcript-version="2">
 as an embedding.
 </span>
</p>
<p>
 <span data-rw-start="67.439" data-rw-transcript-version="2">
 From here, a third model known as a
 </span>
 <span data-rw-start="69.52" data-rw-transcript-version="2">
 predictor is trained to predict the
 </span>
 <span data-rw-start="71.439" data-rw-transcript-version="2">
 embedding of Y given the embedding of X.
 </span>
 <span data-rw-start="75.28" data-rw-transcript-version="2">
 Why might this be a better way to build
 </span>
 <span data-rw-start="77.2" data-rw-transcript-version="2">
 AI systems? Do you think that Jeepa or
 </span>
 <span data-rw-start="80.24" data-rw-transcript-version="2">
 world model-based approaches, do you
 </span>
 <span data-rw-start="81.92" data-rw-transcript-version="2">
 think they'll replace LLMs one day or
 </span>
 <span data-rw-start="83.52" data-rw-transcript-version="2">
 are they kind of solving different
 </span>
 <span data-rw-start="84.56" data-rw-transcript-version="2">
 problems?
 </span>
</p>
<p>
 <span data-rw-start="85.759" data-rw-transcript-version="2">
 Initially, they'll solve different
 </span>
 <span data-rw-start="87.04" data-rw-transcript-version="2">
 problems.
 </span>
 <span data-rw-start="88.32" data-rw-transcript-version="2">
 &gt;&gt; Eventually, they replace LLM, okay,
 </span>
 <span data-rw-start="91.6" data-rw-transcript-version="2">
 because, you know, LLMs are really good at
 </span>
 <span data-rw-start="93.2" data-rw-transcript-version="2">
 manipulating language, but basically,
 </span>
 <span data-rw-start="94.88" data-rw-transcript-version="2">
 nothing else.
 </span>
</p>
<p>
 <span data-rw-start="96.4" data-rw-transcript-version="2">
 &gt;&gt; They're really good in domains where the
 </span>
 <span data-rw-start="99.119" data-rw-transcript-version="2">
 language itself is the substrate of
 </span>
 <span data-rw-start="102.32" data-rw-transcript-version="2">
 reasoning.
 </span>
 <span data-rw-start="103.119" data-rw-transcript-version="2">
 &gt;&gt; Compared to the mainline generative
 </span>
 <span data-rw-start="105.04" data-rw-transcript-version="2">
 language approach to AI, Jeepa lives on
 </span>
 <span data-rw-start="108.079" data-rw-transcript-version="2">
 an alternative path of joint embedding
 </span>
 <span data-rw-start="110.32" data-rw-transcript-version="2">
 architectures.
 </span>
 <span data-rw-start="112" data-rw-transcript-version="2">
 Interestingly, Lacun played a
 </span>
 <span data-rw-start="113.439" data-rw-transcript-version="2">
 Significant role at the outset of both
 </span>
 <span data-rw-start="115.28" data-rw-transcript-version="2">
 paths. In part one of this two-part
 </span>
 <span data-rw-start="118.159" data-rw-transcript-version="2">
 series, we'll explore this alternative
 </span>
 <span data-rw-start="120.24" data-rw-transcript-version="2">
 path to Jeepa. We'll dig into why Yan
 </span>
 <span data-rw-start="123.04" data-rw-transcript-version="2">
 moved away from generative architectures
 </span>
 <span data-rw-start="125.36" data-rw-transcript-version="2">
 just as they were gaining traction in
 </span>
 <span data-rw-start="127.04" data-rw-transcript-version="2">
 language and explore Yan's epiphany for
 </span>
 <span data-rw-start="129.92" data-rw-transcript-version="2">
 a new solution to the representation
 </span>
 <span data-rw-start="131.84" data-rw-transcript-version="2">
 collapse problem that plagued joint
 </span>
 <span data-rw-start="133.92" data-rw-transcript-version="2">
 embedding architectures for years.
 </span>
</p>
<p>
 <span data-rw-start="136.319" data-rw-transcript-version="2">
 Finally, we'll dig into the Jeepa
 </span>
 <span data-rw-start="137.76" data-rw-transcript-version="2">
 architecture itself.
 </span>
 <span data-rw-start="139.92" data-rw-transcript-version="2">
 In part two, we'll dive into JEPA
 </span>
 <span data-rw-start="141.599" data-rw-transcript-version="2">
 implementations and see exactly how
 </span>
 <span data-rw-start="143.92" data-rw-transcript-version="2">
 these models stack up against LLM-driven
 </span>
 <span data-rw-start="146.16" data-rw-transcript-version="2">
 approaches.
 </span>
</p>
<p>
 <span data-rw-start="151.28" data-rw-transcript-version="2">
 Yan Lun saw the revolution coming in the
 </span>
 <span data-rw-start="155.12" data-rw-transcript-version="2">
 1980s. While most of the AI field was
 </span>
 <span data-rw-start="157.12" data-rw-transcript-version="2">
 busy building expert systems that were
 </span>
 <span data-rw-start="159.28" data-rw-transcript-version="2">
 explicitly programmed instead of learned
 </span>
 <span data-rw-start="161.12" data-rw-transcript-version="2">
 from data, Jan pioneered the
 </span>
 <span data-rw-start="163.68" data-rw-transcript-version="2">
 convolutional neural network. Twenty-five
 </span>
 <span data-rw-start="166.8" data-rw-transcript-version="2">
 years later, when deep learning began its rise
 </span>
 <span data-rw-start="168.959" data-rw-transcript-version="2">
 to its now dominant position in AI, the
 </span>
 <span data-rw-start="171.68" data-rw-transcript-version="2">
 breakthrough deep learning model AlexNet
 </span>
 <span data-rw-start="174.08" data-rw-transcript-version="2">
 Turned out to be uncannily similar to
 </span>
 <span data-rw-start="176.16" data-rw-transcript-version="2">
 Lacun's convolutional nets from the
 </span>
 <span data-rw-start="178" data-rw-transcript-version="2">
 1990s.
 </span>
</p>
<p>
 <span data-rw-start="180.239" data-rw-transcript-version="2">
 However, as deep learning continued to
 </span>
 <span data-rw-start="181.68" data-rw-transcript-version="2">
 pick up steam through the 2010s, Lacun
 </span>
 <span data-rw-start="184.319" data-rw-transcript-version="2">
 and other researchers became
 </span>
 <span data-rw-start="185.44" data-rw-transcript-version="2">
 increasingly concerned by just how much
 </span>
 <span data-rw-start="188" data-rw-transcript-version="2">
 this approach to AI depended on labeled
 </span>
 <span data-rw-start="190.4" data-rw-transcript-version="2">
 training data. AlexNet was trained on
 </span>
 <span data-rw-start="193.12" data-rw-transcript-version="2">
 the enormous and meticulously labeled
 </span>
 <span data-rw-start="194.959" data-rw-transcript-version="2">
 ImageNet data set using supervised
 </span>
 <span data-rw-start="197.44" data-rw-transcript-version="2">
 learning, where AlexNet was trained to
 </span>
 <span data-rw-start="199.599" data-rw-transcript-version="2">
 match the labels assigned to each image
 </span>
 <span data-rw-start="201.44" data-rw-transcript-version="2">
 by human annotators.
 </span>
 <span data-rw-start="203.68" data-rw-transcript-version="2">
 In contrast, children are able to learn
 </span>
 <span data-rw-start="205.68" data-rw-transcript-version="2">
 very general representations for
 </span>
 <span data-rw-start="207.44" data-rw-transcript-version="2">
 concepts like dog with very few
 </span>
 <span data-rw-start="209.92" data-rw-transcript-version="2">
 explicitly labeled examples.
 </span>
 <span data-rw-start="213.44" data-rw-transcript-version="2">
 As manually labeled data became a
 </span>
 <span data-rw-start="215.28" data-rw-transcript-version="2">
 bottleneck for supervised learning,
 </span>
 <span data-rw-start="217.28" data-rw-transcript-version="2">
 interest grew in alternative approaches.
 </span>
 <span data-rw-start="220.159" data-rw-transcript-version="2">
 Reinforcement learning, where models
 </span>
 <span data-rw-start="222" data-rw-transcript-version="2">
 learn from interacting with their
 </span>
 <span data-rw-start="223.28" data-rw-transcript-version="2">
 environments instead of from labeled
 </span>
 <span data-rw-start="224.959" data-rw-transcript-version="2">
 data, experienced a many renaissance in
 </span>
 <span data-rw-start="227.599" data-rw-transcript-version="2">
 The mid-2010s,
 </span>
 <span data-rw-start="229.44" data-rw-transcript-version="2">
 highlighted by Google DeepMind's
 </span>
 <span data-rw-start="231.04" data-rw-transcript-version="2">
 breakthrough performance on Atari games
 </span>
 <span data-rw-start="232.879" data-rw-transcript-version="2">
 and the highly complex board game Go.
 </span>
</p>
<p>
 <span data-rw-start="236.08" data-rw-transcript-version="2">
 Concurrently, Lacun and others explored
 </span>
 <span data-rw-start="238" data-rw-transcript-version="2">
 unsupervised methods that learn from
 </span>
 <span data-rw-start="240.319" data-rw-transcript-version="2">
 data without labels, including a variant
 </span>
 <span data-rw-start="243.2" data-rw-transcript-version="2">
 called self-supervised learning, where
 </span>
 <span data-rw-start="245.36" data-rw-transcript-version="2">
 the labels are taken from the data
 </span>
 <span data-rw-start="246.879" data-rw-transcript-version="2">
 itself. Starting in 2015 or so, I
 </span>
 <span data-rw-start="250.319" data-rw-transcript-version="2">
 started showing a slide that has become
 </span>
 <span data-rw-start="252.08" data-rw-transcript-version="2">
 a bit of a meme in the machine learning
 </span>
 <span data-rw-start="253.599" data-rw-transcript-version="2">
 community where I said like, you know,
 </span>
 <span data-rw-start="255.68" data-rw-transcript-version="2">
 if it's the cake slide, right? So, if uh
 </span>
 <span data-rw-start="259.199" data-rw-transcript-version="2">
 intelligence is a cake, the bulk of the
 </span>
 <span data-rw-start="260.959" data-rw-transcript-version="2">
 cake is self-supervised learning, the
 </span>
 <span data-rw-start="263.84" data-rw-transcript-version="2">
 icing on the cake, supervised learning,
 </span>
 <span data-rw-start="265.12" data-rw-transcript-version="2">
 and the chair on the cake, reinforcement
 </span>
 <span data-rw-start="266.56" data-rw-transcript-version="2">
 learning. At the time, people were kind
 </span>
 <span data-rw-start="268.16" data-rw-transcript-version="2">
 of crazy about reinforcement learning.
 </span>
 <span data-rw-start="269.68" data-rw-transcript-version="2">
 So I was trying to tell them like this
 </span>
 <span data-rw-start="271.44" data-rw-transcript-version="2">
 is not never going to you know take us
 </span>
 <span data-rw-start="273.84" data-rw-transcript-version="2">
 to you know anywhere close to human or
 </span>
 <span data-rw-start="275.919" data-rw-transcript-version="2">
 animal intelligence because it's too
 </span>
 <span data-rw-start="277.759" data-rw-transcript-version="2">
 inefficient. Um, and uh turns out the
 </span>
 <span data-rw-start="282.32" data-rw-transcript-version="2">
 Success of self-supervised learning, uh,
 </span>
 <span data-rw-start="286.16" data-rw-transcript-version="2">
 you know, happened in, in text and, and
 </span>
 <span data-rw-start="289.04" data-rw-transcript-version="2">
 language much faster than it did in sort
 </span>
</p>
<p>
 <span data-rw-start="291.84" data-rw-transcript-version="2">
 of more, uh, you know, natural, uh,
 </span>
 <span data-rw-start="294.96" data-rw-transcript-version="2">
 modalities, like, uh, like vision. Here, Jan
 </span>
 <span data-rw-start="298" data-rw-transcript-version="2">
 is referring to the success of next
 </span>
 <span data-rw-start="299.52" data-rw-transcript-version="2">
 token prediction for training large
 </span>
 <span data-rw-start="301.199" data-rw-transcript-version="2">
 language models. OpenAI was founded in
 </span>
 <span data-rw-start="304.08" data-rw-transcript-version="2">
 2015, and initially focused their efforts
 </span>
 <span data-rw-start="306.8" data-rw-transcript-version="2">
 on reinforcement learning, creating
 </span>
 <span data-rw-start="308.96" data-rw-transcript-version="2">
 OpenAI Gym and Universe, and showing very
 </span>
 <span data-rw-start="311.919" data-rw-transcript-version="2">
 impressive performance on complex video
 </span>
 <span data-rw-start="314" data-rw-transcript-version="2">
 games. While much of the company was
 </span>
 <span data-rw-start="316.639" data-rw-transcript-version="2">
 focused on reinforcement learning, Ilia
 </span>
 <span data-rw-start="319.039" data-rw-transcript-version="2">
 Sutskever, Alec Radford, and others
 </span>
 <span data-rw-start="320.96" data-rw-transcript-version="2">
 became interested in a new neural
 </span>
 <span data-rw-start="322.56" data-rw-transcript-version="2">
 network architecture from Google, the
 </span>
 <span data-rw-start="324.72" data-rw-transcript-version="2">
 transformer. Initially designed for
 </span>
 <span data-rw-start="326.96" data-rw-transcript-version="2">
 language translation,
 </span>
 <span data-rw-start="329.44" data-rw-transcript-version="2">
 while experimenting, Radford tried an
 </span>
 <span data-rw-start="331.36" data-rw-transcript-version="2">
 interesting modification. Instead of
 </span>
 <span data-rw-start="333.44" data-rw-transcript-version="2">
 having the transformer translate from a
 </span>
 <span data-rw-start="335.28" data-rw-transcript-version="2">
 block of text in one language to a block
 </span>
 <span data-rw-start="337.36" data-rw-transcript-version="2">
 of text in another language, he switched
 </span>
 <span data-rw-start="339.52" data-rw-transcript-version="2">
 to a simpler self-supervised approach.
 </span>
</p>
<p>
 <span data-rw-start="342.24" data-rw-transcript-version="2">
 Where training text is broken into
 </span>
 <span data-rw-start="343.84" data-rw-transcript-version="2">
 sequences and the transformer is given
 </span>
 <span data-rw-start="346.4" data-rw-transcript-version="2">
 all but the last little piece of text
 </span>
 <span data-rw-start="348.72" data-rw-transcript-version="2">
 known as a token in each sequence, and
 </span>
 <span data-rw-start="351.28" data-rw-transcript-version="2">
 trained to predict what this final token
 </span>
 <span data-rw-start="352.96" data-rw-transcript-version="2">
 will be.
 </span>
</p>
<p>
 <span data-rw-start="355.199" data-rw-transcript-version="2">
 Radford and his OpenAI colleagues
 </span>
 <span data-rw-start="356.8" data-rw-transcript-version="2">
 trained their transformer on a fairly
 </span>
 <span data-rw-start="358.479" data-rw-transcript-version="2">
 large internal OpenAI data set of 7,000
 </span>
 <span data-rw-start="361.28" data-rw-transcript-version="2">
 books. Note that we now call this phase
 </span>
 <span data-rw-start="363.919" data-rw-transcript-version="2">
 pre-training, and then they further train
 </span>
 <span data-rw-start="366.319" data-rw-transcript-version="2">
 their model using standard supervised
 </span>
 <span data-rw-start="368" data-rw-transcript-version="2">
 learning from human-generated labels on
 </span>
 <span data-rw-start="370.24" data-rw-transcript-version="2">
 specific language tasks.
 </span>
</p>
<p>
 <span data-rw-start="372.88" data-rw-transcript-version="2">
 Their two-stage training approach worked
 </span>
 <span data-rw-start="374.96" data-rw-transcript-version="2">
 well, setting new state-of-the-art
 </span>
 <span data-rw-start="376.96" data-rw-transcript-version="2">
 results on nine language benchmarks,
 </span>
 <span data-rw-start="379.759" data-rw-transcript-version="2">
 including tasks like high school level
 </span>
 <span data-rw-start="381.44" data-rw-transcript-version="2">
 reading comprehension questions,
 </span>
 <span data-rw-start="383.44" data-rw-transcript-version="2">
 outperforming architectures and methods
 </span>
 <span data-rw-start="385.199" data-rw-transcript-version="2">
 that were individually designed and
 </span>
 <span data-rw-start="386.72" data-rw-transcript-version="2">
 trained for each individual task.
 </span>
</p>
<p>
 <span data-rw-start="389.68" data-rw-transcript-version="2">
 Radford's model is now known as
 </span>
 <span data-rw-start="391.36" data-rw-transcript-version="2">
 generative pre-trained transformer 1 or
 </span>
 <span data-rw-start="394.479" data-rw-transcript-version="2">
 GPT-1.
 </span>
</p>
<p>
 <span data-rw-start="396.16" data-rw-transcript-version="2">
 GPT1 didn't receive much public
 </span>
 <span data-rw-start="398" data-rw-transcript-version="2">
 attention at the time, but was a huge
 </span>
 <span data-rw-start="400.319" data-rw-transcript-version="2">
 unlock, breaking models free from their
 </span>
 <span data-rw-start="402.8" data-rw-transcript-version="2">
 dependence on human-labeled data and
 </span>
 <span data-rw-start="405.199" data-rw-transcript-version="2">
 opening up unprecedented levels of
 </span>
 <span data-rw-start="407.039" data-rw-transcript-version="2">
 scale.
 </span>
 <span data-rw-start="408.72" data-rw-transcript-version="2">
 Other researchers at OpenAI quickly
 </span>
 <span data-rw-start="410.639" data-rw-transcript-version="2">
 grasp the significance of Radford's
 </span>
 <span data-rw-start="412.319" data-rw-transcript-version="2">
 results, and the team went all in on this
 </span>
 <span data-rw-start="414.96" data-rw-transcript-version="2">
 approach, aggressively scaling up to
 </span>
 <span data-rw-start="417.36" data-rw-transcript-version="2">
 GPT-2 in 2019, GPT-3 in 2020, and ChatGPT
 </span>
 <span data-rw-start="422.319" data-rw-transcript-version="2">
 in 2022.
 </span>
</p>
<p>
 <span data-rw-start="424.72" data-rw-transcript-version="2">
 In 2012, AlexNet was trained on around a
 </span>
 <span data-rw-start="427.44" data-rw-transcript-version="2">
 million examples. In 2020, GPT-3 was
 </span>
 <span data-rw-start="430.8" data-rw-transcript-version="2">
 trained on hundreds of billions of
 </span>
 <span data-rw-start="432.56" data-rw-transcript-version="2">
 examples. And interestingly, the new
 </span>
 <span data-rw-start="435.199" data-rw-transcript-version="2">
 training paradigm that emerged exactly
 </span>
 <span data-rw-start="437.28" data-rw-transcript-version="2">
 matched Yann LeCun's predictions from a
 </span>
 <span data-rw-start="439.12" data-rw-transcript-version="2">
 few years earlier. An extensive
 </span>
 <span data-rw-start="441.599" data-rw-transcript-version="2">
 self-supervised pre-training phase
 </span>
 <span data-rw-start="444.08" data-rw-transcript-version="2">
 followed by supervised learning and
 </span>
 <span data-rw-start="445.599" data-rw-transcript-version="2">
 finally reinforcement learning to shape
 </span>
 <span data-rw-start="448.08" data-rw-transcript-version="2">
 the raw next token predictor model into
 </span>
 <span data-rw-start="450.16" data-rw-transcript-version="2">
 a helpful AI assistant.
 </span>
</p>
<p>
 <span data-rw-start="452.8" data-rw-transcript-version="2">
 However, while these self-supervised
 </span>
 <span data-rw-start="454.479" data-rw-transcript-version="2">
 Generative approaches clearly broke
 </span>
 <span data-rw-start="456.16" data-rw-transcript-version="2">
 through in language, the picture was
 </span>
 <span data-rw-start="458.4" data-rw-transcript-version="2">
 much fuzzier for image and video data.
 </span>
</p>
<p>
 <span data-rw-start="461.68" data-rw-transcript-version="2">
 But I, I, I kept working on vision, and
 </span>
 <span data-rw-start="464.16" data-rw-transcript-version="2">
 then initially, uh, the, the, uh idea was to
 </span>
 <span data-rw-start="469.199" data-rw-transcript-version="2">
 use, um, so to train a system to predict
 </span>
 <span data-rw-start="472" data-rw-transcript-version="2">
 what happens in video, but to use, uh,
 </span>
 <span data-rw-start="474.639" data-rw-transcript-version="2">
 generative architectures. Um, so
 </span>
 <span data-rw-start="477.36" data-rw-transcript-version="2">
 basically, train at a pixel level what's
 </span>
 <span data-rw-start="479.599" data-rw-transcript-version="2">
 going to happen in the video. Years
 </span>
 <span data-rw-start="481.52" data-rw-transcript-version="2">
 before the success of GPT-1, researchers
 </span>
 <span data-rw-start="484.24" data-rw-transcript-version="2">
 including Lacun had tried to apply the
 </span>
 <span data-rw-start="486.24" data-rw-transcript-version="2">
 same self-supervised generative approach
 </span>
 <span data-rw-start="488.319" data-rw-transcript-version="2">
 to video. In the most straightforward
 </span>
 <span data-rw-start="490.879" data-rw-transcript-version="2">
 implementation, we configure our neural
 </span>
 <span data-rw-start="493.039" data-rw-transcript-version="2">
 network to take in the RGB pixel values
 </span>
 <span data-rw-start="495.199" data-rw-transcript-version="2">
 from a sequence of video frames and then
 </span>
 <span data-rw-start="497.759" data-rw-transcript-version="2">
 predict the pixel values in the next
 </span>
 <span data-rw-start="499.52" data-rw-transcript-version="2">
 frame, just as the GPT models are trained
 </span>
 <span data-rw-start="502" data-rw-transcript-version="2">
 to predict the next token in language.
 </span>
</p>
<p>
 <span data-rw-start="504.879" data-rw-transcript-version="2">
 However, when we use these models to
 </span>
 <span data-rw-start="506.479" data-rw-transcript-version="2">
 predict the next frame, the results are
 </span>
 <span data-rw-start="508.4" data-rw-transcript-version="2">
 blurry. And this blurriness compounds
 </span>
 <span data-rw-start="511.36" data-rw-transcript-version="2">
 dramatically in longer horizon
 </span>
 <span data-rw-start="513.12" data-rw-transcript-version="2">
 predictions. Large language models are
 </span>
 <span data-rw-start="515.599" data-rw-transcript-version="2">
 Auto regressive. When chat GPT answers
 </span>
 <span data-rw-start="518.32" data-rw-transcript-version="2">
 a question, it generates one token at a
 </span>
 <span data-rw-start="520.399" data-rw-transcript-version="2">
 time. At each step, feeding its latest
 </span>
 <span data-rw-start="522.88" data-rw-transcript-version="2">
 generated token back into its input to
 </span>
 <span data-rw-start="525.12" data-rw-transcript-version="2">
 create the next output. If we try this
 </span>
 <span data-rw-start="527.6" data-rw-transcript-version="2">
 auto regressive approach with a next
 </span>
 <span data-rw-start="529.36" data-rw-transcript-version="2">
 frame video prediction model, the
 </span>
 <span data-rw-start="531.68" data-rw-transcript-version="2">
 results quickly devolve into blurry
 </span>
 <span data-rw-start="533.44" data-rw-transcript-version="2">
 nothingness.
 </span>
</p>
<p>
 <span data-rw-start="535.279" data-rw-transcript-version="2">
 Before we see exactly how JEA is able to
 </span>
 <span data-rw-start="537.519" data-rw-transcript-version="2">
 get around this blurry prediction
 </span>
 <span data-rw-start="539.04" data-rw-transcript-version="2">
 problem, let's look at another
 </span>
 <span data-rw-start="540.88" data-rw-transcript-version="2">
 fascinating application of transformers
 </span>
 <span data-rw-start="542.88" data-rw-transcript-version="2">
 beyond language models. This video is
 </span>
 <span data-rw-start="546" data-rw-transcript-version="2">
 sponsored by Hudson River Trading, and
 </span>
 <span data-rw-start="548.399" data-rw-transcript-version="2">
 this is an order book. The left column
 </span>
 <span data-rw-start="551.36" data-rw-transcript-version="2">
 shows all the bids to buy Nvidia stock
 </span>
 <span data-rw-start="554.16" data-rw-transcript-version="2">
 ranked by bid price, and the right
 </span>
 <span data-rw-start="556.56" data-rw-transcript-version="2">
 column shows all the current offers to
 </span>
 <span data-rw-start="558.16" data-rw-transcript-version="2">
 sell Nvidia stock ranked by asking
 </span>
 <span data-rw-start="560.72" data-rw-transcript-version="2">
 price. On a busy trading day, about
 </span>
 <span data-rw-start="563.92" data-rw-transcript-version="2">
 1,000 new buy and sell orders
 </span>
 <span data-rw-start="566.399" data-rw-transcript-version="2">
 like this come in every second. This
 </span>
 <span data-rw-start="568.959" data-rw-transcript-version="2">
 deluge of orders is an incredibly rich
 </span>
 <span data-rw-start="571.12" data-rw-transcript-version="2">
 information source. Is it possible to
 </span>
 <span data-rw-start="573.839" data-rw-transcript-version="2">
 Train a transformer like the ones used
 </span>
 <span data-rw-start="575.839" data-rw-transcript-version="2">
 in VJA to find patterns in this data and
 </span>
 <span data-rw-start="579.68" data-rw-transcript-version="2">
 use these patterns to predict future
 </span>
 <span data-rw-start="581.44" data-rw-transcript-version="2">
 prices? Hudson River Trading has
 </span>
 <span data-rw-start="583.92" data-rw-transcript-version="2">
 trillions of tokens of historical data.
 </span>
</p>
<p>
 <span data-rw-start="586.56" data-rw-transcript-version="2">
 This is the same order of magnitude of
 </span>
 <span data-rw-start="588.32" data-rw-transcript-version="2">
 training data used to train Frontier
 </span>
 <span data-rw-start="590.24" data-rw-transcript-version="2">
 LLMs.
 </span>
 <span data-rw-start="591.76" data-rw-transcript-version="2">
 And their researchers are working to
 </span>
 <span data-rw-start="593.12" data-rw-transcript-version="2">
 push the frontiers of machine learning
 </span>
 <span data-rw-start="595.04" data-rw-transcript-version="2">
 on this data.
 </span>
</p>
<p>
 <span data-rw-start="597.12" data-rw-transcript-version="2">
 The VJEPA model we'll see later in the
 </span>
 <span data-rw-start="599.12" data-rw-transcript-version="2">
 video maps patches of videos to
 </span>
 <span data-rw-start="601.36" data-rw-transcript-version="2">
 individual embedding vectors. We could
 </span>
 <span data-rw-start="603.76" data-rw-transcript-version="2">
 take a similar approach with order book
 </span>
 <span data-rw-start="605.6" data-rw-transcript-version="2">
 data tokenizing groups of orders using
 </span>
 <span data-rw-start="608.08" data-rw-transcript-version="2">
 some financial intuition.
 </span>
</p>
<p>
 <span data-rw-start="610.32" data-rw-transcript-version="2">
 However, this naive approach does not
 </span>
 <span data-rw-start="612" data-rw-transcript-version="2">
 work well in practice, and the Hudson
 </span>
 <span data-rw-start="614.32" data-rw-transcript-version="2">
 River trading team has developed some
 </span>
 <span data-rw-start="615.92" data-rw-transcript-version="2">
 really interesting approaches to adapt
 </span>
 <span data-rw-start="617.76" data-rw-transcript-version="2">
 cutting edge transformer architectures
 </span>
 <span data-rw-start="619.6" data-rw-transcript-version="2">
 to the complexities and constraints of
 </span>
 <span data-rw-start="621.44" data-rw-transcript-version="2">
 trading data. And all of this is
 </span>
 <span data-rw-start="623.76" data-rw-transcript-version="2">
 happening in a setting where speed is
 </span>
 <span data-rw-start="625.519" data-rw-transcript-version="2">
 Everything. Models have to run under
 </span>
 <span data-rw-start="628" data-rw-transcript-version="2">
 incredibly tight latency constraints.
 </span>
</p>
<p>
 <span data-rw-start="631.44" data-rw-transcript-version="2">
 These fascinating and highly complex
 </span>
 <span data-rw-start="633.36" data-rw-transcript-version="2">
 research and engineering challenges
 </span>
 <span data-rw-start="635.519" data-rw-transcript-version="2">
 combined with the resources to actually
 </span>
 <span data-rw-start="637.279" data-rw-transcript-version="2">
 tackle them and an open, highly
 </span>
 <span data-rw-start="639.12" data-rw-transcript-version="2">
 collaborative environment make Hudson
 </span>
 <span data-rw-start="641.2" data-rw-transcript-version="2">
 River Trading an incredibly unique place
 </span>
 <span data-rw-start="643.2" data-rw-transcript-version="2">
 to work. I hear a lot from potential
 </span>
 <span data-rw-start="646" data-rw-transcript-version="2">
 sponsors these days and have been
 </span>
 <span data-rw-start="648.079" data-rw-transcript-version="2">
 seriously impressed in my interactions
 </span>
 <span data-rw-start="649.76" data-rw-transcript-version="2">
 with the Hudson River Trading team. The
 </span>
 <span data-rw-start="652.16" data-rw-transcript-version="2">
 level of technical discussion and
 </span>
 <span data-rw-start="653.6" data-rw-transcript-version="2">
 enthusiasm for these deep and
 </span>
 <span data-rw-start="655.2" data-rw-transcript-version="2">
 interesting problems is unparalleled in
 </span>
 <span data-rw-start="657.12" data-rw-transcript-version="2">
 my experience. If this sounds
 </span>
 <span data-rw-start="659.36" data-rw-transcript-version="2">
 interesting, Hudson River Trading is
 </span>
 <span data-rw-start="661.12" data-rw-transcript-version="2">
 currently hiring for AI researchers,
 </span>
 <span data-rw-start="663.279" data-rw-transcript-version="2">
 algorithm developers, and software
 </span>
 <span data-rw-start="665.2" data-rw-transcript-version="2">
 engineers. They're hiring globally, and
 </span>
 <span data-rw-start="667.92" data-rw-transcript-version="2">
 you don't need a finance background. You
 </span>
 <span data-rw-start="670.399" data-rw-transcript-version="2">
 can learn more at hudson
 </span>
 <span data-rw-start="671.36" data-rw-transcript-version="2">
 rivertrading.com/welchlabs.
 </span>
 <span data-rw-start="674.56" data-rw-transcript-version="2">
 Now, back to Jeepa.
 </span>
 <span data-rw-start="677.04" data-rw-transcript-version="2">
 Now, the blurry frames produced by our
 </span>
 <span data-rw-start="679.04" data-rw-transcript-version="2">
 Generative video prediction approaches are
 </span>
 <span data-rw-start="681.279" data-rw-transcript-version="2">
 not some huge mystery. Language is
 </span>
 <span data-rw-start="683.839" data-rw-transcript-version="2">
 complex and unpredictable, but it's
 </span>
 <span data-rw-start="686" data-rw-transcript-version="2">
 nothing compared to video.
 </span>
</p>
<p>
 <span data-rw-start="688.32" data-rw-transcript-version="2">
 Language models use fixed-size
 </span>
 <span data-rw-start="690" data-rw-transcript-version="2">
 vocabularies.
 </span>
 <span data-rw-start="691.6" data-rw-transcript-version="2">
 GPT-2 has 50,257
 </span>
 <span data-rw-start="694.16" data-rw-transcript-version="2">
 discrete outputs, one for each token
 </span>
 <span data-rw-start="696.64" data-rw-transcript-version="2">
 that the model could say next. This
 </span>
 <span data-rw-start="699.2" data-rw-transcript-version="2">
 complete enumeration approach is
 </span>
 <span data-rw-start="700.959" data-rw-transcript-version="2">
 hopeless in video. For full HD video, in
 </span>
 <span data-rw-start="704.32" data-rw-transcript-version="2">
 the most general case, each pixel can
 </span>
 <span data-rw-start="706.72" data-rw-transcript-version="2">
 take on 256 discrete values. And we have
 </span>
 <span data-rw-start="710.24" data-rw-transcript-version="2">
 1920 \* 1080 \* 3 color pixels. Meaning
 </span>
 <span data-rw-start="714.48" data-rw-transcript-version="2">
 there are something like 10 to the power
 </span>
 <span data-rw-start="716.16" data-rw-transcript-version="2">
 of 15 million possible next video frames
 </span>
 <span data-rw-start="720.079" data-rw-transcript-version="2">
 dwarfing the number of atoms in the
 </span>
 <span data-rw-start="721.76" data-rw-transcript-version="2">
 observable universe. So there's no way
 </span>
 <span data-rw-start="724.48" data-rw-transcript-version="2">
 our video prediction model can have a
 </span>
 <span data-rw-start="726.16" data-rw-transcript-version="2">
 discrete output for each possible next
 </span>
 <span data-rw-start="728.32" data-rw-transcript-version="2">
 video frame as our language model has a
 </span>
 <span data-rw-start="731.04" data-rw-transcript-version="2">
 discrete output for each next possible
 </span>
 <span data-rw-start="732.8" data-rw-transcript-version="2">
 token.
 </span>
 <span data-rw-start="734.48" data-rw-transcript-version="2">
 Instead, many generative video
 </span>
 <span data-rw-start="736.16" data-rw-transcript-version="2">
 approaches of this era had the network
 </span>
 <span data-rw-start="738.639" data-rw-transcript-version="2">
 Directly output pixel intensity values.
 </span>
</p>
<p>
 <span data-rw-start="742.32" data-rw-transcript-version="2">
 The big challenge with this approach is
 </span>
 <span data-rw-start="744" data-rw-transcript-version="2">
 how the model learns to handle
 </span>
 <span data-rw-start="745.519" data-rw-transcript-version="2">
 uncertainty.
 </span>
 <span data-rw-start="747.44" data-rw-transcript-version="2">
 If we compare an LLM learning to
 </span>
 <span data-rw-start="749.2" data-rw-transcript-version="2">
 complete the sentence, the ball bounced
 </span>
 <span data-rw-start="750.88" data-rw-transcript-version="2">
 to the and a neural network predicting
 </span>
 <span data-rw-start="753.2" data-rw-transcript-version="2">
 the next frame of a video of a ball
 </span>
 <span data-rw-start="755.2" data-rw-transcript-version="2">
 actually bouncing, we can see exactly
 </span>
 <span data-rw-start="757.6" data-rw-transcript-version="2">
 what goes wrong. In the LLM training
 </span>
 <span data-rw-start="760.56" data-rw-transcript-version="2">
 case, the model will see various
 </span>
 <span data-rw-start="762.56" data-rw-transcript-version="2">
 examples in its training set of the ball
 </span>
 <span data-rw-start="764.8" data-rw-transcript-version="2">
 bouncing left and right. And since the
 </span>
 <span data-rw-start="767.6" data-rw-transcript-version="2">
 model has separate outputs for each of
 </span>
 <span data-rw-start="769.2" data-rw-transcript-version="2">
 these tokens, it can essentially
 </span>
 <span data-rw-start="771.519" data-rw-transcript-version="2">
 independently update these
 </span>
 <span data-rw-start="772.8" data-rw-transcript-version="2">
 probabilities.
 </span>
</p>
<p>
 <span data-rw-start="774.56" data-rw-transcript-version="2">
 Our video model doesn't have it so easy.
 </span>
 <span data-rw-start="777.44" data-rw-transcript-version="2">
 If our data set includes videos of the
 </span>
 <span data-rw-start="779.2" data-rw-transcript-version="2">
 ball starting down the same path and
 </span>
 <span data-rw-start="781.2" data-rw-transcript-version="2">
 then bouncing in various directions,
 </span>
 <span data-rw-start="783.68" data-rw-transcript-version="2">
 since our model is forced to directly
 </span>
 <span data-rw-start="785.44" data-rw-transcript-version="2">
 predict a single output frame for a
 </span>
 <span data-rw-start="787.44" data-rw-transcript-version="2">
 given input, the best it can do in the
 </span>
 <span data-rw-start="790.079" data-rw-transcript-version="2">
 face of this ambiguity is to predict the
 </span>
 <span data-rw-start="792" data-rw-transcript-version="2">
 Average of these outcomes.
 </span>
</p>
<p>
 <span data-rw-start="794.32" data-rw-transcript-version="2">
 When we average the pixel values of our
 </span>
 <span data-rw-start="796.24" data-rw-transcript-version="2">
 videos, we end up with a blurry, washed
 </span>
 <span data-rw-start="798.56" data-rw-transcript-version="2">
 out mess.
 </span>
 <span data-rw-start="800.48" data-rw-transcript-version="2">
 Now, this is only the most naive
 </span>
 <span data-rw-start="802.079" data-rw-transcript-version="2">
 approach, and there have been many, many
 </span>
 <span data-rw-start="804.399" data-rw-transcript-version="2">
 interesting video and image prediction
 </span>
 <span data-rw-start="806" data-rw-transcript-version="2">
 strategies tried with various degrees of
 </span>
 <span data-rw-start="807.92" data-rw-transcript-version="2">
 success over the last couple decades.
 </span>
</p>
<p>
 <span data-rw-start="811.04" data-rw-transcript-version="2">
 However, the challenges that naturally
 </span>
 <span data-rw-start="812.8" data-rw-transcript-version="2">
 arise led Lun and other researchers to
 </span>
 <span data-rw-start="815.36" data-rw-transcript-version="2">
 ask an interesting question. Do our
 </span>
 <span data-rw-start="818.16" data-rw-transcript-version="2">
 models really need to be generative? In
 </span>
 <span data-rw-start="821.2" data-rw-transcript-version="2">
 our GPT example, during the crucial
 </span>
 <span data-rw-start="823.68" data-rw-transcript-version="2">
 pre-training phase, it really doesn't
 </span>
 <span data-rw-start="826.079" data-rw-transcript-version="2">
 matter that our model is generative.
 </span>
 <span data-rw-start="828.88" data-rw-transcript-version="2">
 After pre-training on next token
 </span>
 <span data-rw-start="830.48" data-rw-transcript-version="2">
 prediction, we're left with a model
 </span>
 <span data-rw-start="832.32" data-rw-transcript-version="2">
 that's essentially a really good
 </span>
 <span data-rw-start="833.92" data-rw-transcript-version="2">
 autocomplete.
 </span>
 <span data-rw-start="835.44" data-rw-transcript-version="2">
 But this is not the point. What actually
 </span>
 <span data-rw-start="838.079" data-rw-transcript-version="2">
 matters are the internal representations
 </span>
 <span data-rw-start="840.16" data-rw-transcript-version="2">
 and features that the model learns to
 </span>
 <span data-rw-start="842.399" data-rw-transcript-version="2">
 solve the next token prediction task.
 </span>
 <span data-rw-start="845.76" data-rw-transcript-version="2">
 These learned internal representations
 </span>
 <span data-rw-start="847.519" data-rw-transcript-version="2">
 Are what allows pre-trained models to be
 </span>
 <span data-rw-start="850.16" data-rw-transcript-version="2">
 quickly adapted into powerful AI
 </span>
 <span data-rw-start="852.32" data-rw-transcript-version="2">
 assistance.
 </span>
</p>
<p>
 <span data-rw-start="854.48" data-rw-transcript-version="2">
 Next token prediction on language is a
 </span>
 <span data-rw-start="856.399" data-rw-transcript-version="2">
 proxy for intelligence that has turned
 </span>
 <span data-rw-start="858.639" data-rw-transcript-version="2">
 out to work shockingly well.
 </span>
 <span data-rw-start="862.24" data-rw-transcript-version="2">
 But are there other signals and methods
 </span>
 <span data-rw-start="864" data-rw-transcript-version="2">
 that we can use to learn these powerful
 </span>
 <span data-rw-start="866" data-rw-transcript-version="2">
 internal representations that we need to
 </span>
 <span data-rw-start="868.399" data-rw-transcript-version="2">
 build intelligent systems?
 </span>
</p>
<p>
 <span data-rw-start="870.56" data-rw-transcript-version="2">
 Simultaneously we started realizing in
 </span>
 <span data-rw-start="873.36" data-rw-transcript-version="2">
 the, you know, around
 </span>
 <span data-rw-start="876.32" data-rw-transcript-version="2">
 2017-18, that uh, the best system to
 </span>
 <span data-rw-start="880.8" data-rw-transcript-version="2">
 learn representations of images are
 </span>
 <span data-rw-start="883.36" data-rw-transcript-version="2">
 systems that do not are not generative.
 </span>
 <span data-rw-start="886" data-rw-transcript-version="2">
 They don't reconstruct, they, you
 </span>
 <span data-rw-start="888.56" data-rw-transcript-version="2">
 know, you, you, you get an image and you
 </span>
 <span data-rw-start="891.12" data-rw-transcript-version="2">
 run it to an encoder, and then you try to
 </span>
 <span data-rw-start="893.76" data-rw-transcript-version="2">
 kind of coerce this encoder to extract as
 </span>
 <span data-rw-start="896.72" data-rw-transcript-version="2">
 much information as possible with
 </span>
 <span data-rw-start="898.16" data-rw-transcript-version="2">
 certain properties. So, for example, you
 </span>
 <span data-rw-start="900.56" data-rw-transcript-version="2">
 take two images of the same scene, or you
 </span>
 <span data-rw-start="903.04" data-rw-transcript-version="2">
 take an image and you corrupt it or
 </span>
 <span data-rw-start="904.48" data-rw-transcript-version="2">
 transform it in some ways. You run them
 </span>
</p>
<p>
 <span data-rw-start="908.48" data-rw-transcript-version="2">
 System, the representation, whatever you
 </span>
 <span data-rw-start="910.56" data-rw-transcript-version="2">
 extract to really be the same for those
 </span>
 <span data-rw-start="912" data-rw-transcript-version="2">
 two images because they semantically
 </span>
 <span data-rw-start="914" data-rw-transcript-version="2">
 represent the same thing. Um, and I've
 </span>
 <span data-rw-start="917.04" data-rw-transcript-version="2">
 been working on things like this since
 </span>
 <span data-rw-start="918.24" data-rw-transcript-version="2">
 the '90s. So, this is not a new idea. This
 </span>
 <span data-rw-start="920.959" data-rw-transcript-version="2">
 this idea—joint embedding—we used to
 </span>
 <span data-rw-start="922.959" data-rw-transcript-version="2">
 call this Siamese neural net. The method
 </span>
 <span data-rw-start="925.519" data-rw-transcript-version="2">
 Yan is referring to here, Siamese
 </span>
 <span data-rw-start="927.44" data-rw-transcript-version="2">
 networks, was created by Yan and his
 </span>
 <span data-rw-start="929.68" data-rw-transcript-version="2">
 collaborators at Bell Labs in the early
 </span>
 <span data-rw-start="931.76" data-rw-transcript-version="2">
 1990s when developing systems to detect
 </span>
 <span data-rw-start="934.639" data-rw-transcript-version="2">
 fraudulent signatures.
 </span>
</p>
<p>
 <span data-rw-start="937.199" data-rw-transcript-version="2">
 The system worked by passing a pair of
 </span>
 <span data-rw-start="939.04" data-rw-transcript-version="2">
 signature images into two copies of the
 </span>
 <span data-rw-start="941.279" data-rw-transcript-version="2">
 same neural network. The network copies
 </span>
 <span data-rw-start="944" data-rw-transcript-version="2">
 were not trained to generate any kind of
 </span>
 <span data-rw-start="945.76" data-rw-transcript-version="2">
 data. Instead, they output vectors of
 </span>
 <span data-rw-start="948.16" data-rw-transcript-version="2">
 numbers, often referred to as embedding
 </span>
 <span data-rw-start="950.48" data-rw-transcript-version="2">
 vectors. These network copies were
 </span>
 <span data-rw-start="952.959" data-rw-transcript-version="2">
 trained on two types of examples.
 </span>
 <span data-rw-start="955.68" data-rw-transcript-version="2">
 Positive examples that contain a
 </span>
 <span data-rw-start="957.12" data-rw-transcript-version="2">
 reference signature and a nonfraudulent
 </span>
 <span data-rw-start="959.199" data-rw-transcript-version="2">
 signature. So, these are by the same
 </span>
 <span data-rw-start="960.959" data-rw-transcript-version="2">
 person. And negative examples that
 </span>
 <span data-rw-start="963.44" data-rw-transcript-version="2">
 Contain a reference signature and a
 </span>
 <span data-rw-start="965.04" data-rw-transcript-version="2">
 fraudulent signature.
 </span>
</p>
<p>
 <span data-rw-start="967.36" data-rw-transcript-version="2">
 For fraudulent examples, the network
 </span>
 <span data-rw-start="969.44" data-rw-transcript-version="2">
 copies are trained to produce embedding
 </span>
 <span data-rw-start="971.12" data-rw-transcript-version="2">
 vectors that are maximally different.
 </span>
 <span data-rw-start="973.6" data-rw-transcript-version="2">
 And for positive examples, produce
 </span>
 <span data-rw-start="975.279" data-rw-transcript-version="2">
 embedding vectors that are maximally
 </span>
 <span data-rw-start="976.959" data-rw-transcript-version="2">
 similar.
 </span>
 <span data-rw-start="978.8" data-rw-transcript-version="2">
 When a new signature comes along, we can
 </span>
 <span data-rw-start="980.72" data-rw-transcript-version="2">
 pass it into our network to compute an
 </span>
 <span data-rw-start="982.399" data-rw-transcript-version="2">
 embedding vector and compare it to the
 </span>
 <span data-rw-start="984.56" data-rw-transcript-version="2">
 embedding vector produced from our
 </span>
 <span data-rw-start="986.079" data-rw-transcript-version="2">
 reference signature. If the resulting
 </span>
 <span data-rw-start="988.48" data-rw-transcript-version="2">
 embedding vectors are not similar
 </span>
 <span data-rw-start="990.16" data-rw-transcript-version="2">
 enough, the signature is detected as
 </span>
 <span data-rw-start="992.48" data-rw-transcript-version="2">
 fraudulent.
 </span>
 <span data-rw-start="994.079" data-rw-transcript-version="2">
 By jointly embedding our signatures, our
 </span>
 <span data-rw-start="996.48" data-rw-transcript-version="2">
 Siamese network learns a very useful
 </span>
 <span data-rw-start="998.399" data-rw-transcript-version="2">
 internal representation of the images of
 </span>
 <span data-rw-start="1000.399" data-rw-transcript-version="2">
 our signatures, notably without learning
 </span>
 <span data-rw-start="1002.959" data-rw-transcript-version="2">
 to predict or generate any actual
 </span>
 <span data-rw-start="1004.959" data-rw-transcript-version="2">
 signature images. As a GPT-based
 </span>
 <span data-rw-start="1007.44" data-rw-transcript-version="2">
 approach would
 </span>
 <span data-rw-start="1009.44" data-rw-transcript-version="2">
 joint embeddings offer a potentially
 </span>
 <span data-rw-start="1011.12" data-rw-transcript-version="2">
 viable solution to our blurry video
 </span>
 <span data-rw-start="1013.199" data-rw-transcript-version="2">
 Problem. As Yan explains,
 </span>
 <span data-rw-start="1015.759" data-rw-transcript-version="2">
 &gt;&gt; You, you get an image and you run it to
 </span>
 <span data-rw-start="1018.32" data-rw-transcript-version="2">
 an encoder and then you try to kind of
 </span>
</p>
<p>
 <span data-rw-start="1020.959" data-rw-transcript-version="2">
 coerce this encoder to extract as much
 </span>
 <span data-rw-start="1023.68" data-rw-transcript-version="2">
 information as possible with certain
 </span>
 <span data-rw-start="1025.28" data-rw-transcript-version="2">
 properties. So, for example, you take two
 </span>
 <span data-rw-start="1027.76" data-rw-transcript-version="2">
 images of the same scene, or you take an
 </span>
 <span data-rw-start="1030.16" data-rw-transcript-version="2">
 image and you corrupt it or transform it
 </span>
 <span data-rw-start="1031.76" data-rw-transcript-version="2">
 in some ways. You run them both through
 </span>
 <span data-rw-start="1033.76" data-rw-transcript-version="2">
 encoders, and you tell the system the
 </span>
 <span data-rw-start="1036.24" data-rw-transcript-version="2">
 representation — whatever you extract
 </span>
 <span data-rw-start="1037.76" data-rw-transcript-version="2">
 should really be the same for those two
 </span>
 <span data-rw-start="1038.959" data-rw-transcript-version="2">
 images because they semantically
 </span>
 <span data-rw-start="1040.799" data-rw-transcript-version="2">
 represent the same thing. So, the idea
 </span>
 <span data-rw-start="1042.799" data-rw-transcript-version="2">
 here is that we sidestep the blurry
 </span>
 <span data-rw-start="1044.559" data-rw-transcript-version="2">
 video problem we saw with generative
 </span>
 <span data-rw-start="1046.24" data-rw-transcript-version="2">
 models by using a joint embedding
 </span>
 <span data-rw-start="1048.88" data-rw-transcript-version="2">
 architecture to map copies of images or
 </span>
 <span data-rw-start="1051.76" data-rw-transcript-version="2">
 videos with one or both corrupted or
 </span>
 <span data-rw-start="1054.32" data-rw-transcript-version="2">
 transformed to similar embedding
 </span>
 <span data-rw-start="1056.64" data-rw-transcript-version="2">
 vectors. This trained model will ideally
 </span>
 <span data-rw-start="1059.44" data-rw-transcript-version="2">
 learn a useful internal representation
 </span>
 <span data-rw-start="1061.2" data-rw-transcript-version="2">
 of images or video that we can repurpose
 </span>
 <span data-rw-start="1064.16" data-rw-transcript-version="2">
 for other tasks, just as GPT models learn
 </span>
 <span data-rw-start="1067.36" data-rw-transcript-version="2">
 internal representations during
 </span>
 <span data-rw-start="1068.88" data-rw-transcript-version="2">
 Pre-training that can be adapted into AI
 </span>
 <span data-rw-start="1071.44" data-rw-transcript-version="2">
 assistant behaviors.
 </span>
</p>
<p>
 <span data-rw-start="1074" data-rw-transcript-version="2">
 However, this joint embedding strategy
 </span>
 <span data-rw-start="1075.84" data-rw-transcript-version="2">
 has a huge problem. Since we're training
 </span>
 <span data-rw-start="1078.64" data-rw-transcript-version="2">
 our network to make the embeddings of
 </span>
 <span data-rw-start="1080.32" data-rw-transcript-version="2">
 our original and corrupted images or
 </span>
 <span data-rw-start="1082.32" data-rw-transcript-version="2">
 videos as similar as possible, the
 </span>
 <span data-rw-start="1084.96" data-rw-transcript-version="2">
 network can find a trivial solution
 </span>
 <span data-rw-start="1087.44" data-rw-transcript-version="2">
 where it simply returns the same
 </span>
 <span data-rw-start="1088.96" data-rw-transcript-version="2">
 embedding vector for any input that we
 </span>
 <span data-rw-start="1091.12" data-rw-transcript-version="2">
 pass in. If our network learns to
 </span>
 <span data-rw-start="1093.52" data-rw-transcript-version="2">
 output, for example, a vector of all
 </span>
 <span data-rw-start="1095.52" data-rw-transcript-version="2">
 ones for any input, then the network
 </span>
 <span data-rw-start="1098" data-rw-transcript-version="2">
 will return all ones for a corrupted and
 </span>
 <span data-rw-start="1100.16" data-rw-transcript-version="2">
 non-corrupted view of the same image,
 </span>
 <span data-rw-start="1102.88" data-rw-transcript-version="2">
 maximizing the resulting similarity, but
 </span>
 <span data-rw-start="1105.039" data-rw-transcript-version="2">
 without actually learning anything
 </span>
 <span data-rw-start="1106.64" data-rw-transcript-version="2">
 useful.
 </span>
</p>
<p>
 <span data-rw-start="1108.32" data-rw-transcript-version="2">
 This problem is known as representation
 </span>
 <span data-rw-start="1110.24" data-rw-transcript-version="2">
 collapse.
 </span>
 <span data-rw-start="1111.919" data-rw-transcript-version="2">
 In Lacun's original Siamese network
 </span>
 <span data-rw-start="1113.84" data-rw-transcript-version="2">
 approach, the team used what’s now known
 </span>
 <span data-rw-start="1116.32" data-rw-transcript-version="2">
 as contrastive learning to avoid
 </span>
 <span data-rw-start="1118.48" data-rw-transcript-version="2">
 representation collapse, giving the
 </span>
 <span data-rw-start="1121.039" data-rw-transcript-version="2">
 network both positive and negative
 </span>
 <span data-rw-start="1122.88" data-rw-transcript-version="2">
 examples.
 </span>
</p>
<p>
 <span data-rw-start="1124.559" data-rw-transcript-version="2">
 It turns out we can apply the same
 </span>
 <span data-rw-start="1126.16" data-rw-transcript-version="2">
 contrastive approach to images and
 </span>
 <span data-rw-start="1127.919" data-rw-transcript-version="2">
 video, training our network to output
 </span>
 <span data-rw-start="1130.48" data-rw-transcript-version="2">
 similar embeddings for views of the same
 </span>
 <span data-rw-start="1132.32" data-rw-transcript-version="2">
 underlying images or videos and
 </span>
 <span data-rw-start="1134.4" data-rw-transcript-version="2">
 dissimilar embeddings for different
 </span>
 <span data-rw-start="1136.08" data-rw-transcript-version="2">
 images or video. These contrastive
 </span>
 <span data-rw-start="1138.799" data-rw-transcript-version="2">
 methods have been successfully
 </span>
 <span data-rw-start="1139.919" data-rw-transcript-version="2">
 implemented on images and videos, but
 </span>
 <span data-rw-start="1142.559" data-rw-transcript-version="2">
 can run into issues when they're scaled
 </span>
 <span data-rw-start="1144.16" data-rw-transcript-version="2">
 up, requiring large amounts of
 </span>
 <span data-rw-start="1146.16" data-rw-transcript-version="2">
 computation and many negative examples
 </span>
 <span data-rw-start="1148.24" data-rw-transcript-version="2">
 to learn meaningful representations. And
 </span>
 <span data-rw-start="1150.799" data-rw-transcript-version="2">
 Lacun has argued that in the worst case,
 </span>
 <span data-rw-start="1153.36" data-rw-transcript-version="2">
 the number of contrastive samples may
 </span>
 <span data-rw-start="1155.36" data-rw-transcript-version="2">
 grow exponentially with the dimension of
 </span>
 <span data-rw-start="1157.28" data-rw-transcript-version="2">
 the representation.
 </span>
</p>
<p>
 <span data-rw-start="1159.28" data-rw-transcript-version="2">
 By the end of the 2010s, it was clear to
 </span>
 <span data-rw-start="1161.76" data-rw-transcript-version="2">
 Lun and others that using generative
 </span>
 <span data-rw-start="1163.919" data-rw-transcript-version="2">
 models to fully reconstruct images and
 </span>
 <span data-rw-start="1166" data-rw-transcript-version="2">
 video was not a good strategy for
 </span>
 <span data-rw-start="1168.16" data-rw-transcript-version="2">
 self-supervised learning. But there
 </span>
 <span data-rw-start="1170.4" data-rw-transcript-version="2">
 wasn't a straightforward solution to the
 </span>
 <span data-rw-start="1172.16" data-rw-transcript-version="2">
 representation collapse problem that
 </span>
 <span data-rw-start="1174.48" data-rw-transcript-version="2">
 Would allow joint embedding
 </span>
 <span data-rw-start="1175.679" data-rw-transcript-version="2">
 architectures to learn the same level of
 </span>
 <span data-rw-start="1177.76" data-rw-transcript-version="2">
 powerful and general internal
 </span>
 <span data-rw-start="1179.36" data-rw-transcript-version="2">
 representations that large language
 </span>
 <span data-rw-start="1181.44" data-rw-transcript-version="2">
 models were enjoying.
 </span>
</p>
<p>
 <span data-rw-start="1183.2" data-rw-transcript-version="2">
 &gt;&gt; And so it was pretty clear that
 </span>
 <span data-rw-start="1184.88" data-rw-transcript-version="2">
 reconstruction was a bad idea for uh
 </span>
 <span data-rw-start="1187.52" data-rw-transcript-version="2">
 signals like like images and
 </span>
 <span data-rw-start="1190.24" data-rw-transcript-version="2">
 &gt;&gt; a fortory for video.
 </span>
 <span data-rw-start="1192.64" data-rw-transcript-version="2">
 And
 </span>
 <span data-rw-start="1194.16" data-rw-transcript-version="2">
 I had a bit of an epiphany because uh
 </span>
 <span data-rw-start="1197.84" data-rw-transcript-version="2">
 the uh the the methods that we were
 </span>
 <span data-rw-start="1201.28" data-rw-transcript-version="2">
 using to train those joint emitting
 </span>
 <span data-rw-start="1202.72" data-rw-transcript-version="2">
 architectures were kind of hacks a
 </span>
 <span data-rw-start="1204.48" data-rw-transcript-version="2">
 little bit until um I did some work with
 </span>
 <span data-rw-start="1209.52" data-rw-transcript-version="2">
 a couple postdocs at at Meta, particularly
 </span>
 <span data-rw-start="1212.799" data-rw-transcript-version="2">
 a guy called Stefan Deni who uh came up
 </span>
 <span data-rw-start="1216.4" data-rw-transcript-version="2">
 with a technique called Ballot twin. So
 </span>
 <span data-rw-start="1218.559" data-rw-transcript-version="2">
 it's based on an old idea in uh in
 </span>
 <span data-rw-start="1221.919" data-rw-transcript-version="2">
 computational noise science in machine
 </span>
 <span data-rw-start="1223.52" data-rw-transcript-version="2">
 learning that Jeffington also played on
 </span>
 <span data-rw-start="1225.44" data-rw-transcript-version="2">
 with similar ideas which is that you you
 </span>
 <span data-rw-start="1227.679" data-rw-transcript-version="2">
 should have time to have some measure of
 </span>
 <span data-rw-start="1230" data-rw-transcript-version="2">
 information content and try to maximize
 </span>
 <span data-rw-start="1231.84" data-rw-transcript-version="2">
 that and there's some real world work by
 </span>
 <span data-rw-start="1235.039" data-rw-transcript-version="2">
 Uh, by Barlo about is a famous
 </span>
 <span data-rw-start="1238.88" data-rw-transcript-version="2">
 computational neuroscientist and right
 </span>
 <span data-rw-start="1240.96" data-rw-transcript-version="2">
 &gt;&gt; theoretical neuroscientist.
 </span>
</p>
<p>
 <span data-rw-start="1242.4" data-rw-transcript-version="2">
 &gt;&gt; Here, Jan is referencing the work of
 </span>
 <span data-rw-start="1244.08" data-rw-transcript-version="2">
 Horus Barlo, who hypothesized in 1961 one
 </span>
 <span data-rw-start="1248.24" data-rw-transcript-version="2">
 that the neurons in animal and human
 </span>
 <span data-rw-start="1250.08" data-rw-transcript-version="2">
 vision systems operate by reducing
 </span>
 <span data-rw-start="1252.48" data-rw-transcript-version="2">
 redundant information between neurons.
 </span>
</p>
<p>
 <span data-rw-start="1255.76" data-rw-transcript-version="2">
 Stefan Deni, a postdoctoral researcher, was working
 </span>
 <span data-rw-start="1258.4" data-rw-transcript-version="2">
 with in 2020 and was familiar with Barlo's
 </span>
 <span data-rw-start="1261.12" data-rw-transcript-version="2">
 work and proposed that one way to avoid
 </span>
 <span data-rw-start="1263.76" data-rw-transcript-version="2">
 representation collapse could be to
 </span>
 <span data-rw-start="1265.919" data-rw-transcript-version="2">
 apply Barlo's idea to the outputs of
 </span>
 <span data-rw-start="1268.159" data-rw-transcript-version="2">
 their networks.
 </span>
</p>
<p>
 <span data-rw-start="1270" data-rw-transcript-version="2">
 In the joint embedding architectures
 </span>
 <span data-rw-start="1271.52" data-rw-transcript-version="2">
 we've been considering, our embedding
 </span>
 <span data-rw-start="1273.52" data-rw-transcript-version="2">
 vectors are produced by a final layer of
 </span>
 <span data-rw-start="1275.44" data-rw-transcript-version="2">
 artificial neurons in our embedding
 </span>
 <span data-rw-start="1277.28" data-rw-transcript-version="2">
 networks. So, if our embedding vectors
 </span>
 <span data-rw-start="1279.919" data-rw-transcript-version="2">
 are of length 128, then the output layer
 </span>
 <span data-rw-start="1282.96" data-rw-transcript-version="2">
 of each of our networks contains 128 neurons.
 </span>
 <span data-rw-start="1285.28" data-rw-transcript-version="2">
 If we pass in a batch of various images
 </span>
 <span data-rw-start="1289.36" data-rw-transcript-version="2">
 into each of our networks and plot the
 </span>
 <span data-rw-start="1291.679" data-rw-transcript-version="2">
 output activation of the first neuron as
 </span>
 <span data-rw-start="1293.919" data-rw-transcript-version="2">
 We step through our images, we can see
 </span>
 <span data-rw-start="1296.08" data-rw-transcript-version="2">
 that this neuron fires strongly on this
 </span>
 <span data-rw-start="1298.24" data-rw-transcript-version="2">
 first picture of a dog, not so much on
 </span>
 <span data-rw-start="1300.72" data-rw-transcript-version="2">
 this cat picture, and so on.
 </span>
</p>
<p>
 <span data-rw-start="1303.52" data-rw-transcript-version="2">
 Following our joint embedding approach,
 </span>
 <span data-rw-start="1305.84" data-rw-transcript-version="2">
 our network takes in a distorted view of
 </span>
 <span data-rw-start="1307.84" data-rw-transcript-version="2">
 the same batch of images.
 </span>
 <span data-rw-start="1310.32" data-rw-transcript-version="2">
 The whole point of our joint embedding
 </span>
 <span data-rw-start="1312" data-rw-transcript-version="2">
 architecture is to make the resulting
 </span>
 <span data-rw-start="1313.76" data-rw-transcript-version="2">
 embeddings of the same underlying images
 </span>
 <span data-rw-start="1315.84" data-rw-transcript-version="2">
 or videos similar. So we want the output
 </span>
 <span data-rw-start="1318.72" data-rw-transcript-version="2">
 of our first neuron in our second
 </span>
 <span data-rw-start="1320.32" data-rw-transcript-version="2">
 network to be similar to the output of
 </span>
 <span data-rw-start="1322.159" data-rw-transcript-version="2">
 our first neuron in our first network.
 </span>
 <span data-rw-start="1325.2" data-rw-transcript-version="2">
 In a standard joint embedding
 </span>
 <span data-rw-start="1326.64" data-rw-transcript-version="2">
 architecture, we would simply measure
 </span>
 <span data-rw-start="1328.559" data-rw-transcript-version="2">
 and maximize the similarity between
 </span>
 <span data-rw-start="1330.559" data-rw-transcript-version="2">
 these two vectors.
 </span>
 <span data-rw-start="1332.799" data-rw-transcript-version="2">
 However, as we've seen, this approach is
 </span>
 <span data-rw-start="1334.4" data-rw-transcript-version="2">
 susceptible to representation collapse.
 </span>
 <span data-rw-start="1337.12" data-rw-transcript-version="2">
 With the network simply learning to
 </span>
 <span data-rw-start="1338.48" data-rw-transcript-version="2">
 output the same values for any input
 </span>
 <span data-rw-start="1340.64" data-rw-transcript-version="2">
 image.
 </span>
 <span data-rw-start="1342.24" data-rw-transcript-version="2">
 But now applying Barllo's hypothesis as
 </span>
 <span data-rw-start="1344.799" data-rw-transcript-version="2">
 proposed by Stefan Deni, we should
 </span>
 <span data-rw-start="1347.039" data-rw-transcript-version="2">
 Reduce the redundancy between the
 </span>
 <span data-rw-start="1348.64" data-rw-transcript-version="2">
 outputs of different neurons.
 </span>
</p>
<p>
 <span data-rw-start="1351.28" data-rw-transcript-version="2">
 We have a bit of a choice to make here.
 </span>
 <span data-rw-start="1353.52" data-rw-transcript-version="2">
 We could compare the output of the first
 </span>
 <span data-rw-start="1355.2" data-rw-transcript-version="2">
 neuron in our first network to the
 </span>
 <span data-rw-start="1356.88" data-rw-transcript-version="2">
 output of our second neuron in our first
 </span>
 <span data-rw-start="1358.559" data-rw-transcript-version="2">
 network or to the output of the second
 </span>
 <span data-rw-start="1360.799" data-rw-transcript-version="2">
 neuron in our second network. The team
 </span>
 <span data-rw-start="1363.36" data-rw-transcript-version="2">
 chose to compare to the output of the
 </span>
 <span data-rw-start="1364.88" data-rw-transcript-version="2">
 second network. As we'll see, this
 </span>
 <span data-rw-start="1366.96" data-rw-transcript-version="2">
 results in a simpler implementation, and
 </span>
 <span data-rw-start="1369.12" data-rw-transcript-version="2">
 the team further notes in the appendix
 </span>
 <span data-rw-start="1370.64" data-rw-transcript-version="2">
 of their paper that in practice they
 </span>
 <span data-rw-start="1372.48" data-rw-transcript-version="2">
 didn't see much difference between these
 </span>
 <span data-rw-start="1373.84" data-rw-transcript-version="2">
 alternatives.
 </span>
</p>
<p>
 <span data-rw-start="1375.919" data-rw-transcript-version="2">
 Here's the output of the second neuron
 </span>
 <span data-rw-start="1377.6" data-rw-transcript-version="2">
 in our second model. To measure the
 </span>
 <span data-rw-start="1380.32" data-rw-transcript-version="2">
 redundancy between neuron outputs, the
 </span>
 <span data-rw-start="1382.64" data-rw-transcript-version="2">
 team computed the cross-correlation
 </span>
 <span data-rw-start="1384.64" data-rw-transcript-version="2">
 between these output vectors. This
 </span>
 <span data-rw-start="1387.2" data-rw-transcript-version="2">
 computation consists of scaling each
 </span>
 <span data-rw-start="1389.12" data-rw-transcript-version="2">
 vector and taking the dot product,
 </span>
 <span data-rw-start="1391.84" data-rw-transcript-version="2">
 resulting in a single number, the
 </span>
 <span data-rw-start="1393.919" data-rw-transcript-version="2">
 correlation, or more precisely, the
 </span>
 <span data-rw-start="1396.4" data-rw-transcript-version="2">
 Pearson correlation coefficient between
 </span>
 <span data-rw-start="1398.64" data-rw-transcript-version="2">
 Our vectors. To reduce the redundancy
 </span>
 <span data-rw-start="1401.36" data-rw-transcript-version="2">
 between our neurons, as proposed by
 </span>
 <span data-rw-start="1402.96" data-rw-transcript-version="2">
 Barlo, we want this correlation to be
 </span>
 <span data-rw-start="1405.36" data-rw-transcript-version="2">
 close to zero. If we arrange the neuron
 </span>
 <span data-rw-start="1408.559" data-rw-transcript-version="2">
 outputs of our first encoder vertically,
 </span>
 <span data-rw-start="1410.799" data-rw-transcript-version="2">
 and the outputs of our second encoder,
 </span>
 <span data-rw-start="1412.559" data-rw-transcript-version="2">
 horizontally, we can compute and place
 </span>
 <span data-rw-start="1415.12" data-rw-transcript-version="2">
 the correlations between all pairs of
 </span>
 <span data-rw-start="1417.039" data-rw-transcript-version="2">
 neurons into a single matrix. This
 </span>
 <span data-rw-start="1419.919" data-rw-transcript-version="2">
 cross-correlation matrix has one row for
 </span>
 <span data-rw-start="1422.24" data-rw-transcript-version="2">
 each output neuron in our first encoder,
 </span>
 <span data-rw-start="1424.64" data-rw-transcript-version="2">
 and one column for each output neuron in
 </span>
 <span data-rw-start="1426.799" data-rw-transcript-version="2">
 our second encoder. The elements along
 </span>
 <span data-rw-start="1429.44" data-rw-transcript-version="2">
 the diagonal capture the correlations,
 </span>
 <span data-rw-start="1431.28" data-rw-transcript-version="2">
 between corresponding neurons.
 </span>
</p>
<p>
 <span data-rw-start="1434.159" data-rw-transcript-version="2">
 Since the whole idea here of this joint
 </span>
 <span data-rw-start="1435.919" data-rw-transcript-version="2">
 embedding architecture is to produce
 </span>
 <span data-rw-start="1437.52" data-rw-transcript-version="2">
 similar outputs for distorted versions
 </span>
 <span data-rw-start="1439.6" data-rw-transcript-version="2">
 of the same image, we want the
 </span>
 <span data-rw-start="1441.52" data-rw-transcript-version="2">
 corresponding neurons in our two
 </span>
 <span data-rw-start="1443.039" data-rw-transcript-version="2">
 encoders to have high correlations.
 </span>
 <span data-rw-start="1446.24" data-rw-transcript-version="2">
 Alternatively, all of the off-diagonal
 </span>
 <span data-rw-start="1448.32" data-rw-transcript-version="2">
 entries in our cross-correlation matrix
 </span>
 <span data-rw-start="1450.48" data-rw-transcript-version="2">
 correspond to different neurons in our
 </span>
 <span data-rw-start="1452.4" data-rw-transcript-version="2">
 two encoders.
 </span>
</p>
<p>
 <span data-rw-start="1454.159" data-rw-transcript-version="2">
 And following Barlo's hypothesis, we
 </span>
 <span data-rw-start="1456.64" data-rw-transcript-version="2">
 want to reduce the redundancy between
 </span>
 <span data-rw-start="1458.64" data-rw-transcript-version="2">
 these neurons. So we want these
 </span>
 <span data-rw-start="1460.799" data-rw-transcript-version="2">
 correlations to be zero. So ideally, our
 </span>
 <span data-rw-start="1464.08" data-rw-transcript-version="2">
 cross-correlation matrix looks like the
 </span>
 <span data-rw-start="1466.24" data-rw-transcript-version="2">
 identity matrix.
 </span>
 <span data-rw-start="1468.72" data-rw-transcript-version="2">
 Deni Lacun and their collaborators
 </span>
 <span data-rw-start="1470.559" data-rw-transcript-version="2">
 designed a new loss function for their
 </span>
 <span data-rw-start="1472.48" data-rw-transcript-version="2">
 joint embedding architecture that
 </span>
 <span data-rw-start="1474.559" data-rw-transcript-version="2">
 measured the deviation of their
 </span>
 <span data-rw-start="1476" data-rw-transcript-version="2">
 cross-correlation matrix from the identity
 </span>
 <span data-rw-start="1478.4" data-rw-transcript-version="2">
 matrix.
 </span>
 <span data-rw-start="1479.919" data-rw-transcript-version="2">
 Their new method, which they called Barlo
 </span>
 <span data-rw-start="1482" data-rw-transcript-version="2">
 twins, worked surprisingly well, avoiding
 </span>
 <span data-rw-start="1485.2" data-rw-transcript-version="2">
 representation collapse while learning a
 </span>
 <span data-rw-start="1487.279" data-rw-transcript-version="2">
 powerful internal representation of the
 </span>
 <span data-rw-start="1489.2" data-rw-transcript-version="2">
 images that it was trained on.
 </span>
 <span data-rw-start="1492.4" data-rw-transcript-version="2">
 The team used a few different methods to
 </span>
 <span data-rw-start="1494.24" data-rw-transcript-version="2">
 measure the quality of these internal
 </span>
 <span data-rw-start="1495.919" data-rw-transcript-version="2">
 representations.
 </span>
 <span data-rw-start="1498.4" data-rw-transcript-version="2">
 Earlier, we saw how by using
 </span>
 <span data-rw-start="1500.159" data-rw-transcript-version="2">
 self-supervised pre-training, GPT-1 was
 </span>
 <span data-rw-start="1503.039" data-rw-transcript-version="2">
 able to outperform purely supervised
 </span>
 <span data-rw-start="1505.039" data-rw-transcript-version="2">
 models that had been adapted to specific
 </span>
 <span data-rw-start="1507.039" data-rw-transcript-version="2">
 language tasks.
 </span>
</p>
<p>
 <span data-rw-start="1509.679" data-rw-transcript-version="2">
 For vision tasks, one of the most
 </span>
 <span data-rw-start="1511.6" data-rw-transcript-version="2">
 important benchmarks at the time was
 </span>
 <span data-rw-start="1513.44" data-rw-transcript-version="2">
 accuracy on the ImageNet data set. This
 </span>
 <span data-rw-start="1516.64" data-rw-transcript-version="2">
 is the same image classification data
 </span>
 <span data-rw-start="1518.48" data-rw-transcript-version="2">
 set that the AlexNet model had shown
 </span>
 <span data-rw-start="1520.4" data-rw-transcript-version="2">
 breakthrough performance on back in
 </span>
 <span data-rw-start="1522" data-rw-transcript-version="2">
 2012. The original AlexNet paper
 </span>
 <span data-rw-start="1524.799" data-rw-transcript-version="2">
 achieved an accuracy of 59.3% on the
 </span>
 <span data-rw-start="1527.679" data-rw-transcript-version="2">
 ImageNet validation set. To compare the
 </span>
 <span data-rw-start="1530.559" data-rw-transcript-version="2">
 self-supervised Barlo twins approach to
 </span>
 <span data-rw-start="1533.279" data-rw-transcript-version="2">
 fully supervised models like AlexNet,
 </span>
 <span data-rw-start="1536.08" data-rw-transcript-version="2">
 the team used a common approach known as
 </span>
 <span data-rw-start="1538.08" data-rw-transcript-version="2">
 a linear probe, where a single layer of
 </span>
 <span data-rw-start="1541.12" data-rw-transcript-version="2">
 neurons are tacked onto the output of
 </span>
 <span data-rw-start="1543.2" data-rw-transcript-version="2">
 the Barlo twins trained encoder model
 </span>
 <span data-rw-start="1546.24" data-rw-transcript-version="2">
 and trained using supervised learning to
 </span>
 <span data-rw-start="1548.32" data-rw-transcript-version="2">
 classify the ImageNet data set.
 </span>
 <span data-rw-start="1551.12" data-rw-transcript-version="2">
 Importantly, the main encoder model is
 </span>
 <span data-rw-start="1553.2" data-rw-transcript-version="2">
 frozen during this training process.
 </span>
 <span data-rw-start="1556.32" data-rw-transcript-version="2">
 So the simple linear probe is
 </span>
 <span data-rw-start="1558" data-rw-transcript-version="2">
 effectively adapting the Barlo twins
 </span>
 <span data-rw-start="1560.08" data-rw-transcript-version="2">
 encoders' learned representation to solve
 </span>
 <span data-rw-start="1562.96" data-rw-transcript-version="2">
 the ImageNet classification task.
 </span>
 <span data-rw-start="1565.84" data-rw-transcript-version="2">
 Impressively, the frozen Barlo twins
 </span>
 <span data-rw-start="1567.679" data-rw-transcript-version="2">
 encoder with a linear probe achieved an
 </span>
 <span data-rw-start="1570.159" data-rw-transcript-version="2">
 Imageet accuracy of 73.2%.
 </span>
</p>
<p>
 <span data-rw-start="1573.919" data-rw-transcript-version="2">
 Outperforming the original fully
 </span>
 <span data-rw-start="1575.52" data-rw-transcript-version="2">
 supervised AlexNet model by over 10
 </span>
 <span data-rw-start="1577.84" data-rw-transcript-version="2">
 percentage points.
 </span>
 <span data-rw-start="1579.84" data-rw-transcript-version="2">
 However, in the nine years from the
 </span>
 <span data-rw-start="1581.44" data-rw-transcript-version="2">
 AlexNet paper in 2012 to the Barlo twins
 </span>
 <span data-rw-start="1584.64" data-rw-transcript-version="2">
 paper in 2021,
 </span>
 <span data-rw-start="1586.64" data-rw-transcript-version="2">
 fully supervised approaches had made
 </span>
 <span data-rw-start="1588.4" data-rw-transcript-version="2">
 significant improvements over AlexNet.
 </span>
 <span data-rw-start="1591.12" data-rw-transcript-version="2">
 In 2020, a team at Google applied the
 </span>
 <span data-rw-start="1593.279" data-rw-transcript-version="2">
 transformer architecture to image
 </span>
 <span data-rw-start="1595.12" data-rw-transcript-version="2">
 classification,
 </span>
 <span data-rw-start="1596.799" data-rw-transcript-version="2">
 achieving a new state-of-the-art ImageNet
 </span>
 <span data-rw-start="1598.799" data-rw-transcript-version="2">
 accuracy of 88.6%.
 </span>
</p>
<p>
 <span data-rw-start="1602.24" data-rw-transcript-version="2">
 So, by 2021, thanks to the Barlo twins
 </span>
 <span data-rw-start="1605.279" data-rw-transcript-version="2">
 epiphany and other joint embedding
 </span>
 <span data-rw-start="1607.039" data-rw-transcript-version="2">
 approaches, self-supervised learning was
 </span>
 <span data-rw-start="1609.84" data-rw-transcript-version="2">
 advancing rapidly for vision tasks, but
 </span>
 <span data-rw-start="1612.96" data-rw-transcript-version="2">
 was still inferior to fully supervised
 </span>
 <span data-rw-start="1615.2" data-rw-transcript-version="2">
 methods. The general and clearly
 </span>
 <span data-rw-start="1617.84" data-rw-transcript-version="2">
 superior self-supervised generative
 </span>
 <span data-rw-start="1619.84" data-rw-transcript-version="2">
 pre-training methods in language that
 </span>
 <span data-rw-start="1622.159" data-rw-transcript-version="2">
 were fueling the rapid advancement of
 </span>
 <span data-rw-start="1624" data-rw-transcript-version="2">
 LLMs were still out of reach for image
 </span>
 <span data-rw-start="1626.799" data-rw-transcript-version="2">
 and video applications. And so it became
 </span>
 <span data-rw-start="1629.84" data-rw-transcript-version="2">
 Clear that this really was the right
 </span>
 <span data-rw-start="1632.72" data-rw-transcript-version="2">
 way to go. So we kind of, uh, after that
 </span>
 <span data-rw-start="1635.36" data-rw-transcript-version="2">
 published another version, a simplified
 </span>
</p>
<p>
 <span data-rw-start="1637.36" data-rw-transcript-version="2">
 version, basically, of Battle Twins called
 </span>
 <span data-rw-start="1639.2" data-rw-transcript-version="2">
 Vicrag, which turned out to be quite
 </span>
 <span data-rw-start="1641.52" data-rw-transcript-version="2">
 good. Uh, and then simultaneously, another
 </span>
 <span data-rw-start="1643.679" data-rw-transcript-version="2">
 group, some of our colleagues at Fair
 </span>
 <span data-rw-start="1645.2" data-rw-transcript-version="2">
 Paris, were working on, uh, similar
 </span>
 <span data-rw-start="1648.64" data-rw-transcript-version="2">
 methods, which eventually came to be
 </span>
 <span data-rw-start="1651.36" data-rw-transcript-version="2">
 known as Dino. Uh, Dino V1, V2, V3. Now I have
 </span>
 <span data-rw-start="1656.08" data-rw-transcript-version="2">
 a new version, which is not called Dino
 </span>
 <span data-rw-start="1658.32" data-rw-transcript-version="2">
 anymore, uh, and this is also a
 </span>
 <span data-rw-start="1660.72" data-rw-transcript-version="2">
 jettison, uh, technique. So, it's really
 </span>
 <span data-rw-start="1664.48" data-rw-transcript-version="2">
 clear, John, embedding
 </span>
 <span data-rw-start="1666.799" data-rw-transcript-version="2">
 was better for representation learning, you
 </span>
 <span data-rw-start="1669.6" data-rw-transcript-version="2">
 know, right?
 </span>
</p>
<p>
 <span data-rw-start="1670.24" data-rw-transcript-version="2">
 &gt;&gt;
 </span>
 <span data-rw-start="1672.72" data-rw-transcript-version="2">
 Self-supervised learning to, to, represent
 </span>
 <span data-rw-start="1673.679" data-rw-transcript-version="2">
 &gt;&gt; The Dino V3 paper released in August
 </span>
 <span data-rw-start="1676.559" data-rw-transcript-version="2">
 2025 marked an important turning point,
 </span>
 <span data-rw-start="1680.159" data-rw-transcript-version="2">
 achieving a very near state-of-the-art,
 </span>
 <span data-rw-start="1682" data-rw-transcript-version="2">
 image accuracy of 88.4%.
 </span>
 <span data-rw-start="1685.36" data-rw-transcript-version="2">
 Using a joint embedding architecture.
 </span>
</p>
<p>
 <span data-rw-start="1688.88" data-rw-transcript-version="2">
 As the authors say in their paper, all
 </span>
 <span data-rw-start="1691.6" data-rw-transcript-version="2">
 in all, this is the first time that a
 </span>
 <span data-rw-start="1693.279" data-rw-transcript-version="2">
 The self-supervised model has reached
 </span>
 <span data-rw-start="1695.039" data-rw-transcript-version="2">
 comparable results to weekly and
 </span>
 <span data-rw-start="1697.12" data-rw-transcript-version="2">
 supervised models on image
 </span>
 <span data-rw-start="1698.64" data-rw-transcript-version="2">
 classification.
 </span>
</p>
<p>
 <span data-rw-start="1700.48" data-rw-transcript-version="2">
 The quality of representations that Dino
 </span>
 <span data-rw-start="1703.12" data-rw-transcript-version="2">
 V3 is able to learn without access to
 </span>
 <span data-rw-start="1705.6" data-rw-transcript-version="2">
 any human-generated labels is
 </span>
 <span data-rw-start="1707.44" data-rw-transcript-version="2">
 astounding. Dino outputs an embedding
 </span>
 <span data-rw-start="1709.76" data-rw-transcript-version="2">
 vector for each patch of image that it
 </span>
 <span data-rw-start="1711.679" data-rw-transcript-version="2">
 analyzes. If I take this image of myself
 </span>
 <span data-rw-start="1715.12" data-rw-transcript-version="2">
 and take Dino's embedding vector from
 </span>
 <span data-rw-start="1717.039" data-rw-transcript-version="2">
 this image patch on my hand and compare
 </span>
 <span data-rw-start="1719.84" data-rw-transcript-version="2">
 this embedding vector to the rest of the
 </span>
 <span data-rw-start="1721.36" data-rw-transcript-version="2">
 patches in the image, visualizing how
 </span>
 <span data-rw-start="1723.679" data-rw-transcript-version="2">
 similar each patch is to the hand patch
 </span>
 <span data-rw-start="1726" data-rw-transcript-version="2">
 using a color map. Dino does a
 </span>
 <span data-rw-start="1728.32" data-rw-transcript-version="2">
 remarkably good job segmenting my hand
 </span>
 <span data-rw-start="1730.559" data-rw-transcript-version="2">
 from the background. Here's the same
 </span>
 <span data-rw-start="1732.96" data-rw-transcript-version="2">
 approach applied to a ball, a cat, and a
 </span>
 <span data-rw-start="1737.039" data-rw-transcript-version="2">
 book.
 </span>
</p>
<p>
 <span data-rw-start="1738.96" data-rw-transcript-version="2">
 Following the success of Barlo twins
 </span>
 <span data-rw-start="1740.88" data-rw-transcript-version="2">
 Vicreg and Dinov1, in 2022, Lun brought
 </span>
 <span data-rw-start="1744.799" data-rw-transcript-version="2">
 these and many other threads together
 </span>
 <span data-rw-start="1746.559" data-rw-transcript-version="2">
 into a 60-page position paper called a
 </span>
 <span data-rw-start="1749.44" data-rw-transcript-version="2">
 path towards autonomous machine
 </span>
 <span data-rw-start="1751.2" data-rw-transcript-version="2">
 Intelligence. Unlike the great majority
 </span>
 <span data-rw-start="1753.679" data-rw-transcript-version="2">
 of Lun's papers where he works on
 </span>
 <span data-rw-start="1756" data-rw-transcript-version="2">
 specific and technical pieces of machine
 </span>
 <span data-rw-start="1757.84" data-rw-transcript-version="2">
 learning theory or practice, a path
 </span>
 <span data-rw-start="1760.559" data-rw-transcript-version="2">
 towards autonomous machine intelligence
 </span>
 <span data-rw-start="1762.88" data-rw-transcript-version="2">
 takes a holistic first principles
 </span>
 <span data-rw-start="1764.88" data-rw-transcript-version="2">
 approach to how we should build
 </span>
 <span data-rw-start="1766.399" data-rw-transcript-version="2">
 intelligent machines. Lun begins by
 </span>
 <span data-rw-start="1769.36" data-rw-transcript-version="2">
 arguing that our current approaches to
 </span>
 <span data-rw-start="1770.96" data-rw-transcript-version="2">
 AI are nowhere near the capabilities of
 </span>
 <span data-rw-start="1773.279" data-rw-transcript-version="2">
 human learning, giving the example of a
 </span>
 <span data-rw-start="1776.08" data-rw-transcript-version="2">
 teenager that can learn to drive a car
 </span>
 <span data-rw-start="1777.52" data-rw-transcript-version="2">
 in around 20 hours of practice. How is
 </span>
 <span data-rw-start="1780.48" data-rw-transcript-version="2">
 it that we have those millions of hours
 </span>
 <span data-rw-start="1782.24" data-rw-transcript-version="2">
 of training data where we have we can
 </span>
 <span data-rw-start="1785.039" data-rw-transcript-version="2">
 train kind of level two system with it
 </span>
 <span data-rw-start="1787.039" data-rw-transcript-version="2">
 which is what Tesla is doing basically.
 </span>
</p>
<p>
 <span data-rw-start="1788.799" data-rw-transcript-version="2">
 &gt;&gt; Yeah.
 </span>
 <span data-rw-start="1789.12" data-rw-transcript-version="2">
 &gt;&gt; Um but
 </span>
 <span data-rw-start="1791.36" data-rw-transcript-version="2">
 &gt;&gt; nowhere near level three, four, five.
 </span>
 <span data-rw-start="1793.52" data-rw-transcript-version="2">
 Okay. Uh yet a 17-year-old can learn to
 </span>
 <span data-rw-start="1796.799" data-rw-transcript-version="2">
 drive in a few hours of practice. Like
 </span>
 <span data-rw-start="1798.399" data-rw-transcript-version="2">
 how does that happen, right? Shouldn't
 </span>
 <span data-rw-start="1800.159" data-rw-transcript-version="2">
 we figure out what the what's the secret
 </span>
 <span data-rw-start="1802.32" data-rw-transcript-version="2">
 there?
 </span>
</p>
<p>
 <span data-rw-start="1803.2" data-rw-transcript-version="2">
 &gt;&gt; And my guess about it is the secret is
 </span>
 <span data-rw-start="1805.6" data-rw-transcript-version="2">
 role models. Lacun's billion-dollar bet
 </span>
 <span data-rw-start="1808.559" data-rw-transcript-version="2">
 is that the missing piece of modern AI
 </span>
 <span data-rw-start="1810.48" data-rw-transcript-version="2">
 is world models. Models that make
 </span>
 <span data-rw-start="1813.36" data-rw-transcript-version="2">
 predictions about the physical world. As
 </span>
 <span data-rw-start="1816.24" data-rw-transcript-version="2">
 he says in his 2022 position paper,
 </span>
 <span data-rw-start="1819.039" data-rw-transcript-version="2">
 common sense can be seen as a collection
 </span>
 <span data-rw-start="1820.559" data-rw-transcript-version="2">
 of models of the world that can tell an
 </span>
 <span data-rw-start="1823.039" data-rw-transcript-version="2">
 agent what is likely, what is plausible,
 </span>
 <span data-rw-start="1825.679" data-rw-transcript-version="2">
 and what is impossible. Using such world
 </span>
 <span data-rw-start="1828.799" data-rw-transcript-version="2">
 models, animals can learn new skills
 </span>
 <span data-rw-start="1831.039" data-rw-transcript-version="2">
 with very few trials. They can predict
 </span>
 <span data-rw-start="1833.919" data-rw-transcript-version="2">
 the consequences of their actions. They
 </span>
 <span data-rw-start="1836.48" data-rw-transcript-version="2">
 can reason, plan, explore, and imagine
 </span>
 <span data-rw-start="1838.799" data-rw-transcript-version="2">
 new solutions to problems. Lung goes on
 </span>
 <span data-rw-start="1841.84" data-rw-transcript-version="2">
 to argue that joint embedding
 </span>
 <span data-rw-start="1843.279" data-rw-transcript-version="2">
 architectures offer the right foundation
 </span>
 <span data-rw-start="1845.6" data-rw-transcript-version="2">
 to build world models on top of.
 </span>
</p>
<p>
 <span data-rw-start="1848" data-rw-transcript-version="2">
 &gt;&gt; So, JPA means joint embedding predictive
 </span>
 <span data-rw-start="1850.48" data-rw-transcript-version="2">
 architecture and it's, you, you take an
 </span>
 <span data-rw-start="1853.84" data-rw-transcript-version="2">
 observation in the world, and then the
 </span>
 <span data-rw-start="1855.52" data-rw-transcript-version="2">
 next observation in the world. Uh, you
 </span>
 <span data-rw-start="1857.679" data-rw-transcript-version="2">
 run them through encoders. So this is
 </span>
 <span data-rw-start="1859.12" data-rw-transcript-version="2">
 like a joint embedding type architecture,
 </span>
 <span data-rw-start="1861.2" data-rw-transcript-version="2">
 and then you have a predictor that tries.
 </span>
</p>
<p>
 <span data-rw-start="1862.799" data-rw-transcript-version="2">
 To predict that the state at time t plus
 </span>
 <span data-rw-start="1864.64" data-rw-transcript-version="2">
 one from the state at time t, and you
 </span>
 <span data-rw-start="1866.72" data-rw-transcript-version="2">
 might condition this on an action, and
 </span>
 <span data-rw-start="1868.24" data-rw-transcript-version="2">
 now you have a world model.
 </span>
 <span data-rw-start="1869.6" data-rw-transcript-version="2">
 &gt;&gt; As a concrete example, instead of using a
 </span>
 <span data-rw-start="1872.24" data-rw-transcript-version="2">
 generative architecture to predict the
 </span>
 <span data-rw-start="1874.399" data-rw-transcript-version="2">
 pixel values in the next frame of video,
 </span>
 <span data-rw-start="1876.88" data-rw-transcript-version="2">
 we can map the video and next frame to
 </span>
 <span data-rw-start="1879.039" data-rw-transcript-version="2">
 embeddings and then train a predictor
 </span>
 <span data-rw-start="1881.36" data-rw-transcript-version="2">
 model to predict the embedding of the
 </span>
 <span data-rw-start="1883.2" data-rw-transcript-version="2">
 next frame, given the embedding of the
 </span>
 <span data-rw-start="1885.679" data-rw-transcript-version="2">
 video. In this implementation, the JEPA
 </span>
 <span data-rw-start="1888.72" data-rw-transcript-version="2">
 architecture frees the model of the
 </span>
 <span data-rw-start="1890.48" data-rw-transcript-version="2">
 intractable task of predicting every
 </span>
 <span data-rw-start="1893.279" data-rw-transcript-version="2">
 pixel in the next frame of video, and
 </span>
 <span data-rw-start="1895.679" data-rw-transcript-version="2">
 theoretically allows the predictor to
 </span>
 <span data-rw-start="1897.44" data-rw-transcript-version="2">
 focus on predicting only the salient
 </span>
 <span data-rw-start="1899.519" data-rw-transcript-version="2">
 features of the scene that make it
 </span>
 <span data-rw-start="1901.44" data-rw-transcript-version="2">
 through the encoder. Jan gives a nice
 </span>
 <span data-rw-start="1903.919" data-rw-transcript-version="2">
 example here. If you train a geology
 </span>
 <span data-rw-start="1906.32" data-rw-transcript-version="2">
 model, you know, to predict what's going
 </span>
 <span data-rw-start="1907.919" data-rw-transcript-version="2">
 to happen in a dash cam video, uh, it
 </span>
 <span data-rw-start="1911.039" data-rw-transcript-version="2">
 will spend most of its resources
 </span>
 <span data-rw-start="1912.559" data-rw-transcript-version="2">
 predicting the random motion of the
 </span>
 <span data-rw-start="1914.08" data-rw-transcript-version="2">
 leaves on the trees that border.
 </span>
</p>
<p>
 <span data-rw-start="1915.919" data-rw-transcript-version="2">
 The road, and those are things that
 </span>
 <span data-rw-start="1918.48" data-rw-transcript-version="2">
 are essentially not predictable, but
 </span>
 <span data-rw-start="1919.84" data-rw-transcript-version="2">
 they have a lot of pixels, you know,
 </span>
 <span data-rw-start="1921.76" data-rw-transcript-version="2">
 that move around.
 </span>
 <span data-rw-start="1923.039" data-rw-transcript-version="2">
 &gt;&gt; As Jan mentioned earlier, we can take
 </span>
 <span data-rw-start="1925.039" data-rw-transcript-version="2">
 Jeepo one step further by conditioning
 </span>
 <span data-rw-start="1927.039" data-rw-transcript-version="2">
 on actions. In the VJEPA 2 paper, which
 </span>
 <span data-rw-start="1930.399" data-rw-transcript-version="2">
 we'll dig into in part two, the team
 </span>
 <span data-rw-start="1932.88" data-rw-transcript-version="2">
 conditions a JEPA model on the action
 </span>
 <span data-rw-start="1934.799" data-rw-transcript-version="2">
 signals sent to a robot arm. So, the
 </span>
 <span data-rw-start="1938" data-rw-transcript-version="2">
 JEPA model sees a sequence of images of
 </span>
 <span data-rw-start="1940" data-rw-transcript-version="2">
 the robot's arm and environment and then
 </span>
 <span data-rw-start="1942.559" data-rw-transcript-version="2">
 is trained to predict the embedding of
 </span>
 <span data-rw-start="1944.159" data-rw-transcript-version="2">
 the next video frame, but is also given
 </span>
 <span data-rw-start="1947.039" data-rw-transcript-version="2">
 the control signals that are sent to the
 </span>
 <span data-rw-start="1948.799" data-rw-transcript-version="2">
 robot arm. This allows the predictor to
 </span>
 <span data-rw-start="1951.519" data-rw-transcript-version="2">
 learn to predict how various control
 </span>
 <span data-rw-start="1953.44" data-rw-transcript-version="2">
 signals will change the robot arm's
 </span>
 <span data-rw-start="1955.36" data-rw-transcript-version="2">
 position in the embedded image.
 </span>
</p>
<p>
 <span data-rw-start="1958.72" data-rw-transcript-version="2">
 This learned world model can then be
 </span>
 <span data-rw-start="1960.64" data-rw-transcript-version="2">
 used for robot planning and control.
 </span>
 <span data-rw-start="1963.2" data-rw-transcript-version="2">
 Given an image of some goal state, for
 </span>
 <span data-rw-start="1965.679" data-rw-transcript-version="2">
 example, moving a cup off of a platform,
 </span>
 <span data-rw-start="1968.559" data-rw-transcript-version="2">
 this image is passed into the next frame
 </span>
 <span data-rw-start="1970.48" data-rw-transcript-version="2">
 encoder, resulting in an embedding of
 </span>
 <span data-rw-start="1972.96" data-rw-transcript-version="2">
 The goal state of the robot. From here,
 </span>
 <span data-rw-start="1975.6" data-rw-transcript-version="2">
 a control algorithm can be used to
 </span>
 <span data-rw-start="1977.519" data-rw-transcript-version="2">
 explore the world model's predictions
 </span>
 <span data-rw-start="1979.76" data-rw-transcript-version="2">
 given various hypothetical actions, and
 </span>
 <span data-rw-start="1982.88" data-rw-transcript-version="2">
 find a set of actions that will lead the
 </span>
 <span data-rw-start="1984.48" data-rw-transcript-version="2">
 model's predicted future state to match
 </span>
 <span data-rw-start="1986.48" data-rw-transcript-version="2">
 its goal state. As Jan says, this is
 </span>
 <span data-rw-start="1989.279" data-rw-transcript-version="2">
 really a new twist on an old idea.
 </span>
</p>
<p>
 <span data-rw-start="1991.84" data-rw-transcript-version="2">
 &gt;&gt; You build a model that gives you the
 </span>
 <span data-rw-start="1993.44" data-rw-transcript-version="2">
 state of the world at time t plus one as
 </span>
 <span data-rw-start="1995.039" data-rw-transcript-version="2">
 a function of the state of the world at
 </span>
 <span data-rw-start="1996.24" data-rw-transcript-version="2">
 time t and an action you imagine taking,
 </span>
 <span data-rw-start="1998.399" data-rw-transcript-version="2">
 or intervention or control, right? And
 </span>
 <span data-rw-start="2001.6" data-rw-transcript-version="2">
 then if you have this, you can predict
 </span>
 <span data-rw-start="2004.159" data-rw-transcript-version="2">
 the outcome of a sequence of actions, and
 </span>
 <span data-rw-start="2006.08" data-rw-transcript-version="2">
 you can, by optimization, figure
 </span>
 <span data-rw-start="2007.919" data-rw-transcript-version="2">
 out an optimal sequence of actions to
 </span>
 <span data-rw-start="2010.24" data-rw-transcript-version="2">
 arrive at a particular outcome.
 </span>
 <span data-rw-start="2013.12" data-rw-transcript-version="2">
 Right? This is classical optimal
 </span>
 <span data-rw-start="2014.72" data-rw-transcript-version="2">
 control. This is, you know, this is going
 </span>
 <span data-rw-start="2016.48" data-rw-transcript-version="2">
 back to the late 50s in the Soviet Union,
 </span>
 <span data-rw-start="2020.08" data-rw-transcript-version="2">
 early 60s in the West.
 </span>
</p>
<p>
 <span data-rw-start="2023.2" data-rw-transcript-version="2">
 &gt;&gt; Very classical stuff.
 </span>
 <span data-rw-start="2024.48" data-rw-transcript-version="2">
 &gt;&gt; Yeah.
 </span>
 <span data-rw-start="2025.2" data-rw-transcript-version="2">
 &gt;&gt; What is not classical is you learn the
 </span>
 <span data-rw-start="2027.6" data-rw-transcript-version="2">
 Model. You use machine learning to learn
 </span>
 <span data-rw-start="2029.76" data-rw-transcript-version="2">
 the model.
 </span>
</p>
<p>
 <span data-rw-start="2030.24" data-rw-transcript-version="2">
 &gt;&gt; Right. Yeah,
 </span>
 <span data-rw-start="2030.72" data-rw-transcript-version="2">
 &gt;&gt; what is even less classical is you learn
 </span>
 <span data-rw-start="2033.36" data-rw-transcript-version="2">
 a representation of the input that
 </span>
 <span data-rw-start="2036.799" data-rw-transcript-version="2">
 computes a state, an abstract state,
 </span>
 <span data-rw-start="2039.76" data-rw-transcript-version="2">
 representation, and you learn the
 </span>
 <span data-rw-start="2042.559" data-rw-transcript-version="2">
 model in that, uh, in that
 </span>
 <span data-rw-start="2045.039" data-rw-transcript-version="2">
 state. And that's JPA.
 </span>
</p>
<p>
 <span data-rw-start="2049.599" data-rw-transcript-version="2">
 But will Jeppa or other world model
 </span>
 <span data-rw-start="2051.599" data-rw-transcript-version="2">
 based approaches really overtake large
 </span>
 <span data-rw-start="2053.839" data-rw-transcript-version="2">
 language models since LeCun first
 </span>
 <span data-rw-start="2056.399" data-rw-transcript-version="2">
 proposed Jeppa in 2022? The architecture
 </span>
 <span data-rw-start="2059.359" data-rw-transcript-version="2">
 has been applied by various teams to a
 </span>
 <span data-rw-start="2061.679" data-rw-transcript-version="2">
 wide range of problems.
 </span>
</p>
<p>
 <span data-rw-start="2063.919" data-rw-transcript-version="2">
 How exactly do these models stack up? In
 </span>
 <span data-rw-start="2067.28" data-rw-transcript-version="2">
 part two, we'll dive deeper into VJeppa
 </span>
 <span data-rw-start="2069.44" data-rw-transcript-version="2">
 to get a sense of what's really
 </span>
 <span data-rw-start="2071.359" data-rw-transcript-version="2">
 happening inside the models' embedding
 </span>
 <span data-rw-start="2073.119" data-rw-transcript-version="2">
 space and see how VJA 2 fares as a
 </span>
 <span data-rw-start="2076.32" data-rw-transcript-version="2">
 robotics control algorithm against
 </span>
 <span data-rw-start="2078.56" data-rw-transcript-version="2">
 rapidly advancing VLA approaches.
 </span>
</p>
<p>
 <span data-rw-start="2081.76" data-rw-transcript-version="2">
 We'll also explore VLJA, which solves
 </span>
 <span data-rw-start="2084.639" data-rw-transcript-version="2">
 many of the same vision-language
 </span>
 <span data-rw-start="2086.159" data-rw-transcript-version="2">
 problems we solve today with multimodal.
 </span>
</p>
<p>
 <span data-rw-start="2088.159" data-rw-transcript-version="2">
 LLMs, but in a very different way, and
 </span>
 <span data-rw-start="2091.44" data-rw-transcript-version="2">
 with impressive results. Finally, we'll
 </span>
 <span data-rw-start="2093.76" data-rw-transcript-version="2">
 spend some time on an implementation of
 </span>
 <span data-rw-start="2095.2" data-rw-transcript-version="2">
 Jeepa called Layworld model. The Layworld
 </span>
 <span data-rw-start="2098.32" data-rw-transcript-version="2">
 model gives perhaps the most complete
 </span>
 <span data-rw-start="2100.079" data-rw-transcript-version="2">
 albeit early picture of what Jeepa-based
 </span>
 <span data-rw-start="2102.16" data-rw-transcript-version="2">
 systems can do. Until next time, I'll
 </span>
 <span data-rw-start="2105.04" data-rw-transcript-version="2">
 leave you with Yan's take. Okay, then
 </span>
 <span data-rw-start="2107.76" data-rw-transcript-version="2">
 let me make a controversial statement
 </span>
 <span data-rw-start="2110" data-rw-transcript-version="2">
 that, again, is going to get me a lot of
 </span>
 <span data-rw-start="2111.92" data-rw-transcript-version="2">
 friends in Silicon Valley. Um, I do not
 </span>
 <span data-rw-start="2115.2" data-rw-transcript-version="2">
 understand how you can even think of
 </span>
 <span data-rw-start="2117.92" data-rw-transcript-version="2">
 building an agentic system without an
 </span>
 <span data-rw-start="2121.2" data-rw-transcript-version="2">
 agentic system having the ability of
 </span>
 <span data-rw-start="2124.079" data-rw-transcript-version="2">
 predicting the consequences of its
 </span>
 <span data-rw-start="2125.68" data-rw-transcript-version="2">
 actions.
 </span>
</p>
<p>
 <span data-rw-start="2127.2" data-rw-transcript-version="2">
 &gt;&gt; Okay? And a VA doesn't, doesn't do that.
 </span>
 <span data-rw-start="2130.48" data-rw-transcript-version="2">
 &gt;&gt; Sure.
 </span>
</p>
<p>
 <span data-rw-start="2130.88" data-rw-transcript-version="2">
 &gt;&gt; Right. Airlines do not have world
 </span>
 <span data-rw-start="2132.4" data-rw-transcript-version="2">
 models. They cannot predict the
 </span>
 <span data-rw-start="2133.599" data-rw-transcript-version="2">
 consequences of their actions
 </span>
 <span data-rw-start="2134.8" data-rw-transcript-version="2">
 beforehand. They just take the action
 </span>
 <span data-rw-start="2136.96" data-rw-transcript-version="2">
 and then
 </span>
 <span data-rw-start="2139.28" data-rw-transcript-version="2">
 deluge, as, uh, you know, as some famous
 </span>
 <span data-rw-start="2143.68" data-rw-transcript-version="2">
 French kings said. So, uh, if you really
 </span>
 <span data-rw-start="2147.52" data-rw-transcript-version="2">
 Want to build reliable agentic systems,
 </span>
 <span data-rw-start="2150.48" data-rw-transcript-version="2">
 they absolutely have to be able to
 </span>
 <span data-rw-start="2152.079" data-rw-transcript-version="2">
 predict the consequences of their
 </span>
 <span data-rw-start="2153.44" data-rw-transcript-version="2">
 actions so that they can plan a sequence
 </span>
 <span data-rw-start="2155.839" data-rw-transcript-version="2">
 of actions to do something. First of all,
 </span>
 <span data-rw-start="2157.76" data-rw-transcript-version="2">
 to fulfill the task that they are
 </span>
 <span data-rw-start="2161.359" data-rw-transcript-version="2">
 being asked to fulfill, but also, uh,
 </span>
 <span data-rw-start="2164.8" data-rw-transcript-version="2">
 perhaps to, you know, guarantee some
 </span>
 <span data-rw-start="2166.32" data-rw-transcript-version="2">
 safety guard rails.
 </span>
</p>
<p>
 <span data-rw-start="2167.68" data-rw-transcript-version="2">
 &gt;&gt;Right.
 </span>
</p>
<p>
 <span data-rw-start="2168.56" data-rw-transcript-version="2">
 &gt;&gt;And the inference process now becomes a
 </span>
 <span data-rw-start="2170.88" data-rw-transcript-version="2">
 search, as opposed to just an
 </span>
 <span data-rw-start="2172.48" data-rw-transcript-version="2">
 autogressive prediction.
 </span>
 <span data-rw-start="2173.92" data-rw-transcript-version="2">
 &gt;&gt;Right. Uh, so that's a world model. That
 </span>
 <span data-rw-start="2176.96" data-rw-transcript-version="2">
 is the whole idea of a world model.
 </span>
 <span data-rw-start="2179.599" data-rw-transcript-version="2">
 &gt;&gt;If you enjoyed this video, check out the
 </span>
 <span data-rw-start="2181.68" data-rw-transcript-version="2">
 Welch Labs illustrated guide to AI. Its
 </span>
 <span data-rw-start="2185.04" data-rw-transcript-version="2">
 cover produces highly consistent Dino
 </span>
 <span data-rw-start="2187.359" data-rw-transcript-version="2">
 representations, so you know it has to
 </span>
 <span data-rw-start="2189.599" data-rw-transcript-version="2">
 be good. The book is beautifully
 </span>
 <span data-rw-start="2192.32" data-rw-transcript-version="2">
 illustrated and is a great way to dig
 </span>
 <span data-rw-start="2194.24" data-rw-transcript-version="2">
 deeper into many of the topics we
 </span>
 <span data-rw-start="2195.76" data-rw-transcript-version="2">
 touched on in this video. Chapter 5 on
 </span>
 <span data-rw-start="2198.72" data-rw-transcript-version="2">
 Alexnet is a great way to learn more
 </span>
 <span data-rw-start="2200.32" data-rw-transcript-version="2">
 about embedding vectors and the rise of
 </span>
 <span data-rw-start="2202.4" data-rw-transcript-version="2">
 Deep learning.
 </span>
</p>
<p>
 <span data-rw-start="2204.079" data-rw-transcript-version="2">
 Chapter six on neural scaling laws takes
 </span>
 <span data-rw-start="2206.4" data-rw-transcript-version="2">
 a deeper look at the fascinating buildup
 </span>
 <span data-rw-start="2208.48" data-rw-transcript-version="2">
 from GPT-1 to GPT-3 at OpenAI.
 </span>
 <span data-rw-start="2212.48" data-rw-transcript-version="2">
 Chapter 9 covers diffusion models, which
 </span>
 <span data-rw-start="2215.28" data-rw-transcript-version="2">
 are able to reconstruct highly accurate
 </span>
 <span data-rw-start="2217.44" data-rw-transcript-version="2">
 pixel-level representations of images
 </span>
 <span data-rw-start="2219.28" data-rw-transcript-version="2">
 and video, but with some notable
 </span>
 <span data-rw-start="2221.52" data-rw-transcript-version="2">
 trade-offs.
 </span>
</p>
<p>
 <span data-rw-start="2223.599" data-rw-transcript-version="2">
 Chapters 1 through 4 give some great
 </span>
 <span data-rw-start="2225.44" data-rw-transcript-version="2">
 background on all these topics, covering
 </span>
 <span data-rw-start="2227.92" data-rw-transcript-version="2">
 the fundamentals of neural networks, back
 </span>
 <span data-rw-start="2229.76" data-rw-transcript-version="2">
 propagation, and deep learning.
 </span>
 <span data-rw-start="2232.4" data-rw-transcript-version="2">
 Each chapter includes thought-provoking
 </span>
 <span data-rw-start="2234.16" data-rw-transcript-version="2">
 exercises and supporting code. The book
 </span>
 <span data-rw-start="2236.8" data-rw-transcript-version="2">
 is now shipping to 24 countries. You can
 </span>
 <span data-rw-start="2239.359" data-rw-transcript-version="2">
 pick up a copy today at welchlabs.com.
 </span>
</p>