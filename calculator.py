"""

@Authored By: Lee Rowe
"""


from tkinter import *;
from tkinter import messagebox;

def actionauthor():
    messagebox.showinfo("Authored by...", "  Lee Rowe \nJanuary 2022")

def is_number(n):
    if(n != ''):
        if (n.replace('.', '', 1).isdigit()):
            return True
        if (n.isdigit()):
            return True;
        if n[0] in ['-', '+', '.', '0', ' ']:
            if (n[1] == '.'):
                if (n[2:].isdigit()):
                    return True
            if (n[1] == '0' and n[2] == '.'):
                if (n[3:].isdigit()):
                    return True
            if n[1:].isdigit():
                return True;
        return False;

def casting(num):
    if('.' in num):
        return float(num);
    else:
        return int(num)


def actionPlus():
    Showtemplabel.delete(0, END);
    Showlabel.delete(0, END)

    Showtemplabel.config(fg='black', bg='#ece7e2')
    Showtemplabel.insert(0, '=');
    Showtemplabel.place(relx=0.5, rely=0.5,anchor='center')
    ans = "0";
    Showlabel.insert(0, ans);
    Showlabel.place(relx=0.5, rely=0.6,anchor='center')

    num1 = Numberentry1.get();
    num2 = Numberentry2.get();

    if(is_number(num1) == True and is_number(num2) == True and num1 != ' ' and num2 != ' '):
        num1 = casting(num1);
        num2 = casting(num2);
        ans = str(num1 + num2);

        Showtemplabel.delete(0, END);
        Showlabel.delete(0, END)

        Showtemplabel.config(fg='black', bg='#ece7e2')
        Showtemplabel.insert(0, '=');
        Showtemplabel.place(relx=0.5, rely=0.5,anchor='center')

        Showlabel.insert(0, ans);
        Showlabel.place(relx=0.5, rely=0.6,anchor='center')
    else:
        messagebox.showerror("Error", "Enter a Valid number\ne.g. 123, 0.123, .123, -0.123, 123.456")


def actionMinus():
    Showtemplabel.delete(0, END);
    Showlabel.delete(0, END)

    Showtemplabel.config(fg='black', bg='#ece7e2')
    Showtemplabel.insert(0, '-');
    Showtemplabel.place(relx=0.5, rely=0.5,anchor='center')

    ans = "0";

    Showlabel.insert(0, ans);
    Showlabel.place(relx=0.5, rely=0.6,anchor='center')

    num1 = Numberentry1.get();
    num2 = Numberentry2.get();

    if(is_number(num1)==True and is_number(num2)==True):
        num1 = casting(num1);
        num2 = casting(num2);
        ans = str(num1 - num2);

        Showtemplabel.delete(0, END);
        Showlabel.delete(0, END)

        Showtemplabel.config(fg='black', bg='#ece7e2')
        Showtemplabel.insert(0, '-');
        Showtemplabel.place(relx=0.5, rely=0.5,anchor='center')

        Showlabel.insert(0, ans);
        Showlabel.place(relx=0.5, rely=0.6,anchor='center')
    else:
        messagebox.showerror("Error", "Enter a Valid number\ne.g. 123, 0.123, .123, -0.123, 123.456")


def actionMul():
    Showtemplabel.delete(0, END);
    Showlabel.delete(0, END)

    Showtemplabel.config(fg='black', bg='#ece7e2')
    Showtemplabel.insert(0, '*');
    Showtemplabel.place(relx=0.5, rely=0.5,anchor='center')

    ans = "0"

    Showlabel.insert(0, ans);
    Showlabel.place(relx=0.5, rely=0.6,anchor='center')

    num1 = Numberentry1.get();
    num2 = Numberentry2.get();

    if(is_number(num1)==True and is_number(num2)==True):
        num1 = casting(num1);
        num2 = casting(num2);
        ans = str(num1 * num2);

        Showtemplabel.delete(0, END);
        Showlabel.delete(0, END)

        Showtemplabel.config(fg='black', bg='#ece7e2')
        Showtemplabel.insert(0, '*');
        Showtemplabel.place(relx=0.5, rely=0.5, anchor='center')

        Showlabel.insert(0, ans);
        Showlabel.place(relx=0.5, rely=0.6,anchor='center')
    else:
        messagebox.showerror("Error", "Enter a Valid number\ne.g. 123, 0.123, .123, -0.123, 123.456")


def actionDiv():
    Showtemplabel.delete(0, END);
    Showlabel.delete(0, END)

    Showtemplabel.delete(0, END);
    Showlabel.delete(0, END)

    Showtemplabel.config(fg='black', bg='#ece7e2')
    Showtemplabel.insert(0, '/');
    Showtemplabel.place(relx=0.5, rely=0.5, anchor='center')

    ans = "0"

    Showlabel.insert(0, ans);
    Showlabel.place(relx=0.5, rely=0.6, anchor='center')

    num1 = Numberentry1.get();
    num2 = Numberentry2.get();

    if(is_number(num1)==True and is_number(num2)==True):
        num1 = casting(num1);
        num2 = casting(num2);
        ans = str(num1 / num2);

        Showtemplabel.delete(0, END);
        Showlabel.delete(0, END)

        Showtemplabel.config(fg='black', bg='#ece7e2')
        Showtemplabel.insert(0, '/');
        Showtemplabel.place(relx=0.5, rely=0.5, anchor='center')

        Showlabel.insert(0, ans);
        Showlabel.place(relx=0.5, rely=0.6, anchor='center')
    else:
        messagebox.showerror("Error", "Enter a Valid number\ne.g. 123, 0.123, .123, -0.123, 123.456")

root = Tk();
root.title('Simple Python Calculator');
root.geometry('325x325');
Titlelabel = Label(root, fg = 'black' , font = 'none 10 bold underline' ,text = 'Simple Python Calculator', compound = CENTER)
Titlelabel.place(relx=0.5, rely=0.1, anchor='center')
Showlabel = Entry(root);
Showtemplabel = Entry(root);
Numberentry1 = Entry(root);
Numberentry2 = Entry(root);
Numberentry1.place(relx=0.5, rely=0.3, anchor='center')
Numberentry2.place(relx=0.5, rely=0.4, anchor='center')

plusbutton = Button(root, text="+", width = 5, command = actionPlus);
plusbutton.place(relx=0.15, rely=0.7)

minusbutton = Button(root, text="-", width = 5, command = actionMinus);
minusbutton.place(relx=0.35, rely=0.7)

mulbutton = Button(root, text="*", width = 5, command = actionMul);
mulbutton.place(relx=0.55, rely=0.7)

divbutton = Button(root, text="/", width = 5, command = actionDiv);
divbutton.place(relx=0.75, rely=0.7)

authorbutton = Button(root, text='Author', width=6, command = actionauthor);
authorbutton.place(relx = 0.5, rely=0.9, anchor='center');

root.resizable(False, False);
root.mainloop();
