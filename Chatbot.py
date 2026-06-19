# ============================================================
#   DecodeLabs | AI Internship – Project 1
#   Rule-Based AI Chatbot
#   Author : poonkvi R
#   Batch  : 2026
# ============================================================

KNOWLEDGE BASE 
responses = {
    "hello"        : "Hello!  I'm DecoBot. How can I help you today?",
    "hi"           : "Hi there!  What can I do for you?",
    "hey"          : "Hey! Great to see you. Ask me anything!",
    "who are you"  : "I'm DecoBot  – a rule-based AI chatbot built at DecodeLabs.",
    "what is your name" : "My name is DecoBot! Built with pure Python logic. ",
    "what is ai"   : "AI stands for Artificial Intelligence – machines programmed to simulate human thinking. ",
    "what is machine learning" : "Machine Learning is a subset of AI where systems learn patterns from data instead of being explicitly programmed.",
    "what is deep learning" : "Deep Learning uses neural networks with many layers to learn complex patterns – it's the engine behind modern AI!",
    "what is decodelabs" : "DecodeLabs is an ed-tech platform that trains students with real-world AI & tech projects. ",
    "tell me about decodelabs" : "DecodeLabs provides hands-on industrial training in AI, Python, and more. Visit www.decodelabs.tech!",
    "help"         : "I can answer questions about AI, DecodeLabs, or just chat! Type 'exit' to quit.",
    "what can you do" : "I can discuss AI concepts, tell you about DecodeLabs, greet you, and keep you company! ",
    "tell me a joke": "Why do programmers prefer dark mode? Because light attracts bugs! ",
    "how are you"  : "I'm running at 100% efficiency – no bugs detected! ",
    "thank you"    : "You're welcome! Happy coding!",
    "thanks"       : "Anytime! Keep building great things. ",
    "bye"          : "Goodbye! Keep coding and stay curious! ",
    "goodbye"      : "See you next time! Happy learning at DecodeLabs. ",
}
FALLBACK = " I don't understand that yet. Try asking about AI, DecodeLabs, or type 'help'."

print("=" * 55)
print("       Welcome to DecoBot )
print("=" * 55)
print("  Type 'help' to see what I can do.")
print("  Type 'exit' or 'quit' to end the session.")
print("-" * 55)
while True:
    raw_input_text = input("\nYou: ")
    clean_input    = raw_input_text.lower().strip()
    if clean_input in ("exit", "quit", "q"):
        print("\nDecoBot: Goodbye! Session ended. Keep learning! ")
        print("=" * 55)
        break
    if not clean_input:
        print("DecoBot: Please type something! I'm listening. ")
        continue
    reply = responses.get(clean_input, FALLBACK)
    print(f"DecoBot: {reply}")
