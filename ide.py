from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
from tkinter import messagebox
import subprocess
import os
import webbrowser


app = Tk()
app.title('pyIDE')

editor = Text()
editor.pack()

codeOutput = Text()
codeOutput.pack()


filepath = ''


dark_mode = False


def saveFilePath(path):
    global filepath
    filepath = path

    


def save():
    try:
        if filepath == '':
            path = asksaveasfilename(filetypes=[('Python Files', '*.py'),('JS Files', '*.js'),
                                            ("Text Files", "*.txt"),("All Files", "*.*")])
        else:
            path = filepath
        
        with open(path, 'w') as file:
            code = editor.get('1.0', END)
            file.write(code)
            saveFilePath(path)
            
    except Exception as e:
        messagebox.showinfo("","Something wrong...")




def saveAs():
    try:
        path = asksaveasfilename(filetypes=[('Python Files', '*.py'),('JS Files', '*.js'),
                                        ("Text Files", "*.txt"),("All Files", "*.*")])

        with open(path, 'w') as file:
            code = editor.get('1.0', END)
            file.write(code)
            saveFilePath(path)
            
    except Exception as e:
        messagebox.showinfo("","Something wrong...")
    




    
def openFile():
    try:
        path = askopenfilename(filetypes=[("All Files", "*.*"),('Python Files', '*.py'),
                                      ('JS Files', '*.js'),("Text Files", "*.txt")])

        with open(path, 'r') as file:
            code = file.read()
            editor.delete('1.0', END)
            editor.insert('1.0', code)
            saveFilePath(path)
            
    except Exception as e:
        messagebox.showinfo("","Something wrong...")



def run():
    try:
        if filepath == '':
            save_prompt = Toplevel()
            text = Label(save_prompt, text='Please save first then run code !')
            text.pack()
            return
    
        save()

        extension = os.path.splitext(filepath)[1].lower()

        if extension == ".py":
            command=["python", filepath] 
        
        elif extension == ".js":
            command=["node", filepath]

        elif extension == ".bat":
            command = ["cmd", "/c", filepath]
        
        elif extension == ".html":
            webbrowser.open(filepath)
            return 



        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        codeOutput.insert('1.0', output)
        codeOutput.insert('1.0',  error)
    

    except Exception as e:
        messagebox.showinfo("Error", "Something wrong...")



def darkMode():
    global dark_mode
    dark_mode = not dark_mode

    if dark_mode:
        editor.config(bg="#1e1e1e",fg="white",insertbackground="white")
        codeOutput.config(bg="#1e1e1e",fg="white",insertbackground="white")
        app.config(bg="#2b2b2b")
        filemenu.config(bg="black", fg="white")
        
    else:
        editor.config(bg="white",fg="black",insertbackground="black")
        codeOutput.config(bg="white",fg="black",insertbackground="black")
        app.config(bg="white") 
        filemenu.config(bg="white", fg="black")




def exitApp():
    answer = messagebox.askyesno(
        "Exit",
        "Do you want to exit ?"
    )

    if answer:
        app.destroy()



menu_bar = Menu(app)
app.config(menu=menu_bar)

filemenu = Menu(menu_bar, tearoff=0)
filemenu.add_command(label='Run', command=run)
menu_bar.add_cascade(label='Run Code', menu=filemenu)

filemenu = Menu(menu_bar, tearoff=0)
filemenu.add_command(label='Open', command=openFile)
filemenu.add_command(label='Save', command=save)
filemenu.add_command(label='Save As', command=saveAs)
filemenu.add_command(label='Dark/Light Mode', command=darkMode)
filemenu.add_command(label='Exit', command=exitApp)

menu_bar.add_cascade(label='Options', menu=filemenu)

app.mainloop()

