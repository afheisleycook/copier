import tkinter as tk
from  tkinter import messagebox
class UI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("400x400")
        self.title("file copier")
        self
        self.lblsrc = tk.Label(self,text="src")
        self.lblsrc.pack()
        self.txtsrc = tk.Entry()
        self.txtsrc.pack()
        self.lbldest = tk.Label(self,text="dest")
        self.lbldest.pack()
        self.txtdest = tk.Entry()
        self.txtdest.pack()
        self.btnCopy = tk.Button(self,text="copy",command=self.copy)
        self.btnCopy.pack()

    def copy(self):
        try:
            with open(self.txtsrc.get(), "r+") as source:
                for a in source.readlines():
                    with open(self.txtdest.get(), "+w") as t:
                        t.write(a)
            messagebox.showinfo("done coping")
        except IndexError as e:
            print("""
            no arguments for src or dest
            for example do red.txt /Docuements

            """)
        except IsADirectoryError:
            print(f"""
            this is a directory:{sys.argv[0]} not a file try a file 
            """)
        except FileNotFoundError:
            messagebox.showerror("error",f"the file {self.txtsrc.get()} or directory doesnt exist")



