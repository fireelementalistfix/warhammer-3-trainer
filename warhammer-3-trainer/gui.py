import tkinter as tk
from tkinter import messagebox
from .trainer import Warhammer3Trainer

class Warhammer3TrainerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Warhammer III Trainer")
        self.trainer = Warhammer3Trainer()

        self.setup_ui()

    def setup_ui(self):
        tk.Label(self.root, text="Warhammer III Trainer").pack(pady=10)

        self.money_var = tk.IntVar(value=999999)
        tk.Label(self.root, text="Money:").pack()
        tk.Entry(self.root, textvariable=self.money_var).pack()

        tk.Button(self.root, text="Apply", command=self.apply_money).pack(pady=10)
        tk.Button(self.root, text="Exit", command=self.root.quit).pack()

    def apply_money(self):
        if not self.trainer.find_process():
            messagebox.showerror("Error", "Warhammer III process not found!")
            return

        if self.trainer.set_money(self.money_var.get()):
            messagebox.showinfo("Success", f"Money set to {self.money_var.get()}!")
        else:
            messagebox.showerror("Error", "Failed to set money.")

def run_gui():
    root = tk.Tk()
    app = Warhammer3TrainerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    run_gui()