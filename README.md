 Rule-Based AI Chatbot
 Project Overview

DecoBot is a **Rule-Based AI Chatbot** built using pure Python logic — no machine learning libraries required. It uses a dictionary-based knowledge base (O(1) lookup) to respond to predefined user inputs in a continuous conversation loop.

This project demonstrates foundational AI concepts:
- Control Flow & Decision-Making Logic
- Input Sanitization & Normalization
- Dictionary-based Intent Matching
- Infinite Loop with Clean Exit Strategy

 Features

- Continuous conversation loop (`while True`)
-  Input sanitization (lowercase + strip whitespace)
 20+ predefined intents in a dictionary knowledge base
-  Graceful fallback for unknown inputs
-  Clean exit on `exit` / `quit` / `q`
-  Covers: greetings, AI topics, DecodeLabs info, jokes & more

 Tech Stack

| Tool | Details |
|------|---------|
| Language | Python 3.x |
| Libraries | None (pure Python) |
| Concepts | Control Flow, Dictionaries, Loops |

 Project Structure
chatbot-project
│
├── chatbot.py        # Main chatbot source code
├── README.md         # Project documentation
└── screenshot.png    # Sample output screenshot


 Sample Conversation
=======================================================
                 AI CHATBOT
=======================================================
  Type 'help' to see what I can do.
  Type 'exit' or 'quit' to end the session.
-------------------------------------------------------

You: hello
DecoBot: Hello! 👋 I'm DecoBot. How can I help you today?

You: what is ai
DecoBot: AI stands for Artificial Intelligence – machines programmed to simulate human thinking. 

You: tell me a joke
DecoBot: Why do programmers prefer dark mode? Because light attracts bugs! 

You: exit
DecoBot: Goodbye! Session ended. Keep learning! 🎓
=======================================================
 How It Works (IPO Model)
INPUT  →  Sanitize (lower + strip)  →  PROCESS (dict lookup)  →  OUTPUT (response)

- **Input Phase:** Raw user text is collected and normalized
- **Process Phase:** Cleaned input is matched against the knowledge base dictionary
- **Output Phase:** Matched response is printed; fallback shown if no match

 Key Concepts Learned

- **Rule-Based AI** vs Probabilistic AI (LLMs)
- **Dictionary O(1)** lookup vs If-Elif ladder O(n)
- **IPO Model:** Input → Process → Output
- **AI Guardrails:** Deterministic control layer over probabilistic systems

## 🏢 About DecodeLabs

DecodeLabs is an ed-tech platform providing hands-on industrial training in AI and technology.  
🌐 www.decodelabs.tech | 📞 +91 89330 06408


