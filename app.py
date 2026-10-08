import tkinter as tk
from tkinter import scrolledtext
import datetime

# --- CORE FUNCTION: Rule-Based Chatbot Logic (PDF: if-elif, functions) ---
def get_bot_response(user_message):
    msg = user_message.lower().strip()

    # 1. Greetings (PDF requirement: 'hello' -> 'Hi!')
    if any(greet in msg for greet in ["hello", "hi", "hey"]):
        return "Hi! How can I assist you today?"

    # 2. Health & Status (PDF requirement: 'how are you' -> 'I'm fine, thanks!')
    elif "how are you" in msg:
        return "I'm fine, thanks! How are you doing today?"

    # 3. Identity & Creator
    elif "who are you" in msg or "what is your name" in msg:
        return "I am AlphaBot, a smart rule-based desktop assistant built for CodeAlpha!"

    # 4. Live Date & Time
    elif "time" in msg:
        now_time = datetime.datetime.now().strftime("%I:%M %p")
        return f"The current system time is {now_time}."
    elif "date" in msg or "today" in msg:
        today_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
        return f"Today is {today_date}."

    # 5. Quick Calculator Feature
    elif msg.startswith("calc ") or msg.startswith("calculate "):
        expr = msg.replace("calc", "").replace("calculate", "").strip()
        try:
            allowed = "0123456789+-*/.() "
            if all(ch in allowed for ch in expr):
                result = eval(expr)
                return f"Result: {expr} = {result}"
            else:
                return "I can only calculate numbers with +, -, *, and /."
        except Exception:
            return "Invalid math expression. Example: 'calc 25 * 4'"

    # 6. Farewell (PDF requirement: 'bye' -> 'Goodbye!')
    elif any(bye in msg for bye in ["bye", "goodbye", "exit"]):
        return "Goodbye! Have a great and productive day ahead!"

    # 7. Fallback response
    else:
        return "I'm still learning! You can greet me ('hello'), ask 'how are you', request 'time'/'date', or type 'calc 10 * 5'."

# --- GUI LOGIC (Desktop Chat Window) ---
def send_message():
    user_text = entry_box.get().strip()
    if not user_text:
        return

    # Display user's message
    chat_history.config(state=tk.NORMAL)
    chat_history.insert(tk.END, f"You: {user_text}\n", "user_style")
    entry_box.delete(0, tk.END)

    # Get bot response
    bot_reply = get_bot_response(user_text)
    chat_history.insert(tk.END, f"AlphaBot: {bot_reply}\n\n", "bot_style")
    chat_history.config(state=tk.DISABLED)
    chat_history.yview(tk.END)

# Create main window
root = tk.Tk()
root.title("AlphaBot - Smart Desktop Assistant")
root.geometry("450x520")
root.configure(bg="#1E1E2E")

# Chat display area
chat_history = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED, bg="#2A2A3C", fg="#FFFFFF", font=("Segoe UI", 10))
chat_history.pack(padx=12, pady=12, fill=tk.BOTH, expand=True)

# Styling message tags
chat_history.tag_config("user_style", foreground="#89B4FA", font=("Segoe UI", 10, "bold"))
chat_history.tag_config("bot_style", foreground="#A6E3A1", font=("Segoe UI", 10))

# Initial welcome message
chat_history.config(state=tk.NORMAL)
chat_history.insert(tk.END, "AlphaBot: Hi! I am AlphaBot. How can I assist you today?\n\n", "bot_style")
chat_history.config(state=tk.DISABLED)

# Input container
input_frame = tk.Frame(root, bg="#1E1E2E")
input_frame.pack(padx=12, pady=(0, 12), fill=tk.X)

# Text entry box
entry_box = tk.Entry(input_frame, font=("Segoe UI", 11), bg="#313244", fg="#FFFFFF", insertbackground="white")
entry_box.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=6, padx=(0, 8))
entry_box.bind("<Return>", lambda event: send_message())

# Send button
send_btn = tk.Button(input_frame, text="Send", font=("Segoe UI", 10, "bold"), bg="#89B4FA", fg="#11111B", activebackground="#B4BEFE", cursor="hand2", command=send_message)
send_btn.pack(side=tk.RIGHT, ipadx=10, ipady=3)

# Run the desktop app
root.mainloop()