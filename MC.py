#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import *

class Question():
    def __init__(self, q, r, w1, w2, w3):
        self.question = q
        self.right_answer = r
        self.wrong1 = w1
        self.wrong2 = w2
        self.wrong3 = w3

question_list = [
    Question('Государственный язык Бразилии', 'Португальский', 'Английский', 'Китайский', 'Русский'),
    Question('2 + 2 = ?', '4', '99', '2^32', '50/2')
]

app = QApplication([])
window = QWidget()
window.setWindowTitle('Memory Card')

btn_ok = QPushButton('Ответить')
lbl_question = QLabel('2 + 2 = ?')

RadioGroupBox = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('1')
rbtn_2 = QRadioButton('2')
rbtn_3 = QRadioButton('3')
rbtn_4 = QRadioButton('4')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)


layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line1.addWidget(lbl_question, alignment = Qt.AlignCenter)
layout_line2.addWidget(RadioGroupBox)
layout_line3.addStretch(1)
layout_line3.addWidget(btn_ok, stretch = 2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1)
layout_card.addLayout(layout_line2)
layout_card.addLayout(layout_line3)
window.setLayout(layout_card)

AnsGroupBox = QGroupBox('Результат теста')
lbl_result = QLabel('Правильно или нет?')
lbl_correct = QLabel('Здесь мог быть правильный ответ')

layout_res = QVBoxLayout()
layout_res.addWidget(lbl_result, alignment = (Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lbl_correct, alignment = Qt.AlignCenter)
AnsGroupBox.setLayout(layout_res)
layout_line2.addWidget(AnsGroupBox)


def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_ok.setText('Следующий вопрос')


def show_qestion():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_ok.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(question, right_answer, wrong1, wrong2, wrong3):
    shuffle(answers)
    answers[0].setText(right_answer)
    answers[1].setText(wrong1)
    answers[2].setText(wrong2)
    answers[3].setText(wrong3)
    lbl_question.setText(question)
    lbl_correct.setText(right_answer)
    show_qestion()

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lbl_question.setText(q.question)
    lbl_correct.setText(q.right_answer)
    show_qestion()




def show_correct(res):
    lbl_result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Праввильно!')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')




def next_queston():
    x = randint(0, len(question_list) - 1)
    q = question_list[x]
    ask(q)

def click_ok():
    if btn_ok.text() == 'Ответить':
        check_answer()
    else:
        next_queston()

next_queston()
btn_ok.clicked.connect(click_ok)























AnsGroupBox.hide()
window.show()
app.exec()