import tkinter as tk
from tkinter import *
import random
import sqlite3
import time
from tkinter import ttk
from tkinter import messagebox

def loginPage(logdata):
    sup.destroy()
    global login
    login = Tk()

    user_name = StringVar()
    password = StringVar()

    login_canvas = Canvas(login,width=720,height=440,bg="pink")
    login_canvas.pack()

    login_frame = Frame(login_canvas,bg="white")
    login_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    heading = Label(login_frame,text="Авторизация",fg="black",bg="white")
    heading.config(font=('calibri 40'))
    heading.place(relx=0.2,rely=0.1)

    #USER NAME
    ulabel = Label(login_frame,text="Имя пользователя",fg='black',bg='white')
    ulabel.place(relx=0.12,rely=0.4)
    uname = Entry(login_frame,bg='#d3d3d3',fg='black',textvariable = user_name)
    uname.config(width=42)
    uname.place(relx=0.31,rely=0.4)

    #PASSWORD
    plabel = Label(login_frame,text="Пароль",fg='black',bg='white')
    plabel.place(relx=0.215,rely=0.5)
    pas = Entry(login_frame,bg='#d3d3d3',fg='black',show="*",textvariable = password)
    pas.config(width=42)
    pas.place(relx=0.31,rely=0.5)

    def check():
        global global_username
        for a, b, c, d in logdata:
            if b == uname.get() and c == pas.get():
                global_username = uname.get()
                messagebox.showinfo("Успешный вход", "Вы успешно вошли в систему!")
                if uname.get() == "admin" and pas.get() == "adminadmin":
                    adminpage()
                else:
                    menu()
                    # Отображение сообщения об успешном входе

                break
        else:
            error = Label(login_frame, text="Не правильное имя пользователя или пароль!", fg='black', bg='white')
            error.place(relx=0.37, rely=0.7)


    #LOGIN BUTTON
    log = Button(login_frame,text='Войти',padx=5,pady=5,width=5,command=check)
    log.configure(width = 15,height=1, activebackground = "#33B5E5", relief = FLAT)
    log.place(relx=0.4,rely=0.6)


    login.mainloop()

def adminpage():
    global global_username

    def search_records():
        search_name = search_entry.get().strip()  # Getting the entered username
        tree.delete(*tree.get_children())  # Clearing the Treeview before displaying search results

        # Getting data from the UserResult table for the specified username
        conn = sqlite3.connect('quiz.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM UserResult WHERE UserName=?", (search_name,))
        rows = cursor.fetchall()
        conn.close()

        # Inserting the found data into the Treeview
        for row in rows:
            tree.insert("", tk.END, values=(row[0], row[1], row[2]))

    admin = tk.Tk()
    admin.title("Admin Page")
    admin.geometry("800x600")

    # Creating search entry and button
    search_label = tk.Label(admin, text="Enter Username:")
    search_label.pack()

    search_entry = tk.Entry(admin)
    search_entry.pack()

    search_button = tk.Button(admin, text="Search", command=search_records)
    search_button.pack()

    # Creating Treeview
    tree = ttk.Treeview(admin)
    tree["columns"] = ("ResultID", "UserName", "Score")
    tree["displaycolumns"] = ("ResultID", "UserName", "Score")

    # Setting column headings
    tree.heading("ResultID", text="Номер результата")
    tree.heading("UserName", text="Имя пользователя")
    tree.heading("Score", text="Оценка")

    # Getting data from the UserResult table
    conn = sqlite3.connect('quiz.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM UserResult")
    rows = cursor.fetchall()

    # Inserting data into Treeview
    for row in rows:
        tree.insert("", tk.END, values=(row[0], row[1], row[2]))  # Using column indices

    conn.close()

    # Placing the Treeview on the page
    tree.pack(fill=tk.BOTH, expand=True)

    admin.mainloop()

def signUpPage():
    root.destroy()
    global sup
    sup = Tk()
    
    fname = StringVar()
    uname = StringVar()
    passW = StringVar()
    country = StringVar()
    
    
    sup_canvas = Canvas(sup,width=720,height=440,bg="pink")
    sup_canvas.pack()

    sup_frame = Frame(sup_canvas,bg="white")
    sup_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    heading = Label(sup_frame,text="Регистрация",fg="black",bg="white")
    heading.config(font=('calibri 40'))
    heading.place(relx=0.30,rely=0.1)

    #full name
    flabel = Label(sup_frame,text="ФИО",fg='black',bg='white')
    flabel.place(relx=0.21,rely=0.4)
    fname = Entry(sup_frame,bg='#d3d3d3',fg='black',textvariable = fname)
    fname.config(width=42)
    fname.place(relx=0.31,rely=0.4)

    #username
    ulabel = Label(sup_frame,text="Имя пользователя",fg='black',bg='white')
    ulabel.place(relx=0.12,rely=0.5)
    user = Entry(sup_frame,bg='#d3d3d3',fg='black',textvariable = uname)
    user.config(width=42)
    user.place(relx=0.31,rely=0.5)
    
    
    #password
    plabel = Label(sup_frame,text="Пароль",fg='black',bg='white')
    plabel.place(relx=0.215,rely=0.6)
    pas = Entry(sup_frame,bg='#d3d3d3',fg='black',show="*",textvariable = passW)
    pas.config(width=42)
    pas.place(relx=0.31,rely=0.6)
    
    
    
    #country
    clabel = Label(sup_frame,text="Страна",fg='black',bg='white')
    clabel.place(relx=0.215,rely=0.7)
    c = Entry(sup_frame,bg='#d3d3d3',fg='black',textvariable = country)
    c.config(width=42)
    c.place(relx=0.31,rely=0.7)
    def addUserToDataBase():
        
        fullname = fname.get()
        username = user.get()
        password = pas.get()
        country = c.get()
        
        conn = sqlite3.connect('quiz.db')
        create = conn.cursor()
        create.execute('CREATE TABLE IF NOT EXISTS userSignUp(FULLNAME text, USERNAME text,PASSWORD text,COUNTRY text)')
        create.execute("INSERT INTO userSignUp VALUES (?,?,?,?)",(fullname,username,password,country)) 
        conn.commit()
        create.execute('SELECT * FROM userSignUp')
        z=create.fetchall()
        print(z)
#        L2.config(text="Username is "+z[0][0]+"\nPassword is "+z[-1][1])
        conn.close()
        loginPage(z)
    def gotoLogin():
        conn = sqlite3.connect('quiz.db')
        create = conn.cursor()
        conn.commit()
        create.execute('SELECT * FROM userSignUp')
        z=create.fetchall()
        loginPage(z)
    #signup BUTTON
    sp = Button(sup_frame,text='Зарегистрироваться',padx=5,pady=5,width=5,command = addUserToDataBase,bg='green')
    sp.configure(width = 15,height=1, activebackground = "#33B5E5", relief = FLAT)
    sp.place(relx=0.4,rely=0.8)

    log = Button(sup_frame,text='Уже есть учётная запись?',padx=5,pady=5,width=5,command = gotoLogin,bg="white",fg='blue')
    log.configure(width = 18,height=1, activebackground = "#33B5E5", relief = FLAT)
    log.place(relx=0.39,rely=0.9)

    sup.mainloop()

def menu():
    login.destroy()
    global menu 
    menu = Tk()

    menu_canvas = Canvas(menu,width=720,height=440,bg="pink")
    menu_canvas.pack()

    menu_frame = Frame(menu_canvas,bg="white")
    menu_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    wel = Label(menu_canvas, text=' П р о й д и т е  о п р о с ',fg="white",bg="pink")
    wel.config(font=('Broadway 22'))
    wel.place(relx=0.25,rely=0.01)
    
    
    level = Label(menu_frame,text='Выберите тему викторины',bg="pink",font="calibri 18")
    level.place(relx=0.20,rely=0.3)
    
    
    var = IntVar()
    easyR = Radiobutton(menu_frame,text='Основы языка Python',bg="white",font="calibri 16",value=1,variable = var)
    easyR.place(relx=0.25,rely=0.4)
    
    mediumR = Radiobutton(menu_frame,text='Работа с функциями и модулями в Python',bg="white",font="calibri 16",value=2,variable = var)
    mediumR.place(relx=0.25,rely=0.5)
    
    hardR = Radiobutton(menu_frame,text='Работа с данными в Python',bg="white",font="calibri 16",value=3,variable = var)
    hardR.place(relx=0.25,rely=0.6)
    
    
    def navigate():
        
        x = var.get()
        print(x)
        if x == 1:
            menu.destroy()
            easy()
        elif x == 2:
            menu.destroy()
            medium()
        
        elif x == 3:
            menu.destroy()
            difficult()
        else:
            pass
    letsgo = Button(menu_frame,text="Let's Go",bg="white",font="calibri 12",command=navigate)
    letsgo.place(relx=0.25,rely=0.8)
    menu.mainloop()
def easy():
    
    global e
    e = Tk()
    
    easy_canvas = Canvas(e,width=720,height=440,bg="#101357")
    easy_canvas.pack()

    easy_frame = Frame(easy_canvas,bg="white")
    easy_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    
    def countDown():
        check = 0
        for k in range(10, 0, -1):
            
            if k == 1:
                check=-1
            timer.configure(text=k)
            easy_frame.update()
            time.sleep(1)
            
        timer.configure(text="Times up!")
        if check==-1:
            return (-1)
        else:
            return 0
    global score
    score = 0
    
    easyQ = [
                 [
                     "Какая команда используется для вывода текста на экран в Python?",
                     "print()",
                     "input()",
                     "scan()",
                     "read()"
                 ] ,
                 [
                     "Что такое переменная в Python и как ее объявить?" ,
                    "Это функция для хранения данных. Объявляется с помощью ключевого слова variable.",
                    "Это команда для выполнения определенного действия. Объявляется с помощью ключевого слова var.",
                    "Это имя, используемое для обозначения значения. Объявляется с помощью оператора =.",
                    "Это способ обращения к элементам списка. Объявляется с помощью оператора +."
                     
                 ],
                [
                    "Какой символ используется для обозначения однострочного комментария в Python?" ,
                    "#",
                    "//",
                    "/*",
                    "~"
                ],
                [
                    "Выберите код, который считает сумму двух чисел и выводит результат" ,
                    "sum(2, 3)",
                    "print(sum(2, 3))",
                    "add(2, 3)",
                    "print(add(2, 3))"
                ],
                [
                    "Что такое условный оператор if-else и как он используется в Python?" ,
                    "Это оператор для создания цикла. Используется для повторения определенного блока кода.",
                    "Это оператор для проверки условия. Если условие истинно, выполняется один блок кода, если ложно - другой.",
                    "Это оператор для объявления функции. Используется для выполнения определенного действия.",
                    "Это оператор для работы с текстовыми данными. Используется для поиска и замены символов."
                ]
            ]
    answer = [
                "print()",
                "Это функция для хранения данных. Объявляется с помощью ключевого слова variable.",
                "#",
                "print(sum(2, 3))",
                "Это оператор для проверки условия. Если условие истинно, выполняется один блок кода, если ложно - другой."
             ]
    li = ['',0,1,2,3,4]
    x = random.choice(li[1:])
    
    ques = Label(easy_frame,text =easyQ[x][0],font="calibri 12",bg="white")
    ques.place(relx=0.5,rely=0.2,anchor=CENTER)

    var = StringVar()
    
    a = Radiobutton(easy_frame,text=easyQ[x][1],font="calibri 10",value=easyQ[x][1],variable = var,bg="white")
    a.place(relx=0.5,rely=0.42,anchor=CENTER)

    b = Radiobutton(easy_frame,text=easyQ[x][2],font="calibri 10",value=easyQ[x][2],variable = var,bg="white")
    b.place(relx=0.5,rely=0.52,anchor=CENTER)

    c = Radiobutton(easy_frame,text=easyQ[x][3],font="calibri 10",value=easyQ[x][3],variable = var,bg="white")
    c.place(relx=0.5,rely=0.62,anchor=CENTER) 

    d = Radiobutton(easy_frame,text=easyQ[x][4],font="calibri 10",value=easyQ[x][4],variable = var,bg="white")
    d.place(relx=0.5,rely=0.72,anchor=CENTER) 
    
    li.remove(x)
    
    timer = Label(e)
    timer.place(relx=0.8,rely=0.82,anchor=CENTER)
    
    
    
    def display():
        
        if len(li) == 1:
                e.destroy()
                showMark(score)
        if len(li) == 2:
            nextQuestion.configure(text='End',command=calc)
                
        if li:
            x = random.choice(li[1:])
            ques.configure(text =easyQ[x][0])
            
            a.configure(text=easyQ[x][1],value=easyQ[x][1])
      
            b.configure(text=easyQ[x][2],value=easyQ[x][2])
      
            c.configure(text=easyQ[x][3],value=easyQ[x][3])
      
            d.configure(text=easyQ[x][4],value=easyQ[x][4])
            
            li.remove(x)
            print(li)
            y = countDown()
            if y == -1:
                display()

            
    def calc():
        global score
        if (var.get() in answer):
            score+=1
        display()
    
    submit = Button(easy_frame,command=calc,text="Submit")
    submit.place(relx=0.5,rely=0.82,anchor=CENTER)
    
    nextQuestion = Button(easy_frame,command=display,text="Next")
    nextQuestion.place(relx=0.87,rely=0.82,anchor=CENTER)
    
    y = countDown()
    if y == -1:
        display()
    e.mainloop()
    
    
def medium():
    
    global m
    m = Tk()
    
    med_canvas = Canvas(m,width=720,height=440,bg="#101357")
    med_canvas.pack()

    med_frame = Frame(med_canvas,bg="white")
    med_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    
    def countDown():
        check = 0
        for k in range(10, 0, -1):
            
            if k == 1:
                check=-1
            timer.configure(text=k)
            med_frame.update()
            time.sleep(1)
            
        timer.configure(text="Times up!")
        if check==-1:
            return (-1)
        else:
            return 0
        
    global score
    score = 0
    
    mediumQ = [
                [
                    "Which of the following is not an exception handling keyword in Python?",
                     "accept",
                     "finally",
                     "except",
                     "try"
                ],
                [
                    "Suppose list1 is [3, 5, 25, 1, 3], what is min(list1)?",
                    "3",
                    "5",
                    "25",
                    "1"
                ],
                [
                    "Suppose list1 is [2, 33, 222, 14, 25], What is list1[-1]?",
                    "Error",
                    "None",
                    "25",
                    "2"
                ],
                [
                    "print(0xA + 0xB + 0xC):",
                    "0xA0xB0xC",
                    "Error",
                    "0x22",
                    "33"
                ],
                [
                    "Which of the following is invalid?",
                    "_a = 1",
                    "__a = 1",
                    "__str__ = 1",
                    "none of the mentioned"
                ], 
            ]
    answer = [
            "accept",
            "1",
            "25",
            "33",
            "none of the mentioned"
            ]
    
    li = ['',0,1,2,3,4]
    x = random.choice(li[1:])
    
    ques = Label(med_frame,text =mediumQ[x][0],font="calibri 12",bg="white")
    ques.place(relx=0.5,rely=0.2,anchor=CENTER)

    var = StringVar()
    
    a = Radiobutton(med_frame,text=mediumQ[x][1],font="calibri 10",value=mediumQ[x][1],variable = var,bg="white")
    a.place(relx=0.5,rely=0.42,anchor=CENTER)

    b = Radiobutton(med_frame,text=mediumQ[x][2],font="calibri 10",value=mediumQ[x][2],variable = var,bg="white")
    b.place(relx=0.5,rely=0.52,anchor=CENTER)

    c = Radiobutton(med_frame,text=mediumQ[x][3],font="calibri 10",value=mediumQ[x][3],variable = var,bg="white")
    c.place(relx=0.5,rely=0.62,anchor=CENTER) 

    d = Radiobutton(med_frame,text=mediumQ[x][4],font="calibri 10",value=mediumQ[x][4],variable = var,bg="white")
    d.place(relx=0.5,rely=0.72,anchor=CENTER) 
    
    li.remove(x)
    
    timer = Label(m)
    timer.place(relx=0.8,rely=0.82,anchor=CENTER)
    
    
    
    def display():
        
        if len(li) == 1:
                m.destroy()
                showMark(score)
        if len(li) == 2:
            nextQuestion.configure(text='End',command=calc)
                
        if li:
            x = random.choice(li[1:])
            ques.configure(text =mediumQ[x][0])
            
            a.configure(text=mediumQ[x][1],value=mediumQ[x][1])
      
            b.configure(text=mediumQ[x][2],value=mediumQ[x][2])
      
            c.configure(text=mediumQ[x][3],value=mediumQ[x][3])
      
            d.configure(text=mediumQ[x][4],value=mediumQ[x][4])
            
            li.remove(x)
            print(li)
            y = countDown()
            if y == -1:
                display()

            
    def calc():
        global score
        if (var.get() in answer):
            score+=1
        display()
    
    submit = Button(med_frame,command=calc,text="Submit")
    submit.place(relx=0.5,rely=0.82,anchor=CENTER)
    
    nextQuestion = Button(med_frame,command=display,text="Next")
    nextQuestion.place(relx=0.87,rely=0.82,anchor=CENTER)
    
    y = countDown()
    if y == -1:
        display()
    m.mainloop()
def difficult():
    
       
    global h
    h = Tk()
    
    hard_canvas = Canvas(h,width=720,height=440,bg="#101357")
    hard_canvas.pack()

    hard_frame = Frame(hard_canvas,bg="white")
    hard_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    
    def countDown():
        check = 0
        for k in range(10, 0, -1):
            
            if k == 1:
                check=-1
            timer.configure(text=k)
            hard_frame.update()
            time.sleep(1)
            
        timer.configure(text="Times up!")
        if check==-1:
            return (-1)
        else:
            return 0
        
    global score
    score = 0
    
    hardQ = [
                [
       "All keywords in Python are in _________",
        "lower case",
        "UPPER CASE",
        "Capitalized",
        "None of the mentioned"
    ],
    [
        "Which of the following cannot be a variable?",
        "__init__",
        "in",
        "it",
        "on"
    ],
    [
     "Which of the following is a Python tuple?",
        "[1, 2, 3]",
        "(1, 2, 3)",
        "{1, 2, 3}",
        "{}"   
    ],
    [
        "What is returned by math.ceil(3.4)?",
        "3",
        "4",
        "4.0",
        "3.0"
    ],
    [
        "What will be the output of print(math.factorial(4.5))?",
        "24",
        "120",
        "error",
        "24.0"
    ] 
            
]
    answer = [
            "None of the mentioned",
            "in",
            "(1,2,3)",
            "4",
            "error"
            ]
    
    li = ['',0,1,2,3,4]
    x = random.choice(li[1:])
    
    ques = Label(hard_frame,text =hardQ[x][0],font="calibri 12",bg="white")
    ques.place(relx=0.5,rely=0.2,anchor=CENTER)

    var = StringVar()
    
    a = Radiobutton(hard_frame,text=hardQ[x][1],font="calibri 10",value=hardQ[x][1],variable = var,bg="white")
    a.place(relx=0.5,rely=0.42,anchor=CENTER)

    b = Radiobutton(hard_frame,text=hardQ[x][2],font="calibri 10",value=hardQ[x][2],variable = var,bg="white")
    b.place(relx=0.5,rely=0.52,anchor=CENTER)

    c = Radiobutton(hard_frame,text=hardQ[x][3],font="calibri 10",value=hardQ[x][3],variable = var,bg="white")
    c.place(relx=0.5,rely=0.62,anchor=CENTER) 

    d = Radiobutton(hard_frame,text=hardQ[x][4],font="calibri 10",value=hardQ[x][4],variable = var,bg="white")
    d.place(relx=0.5,rely=0.72,anchor=CENTER) 
    
    li.remove(x)
    
    timer = Label(h)
    timer.place(relx=0.8,rely=0.82,anchor=CENTER)
    
    
    
    def display():
        
        if len(li) == 1:
                h.destroy()
                showMark(score)
        if len(li) == 2:
            nextQuestion.configure(text='End',command=calc)
                
        if li:
            x = random.choice(li[1:])
            ques.configure(text =hardQ[x][0])
            
            a.configure(text=hardQ[x][1],value=hardQ[x][1])
      
            b.configure(text=hardQ[x][2],value=hardQ[x][2])
      
            c.configure(text=hardQ[x][3],value=hardQ[x][3])
      
            d.configure(text=hardQ[x][4],value=hardQ[x][4])
            
            li.remove(x)
            print(li)
            y = countDown()
            if y == -1:
                display()

            
    def calc():
        global score
        if (var.get() in answer):
            score+=1
        display()
    
    submit = Button(hard_frame,command=calc,text="Submit")
    submit.place(relx=0.5,rely=0.82,anchor=CENTER)
    
    nextQuestion = Button(hard_frame,command=display,text="Next")
    nextQuestion.place(relx=0.87,rely=0.82,anchor=CENTER)
    
    y = countDown()
    if y == -1:
        display()
    h.mainloop()

def showMark(mark):
    global sh
    sh = Tk()
    
    show_canvas = Canvas(sh,width=720,height=440,bg="#101357")
    show_canvas.pack()

    show_frame = Frame(show_canvas,bg="white")
    show_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)
    
    st = global_username + ", your score is "+str(mark)

    mlabel = Label(show_canvas,text=st,fg="black")
    mlabel.place(relx=0.5,rely=0.2,anchor=CENTER)
    conn = sqlite3.connect('quiz.db')  # Подставьте имя вашей базы данных
    cursor = conn.cursor()

    # Создание таблицы, если она не существует
    cursor.execute('''CREATE TABLE IF NOT EXISTS UserResult
                         (UserName TEXT, Score INT)''')

    # Вставка данных в таблицу
    cursor.execute("INSERT INTO UserResult (UserName, Score) VALUES (?, ?)",
                   (global_username, mark))

    conn.commit()
    conn.close()



    sh.mainloop()




def start():
    global root 
    root = Tk()
    canvas = Canvas(root,width = 1280,height = 744)
    canvas.grid(column = 0 , row = 1)
    img = PhotoImage(file="background.png")
    canvas.create_image(50,10,image=img,anchor=NW)

    button = Button(root, text='Начать',command = signUpPage)
    button.configure(width = 102,height=2, activebackground = "#33B5E5", bg ='green', relief = RAISED)
    button.grid(column = 0 , row = 2)

    root.mainloop()
    
    
if __name__=='__main__':
    start()
