from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QButtonGroup, QGroupBox, QApplication, QRadioButton, QHBoxLayout, QWidget, QPushButton, QLabel, QVBoxLayout
from random import randint
from PyQt5 import QtGui, QtCore
from random import shuffle

#создай приложение для запоминания информации

class Question:
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
q1 = Question("Какого цвета нет на флаге России", "Зеленый", "Синий", "Белый", "Красный")
q2 = Question("Какого цвета нет на радуге?", "Бирюзовый", "Красный", "Фиолетовый", "Оранжевый")
q3 = Question("Где обитают анчоусы?", "Черном и Средиземном море", "Красном", "Мертвом", "Белом")
q4 = Question("Из шерсти какого животного обычно делают смычок для скрипки", "Конский", "Змеиный", "Овечий", "Кошачий")
q5 = Question("Сколько материков на Земле", "6", "5", "3", "8")
q6 = Question("Сколько планет в Солнечной системе?", "8", "1", "13", "3")
q7 = Question("Какой процент поверхности Земли занимает вода?", "71", "21", "33", "99.9")
q8 = Question("Сколько лет Джинн сидел в лампе, пока его не нашел Алладин?", "10000", "1121", "9999", "Ровно 100")
q9 = Question("Сколько пар крыльев у пчел?", "2", "3", "5", "1")
q10 = Question("Что значит Акуна-Матата", "Нет проблем", "Все плохо", "Мы друзья", "Привет")

question_list.append(q1)
question_list.append(q2)
question_list.append(q3)
question_list.append(q4)
question_list.append(q5)
question_list.append(q6)
question_list.append(q7)
question_list.append(q8)
question_list.append(q9)
question_list.append(q10)



app = QApplication([])
app.setWindowIcon(QtGui.QIcon('pytpng.ico'))
main_win = QWidget()
# 252, 228, 189
main_win.setStyleSheet("background-color: rgb(52, 92, 115);")
main_win.setWindowTitle("color: rgb(6, 141, 34);")

main_win.resize(400, 300)
main_win.setWindowTitle("Memory card")
main_win.setWindowIcon(QtGui.QIcon('pytpng.ico'))
btn1 = QRadioButton("Энцы")
btn2 = QRadioButton("Смурфы")
btn3 = QRadioButton("Чулымцы")
btn4 = QRadioButton("Алеуты")

RadioGroup = QButtonGroup()
RadioGroup.addButton(btn1)
RadioGroup.addButton(btn2)
RadioGroup.addButton(btn3)
RadioGroup.addButton(btn4)




button = QPushButton("Ответить")
button.setStyleSheet("color: rgb(255, 255, 255)")
btn1.setStyleSheet("color: rgb(255, 255, 255)")
btn2.setStyleSheet("color: rgb(0, 0, 0)")
btn3.setStyleSheet("color: rgb(0, 0, 0)")
btn4.setStyleSheet("color: rgb(255, 255, 255)")

text = QLabel("Какой национальности не существует?")
text.setStyleSheet("color: rgb(255, 255, 255)")
 
RadioGroupBox = QGroupBox("Варианты:")
layout1 = QHBoxLayout()
layout2 = QVBoxLayout()
layout3 = QVBoxLayout()


layout2.addWidget(btn1)
layout2.addWidget(btn2)
layout3.addWidget(btn3)
layout3.addWidget(btn4)

layout1.addLayout(layout2)
layout1.addLayout(layout3)




AnsGroupBox = QGroupBox("Результаты теста:")

texttrue1 = QLabel("Правильно\Неправильно")
texttrue2 = QLabel("Правильный ответ")

line1 = QHBoxLayout()
line2 = QHBoxLayout()
line3 = QVBoxLayout()

line1.addWidget(texttrue1)
line2.addWidget(texttrue2, alignment = Qt.AlignCenter)

line3.addLayout(line1)
line3.addLayout(line2)

AnsGroupBox.setLayout(line3)




RadioGroupBox.setLayout(layout1)

layout4 = QHBoxLayout()
layout5 = QHBoxLayout()
layout6 = QHBoxLayout()
layout7 = QVBoxLayout()

layout4.addWidget(text, alignment = Qt.AlignCenter)
layout5.addWidget(RadioGroupBox)
layout5.addWidget(AnsGroupBox)
AnsGroupBox.hide()
layout6.addStretch(1)
layout6.addWidget(button, stretch=2)
layout6.addStretch(1)

layout7.addLayout(layout4)
layout7.addLayout(layout5)
layout7.addLayout(layout6)

main_win.setLayout(layout7)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    button.setText("Слeдующий вопрос")

def show_question():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    button.setText("Ответить")

    RadioGroup.setExclusive(False)
    btn1.setChecked(False)
    btn2.setChecked(False)
    btn3.setChecked(False)
    btn4.setChecked(False)
    RadioGroup.setExclusive(True)

# def start_test():
#     if button.text() == "Ответить":
#         show_result()
#     else:
#         show_question()

answer = [btn1, btn2, btn3, btn4] 

def ask(q: Question):
    shuffle(answer)
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
    text.setText(q.question)
    texttrue2.setText(q.right_answer)

    show_question()

def show_correct(res):
    texttrue1.setText(res)
    show_result()

def check_answer():
    if answer[0].isChecked():
        show_correct("Правильно!")
        main_win.score += 1
        print("Cтатистика\n-Всего вопросов:", main_win.num, "\n-Правильных ответов:", main_win.score)
        print("Рейтинг:", main_win.score/main_win.num*100)
    elif answer[1].isChecked() or answer[2].isChecked() or answer[3].isChecked():
        show_correct("Неправильно")

    

    

def next_question():
    main_win.num += 1
    print("Cтатистика\n-Всего вопросов:", main_win.num, "\n-Правильных ответов:", main_win.score)

    cur_question = randint(0, len(question_list) -1)
    q = question_list[cur_question]
    ask(q)

    
def click_OK():
    if button.text() == "Ответить":
        check_answer()
    else:
        next_question()

main_win.num = 0
main_win.score = 0








button.clicked.connect(click_OK)


next_question()



main_win.show()
app.exec_()
