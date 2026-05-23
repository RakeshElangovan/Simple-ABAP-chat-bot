import tkinter as tk
from tkinter import scrolledtext

from app.core.chatbot import ChatBot


class ChatWindow:

    def __init__(self):
        self.bot = ChatBot()

        self.window = tk.Tk()
        self.window.title("AI ChatBot")
        self.window.geometry("700x500")

        self.chat_area = scrolledtext.ScrolledText(
            self.window,
            wrap=tk.WORD,
            state='disabled'
        )

        self.chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.input_box = tk.Entry(self.window)
        self.input_box.pack(
            padx=10,
            pady=5,
            fill=tk.X
        )

        self.send_button = tk.Button(
            self.window,
            text="Send",
            command=self.send_message
        )

        self.send_button.pack(pady=5)

    def send_message(self):
        user_message = self.input_box.get()

        if not user_message.strip():
            return

        self.display_message("You", user_message)

        response = self.bot.get_response(user_message)

        self.display_message("Bot", response)

        self.input_box.delete(0, tk.END)

    def display_message(self, sender, message):
        self.chat_area.config(state='normal')
        self.chat_area.insert(
            tk.END,
            f"{sender}: {message}\n"
        )
        self.chat_area.config(state='disabled')
        self.chat_area.yview(tk.END)

    def run(self):
        self.window.mainloop()
