import streamlit as st

# Dictionary of fixed questions and answers
question_answer_pairs = {
    "What is your name?": "I am LegalEase, your legal assistant chatbot.",
    "Hii": "Hii! I am LegalEase. How can I help you?",
    "Hi": "Hello! How can I assist you?",
    "Hey": "Hey! What legal issue can I help you with?",
    "Hello": "Hi! How can I help you?",
    "Good morning": "Good morning! How may I help you today?",
    "Good evening": "Good evening! What legal assistance do you need?",

    # Legal help general
    "I need legal help": "Sure, please explain your issue briefly.",
    "I have a legal problem": "I can help! Tell me what happened.",
    "Can you guide me legally?": "Yes, I can guide you. Please describe your situation.",
    "I want legal advice": "I can give general guidance. Tell me your issue.",
    "Is this legally valid?": "Please provide more details to check validity.",

    # Contract related
    "I want to create a legal contract": """A legally-binding contract needs:
1. Parties involved  
2. Agreement  
3. Definitions  
4. Terms and Conditions  
5. Payment / Consideration  
6. Confidentiality  
7. Termination clause  
8. Governing law  
9. Signatures""",

    "How to make a contract?": "A contract needs clear terms, parties, signatures, and consideration.",
    "What should a contract include?": "Parties, scope, terms, payment, obligations, and termination.",
    "Can you draft a contract?": "Yes, tell me what type of contract you need.",
    "Difference between contract and agreement": "All contracts are agreements, but only legally enforceable agreements become contracts.",

    # Legal terms
    "What is an FIR?": "An FIR is a First Information Report filed with police for reporting a crime.",
    "What is a notice?": "A written legal communication informing someone about an action or requirement.",
    "What is an affidavit?": "A written statement of facts sworn under oath.",
    "What is a legal heir?": "A person entitled to inherit property of a deceased person.",
    "What is a power of attorney?": "A document giving someone authority to act on your behalf.",

    # Rights
    "What are my consumer rights?": "You have the right to safety, information, choice, and compensation.",
    "What are my employee rights?": "You have rights to fair pay, safety, and legal working hours.",
    "What are my tenant rights?": "You have the right to proper maintenance and notice before eviction.",
    "What are my basic legal rights?": "Right to equality, privacy, freedom, and constitutional remedies.",

    # Police / Crime
    "How to file a police complaint?": "You can file online, at the nearest police station, or by written complaint.",
    "What to do if someone threatens me?": "Document everything and file a police complaint immediately.",
    "What is cybercrime?": "Any online offense such as hacking, fraud, or harassment.",
    "I am being harassed": "Record evidence and report it to the authorities.",
    "Someone cheated me": "Collect proof and file a complaint under cheating and fraud.",

    # Property
    "How to transfer property?": "Requires a sale deed, stamp duty payment, registration, and mutation.",
    "What is property title?": "Title means legal ownership rights.",
    "What is encumbrance certificate?": "It shows the property is free from loans or legal disputes.",
    "How to register property?": "Prepare deed, pay stamp duty, and register at the sub-registrar office.",

    # Business / Startup
    "How to start a business legally?": "Choose structure, register business, get PAN/TAN, and follow compliance.",
    "What is an LLP?": "A Limited Liability Partnership protects partners from personal liability.",
    "What is a partnership deed?": "A document defining rules and responsibilities of partners.",
    "How to register a company?": "Get DSC, DIN, name approval, and file documents with MCA.",

    # Letters & Complaints
    "Can you help me write a letter?": "Yes! Tell me the purpose.",
    "Can you create a legal notice?": "Yes. Share your issue.",
    "Can you draft a complaint?": "Sure, explain the situation.",

    # Misc
    "Thank you": "You're welcome!",
    "Who are you?": "I am LegalEase, your legal support chatbot.",
    "What is LegalEase?": "LegalEase is an AI-style chatbot that provides simple legal guidance."
}

# UI
st.title("LegalEase")
st.header("Chat with LegalEase")

# User input
new_message = st.text_input("Enter your message:", "")

# Handle send
if st.button("Send"):
    new_message_clean = new_message.strip()

    if new_message_clean in question_answer_pairs:
        bot_response = question_answer_pairs[new_message_clean]
    else:
        bot_response = "Sorry, I don't have information on that. Please ask something legal."

    st.text("⚖️ LegalEase: " + bot_response)
