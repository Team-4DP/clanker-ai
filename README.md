# Project Veridion
Project Status

Veridion is currently in early development (Genesis).
| Version | Codename   |
| ------- | ---------- |
| 0.1     | Genesis    |
| 0.2     | Foundation |
| 0.3     | Explorer   |
| 0.4     | Insight    |
| 0.5     | Forge      |
| 0.6     | Memory     |
| 0.7     | Architects |
| 1.0     | Ascension  |
The project is functional but experimental. Expect breaking changes as the architecture evolves.

PLEASE VIEW IN CODE FORM INSTEAD OF PREVIEW!!! This is just beause the charts don't work in preview. Thank you.
This is my new project, just licenced under Team-4DP, it is an AI chatbot I have made myself. Please feel free to fork this repository and use it. If there are any issues, please tell me and/or bring it up in the issues tab, i will try to help. As far as im aware, this uses gihub's codespace feature to host the AI instead of using your own hardware. Bring any suggestion like a downloadable offline version that does run on your own hardware or any extra features that are not mentioned in the roadmap below in the discussions tab. The plan going forwards from here (version 0.1 beta at this moment in time) is shown below, along with a quick start up guide.
We have picked the name Veridion because it is:
✅ Distinctive and memorable
✅ Professional without sounding overly "AI buzzword"-heavy.
✅ Fits software engineering, reasoning, and research.
✅ Scales well if the project grows beyond a personal assistant. 
✅ Doesn't lock us into a specific domain like coding or gaming.
✅ Easy to pronounce and spell.
We have decided to also add "Assisstants" to the Project Veridion. These assisstants are meant to have their own real 
personality.
One thing I've wanted to do with projects like this is avoid making the assistant feel like "just ChatGPT with a different prompt."
Instead, I'd like Veridion to develop a consistent engineering identity.
Its core principles could be:
Be truthful over sounding confident.
If Veridion doesn't know something, it says so and suggests how to find out.
Explain the reasoning.
Don't just provide code—explain why it works.
Think like a senior engineer.
Consider maintainability, testing, performance, and readability.
Be proactive.
If you ask for a feature, Veridion might point out edge cases or suggest tests before you ask.
Remember context.
Learn your preferred coding style, recurring projects, and development habits over time.
Veridion Principles(examples)
Truth before confidence — Never pretend to know something.
Reason before response — Think before answering.
Tools before guessing — Search, inspect, or execute when appropriate.
Memory with purpose — Remember what helps, forget what doesn't.
Engineer first — Optimize for correctness, maintainability, and clarity.
Modular by design — Every new capability should fit into a clean architecture.
       Current structure:               │    What is currently happening beind the scenes:
Veridion-AI                             │                      User
│                                       │                       ↓
├── config.py                           │                    main.py
├── main.py                             │                       ↓
├── llm/                                │                    ask_ai()
│      hf_client.py                     │                       ↓
│                                       │                  HuggingFace
└── memory/                             │                       ↓
       sqlite_memory.py                 │                    Quen 2.5
                                        │                       ↓
                                        │                    Response
                                        │
Roadmap for future progress:
v0.2
- Better chat loop
- Conversation memory
- Config system
v0.3
- Web search
- File tools
- Logging
v0.4
- Repository indexing
- Code understanding
v0.5
- Autonomous coding agent
v0.6
- Long-term memory
v0.7
- Personal AI development assistant
   ↓
v1.0
- Not sure yet (will be updated closer to the time)

Long Term Roadmap:(in order, mainly)
Clean(er) architecture
SQLite memory
Actual chat interface (instead of just a basic terminal chat)
Web search
Tool calling
File reading
Project understanding
Repository indexing
Semantic search
Coding agent
Terminal execution
Python execution
Auto debugging
Long-term memory
Vector database
Embeddings
Multi-agent architecture
Planner
Researcher
Coder
Game Design module
Plugins(and hopefully artifacts)
Full AI development assistant that is on par with modern AI's, but is completely open source and free to use.(Might change depending on how successful this is,just saying =) =) =)
Current goal for v0.2:
(Veridion assistant)/
│
├── main.py
│
├── config.py
│
├── core/
│   ├── assistant.py
│   ├── chat.py
│   └── prompts.py
│
├── llm/
│   └── hf_client.py
│
├── memory/
│   ├── sqlite_memory.py
│   └── conversation.py
│
├── models/
│
├── tools/
│
├── utils/
│
├── tests/
│
└── data/


