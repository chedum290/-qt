import tkinter as tk


root = tk.Tk()
root.title("tk")
root.geometry("450x400")
root.configure(bg="#e0e0e0")

top_frame = tk.Frame(root, bg="#cccccc", height=100)

top_frame.pack(side="top", fill='x')


button = tk.Button(
    root,
    text="Начать викторину?",
    bg="#e0e0e0"
)
button.pack(expand=True)

root.mainloop()