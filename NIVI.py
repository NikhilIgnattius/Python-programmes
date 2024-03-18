import speech_recognition as sr
import csv
import pywhatkit
from gtts import gTTS
from playsound import playsound
import datetime
from tkinter import *


calculation = ""
text = ""
player = ""
direction = []


def runNivi():
    def speech(text):
        print(text)
        language = "en"
        output = gTTS(text=text, lang=language, slow=False)
        output.save("/Users/Kanix/PycharmProjects/pythonProject12/sounds/output.mp3")
        playsound("/Users/Kanix/PycharmProjects/pythonProject12/sounds/output.mp3")

    def get_audio():
        recorder = sr.Recognizer()

        with sr.Microphone() as source:
            print("listening..")
            playsound("/Users/Kanix/PycharmProjects/pythonProject12/sounds/activate.mp3")
            audio = recorder.listen(source)

        text = recorder.recognize_google(audio)
        print(f"You said:{text}")
        return text

    text = get_audio()

    if "play" in text.lower():
        playsound("/Users/Kanix/PycharmProjects/pythonProject12/sounds/activate2.mp3")
        speech("playing for you on youtube")
        pywhatkit.playonyt(text)

    elif "tic-tac-toe" in text.lower():
        playsound("/Users/Kanix/PycharmProjects/pythonProject12/sounds/activate2.mp3")
        speech("opening tic tac toe. Enjoy playing.")

        import random

        def next_turn(row, column):
            global player

            if buttons[row][column]['text'] == "" and check_winner() is False:

                if player == players[0]:

                    buttons[row][column]['text'] = player

                    if check_winner() is False:
                        player = players[1]
                        label.config(text=(players[1] + " turn"))

                    elif check_winner() is True:
                        label.config(text=(players[0] + " wins"))

                    elif check_winner() == "Tie":
                        label.config(text="Tie!")

                else:

                    buttons[row][column]['text'] = player

                    if check_winner() is False:
                        player = players[0]
                        label.config(text=(players[0] + " turn"))

                    elif check_winner() is True:
                        label.config(text=(players[1] + " wins"))

                    elif check_winner() == "Tie":
                        label.config(text="Tie!")

        def check_winner():
            for row in range(3):
                if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
                    buttons[row][0].config(bg="green")
                    buttons[row][1].config(bg="green")
                    buttons[row][2].config(bg="green")
                    return True

            for column in range(3):
                if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
                    buttons[0][column].config(bg="green")
                    buttons[1][column].config(bg="green")
                    buttons[2][column].config(bg="green")
                    return True

            if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
                buttons[0][0].config(bg="green")
                buttons[1][1].config(bg="green")
                buttons[2][2].config(bg="green")
                return True

            elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
                buttons[0][2].config(bg="green")
                buttons[1][1].config(bg="green")
                buttons[2][0].config(bg="green")
                return True

            elif empty_spaces() is False:

                for row in range(3):
                    for column in range(3):
                        buttons[row][column].config(bg="yellow")
                return "Tie"

            else:
                return False

        def empty_spaces():
            spaces = 9

            for row in range(3):
                for column in range(3):
                    if buttons[row][column]['text'] != "":
                        spaces -= 1

            if spaces == 0:
                return False
            else:
                return True

        def new_game():
            global player

            player = random.choice(players)

            label.config(text=player + " turn")

            for row in range(3):
                for column in range(3):
                    buttons[row][column].config(text="", bg="#F0F0F0")

        window = Tk()
        window.title("Tic-Tac-Toe")
        players = ["x", "o"]
        player = random.choice(players)
        buttons = [[0, 0, 0],
                   [0, 0, 0],
                   [0, 0, 0]]

        label = Label(text=player + " turn", font=('consolas', 40))
        label.pack(side="top")

        reset_button = Button(text="restart", font=('consolas', 20), command=new_game)
        reset_button.pack(side="top")

        frame = Frame(window)
        frame.pack()

        for row in range(3):
            for column in range(3):
                buttons[row][column] = Button(frame, text="", font=('consolas', 40), width=5, height=2,
                                              command=lambda row=row, column=column: next_turn(row, column))
                buttons[row][column].grid(row=row, column=column)

        window.mainloop()





    elif "good night" in text.lower():
        playsound("/Users/Kanix/PycharmProjects/pythonProject12/sounds/activate2.mp3")
        speech("Sleep tight")
        playsound("/Users/Kanix/PycharmProjects/pythonProject12/sounds/closesiri.mp3")
        exit()

    elif "bye" in text.lower():
        speech("goodbye!")
        playsound("/Users/Kanix/PycharmProjects/pythonProject12/sounds/closesiri.mp3")
        exit()

    elif "timer" in text.lower():
        playsound("/Users/Kanix/PycharmProjects/pythonProject12/sounds/activate2.mp3")
        speech("Starting your timer.")
        import tkinter
        import time
        from tkinter import messagebox

        root = tkinter.Tk()
        root.geometry('400x300')
        root.title('Nivi Timer')
        root.config(bg='green')

        root.stop_loop = False

        def Clock():
            displaytime = time.strftime('%H:%M:%S %p')
            displaytimelabel.config(text=displaytime)
            displaytimelabel.after(1000, Clock)

        def stop():
            root.destroy()

        def timer():
            time1 = int(HOUR) * 3600 + int(MINUTE) * 60 + int(SECOND)
            while time1 > -1:
                if time1 == -2:
                    break
                minutes = time1 // 60
                second = time1 % 60
                hour = 0
                if minutes > 59:
                    hour = minutes // 60
                    minutes = minutes % 60
                hr.set(hour)
                minute.set(minutes)
                sec.set(second)
                time1 = time1 - 1
                root.update()
                playsound("/Users/Kanix/PycharmProjects/pythonProject12/sounds/newTick.mp3")
                time.sleep(1)
                if time1 <= -1:
                    hr.set('00')
                    minute.set('00')
                    sec.set('00')
                    playsound("/Users/Kanix/PycharmProjects/pythonProject12/sounds/finish.mp3")
                    speech("You're time is up!")

                    stop()
                    break

        if "hour" in text.lower():
            a = ""
            l = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
            x = text.lower()
            if "min" in x:
                if "sec" in x:
                    typeD = "3"
                else:
                    typeD = "4"
            else:
                if "sec" in x:
                    typeD = "5"
                else:
                    typeD = "3"
            for i in x:
                if i in l:
                    a += i
                if i == "h" or i == "m" or i == "c":
                    a += ","
            for i in a:
                l = a.split(",")
        elif "minute" in text.lower():
            a = ""
            typeD = "2"
            l = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
            x = text.lower()
            for i in x:
                if i in l:
                    a += i
                if i == "m" or i == "c":
                    a += ","
            for i in a:
                l = a.split(",")
        elif "second" in text.lower():
            a = ""
            typeD = "1"
            l = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
            x = text.lower()
            for i in x:
                if i in l:
                    a += i
                if i == "s":
                    a += ","
            for i in a:
                l = a.split(",")
        else:
            pass
        numlist = []
        for i in l:
            if i != "":
                numlist += [i]
        x = str(len(numlist))
        y = typeD + x
        numlist.append(x)
        numlist.append(x)
        keyD = {"52": [numlist[0], 0, numlist[1]], "42": [numlist[0], numlist[1], 0], "33": numlist,
                "31": [numlist[0], 0, 0], "22": [0, numlist[0], numlist[1]], "21": [0, numlist[0], 0],
                "11": [0, 0, numlist[0]]}

        HOUR = keyD[y][0]
        MINUTE = keyD[y][1]
        SECOND = keyD[y][2]

        titlelabel = Label(root, text='Nivi Timer', font='Arial 20 bold', fg='yellow', bg='green')
        titlelabel.pack()

        currenttime = Label(root, text='Current time: ', font='Arial 20 bold', fg='yellow', bg='green')
        currenttime.place(x=30, y=70)

        displaytimelabel = Label(root, text='', font='Times 20 bold', fg='yellow', bg='green')
        displaytimelabel.place(x=225, y=70)

        timerlabel = Label(root, text='Timer: ', font='Arial 20 bold', fg='yellow', bg='green')
        timerlabel.place(x=30, y=150)

        hr = StringVar()
        minute = StringVar()
        sec = StringVar()
        hr.set(str(HOUR))
        minute.set(str(MINUTE))
        sec.set(str(SECOND))

        hrentry = Entry(root, textvariable=hr, width=2, font='Times 20 bold')
        hrentry.place(x=125, y=150)

        minentry = Entry(root, textvariable=minute, width=2, font='Times 20 bold')
        minentry.place(x=175, y=150)

        secentry = Entry(root, textvariable=sec, width=2, font='Times 20 bold')
        secentry.place(x=225, y=150)

        Clock()
        timer()
        root.mainloop()

    elif "good morning" in text.lower():
        playsound("/Users/Kanix/PycharmProjects/pythonProject12/sounds/activate2.mp3")
        speech("Good morning. How can I help?")

    elif "good afternoon" in text.lower():
        playsound("/Users/Kanix/PycharmProjects/pythonProject12/sounds/activate2.mp3")
        speech("Good afternoon. How can I help?")

    elif "time" in text.lower():
        playsound("/Users/Kanix/PycharmProjects/pythonProject12/sounds/activate2.mp3")
        time = datetime.datetime.now().strftime("%I:%M %p")
        speech("Current time is " + time)

    elif "your name" in text.lower():
        playsound("/Users/Kanix/PycharmProjects/pythonProject12/sounds/activate2.mp3")
        speech("my name is Nivi")

    elif "search" in text.lower():
        playsound("/Users/Kanix/PycharmProjects/pythonProject12/sounds/activate2.mp3")
        speech("Searching on google")
        pywhatkit.search(text)

    elif "who is" in text.lower():
        playsound("/Users/Kanix/PycharmProjects/pythonProject12/sounds/activate2.mp3")
        speech("Searching on google for relevant information.")
        pywhatkit.search(text)

    elif "date" in text.lower():
        playsound("/Users/Kanix/PycharmProjects/pythonProject12/sounds/activate2.mp3")
        today = datetime.date.today().strftime("%d/%m/%Y")
        speech("Today's date is " + today)

    elif "thank you" in text.lower():
        playsound("/Users/Kanix/PycharmProjects/pythonProject12/sounds/activate2.mp3")
        speech("You're Welcome")

    elif "about yourself" in text.lower():
        playsound("/Users/Kanix/PycharmProjects/pythonProject12/sounds/activate2.mp3")
        speech("My name is Nivi . I am your virtual voice assistant. I was created by Nikhil and Ravi.")



    elif "calculator" in text.lower():
        playsound("/Users/Kanix/PycharmProjects/pythonProject12/sounds/activate2.mp3")
        speech("Opening Calculator")
        import customtkinter as ctk
        import tkinter as tk
        import csv
        root = ctk.CTk()
        root.title('Nivi Calculator')
        root.geometry("400x330")
        text_result = tk.Text(root, height=2, width=16, font=("Arial", 24), foreground='#FFF')
        text_result.grid(columnspan=8)
        calculation = ""
        text = ""

        # Back End
        calc_his = ''
        f = open("/Users/Kanix/PycharmProjects/pythonProject12/calculation_history.csv", "r+", newline="")
        r = csv. reader(f)
        for i in r:
            for j in i:
                calc_his += j



        def add_to_calculation(symbol):
            global calculation, text
            calculation += str(symbol)
            text += str(symbol)
            text_result.delete(1.0, "end")
            text_result.insert(1.0, text)


        def evaluate_calculation():
            global calculation, text
            try:
                result = str(eval(calculation))
                w = csv.writer(f)
                w. writerow([calculation, result])
                text_result.delete(1.0, "end")
                text_result.insert(1.0, result)
                calculation = ''
                text = ''
            except:
                clear_field()
                text_result.insert(1.0, "Error")
            text = ""


        def power():
            global calculation, text
            calculation += str("**")
            text += str("^")
            text_result.delete(1.0, "end")
            text_result.insert(1.0, text)


        def reciprocal():
            global calculation, text
            calculation += str("**-1")
            text += str("^-1")
            text_result.delete(1.0, "end")
            text_result.insert(1.0, text)


        def clear_field():
            global calculation, text
            calculation = ""
            text = ""
            text_result.delete(1.0, "end")


        def factorial():
            global calculation, text
            text += str("!")
            fact = int(calculation)
            for i in range(1, int(calculation)):
                fact *= i
            calculation = str(fact)
            text_result.delete(1.0, "end")
            text_result.insert(1.0, text)


        def backspace():
            global calculation, text
            x = len(calculation) - 1
            back = calculation[:x]
            calculation = back
            y = len(text) - 1
            bac = text[:y]
            text = bac
            text_result.delete(1.0, "end")
            text_result.insert(1.0, text)


        btn_1 = ctk.CTkButton(root, text="1", command=lambda: add_to_calculation(1), fg_color=('#ddd', '#333'), text_color=('#b700ff', '#0373fc'), hover_color=('#bbb', '#555'), width=50, font=("helvetica", 14))
        btn_1.grid(row=3, column=1, padx=5, pady=5)
        btn_2 = ctk.CTkButton(root, text="2", command=lambda: add_to_calculation(2), fg_color=('#ddd', '#333'), text_color=('#b700ff', '#0373fc'), hover_color=('#bbb', '#555'), width=50, font=("helvetica", 14))
        btn_2.grid(row=3, column=2, padx=5, pady=5)
        btn_3 = ctk.CTkButton(root, text="3", command=lambda: add_to_calculation(3), fg_color=('#ddd', '#333'), text_color=('#b700ff', '#0373fc'), hover_color=('#bbb', '#555'), width=50, font=("helvetica", 14))
        btn_3.grid(row=3, column=3, padx=5, pady=5)
        btn_4 = ctk.CTkButton(root, text="4", command=lambda: add_to_calculation(4), fg_color=('#ddd', '#333'), text_color=('#b700ff', '#0373fc'), hover_color=('#bbb', '#555'), width=50, font=("helvetica", 14))
        btn_4.grid(row=4, column=1, padx=5, pady=5)
        btn_5 = ctk.CTkButton(root, text="5", command=lambda: add_to_calculation(5), fg_color=('#ddd', '#333'), text_color=('#b700ff', '#0373fc'), hover_color=('#bbb', '#555'), width=50, font=("helvetica", 14))
        btn_5.grid(row=4, column=2, padx=5, pady=5)
        btn_6 = ctk.CTkButton(root, text="6", command=lambda: add_to_calculation(6), fg_color=('#ddd', '#333'), text_color=('#b700ff', '#0373fc'), hover_color=('#bbb', '#555'), width=50, font=("helvetica", 14))
        btn_6.grid(row=4, column=3, padx=5, pady=5)
        btn_7 = ctk.CTkButton(root, text="7", command=lambda: add_to_calculation(7), fg_color=('#ddd', '#333'), text_color=('#b700ff', '#0373fc'), hover_color=('#bbb', '#555'), width=50, font=("helvetica", 14))
        btn_7.grid(row=5, column=1, padx=5, pady=5)
        btn_8 = ctk.CTkButton(root, text="8", command=lambda: add_to_calculation(8), fg_color=('#ddd', '#333'), text_color=('#b700ff', '#0373fc'), hover_color=('#bbb', '#555'), width=50, font=("helvetica", 14))
        btn_8.grid(row=5, column=2, padx=5, pady=5)
        btn_9 = ctk.CTkButton(root, text="9", command=lambda: add_to_calculation(9), fg_color=('#ddd', '#333'), text_color=('#b700ff', '#0373fc'), hover_color=('#bbb', '#555'), width=50, font=("helvetica", 14))
        btn_9.grid(row=5, column=3, padx=5, pady=5)
        btn_0 = ctk.CTkButton(root, text="0", command=lambda: add_to_calculation(0), fg_color=('#ddd', '#333'), text_color=('#b700ff', '#0373fc'), hover_color=('#bbb', '#555'), width=50, font=("helvetica", 14))
        btn_0.grid(row=6, column=2, padx=5, pady=5)
        btn_plus = ctk.CTkButton(root, text="+", command=lambda: add_to_calculation("+"), fg_color=('#ddd', '#333'), text_color=('#000', 'white'), hover_color=('#bbb', '#555'), width=50, font=("Arial", 14))
        btn_plus.grid(row=3, column=4, padx=5, pady=5)
        btn_minus = ctk.CTkButton(root, text="-", command=lambda: add_to_calculation("-"), fg_color=('#ddd', '#333'), text_color=('#000', 'white'), hover_color=('#bbb', '#555'), width=50, font=("Arial", 14))
        btn_minus.grid(row=4, column=4, padx=5, pady=5)
        btn_mul = ctk.CTkButton(root, text="*", command=lambda: add_to_calculation("*"), fg_color=('#ddd', '#333'), text_color=('#000', 'white'), hover_color=('#bbb', '#555'), width=50, font=("Arial", 14))
        btn_mul.grid(row=5, column=4, padx=5, pady=5)
        btn_div = ctk.CTkButton(root, text="/", command=lambda: add_to_calculation("/"), fg_color=('#ddd', '#333'), text_color=('#000', 'white'), hover_color=('#bbb', '#555'), width=50, font=("Arial", 14))
        btn_div.grid(row=6, column=4, padx=5, pady=5)
        btn_open = ctk.CTkButton(root, text="(", command=lambda: add_to_calculation("("), fg_color=('#ddd', '#333'), text_color=('#b700ff', '#0373fc'), hover_color=('#bbb', '#555'), width=50, font=("Arial", 14))
        btn_open.grid(row=6, column=1, padx=5, pady=5)
        btn_close = ctk.CTkButton(root, text=")", command=lambda: add_to_calculation(")"), fg_color=('#ddd', '#333'), text_color=('#b700ff', '#0373fc'), hover_color=('#bbb', '#555'), width=50, font=("Arial", 14))
        btn_close.grid(row=6, column=3, padx=5, pady=5)
        btn_equals = ctk.CTkButton(root, text="=", command=evaluate_calculation, fg_color=('#b700ff', '#0373fc'), text_color='white', hover_color=('#9905f5', '#039dfc'), width=105, font=("Arial", 14))
        btn_equals.grid(row=7, column=4, columnspan=2, padx=5, pady=5)
        btn_clear = ctk.CTkButton(root, text="clr", command=clear_field, fg_color=('#b700ff', '#0373fc'), text_color='white', hover_color=('#9905f5', '#039dfc'), width=105, font=("Arial", 14))
        btn_clear.grid(row=7, column=1, columnspan=2, padx=5, pady=5)
        btn_dot = ctk.CTkButton(root, text=".", command=lambda: add_to_calculation("."), fg_color=('#ddd', '#333'), text_color=('#b700ff', '#0373fc'), hover_color=('#bbb', '#555'), width=50, font=("Arial", 14))
        btn_dot.grid(row=7, column=3, padx=5, pady=5)
        btn_fact = ctk.CTkButton(root, text="!", command=lambda: factorial(), fg_color=('#ddd', '#333'), text_color=('#000', 'white'), hover_color=('#bbb', '#555'), width=50, font=("Arial", 14))
        btn_fact.grid(row=6, column=5, padx=5, pady=5)
        btn_recip = ctk.CTkButton(root, text="1/x", command=lambda: reciprocal(), fg_color=('#ddd', '#333'), text_color=('#000', 'white'), hover_color=('#bbb', '#555'), width=50, font=("Arial", 14))
        btn_recip.grid(row=5, column=5, padx=5, pady=5)
        btn_pow = ctk.CTkButton(root, text="xⁿ", command=lambda: power(), fg_color=('#ddd', '#333'), text_color=('#000', 'white'), hover_color=('#bbb', '#555'), width=50, font=("Arial", 14))
        btn_pow.grid(row=4, column=5, padx=5, pady=5)
        btn_backspace = ctk.CTkButton(root, text="⌫", command=backspace, fg_color=('#ddd', '#333'), text_color=('#b700ff', '#0373fc'), hover_color=('#bbb', '#555'), width=50, font=("Arial", 14))
        btn_backspace.grid(row=3, column=5, padx=5, pady=5)
        btn_lm = ctk.CTkButton(root, text="light mode", command=lambda: ctk.set_appearance_mode('light'), fg_color='white', text_color='black', hover_color='#ddd', width=50, font=("Arial", 14))
        btn_lm.grid(row=8, column=1, columnspan=2, padx=5, pady=5)
        btn_dm = ctk.CTkButton(root, text="Dark mode", command=lambda: ctk.set_appearance_mode('Dark'), fg_color='black', text_color='white', hover_color='#222', width=50, font=("Arial", 14))
        btn_dm.grid(row=8, column=4, columnspan=2, padx=5, pady=5)
        root.mainloop()

    elif "open snake game" in text.lower():
        playsound("/Users/Kanix/PycharmProjects/pythonProject12/sounds/activate2.mp3")
        speech("Opening Snake Game.Enjoy playing.")
        try:
            import turtle
            import time
            import random
            import csv
            # leaderboard

            maxi = 0

            delay = 0.1
            score = 0
            high_score = maxi
            # Screen
            screen = turtle.Screen()
            screen.title("NIVI SNAKE GAME")
            screen.setup(width=700, height=700)
            screen.tracer(0)
            screen.bgcolor("green")
            turtle.speed(5)
            turtle.pensize(4)
            turtle.penup()
            turtle.goto(-310, 250)
            turtle.pendown()
            turtle.color("red")
            turtle.forward(600)
            turtle.right(90)
            turtle.forward(500)
            turtle.right(90)
            turtle.forward(600)
            turtle.right(90)
            turtle.forward(500)
            turtle.penup()
            turtle.hideturtle()
            # SNAKE
            snake = turtle.Turtle()
            snake.speed(0)
            snake.shape("square")
            snake.color("yellow")
            snake.penup()
            snake.goto(0, 0)
            snake.direction = "stop"
            # SNAKE FOOD
            food = turtle.Turtle()
            food.speed(0)
            food.shape("circle")
            food.color("red")
            food.penup()
            food.goto(0, 100)
            segments = []
            # pen
            pen = turtle.Turtle()
            pen.speed(0)
            pen.shape("square")
            pen.color("white")
            pen.penup()
            pen.hideturtle()
            pen.goto(0, 260)
            pen.write("Score: 0 High Score: {}".format(high_score), align="center", font=("Courier", 24, "normal"))
            # SNAKE MOVEMENTS

            def go_up():
                if snake.direction != "down":
                    snake.direction = "up"
                    pen.clear()
                    pen.write("Score: {} High Score: {}".format(score, high_score),align="center", font=("Courier", 24, "normal"))

            def go_down():
                if snake.direction != "up":
                    snake.direction = "down"
                    pen.clear()
                    pen.write("Score: {} High Score: {}".format(score, high_score),align="center", font=("Courier", 24, "normal"))

            def go_left():
                if snake.direction != "right":
                    snake.direction = "left"
                    pen.clear()
                    pen.write("Score: {} High Score: {}".format(score, high_score),align="center", font=("Courier", 24, "normal"))

            def go_right():
                if snake.direction != "left":
                    snake.direction = "right"
                    pen.clear()
                    pen.write("Score: {} High Score: {}".format(score, high_score),align="center", font=("Courier", 24, "normal"))

            def move():
                pen.goto(0, 260)
                if snake.direction == 'up':
                    y = snake.ycor()
                    snake.sety(y + 20)
                if snake.direction == 'down':
                    y = snake.ycor()
                    snake.sety(y - 20)
                if snake.direction == 'right':
                    x = snake.xcor()
                    snake.setx(x + 20)
                if snake.direction == 'left':
                    x = snake.xcor()
                    snake.setx(x - 20)
            # KEYBOARD
            screen.listen()
            screen.onkeypress(go_up, "Up")
            screen.onkeypress(go_down, "Down")
            screen.onkeypress(go_left, "Left")
            screen.onkeypress(go_right, "Right")
            # MAIN
            while True:
                screen.update()
            # CHECK FOR COLLISION WITH BORDER
                if snake.xcor() > 270 or snake.xcor() < -290 or snake.ycor() > 230 or snake.ycor() < -230:
                    time.sleep(1)
                    snake.goto(0, 0)
                    snake.direction = 'stop'

                    for segment in segments:
                        segment.goto(1000, 1000)
                    segments.clear()
                    # RESET SCORE
                    pen.clear()
                    pen.goto(0, 270)
                    pen.write("\tGame Over\nScore: {} High Score: {}".format(score,
                    high_score), align="center",font=("Courier", 24, "normal"))
                    a = [[score]]
                    score = 0
                # CHECK FOOD COLLISION
                if snake.distance(food) < 20:
                    x = random.randint(-290, 270)
                    y = random.randint(-230, 230)
                    food.goto(x, y)

                    new_segment = turtle.Turtle()
                    new_segment.speed(0)
                    new_segment.shape("square")
                    new_segment.color("blue")
                    new_segment.penup()
                    segments.append(new_segment)
                # SHORTEN DELAY
                    delay -= 0.001
                # UPDATE SCORE
                    score += 10
                    if score > high_score:
                        high_score = score
                    pen.clear()
                    pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

                # MOVE END TO FIRST
                for index in range(len(segments) - 1, 0, -1):
                    x = segments[index - 1].xcor()
                    y = segments[index - 1].ycor()
                    segments[index].goto(x, y)
                # MOVE SEGMENT 0 TO HEAD
                if len(segments) > 0:
                    x = snake.xcor()
                    y = snake.ycor()
                    segments[0].goto(x, y)
                move()
                # CHECK FOR BODY COLLISION
                for segment in segments:
                    if segment.distance(snake) < 20:
                        print("True")
                        time.sleep(1)
                        snake.goto(0, 0)
                        snake.direction = "stop"
                        pen.clear()
                        pen.goto(0, 270)
                        b = str([score])
                        print(b)
                        pen.write("\tGame Over\nScore: {} High Score: {}".format(score,high_score), align="center",font=("Courier", 24, "normal"))
                        score = 0

                        for segment in segments:
                            segment.goto(1000, 1000)
                # CLEAR
                        segments.clear()
                time.sleep(delay)
        except:
            pass


    elif "calculation history" in text.lower():
        playsound("/Users/Kanix/PycharmProjects/pythonProject12/sounds/activate2.mp3")
        speech("Check your calculation history.")
        import csv
        import customtkinter as ctk

        root = ctk.CTk()
        root.geometry("500x500")
        root.title('calculation history')

        f = open("/Users/Kanix/PycharmProjects/pythonProject12/calculation_history.csv")
        lc = []
        g = csv.reader(f)
        for i in g:
            lc += [i]
        lc = lc[::-1]
        c = 0
        label1 = ctk.CTkLabel(root, text=" Calculation history ", fg_color='black', text_color='#6fceee',
                              font=('helvetica', 24))
        label1.pack()
        for j in lc:
            txt = j[0] + ' = ' + j[1] + ' '
            a = len(txt)
            while a < 40:
                txt = ' ' + txt + ' '
                a = len(txt)
            txt = '  ' + str(c + 1) + '.  ' + txt
            label = ctk.CTkLabel(root, text=txt, fg_color='#6fceee', text_color='black')
            label.pack(pady=5)
            c += 1
        root.mainloop()



    elif "hi" or "hello" in text.lower():
        playsound("/Users/Kanix/PycharmProjects/pythonProject12/sounds/activate2.mp3")
        speech("Hi! How can I help?")

    else:
        speech("I can't understand.")


while True:
    runNivi()
