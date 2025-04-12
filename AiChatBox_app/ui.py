import customtkinter as ctk
from chatbot import ask_gpt

class ChatApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x700")
        self.title("Ai Chat Box")

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.chat_history = []

        self.chat_output = ctk.CTkTextbox(self, width=550, height=500, wrap="word")
        self.chat_output.pack(pady=20)
        self.chat_output.configure(state="disabled")

        self.entry = ctk.CTkEntry(self, width=450, placeholder_text="Type a message...")
        self.entry.pack(side="left", padx=(20, 0), pady=10)

        send_button = ctk.CTkButton(self, text="Send", command=self.send_message)
        send_button.pack(side="left", padx=10, pady=10)

    def update_chatbox(self, message):
        self.chat_output.configure(state="normal")
        self.chat_output.insert("end", message + "\n")
        self.chat_output.configure(state="disabled")
        self.chat_output.see("end")

    def send_message(self):
        user_msg = self.entry.get().strip()
        if not user_msg:
            return

        self.entry.delete(0, "end")
        self.update_chatbox(f"You: {user_msg}")
        self.chat_history.append({"role": "user", "content": user_msg})

        bot_reply = ask_gpt(self.chat_history)
        self.update_chatbox(f"Bot: {bot_reply}")
        self.chat_history.append({"role": "assistant", "content": bot_reply})
