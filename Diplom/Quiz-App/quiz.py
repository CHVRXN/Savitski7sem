import random
import sqlite3
import time
import tkinter as tk
from PIL import Image, ImageTk
import openpyxl
import os
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from openpyxl import Workbook

def loginPage(logdata):
    sup.destroy()
    global login
    login = Tk()

    user_name = StringVar()
    password = StringVar()
    window_width = 720
    window_height = 440

    # Получение размеров экрана
    screen_width = login.winfo_screenwidth()
    screen_height = login.winfo_screenheight()

    # Вычисление позиции окна для центрирования
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    # Установка размеров и позиции окна
    login.geometry(f"{window_width}x{window_height}+{x}+{y}")

    login_canvas = Canvas(login, width=720, height=440, bg="pink")
    login_canvas.pack()

    login_frame = Frame(login_canvas, bg="white")
    login_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    heading = Label(login_frame, text="Авторизация", fg="black", bg="white")
    heading.config(font=('calibri 40'))
    heading.place(relx=0.2, rely=0.1)

    # USER NAME
    ulabel = Label(login_frame, text="Имя пользователя", fg='black', bg='white')
    ulabel.place(relx=0.12, rely=0.4)
    uname = Entry(login_frame, bg='#d3d3d3', fg='black', textvariable=user_name)
    uname.config(width=42)
    uname.place(relx=0.31, rely=0.4)

    # PASSWORD
    plabel = Label(login_frame, text="Пароль", fg='black', bg='white')
    plabel.place(relx=0.215, rely=0.5)
    pas = Entry(login_frame, bg='#d3d3d3', fg='black', show="*", textvariable=password)
    pas.config(width=42)
    pas.place(relx=0.31, rely=0.5)

    def check():
        global global_username
        global testName
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

    # LOGIN BUTTON
    log = Button(login_frame, text='Войти', padx=5, pady=5, width=5, command=check)
    log.configure(width=15, height=1, activebackground="#33B5E5", relief=FLAT)
    log.place(relx=0.4, rely=0.6)

    login.mainloop()


def adminpage():
    global global_username

    def search_records():
        search_name = search_entry.get().strip()  # Получаем введенное имя пользователя
        selected_quiz = quiz_combobox.get()  # Получаем выбранное название викторины
        tree.delete(*tree.get_children())  # Очищаем Treeview перед отображением результатов поиска

        # Если поле для поиска пустое, выводим все данные из таблицы
        if not search_name:
            conn = sqlite3.connect('assets/quiz.db')
            cursor = conn.cursor()
            if selected_quiz == "Все викторины":
                cursor.execute("SELECT * FROM UserResult")
            else:
                cursor.execute("SELECT * FROM UserResult WHERE TestName=?", (selected_quiz,))
            rows = cursor.fetchall()
            conn.close()
        else:
            # Получаем данные из таблицы UserResult для указанного имени пользователя и выбранного названия викторины
            conn = sqlite3.connect('assets/quiz.db')
            cursor = conn.cursor()
            if selected_quiz == "Все викторины":
                cursor.execute("SELECT * FROM UserResult WHERE UserName=?", (search_name,))
            else:
                cursor.execute("SELECT * FROM UserResult WHERE UserName=? AND TestName=?", (search_name, selected_quiz))
            rows = cursor.fetchall()
            conn.close()

        # Вставляем найденные данные в Treeview
        for row in rows:
            tree.insert("", tk.END, values=(row[0], row[1], row[2], row[3]))

    def delete_records():
        selected_items = tree.selection()  # Получаем выбранные элементы в Treeview
        for item in selected_items:
            result_id = tree.item(item)['values'][0]  # Получаем ResultID выбранной записи
            tree.delete(item)  # Удаляем выбранный элемент из Treeview

            # Удаление записи из базы данных
            conn = sqlite3.connect('assets/quiz.db')
            cursor = conn.cursor()
            cursor.execute("DELETE FROM UserResult WHERE ResultID=?", (result_id,))
            conn.commit()
            conn.close()

    def create_excel():
        workbook = Workbook()
        worksheet = workbook.active

        # Заголовки столбцов
        columns = ["ResultID", "UserName", "Score", "TestName"]
        for col_num, column_title in enumerate(columns, 1):
            worksheet.cell(row=1, column=col_num, value=column_title)

        # Данные из Treeview
        for row_num, item in enumerate(tree.get_children(), 2):
            values = tree.item(item)['values']
            for col_num, value in enumerate(values, 1):
                worksheet.cell(row=row_num, column=col_num, value=value)

        # Сохранение файла
        file_name = "quiz_results.xlsx"
        workbook.save(file_name)

        # Открытие Excel-таблицы с использованием программы Excel
        os.system(f'start excel.exe "{file_name}"')

    admin = tk.Tk()
    admin.title("Admin Page")
    admin.geometry("1200x600")
    # Размеры окна
    window_width = 1200
    window_height = 600

    # Получение размеров экрана
    screen_width = admin.winfo_screenwidth()
    screen_height = admin.winfo_screenheight()

    # Вычисление позиции окна для центрирования
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    # Установка размеров и позиции окна
    admin.geometry(f"{window_width}x{window_height}+{x}+{y}")
    # Creating search entry and button
    search_label = tk.Label(admin, text="Введите имя пользователя:")
    search_label.pack()

    search_entry = tk.Entry(admin)
    search_entry.pack()

    # Creating ComboBox for quiz selection
    quiz_label = tk.Label(admin, text="Выберите викторину:")
    quiz_label.pack()

    quiz_combobox = ttk.Combobox(admin, values=["Все викторины", "Работа с функциями и модулями", "Основы языка Python", "Работа с данными в Python"])
    quiz_combobox.current(0)  # Устанавливаем выбор по умолчанию на "Все викторины"
    quiz_combobox.pack()

    search_button = tk.Button(admin, text="Поиск", command=search_records)
    search_button.pack()
    create_excel_button = Button(admin, text="Создать Excel", command=create_excel)
    create_excel_button.pack()
    delete_button = tk.Button(admin, text="Удалить", command=delete_records)
    delete_button.pack()
    # Creating Treeview
    tree = ttk.Treeview(admin, show="headings")
    tree["columns"] = ("ResultID", "UserName", "Score", "TestName")
    tree["displaycolumns"] = ("ResultID", "UserName", "Score", "TestName")

    # Setting column headings
    tree.heading("ResultID", text="Номер результата")
    tree.heading("UserName", text="Имя пользователя")
    tree.heading("Score", text="Оценка")
    tree.heading("TestName", text="Название викторины")

    # Getting data from the UserResult table
    conn = sqlite3.connect('assets/quiz.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM UserResult")
    rows = cursor.fetchall()

    # Inserting data into Treeview
    for row in rows:
        tree.insert("", tk.END, values=(row[0], row[1], row[2], row[3]))  # Using column indices

    conn.close()

    # Placing the Treeview on the page
    tree.pack(fill=tk.BOTH, expand=True)

    admin.mainloop()


def signUpPage():
    root.destroy()
    global sup
    sup = Tk()
    # Центрирование окна
    window_width = 720
    window_height = 440

    screen_width = sup.winfo_screenwidth()
    screen_height = sup.winfo_screenheight()

    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    sup.geometry(f"{window_width}x{window_height}+{x}+{y}")
    fname = StringVar()
    uname = StringVar()
    passW = StringVar()
    country = StringVar()

    sup_canvas = Canvas(sup, width=720, height=440, bg="pink")
    sup_canvas.pack()

    sup_frame = Frame(sup_canvas, bg="white")
    sup_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    heading = Label(sup_frame, text="Регистрация", fg="black", bg="white")
    heading.config(font=('calibri 40'))
    heading.place(relx=0.30, rely=0.1)

    # full name
    flabel = Label(sup_frame, text="ФИО", fg='black', bg='white')
    flabel.place(relx=0.21, rely=0.4)
    fname = Entry(sup_frame, bg='#d3d3d3', fg='black', textvariable=fname)
    fname.config(width=42)
    fname.place(relx=0.31, rely=0.4)

    # username
    ulabel = Label(sup_frame, text="Имя пользователя", fg='black', bg='white')
    ulabel.place(relx=0.12, rely=0.5)
    user = Entry(sup_frame, bg='#d3d3d3', fg='black', textvariable=uname)
    user.config(width=42)
    user.place(relx=0.31, rely=0.5)

    # password
    plabel = Label(sup_frame, text="Пароль", fg='black', bg='white')
    plabel.place(relx=0.215, rely=0.6)
    pas = Entry(sup_frame, bg='#d3d3d3', fg='black', show="*", textvariable=passW)
    pas.config(width=42)
    pas.place(relx=0.31, rely=0.6)

    # country
    clabel = Label(sup_frame, text="Страна", fg='black', bg='white')
    clabel.place(relx=0.215, rely=0.7)
    c = Entry(sup_frame, bg='#d3d3d3', fg='black', textvariable=country)
    c.config(width=42)
    c.place(relx=0.31, rely=0.7)

    def addUserToDataBase():
        fullname = fname.get()
        username = user.get()
        password = pas.get()
        country = c.get()

        conn = sqlite3.connect('assets/quiz.db')
        create = conn.cursor()
        create.execute('CREATE TABLE IF NOT EXISTS userSignUp(FULLNAME text, USERNAME text,PASSWORD text,COUNTRY text)')
        create.execute("INSERT INTO userSignUp VALUES (?,?,?,?)", (fullname, username, password, country))
        conn.commit()
        create.execute('SELECT * FROM userSignUp')
        z = create.fetchall()
        print(z)
        #        L2.config(text="Username is "+z[0][0]+"\nPassword is "+z[-1][1])
        conn.close()
        loginPage(z)

    def gotoLogin():
        conn = sqlite3.connect('assets/quiz.db')
        create = conn.cursor()
        conn.commit()
        create.execute('SELECT * FROM userSignUp')
        z = create.fetchall()
        loginPage(z)

    # signup BUTTON
    sp = Button(sup_frame, text='Зарегистрироваться', padx=5, pady=5, width=5, command=addUserToDataBase, bg='green')
    sp.configure(width=15, height=1, activebackground="#33B5E5", relief=FLAT)
    sp.place(relx=0.4, rely=0.8)

    log = Button(sup_frame, text='Уже есть учётная запись?', padx=5, pady=5, width=5, command=gotoLogin, bg="white",
                 fg='blue')
    log.configure(width=18, height=1, activebackground="#33B5E5", relief=FLAT)
    log.place(relx=0.39, rely=0.9)

    sup.mainloop()


def menu():
    login.destroy()
    global menu
    menu = Tk()
    # Центрирование окна
    window_width = 720
    window_height = 440

    screen_width = menu.winfo_screenwidth()
    screen_height = menu.winfo_screenheight()

    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    menu.geometry(f"{window_width}x{window_height}+{x}+{y}")
    menu_canvas = Canvas(menu, width=720, height=440, bg="pink")
    menu_canvas.pack()

    menu_frame = Frame(menu_canvas, bg="white")
    menu_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    wel = Label(menu_canvas, text=' П р о й д и т е  о п р о с ', fg="white", bg="pink")
    wel.config(font=('Broadway 22'))
    wel.place(relx=0.25, rely=0.01)

    level = Label(menu_frame, text='Выберите тему викторины', bg="pink", font="calibri 18")
    level.place(relx=0.20, rely=0.3)

    var = IntVar()
    easyR = Radiobutton(menu_frame, text='Основы языка Python', bg="white", font="calibri 16", value=1, variable=var)
    easyR.place(relx=0.25, rely=0.4)

    mediumR = Radiobutton(menu_frame, text='Работа с функциями и модулями в Python', bg="white", font="calibri 16",
                          value=2, variable=var)
    mediumR.place(relx=0.25, rely=0.5)

    hardR = Radiobutton(menu_frame, text='Работа с данными в Python', bg="white", font="calibri 16", value=3,
                        variable=var)
    hardR.place(relx=0.25, rely=0.6)

    def navigate():

        x = var.get()
        print(x)
        if x == 1:

            easy()
        elif x == 2:

            medium()

        elif x == 3:

            difficult()
        else:
            pass

    letsgo = Button(menu_frame, text="Let's Go", bg="white", font="calibri 12", command=navigate)
    letsgo.place(relx=0.25, rely=0.8)
    menu.mainloop()


def easy():
    global e
    e = Tk()
    global testName
    testName = "Основы языка Python"
    # Определение размеров окна
    window_width = 720
    window_height = 440

    # Получение размеров экрана
    screen_width = e.winfo_screenwidth()
    screen_height = e.winfo_screenheight()

    # Вычисление координат центра экрана
    x = int((screen_width / 2) - (window_width / 2))
    y = int((screen_height / 2) - (window_height / 2))

    # Установка положения окна
    e.geometry(f"{window_width}x{window_height}+{x}+{y}")
    easy_canvas = Canvas(e, width=720, height=440, bg="#101357")
    easy_canvas.pack()

    easy_frame = Frame(easy_canvas, bg="white")
    easy_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    def countDown():
        check = 0
        for k in range(30, 0, -1):

            if k == 1:
                check = -1
            timer.configure(text=k)
            easy_frame.update()
            time.sleep(1)

        timer.configure(text="Times up!")
        if check == -1:
            return -1
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
        ],
        [
            "Что такое переменная в Python и как ее объявить?",
            "Это функция для хранения данных. Объявляется с помощью ключевого слова variable.",
            "Это команда для выполнения определенного действия. Объявляется с помощью ключевого слова var.",
            "Это имя, используемое для обозначения значения. Объявляется с помощью оператора =.",
            "Это способ обращения к элементам списка. Объявляется с помощью оператора +."
        ],
        [
            "Какой символ используется для обозначения однострочного комментария в Python?",
            "#",
            "//",
            "/*",
            "~"
        ],
        [
            "Выберите код, который считает сумму двух чисел и выводит результат",
            "sum(2, 3)",
            "print(sum(2, 3))",
            "add(2, 3)",
            "print(add(2, 3))"
        ],
        [
            "Что такое условный оператор if-else и как он используется в Python?",
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
    li = ['', 0, 1, 2, 3, 4]
    x = random.choice(li[1:])

    ques = Label(easy_frame, text=easyQ[x][0], font="calibri 12", bg="white")
    ques.place(relx=0.5, rely=0.2, anchor=CENTER)

    var = StringVar()

    a = Radiobutton(easy_frame, text=easyQ[x][1], font="calibri 10", value=easyQ[x][1], variable=var, bg="white")
    a.place(relx=0.5, rely=0.42, anchor=CENTER)

    b = Radiobutton(easy_frame, text=easyQ[x][2], font="calibri 10", value=easyQ[x][2], variable=var, bg="white")
    b.place(relx=0.5, rely=0.52, anchor=CENTER)

    c = Radiobutton(easy_frame, text=easyQ[x][3], font="calibri 10", value=easyQ[x][3], variable=var, bg="white")
    c.place(relx=0.5, rely=0.62, anchor=CENTER)

    d = Radiobutton(easy_frame, text=easyQ[x][4], font="calibri 10", value=easyQ[x][4], variable=var, bg="white")
    d.place(relx=0.5, rely=0.72, anchor=CENTER)

    li.remove(x)

    timer = Label(e)
    timer.place(relx=0.8, rely=0.82, anchor=CENTER)

    def display():
        if len(li) == 1:
            e.destroy()
            showMark(score, testName)

        if len(li) == 2:
            nextQuestion.configure(text='End', command=calc)

        if li:
            x = random.choice(li[1:])
            ques.configure(text=easyQ[x][0])

            a.configure(text=easyQ[x][1], value=easyQ[x][1])

            b.configure(text=easyQ[x][2], value=easyQ[x][2])

            c.configure(text=easyQ[x][3], value=easyQ[x][3])

            d.configure(text=easyQ[x][4], value=easyQ[x][4])

            li.remove(x)
            print(li)
            y = countDown()
            if y == -1:
                display()

    def calc():
        global score
        if var.get() in answer:
            score += 1
        display()

    submit = Button(easy_frame, command=calc, text="Submit")
    submit.place(relx=0.5, rely=0.82, anchor=CENTER)

    nextQuestion = Button(easy_frame, command=display, text="Next")
    nextQuestion.place(relx=0.87, rely=0.82, anchor=CENTER)

    y = countDown()
    if y == -1:
        display()
    e.mainloop()


def medium():

    testName = "Работа с функциями и модулями"

    global m
    m = Tk()
    window_width = 720
    window_height = 440

    screen_width = m.winfo_screenwidth()
    screen_height = m.winfo_screenheight()

    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    m.geometry(f"{window_width}x{window_height}+{x}+{y}")
    med_canvas = Canvas(m, width=720, height=440, bg="#101357")
    med_canvas.pack()

    med_frame = Frame(med_canvas, bg="white")
    med_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    global score
    score = 0

    mediumQ = [
        [
            "Объявите функцию calc",
            "def calc()",
        ],
        [
            "Напишите код для импорта модуля tkinter",
            "import tkinter as tk",
        ],
        [
            "Напишите код, который выводит строку Hello, World! на экран в одну строку",
            "print('Hello, World!')",
        ],
        [
            "Напишите код, который выводит числа от 1 до 10 в одну строку",
            "print(*range(1, 11))",
        ],
        [
            "Напишите код, который выводит квадраты чисел от 1 до 5 в одну строку",
            "print(*[x**2 for x in range(1, 6)])",
        ],
    ]
    answer = [
        "def calc()",
        "import tkinter as tk",
        "print('Hello, World!')",
        "print(*range(1, 11))",
        "print(*[x**2 for x in range(1, 6)])",
    ]

    li = [0, 1, 2, 3, 4]
    random.shuffle(li)
    question_index = 0

    ques = Label(med_frame, text=mediumQ[li[question_index]][0], font="calibri 12", bg="white")
    ques.pack(pady=10, padx=10, anchor=CENTER)

    entry = Entry(med_frame, width=30, font="calibri 10")
    entry.pack(pady=10, padx=10, anchor=CENTER)

    def check_answer():
        user_answer = entry.get().strip()
        if user_answer == answer[li[question_index]]:
            global score
            score += 1
            messagebox.showinfo("Результат", "Верно!")
            next_question()
        else:
            messagebox.showinfo("Результат", "Неверно!")

    def next_question():
        nonlocal question_index
        question_index += 1
        if question_index < len(li):
            ques.configure(text=mediumQ[li[question_index]][0])
            entry.delete(0, END)
        else:
            m.destroy()
            showMark(score, testName)


    submit = Button(med_frame, command=check_answer, text="Submit")
    submit.pack(pady=10, padx=10, anchor=CENTER)

    nextQuestion = Button(med_frame, command=next_question, text="Next")
    nextQuestion.pack(pady=10, padx=10, anchor=CENTER)

    m.mainloop()


def difficult():
    testName = "Работа с данными в Python"



    def check_order():

        if user_order == correct_order:
            success_label.configure(text="Порядок верный! Успех!", fg="green")
            score_label.configure(text="Оценка: 5 баллов")
            global score
            score = 5
            showMark(score, testName)
        else:
            success_label.configure(text="Неправильный порядок. Попробуйте еще раз.", fg="red")

    def move_up():
        selected_index = code_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            if index > 0:
                item = user_order.pop(index)
                user_order.insert(index - 1, item)
                update_code_listbox()
                code_listbox.selection_set(index - 1)

    def move_down():
        selected_index = code_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            if index < len(user_order) - 1:
                item = user_order.pop(index)
                user_order.insert(index + 1, item)
                update_code_listbox()
                code_listbox.selection_set(index + 1)

    def update_code_listbox():
        code_listbox.delete(0, tk.END)
        for code in user_order:
            code_listbox.insert(tk.END, code)

    # Правильный порядок строк кода
    correct_order = [
        "def calc(a, b, operator):",
        "    if operator == '+':",
        "        return a + b",
        "    elif operator == '-':",
        "        return a - b",
        "    elif operator == '*':",
        "        return a * b",
        "    elif operator == '/':",
        "        if b != 0:",
        "            return a / b",
        "        else:",
        "            return 'Error: division by zero'",
        "",
        "result = calc(5, 2, '+')",
        "print('Result:', result)"
    ]

    # Случайное перемешивание строк кода для пользователя
    user_order = correct_order.copy()
    random.shuffle(user_order)

    # Инициализация окна игры
    h = tk.Tk()
    h.geometry("450x450")
    h.title("Разместите код в нужном порядке.Порядок: +-*/")
    # Определение размеров окна
    window_width = 450
    window_height = 450

    # Получение размеров экрана
    screen_width = h.winfo_screenwidth()
    screen_height = h.winfo_screenheight()

    # Вычисление координат центра экрана
    x = int((screen_width / 2) - (window_width / 2))
    y = int((screen_height / 2) - (window_height / 2))

    # Установка положения окна
    h.geometry(f"{window_width}x{window_height}+{x}+{y}")
    # Создание и расположение виджетов
    code_listbox = tk.Listbox(h, width=50, height=15, selectmode=tk.SINGLE)
    code_listbox.pack()

    success_label = tk.Label(h, text="", font="Arial 12 bold")
    success_label.pack()

    score_label = tk.Label(h, text="Оценка: 0 баллов", font="Arial 12 bold")
    score_label.pack()

    check_button = tk.Button(h, text="Проверить порядок", command=check_order)
    check_button.pack()

    update_code_listbox()

    h.bind("<Up>", lambda event: move_up())
    h.bind("<Down>", lambda event: move_down())

    h.mainloop()


def showMark(mark, testName):
    sh = tk.Toplevel()
    sh.title("Результаты викторины")

    window_width = 720
    window_height = 440

    screen_width = sh.winfo_screenwidth()
    screen_height = sh.winfo_screenheight()

    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    sh.geometry(f"{window_width}x{window_height}+{x}+{y}")
    show_canvas = tk.Canvas(sh, width=720, height=440, bg="#101357")
    show_canvas.pack()

    show_frame = tk.Frame(show_canvas, bg="white")
    show_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    st = f"{global_username}, Ваша оценка {mark}"

    title_label = tk.Label(show_frame, text="Результаты викторины", font=("Arial", 20), bg="white")
    title_label.pack(pady=20)

    score_label = tk.Label(show_frame, text=st, font=("Arial", 16), bg="white")
    score_label.pack(pady=20)

    image_path = "succecimage.png" if mark >= 4 else "unsucces.png"
    image = tk.PhotoImage(file=image_path)

    image_label = tk.Label(show_frame, image=image, bg="white")
    image_label.image = image  # Сохраняем ссылку на изображение, чтобы избежать ошибки
    image_label.pack(pady=20)

    conn = sqlite3.connect('assets/quiz.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS UserResult
                    (UserName TEXT, Score INT, TestName)''')

    cursor.execute("INSERT INTO UserResult (UserName, Score, TestName) VALUES (?, ?, ?)",
                   (global_username, mark, testName))

    conn.commit()
    conn.close()

    sh.mainloop()


def start():
    global root
    root = Tk()
    # Размеры окна
    window_width = 1280
    window_height = 744

    # Получение размеров экрана
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Вычисление позиции окна для центрирования
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    # Установка размеров и позиции окна
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")
    canvas = Canvas(root, width=1280, height=700)
    canvas.grid(column=0, row=1)
    img = PhotoImage(file="background.png")
    canvas.create_image(50, 10, image=img, anchor=NW)

    button = Button(root, text='Начать', command=signUpPage)
    button.configure(width=102, height=2, activebackground="#33B5E5", bg='green', relief=RAISED)
    button.grid(column=0, row=2)

    root.mainloop()


if __name__ == '__main__':
    start()
