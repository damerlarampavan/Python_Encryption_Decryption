from  tkinter import *
import tkinter.messagebox
import tkinter.simpledialog

def create_widgets_in_startpage_frame():

    Hi_label = Label(startpage_frame, text = 'Hi', font = 'Courier 44').grid(row = 0, column = 0, padx = 10, pady = 10)
    Welcome_label = Label(startpage_frame, text = 'Welcome to Secret Message Encryptor', font = 'Courier 25').grid(row = 1, column = 0, padx = 10, pady = 10)
    start_button = Button(startpage_frame, text = 'Start', command = call_firstpage_frame_top).grid(row = 2, column = 0)

def create_widgets_in_firstpage_frame():
    createaccount_button = Button(firstpage_frame, text = 'Create an account', command = call_createaccount_frame_top).grid(row = 0, column = 0, padx = 10, pady = 10)
    login_button = Button(firstpage_frame, text = 'Login', command = call_login_frame_top).grid(row = 1, column = 0, padx = 10, pady = 10)

def create_widgets_in_createaccount_frame():

    def createaccount():

        check = open("a&p.txt", "r")
        d = 0
        for eline in check:
            line = eline.split(",")
            z = line[0].rstrip()
            if (createusername_entry.get() != z):
                d = 0
            else:
                d = 1
                break
        if (d != 0):
            tkinter.messagebox.showinfo('Message', 'Account already exists!')
        else:
            file = open("a&p.txt", "a")
            while (createpassword_entry.get() != confirmpassword_entry.get()):
                tkinter.messagebox.showinfo('Message', 'Confirm Password does not match Password!')
                break
            else:
                file.write("\n")
                file.write(createusername_entry.get() + "," + createpassword_entry.get())
                tkinter.messagebox.showinfo('Message', 'Account created sucessfully ;)')
                call_firstpage_frame_top()
            file.close()
        check.close()

    createusername_label = Label(createaccount_frame, text = 'Username', font = 'Courier 20').grid(row = 0, column = 0, padx = 10, pady = 10)
    createpassword_label = Label(createaccount_frame, text = 'Password', font = 'Courier 20').grid(row = 1, column = 0, padx = 10, pady = 10)
    confirmpassword_label = Label(createaccount_frame, text = 'Confirm Password', font = 'Courier 20').grid(row = 2, column = 0, padx = 10, pady = 10)

    createusername_entry = Entry(createaccount_frame)
    createpassword_entry = Entry(createaccount_frame, show = '*')
    confirmpassword_entry = Entry(createaccount_frame, show = '*')
    createusername_entry.grid(row = 0, column = 1, padx = 10, pady = 10)
    createpassword_entry.grid(row = 1, column = 1, padx = 10, pady = 10)
    confirmpassword_entry.grid(row = 2, column = 1, padx = 10, pady = 10)

    signup_button = Button(createaccount_frame, text = 'Sign up', command = createaccount).grid(row = 3, column = 1, columnspan = 2, padx = 10, pady = 10)
    back_button = Button(createaccount_frame, text = 'Back', command = call_firstpage_frame_top).grid(row = 3, column = 0, columnspan = 2, padx = 10, pady = 10)

def create_widgets_in_login_frame():

    def login():

        b = open('a&p.txt', 'r')
        d = 0
        g = 0
        h = 0
        for zline in b:
            g += 1
            z = zline.split(",")
            e = z[0].rstrip()
            if (username_entry.get() == e):
                h = g
                d = 1
                break
            else:
                d = 0
        if (d):
            f = open("a&p.txt", 'r')
            i = 0
            for yline in f:
                y = yline.split(",")
                x = y[1].rstrip()
                k = str(x)
                i += 1
                if (i == h):
                    if (password_entry.get() == k):
                        call_afterlogin_frame_top()
                    elif (password_entry.get() != k):
                        tkinter.messagebox.showinfo('Message', 'Wrong Password')
            f.close()
        else:
            tkinter.messagebox.showinfo('Message', 'Account not found!')
        b.close()

    username_label = Label(login_frame, text = 'Username', font = 'Courier 20').grid(row = 0, column = 0, padx = 10, pady = 10)
    password_label = Label(login_frame, text = 'Password', font = 'Courier 20').grid(row = 1, column = 0, padx = 10, pady = 10)

    username_entry = Entry(login_frame)
    password_entry = Entry(login_frame, show = '*')
    username_entry.grid(row = 0, column = 1, padx = 10, pady = 10)
    password_entry.grid(row = 1, column = 1, padx = 10, pady = 10)

    login_button = Button(login_frame, text = 'Login',command = login).grid(row = 2, column = 0, columnspan = 2, padx = 10, pady = 10)
    back_button = Button(login_frame, text = 'Back', command = call_firstpage_frame_top).grid(row = 2, column = 3, padx = 10, pady = 10)

def create_widgets_in_afterlogin_frame():

    encryption_button = Button(afterlogin_frame, text = 'ENCRYPT', font = 'Courier 40', command = call_encryption_frame_top).grid(row = 0, column = 0, padx = 30, pady = 30)
    decryption_button = Button(afterlogin_frame, text = 'DECRYPT', font = 'Courier 40', command = call_decryption_frame_top).grid(row = 0, column = 1, padx = 30, pady = 30)
    logout_button = Button(afterlogin_frame, text='Log out', command=call_firstpage_frame_top).grid(row=1, column=0, columnspan = 2, padx=10, pady=10)

def create_widgets_in_encryption_frame():

    def reverse(a):
        if (a == 'yes'):
            c = list(encryptiontext_entry.get())
            d = reversed(c)
            e = "".join(d)
            return e
        else:
            return encryptiontext_entry.get()

    def lettershift(a, b = 'no'):
        if (b == "yes"):
            m = []
            c = tkinter.simpledialog.askinteger('Key', 'Please enter the required Letter Shift key')
            for i in a:
                d = ord(i)
                e = d + c
                f = str(e)
                m.append(f)
            n = " ".join(m)
            return n
        else:
            m = []
            for i in a:
                d = ord(i)
                f = str(d)
                m.append(f)
            n = " ".join(m)
            return n

    def outputformat(a, b):

        if (b == 1):
            n = []
            r = []
            c = a.split(" ")
            for i in c:
                d = int(i)
                e = format(d, "b")
                f = str(e)
                g = ""
                for h in f:
                    j = int(h)
                    k = j + 1
                    l = str(k)
                    g += l
                n.append(g)
            aa = " ".join(n)
            bb = list(aa)
            cc = reversed(bb)
            dd = "".join(cc)
            ee = dd.split(" ")
            for o in ee:
                p = int(o)
                q = format(p, "o")
                s = str(q)
                r.append(s)
            t = " ".join(r)
            return t
        else:
            n = []
            r = []
            c = a.split(" ")
            for i in c:
                d = int(i)
                e = format(d, "o")
                f = str(e)
                g = ""
                for h in f:
                    j = int(h)
                    k = j + 1
                    l = str(k)
                    g += l
                n.append(g)
            aa = " ".join(n)
            bb = list(aa)
            cc = reversed(bb)
            dd = "".join(cc)
            ee = dd.split(" ")
            for o in ee:
                p = int(o)
                q = format(p, "b")
                s = str(q)
                r.append(s)
            t = " ".join(r)
            return t

    def encryption():

        reverse_question = tkinter.messagebox.askquestion('Question', 'Would you like to reverse the text?')

        reverse_out_text = reverse(reverse_question)
        lettershift_answer = tkinter.messagebox.askquestion('Question', 'Would you like to include Letter shift?')
        lettershift_out_text = lettershift(reverse_out_text, lettershift_answer)

        format = tkinter.simpledialog.askinteger('Format', 'Which format would you choose, 1 or 2?')

        if(format == 1 or format == 2):

            outputformat_out_text = outputformat(lettershift_out_text, format)
            tkinter.messagebox.showinfo('Encrypted Text', outputformat_out_text)

        else:

            tkinter.messagebox.showinfo('Error', 'Choose 1 or 2')

    text_label = Label(encryption_frame, text = 'Encryption Text', font = 'Courier 25').grid(row = 0, column = 0, padx = 10, pady = 10)

    encryptiontext_entry = Entry(encryption_frame)
    encryptiontext_entry.grid(row = 0, column = 1, padx = 10, pady = 10)

    encrypt_button = Button(encryption_frame, text = 'Encrypt', command = encryption).grid(row = 3, column = 1, padx = 10, pady = 10)
    back_button = Button(encryption_frame, text = 'Back', command = call_afterlogin_frame_top).grid(row = 3, column = 0, padx = 10, pady = 10)

def create_widgets_in_decryption_frame():

    def outputdecrypt(a, b):

        if (b == 1):
            c = []
            d = a.split(" ")
            for e in d:
                f = int(e, 8)
                g = str(f)
                k = ""
                for h in g:
                    j = int(h)
                    j -= 1
                    k += str(j)
                c.append(k)
            l = " ".join(c)
            m = list(l)
            n = reversed(m)
            o = "".join(n)
            p = o.split(" ")
            t = []
            for q in p:
                s = int(q, 2)
                t.append(str(s))
            u = " ".join(t)
            return (u)
        else:
            c = []
            d = a.split(" ")
            for e in d:
                f = int(e, 2)
                g = str(f)
                k = ""
                for h in g:
                    j = int(h)
                    j -= 1
                    k += str(j)
                c.append(k)
            l = " ".join(c)
            m = list(l)
            n = reversed(m)
            o = "".join(n)
            p = o.split(" ")
            t = []
            for q in p:
                s = int(q, 8)
                t.append(str(s))
            u = " ".join(t)
            return (u)

    def letterdecrypt(a, b):

        if (b == "yes"):
            m = []
            c = tkinter.simpledialog.askinteger('Key', 'Please enter the Letter Shift key')
            d = a.split(" ")
            for e in d:
                f = int(e)
                g = f - c
                h = chr(g)
                m.append(h)
            n = "".join(m)
            return n
        else:
            m = []
            d = a.split(" ")
            for e in d:
                f = int(e)
                h = chr(f)
                m.append(h)
            n = "".join(m)
            return n

    def reverse(a, b):
        if (b == "yes"):
            c = list(a)
            d = reversed(c)
            e = "".join(d)
            return e
        else:
            return a

    def decryption():

        format = tkinter.simpledialog.askinteger('Format', 'Which format did you choose, 1 or 2?')

        if (format == 1 or format == 2):

            outputdecrypt_out_text = outputdecrypt(decryptiontext_entry.get(), format)
            lettershift_answer = tkinter.messagebox.askquestion('Question', 'Did you use Letter shift?')
            lettershift_out_text = letterdecrypt(outputdecrypt_out_text, lettershift_answer)
            reverse_answer = tkinter.messagebox.askquestion('Question', 'Did you use reversing?')
            decrypted_text = reverse(lettershift_out_text, reverse_answer)
            tkinter.messagebox.showinfo('Decrypted Text', decrypted_text)

        else:

            tkinter.messagebox.showinfo('Error', 'Choose 1 or 2')

    text_label = Label(decryption_frame, text = 'Decryption Text', font = 'Courier 25').grid(row = 0, column = 0, padx = 10, pady = 10)

    decryptiontext_entry = Entry(decryption_frame)
    decryptiontext_entry.grid(row = 0, column = 1, padx = 10, pady = 10)

    decrypt_button = Button(decryption_frame, text = 'Decrypt', command = decryption).grid(row = 3, column = 1, padx = 10, pady = 10)
    back_button = Button(decryption_frame, text = 'Back', command = call_afterlogin_frame_top).grid(row = 3, column = 0, padx = 10, pady = 10)

###########################
# FRAME CALLING FUNCTIONS #
###########################

def call_startpage_frame_top():

    firstpage_frame.grid_forget()
    createaccount_frame.grid_forget()
    login_frame.grid_forget()
    afterlogin_frame.grid_forget()
    encryption_frame.grid_forget()
    decryption_frame.grid_forget()

    startpage_frame.grid(row = 0, column = 0, padx = 20, pady = 5)

def call_firstpage_frame_top():

    startpage_frame.grid_forget()
    createaccount_frame.grid_forget()
    login_frame.grid_forget()
    afterlogin_frame.grid_forget()
    encryption_frame.grid_forget()
    decryption_frame.grid_forget()

    firstpage_frame.grid(row = 0, column = 0, padx = 20, pady = 5)

def call_createaccount_frame_top():

    firstpage_frame.grid_forget()
    startpage_frame.grid_forget()
    login_frame.grid_forget()
    afterlogin_frame.grid_forget()
    encryption_frame.grid_forget()
    decryption_frame.grid_forget()

    createaccount_frame.grid(row = 0, column = 0, padx = 20, pady = 5)

def call_login_frame_top():

    firstpage_frame.grid_forget()
    createaccount_frame.grid_forget()
    startpage_frame.grid_forget()
    afterlogin_frame.grid_forget()
    encryption_frame.grid_forget()
    decryption_frame.grid_forget()

    login_frame.grid(row = 0, column = 0, padx = 20, pady = 5)

def call_afterlogin_frame_top():

    firstpage_frame.grid_forget()
    createaccount_frame.grid_forget()
    login_frame.grid_forget()
    startpage_frame.grid_forget()
    encryption_frame.grid_forget()
    decryption_frame.grid_forget()

    afterlogin_frame.grid(row = 0, column = 0, padx = 20, pady = 5)

def call_encryption_frame_top():

    firstpage_frame.grid_forget()
    createaccount_frame.grid_forget()
    login_frame.grid_forget()
    afterlogin_frame.grid_forget()
    startpage_frame.grid_forget()
    decryption_frame.grid_forget()

    encryption_frame.grid(row = 0, column = 0, padx = 20, pady = 5)

def call_decryption_frame_top():

    firstpage_frame.grid_forget()
    createaccount_frame.grid_forget()
    login_frame.grid_forget()
    afterlogin_frame.grid_forget()
    encryption_frame.grid_forget()
    startpage_frame.grid_forget()

    decryption_frame.grid(row = 0, column = 0, padx = 20, pady = 5)


#########################
# MAIN CODE STARTS HERE #
#########################

root = Tk()

window_width = 200
window_height = 100

startpage_frame = Frame(root, width = window_width, height = window_height, borderwidth = 2)
startpage_frame.grid(row = 0, column = 0, padx = 20, pady = 5)

firstpage_frame = Frame(root, width = window_width, height = window_height, borderwidth = 2)
firstpage_frame.grid(row = 0, column = 0, padx = 20, pady = 5)

createaccount_frame = Frame(root, width = window_width, height = window_height, borderwidth = 2)
createaccount_frame.grid(row = 0, column = 0, padx = 20, pady = 5)

login_frame = Frame(root, width = window_width, height = window_height, borderwidth = 2)
login_frame.grid(row = 0, column = 0, padx = 20, pady = 5)

afterlogin_frame = Frame(root, width = window_width, height = window_height, borderwidth = 2)
afterlogin_frame.grid(row = 0, column = 0, padx = 20, pady = 5)

encryption_frame = Frame(root, width = window_width, height = window_height, borderwidth = 2)
encryption_frame.grid(row = 0, column = 0, padx = 20, pady = 5)

decryption_frame = Frame(root, width = window_width, height = window_height, borderwidth = 2)
decryption_frame.grid(row = 0, column = 0, padx = 20, pady = 5)

create_widgets_in_startpage_frame()
create_widgets_in_firstpage_frame()
create_widgets_in_createaccount_frame()
create_widgets_in_login_frame()
create_widgets_in_afterlogin_frame()
create_widgets_in_encryption_frame()
create_widgets_in_decryption_frame()

afterlogin_frame.grid_forget()
login_frame.grid_forget()
createaccount_frame.grid_forget()
firstpage_frame.grid_forget()
encryption_frame.grid_forget()
decryption_frame.grid_forget()

root.mainloop()