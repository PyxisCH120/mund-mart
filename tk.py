from tkinter import *

root = Tk()
root.title("MundMart - Login")


largura_tela = root.winfo_screenwidth()
altura_tela = root.winfo_screenheight()


x_pos = int((largura_tela - 500) / 2)
y_pos = int((altura_tela - 500) / 2)
root.geometry(f"500x700")

Label(root, text="").grid(row=0, column=0, padx=10, pady=5)
Label(root, text="Nome de usuário:").grid(row=1, column=0, padx=10, pady=5)
Label(root, text="Email:").grid(row=2, column=0, padx=10, pady=5)
Label(root, text="Senha:").grid(row=3, column=0, padx=10, pady=5)

nome_entry = Entry(root)
nome_entry.grid(row=0, column=1, padx=10, pady=5)

email_entry = Entry(root)
email_entry.grid(row=1, column=1, padx=10, pady=5)

senha_entry = Entry(root, show="*")
senha_entry.grid(row=2, column=1, padx=10, pady=5)

Button(root, text="Entrar", command=fazer_login).grid(row=3, column=1, pady=10)

resultado_label = Label(root, text="")
resultado_label.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()