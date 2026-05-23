import tkinter as tk


def create_button(parent, text, command):
    return tk.Button(
        parent,
        text=text,
        command=command
    )


def create_input(parent):
    return tk.Entry(parent)
