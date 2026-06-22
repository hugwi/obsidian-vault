# GitHub - EvolvingSoftware/screen-pipe: Record your screen & mic 24/7 and connect it to LLMs. Inspired by adept.ai, rewind.ai, Apple Shortcut. Written in Rust. Free. You own your data.

![rw-book-cover](https://opengraph.githubassets.com/0391a89c4358955c6a2828afb6dc283f57d7d4225e1f72f020ae0b130d5b0f0c/EvolvingSoftware/screen-pipe)

## Metadata
- Author: [[https://github.com/EvolvingSoftware/]]
- Full Title: GitHub - EvolvingSoftware/screen-pipe: Record your screen & mic 24/7 and connect it to LLMs. Inspired by adept.ai, rewind.ai, Apple Shortcut. Written in Rust. Free. You own your data.
- Category: #articles
- Summary: screen-pipe is an open-source Rust library that records your screen and mic 24/7 and stores the data locally.  
It connects that life-context data to LLMs for search, automation, summaries, and other apps.  
The project is experimental, privacy-focused, and lets you own and export your data.
- URL: https://github.com/EvolvingSoftware/screen-pipe

## Full Document
### EvolvingSoftware/screen-pipe

Open more actions menu

[![](https://private-user-images.githubusercontent.com/25003283/342756836-289bbee7-79bb-4251-9516-878a1c40dcd0.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NjAzNDEyOTEsIm5iZiI6MTc2MDM0MDk5MSwicGF0aCI6Ii8yNTAwMzI4My8zNDI3NTY4MzYtMjg5YmJlZTctNzliYi00MjUxLTk1MTYtODc4YTFjNDBkY2QwLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTEwMTMlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUxMDEzVDA3MzYzMVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWY5MWM1YjE1YzFmNDNkNmViM2EzYmI4ZTU0MDQxY2UwOTY5MjEyMWI4MjRmNGU3Y2VkNGRjM2E5ZjRkMTdhNzYmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.vpmZQvoNZGmv3JyZ4egYX7NjxUuptPOxqK6O5-LxbeE)](https://private-user-images.githubusercontent.com/25003283/342756836-289bbee7-79bb-4251-9516-878a1c40dcd0.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NjAzNDEyOTEsIm5iZiI6MTc2MDM0MDk5MSwicGF0aCI6Ii8yNTAwMzI4My8zNDI3NTY4MzYtMjg5YmJlZTctNzliYi00MjUxLTk1MTYtODc4YTFjNDBkY2QwLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTEwMTMlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUxMDEzVDA3MzYzMVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWY5MWM1YjE1YzFmNDNkNmViM2EzYmI4ZTU0MDQxY2UwOTY5MjEyMWI4MjRmNGU3Y2VkNGRjM2E5ZjRkMTdhNzYmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.vpmZQvoNZGmv3JyZ4egYX7NjxUuptPOxqK6O5-LxbeE)
[![Join Waitlist for Desktop App](https://camo.githubusercontent.com/13394324420fcd9fd8aab7d89406eebf1f4c1c79b7b3243ea169750a819a3771/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4a6f696e253230576169746c6973742d4465736b746f702532304170702d626c75653f7374796c653d666f722d7468652d6261646765)](https://screenpi.pe)
[![Featured on Ben's Bites](https://camo.githubusercontent.com/633784ee7ef94f942c7a07a4e077eae1afc7697489788514c62571d75cb5bffb/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f46656174757265642532306f6e2d42656e277325323042697465732d626c75653f7374796c653d666c61742d737175617265)](https://www.bensbites.com/)
[![Join us on Discord](https://camo.githubusercontent.com/a0d96960e0025d2bba43e338ce9037ae33c2c86558d9595d799d9d26d735470a/68747470733a2f2f696d672e736869656c64732e696f2f646973636f72642f3832333831333135393539323030313533373f636f6c6f723d353836354632266c6f676f3d646973636f7264266c6f676f436f6c6f723d7768697465267374796c653d666c61742d737175617265)](https://discord.gg/dU9EBuw7Uq)
[![X account](https://camo.githubusercontent.com/4c0969bb945df274715bf7b95790e6fec4e8ae638f354f12e5a56c98c7724a17/68747470733a2f2f696d672e736869656c64732e696f2f747769747465722f75726c2f68747470732f747769747465722e636f6d2f6469666675736572736c69622e7376673f7374796c653d736f6369616c266c6162656c3d466f6c6c6f7725323025343073637265656e5f70697065)](https://twitter.com/screen_pipe)

>  Civilization progresses by the number of operations it can perform without conscious effort.  
>  — **Whitehead**
> 
>  

Record your screen & mic 24/7 and connect it to LLMs. Inspired by `adept.ai`, `rewind.ai`, `Apple Shortcut`. Written in Rust. Free. You own your data.

screenpipe is a library that allows you to gather all your life context and connect it to LLMs easily for:

* search (e.g. go beyond your limited human memory)
* automation (such as making actions on the web while you work, syncing company's knowledge, etc.)
* etc.

#### Example vercel/ai-chatbot that query screenpipe autonomously

Check this example of screenpipe which is a chatbot that make requests to your data to answer your questions

  070424.mp4    
#### Status

Alpha: runs on my computer (`Macbook pro m3 32 GB ram`) 24/7.

* screenshots
* mp4 encoding to disk (30 GB / month)
* sqlite local db
* OCR
* audio + stt
* local api
* TS SDK
* cloud storage options (s3, pgsql, etc.)
* cloud computing options
* bug-free & stable
* storage efficient modes: customizable capture settings (fps, resolution)
* data encryption options & higher security
* fast, optimised, energy-efficient modes

#### Usage

Keep in mind that it's still experimental.

##### Windows

TBD. Own a Windows computer? [Please help us test it!](https://github.com/louis030195/screen-pipe/issues/6).

##### Linux

```
curl -sSL https://raw.githubusercontent.com/louis030195/screen-pipe/main/install.sh | sh
```

Now you should be able to `screenpipe`. (You may need to restart your terminal, or find the CLI in `$HOME/.local/bin`)

##### MacOS

On Mac you need to build the CLI yourself.

1. Install dependencies:

```
# On Mac
brew install ffmpeg
```

Install [Rust](https://www.rust-lang.org/tools/install).

2. Clone the repo:

```
git clone https://github.com/louis030195/screen-pipe
cd screen-pipe
```

3. Run the API:

```
# This runs a local SQLite DB + an API + screenshot, ocr, mic, stt, mp4 encoding
cargo build --release --features metal # remove "--features metal" if you do not have M series processor

# sign the executable to avoid mac killing the process when it's running for too long
codesign --sign - --force --preserve-metadata=entitlements,requirements,flags,runtime ./target/release/pipe

# then run it
./target/release/pipe

# or only stream audio + speech to text to stdout
./target/release/pipe-audio

# or only stream screenshots + ocr to stdout
./target/release/pipe-vision

# or only record mp4 videos + json containing ocr
./target/release/pipe-video
```

Struggle to get it running? [I'll install it with you in a 15 min call.](https://cal.com/louis030195/screenpipe)

We are working toward [making it easier to try](https://github.com/louis030195/screen-pipe/issues/6), feel free to help!

##### What's next?

 Examples to query the API 
```
# 1. Basic search query
curl "http://localhost:3030/search?q=test&limit=5&offset=0"

# 2. Search with content type filter (OCR)
curl "http://localhost:3030/search?q=test&limit=5&offset=0&content_type=ocr"

# 3. Search with content type filter (Audio)
curl "http://localhost:3030/search?q=test&limit=5&offset=0&content_type=audio"

# 4. Search with pagination
curl "http://localhost:3030/search?q=test&limit=10&offset=20"

# 6. Search with no query (should return all results)
curl "http://localhost:3030/search?limit=5&offset=0"
```
 
Now pipe this into a LLM to build:

* memory extension apps
* automatic summaries
* automatic action triggers (say every time you see a dog, send a tweet)
* automatic CRM (fill salesforce while you do sales on linkedin)
* sync your local pkm with company's pkm (obsidian to notion for example)
* maintain cheatsheets of your customers relationships formatted as markdown table in notion
* dating app that make AI agents talk with millions of other potential mates acting like you and scheduling you weekly dates

[Check example with vercel/ai-chatbot project (nextjs)](https://github.com/louis030195/screen-pipe/tree/main/examples/ts/vercel-ai-chatbot)

#### Why open source?

Recent breakthroughs in AI have shown that context is the final frontier. AI will soon be able to incorporate the context of an entire human life into its 'prompt', and the technologies that enable this kind of personalisation should be available to all developers to accelerate access to the next stage of our evolution.

#### Principles

This is a library intended to stick to simple use case:

* record the screen & associated metadata (generated locally or in the cloud) and pipe it somewhere (local, cloud)

Think of this as an API that let's you do this:

```
screenpipe | ocr | llm "turn what i see into my CRM" | api "send data to salesforce api"
```

Any interfaces are out of scope and should be built outside this repo, for example:

* UI to search on these files (like rewind)
* UI to spy on your employees
* etc.

#### Contributing

Contributions are welcome! If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.

Say 👋 in our [public Discord channel](https://discord.gg/dU9EBuw7Uq) . We discuss how to bring this lib to production, help each other with contributions, personal projects or just hang out ☕.

Bit more details on the architecture [here](https://link.excalidraw.com/l/5MKXLddifTr/8subenQGvcd).

#### Licensing

The code in this project is licensed under MIT license. See the [LICENSE](https://github.com/EvolvingSoftware/screen-pipe/blob/main/LICENSE.md) file for more information.

#### Related projects

This is a very quick & dirty example of the end goal that works in a few lines of python: <https://github.com/louis030195/screen-to-crm>

Very thankful for <https://github.com/jasonjmcghee/xrem> which was helpful. Although screenpipe is going in a different direction.

#### FAQ

 What's the difference with adept.ai and rewind.ai? * adept.ai is closed product, focused on automation while we are open and focused on enabling tooling & infra for a wide range of applications like adept
* rewind.ai is closed product, focused on a single use case (they only focus on meetings now), not customisable, your data is owned by them, and not extendable by developers

 
 Where is the data stored? * 100% of the data stay local in a SQLite database and mp4 files
* If you use an LLM like OpenAI, part of your data will be sent to Microsoft servers, you can use a local LLM like [Chrome AI](https://sdk.vercel.ai/providers/community-providers/chrome-ai)

 
 How can I customize capture settings to reduce storage and energy usage? * You can adjust frame rates and resolution in the configuration. Lower values will reduce storage and energy consumption. We're working on making this more user-friendly in future updates.

 
 Is my data secure? * Your data is stored locally by default. We're actively working on implementing encryption options for enhanced security.

 
 What are some practical use cases for screenpipe? * Personal knowledge management
* Automated task logging and time tracking
* Context-aware AI assistants for improved productivity
* Seamless data entry into CRM systems
* We're constantly exploring new use cases and welcome community input!
