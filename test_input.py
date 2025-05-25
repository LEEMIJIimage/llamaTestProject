import tkinter as tk

def on_submit():
    prompt = entry.get()
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, f"입력한 텍스트: {prompt}")

root = tk.Tk()
root.title("입력창 테스트")
root.geometry("600x400")
root.configure(bg="#1e1e1e")

entry_label = tk.Label(root, text="프롬프트 입력:", fg="white", bg="#1e1e1e")
entry_label.pack(pady=(20, 5))

entry = tk.Entry(root, width=80, bg="white", fg="black")
entry.pack(pady=(0, 10))

btn = tk.Button(root, text="입력 확인", command=on_submit)
btn.pack()

output_text = tk.Text(root, height=15, width=70, bg="white", fg="black")
output_text.pack(pady=10)

root.mainloop()