import tkinter as tk
import random
def bTo01(event):
    if event.keysym == "b":
        coverImg.destroy()
        block01Ins.place(x = 300, y = 200)
        block01BtnLeft.place(x = 180, y = 500)
        block01BtnRight.place(x = 540, y = 500)
        window.bind("<KeyPress>", block01To1)

def block01To1(event):
    global question
    if event.keysym == "b":
        coverBtn.destroy()
        block01Ins.destroy()
        coverIns.destroy()
        question = tk.Label(window, text = party_list[0][0], bg = "whitesmoke", fg = "grey", font = ("微軟正黑體", 28), width = 10, height = 3)
        question.place(x = 300, y = 200)
        if party_list[0][1] == "right":
            window.bind("<KeyPress>", answerRight)
        elif party_list[0][1] == "left":
            window.bind("<KeyPress>", answerLeft)

def answerRight(event):
    global count
    global question
    global wrongcount
    question.destroy()
    count += 1
    if event.keysym == "i" and count < 14:
        question = tk.Label(window, text = party_list[count][0], bg = "whitesmoke", fg = "grey", font = ("微軟正黑體", 28), width = 10, height = 3)
        question.place(x = 300, y = 200)
        if party_list[count][1] == "right":
            window.bind("<KeyPress>", answerRight)
        elif party_list[count][1] == "left":
            window.bind("<KeyPress>", answerLeft)

    elif event.keysym == "e" and count < 14:
        wrongcount += 1
        question = tk.Label(window, text = party_list[count][0], bg = "whitesmoke", fg = "grey", font = ("微軟正黑體", 28), width = 10, height = 3)
        question.place(x = 300, y = 200)
        if party_list[count][1] == "right":
            window.bind("<KeyPress>", answerRight)
        elif party_list[count][1] == "left":
            window.bind("<KeyPress>", answerLeft)
    print(wrongcount)

def answerLeft(event):
    global count
    global question
    global wrongcount
    question.destroy()
    count += 1
    if event.keysym == "e" and count < 14:
        question = tk.Label(window, text = party_list[count][0], bg = "whitesmoke", fg = "grey", font = ("微軟正黑體", 28), width = 10, height = 3)
        question.place(x = 300, y = 200)
        if party_list[count][1] == "right":
            window.bind("<KeyPress>", answerRight)
        elif party_list[count][1] == "left":
            window.bind("<KeyPress>", answerLeft)

    elif event.keysym == "i" and count < 14:
        wrongcount += 1
        question = tk.Label(window, text = party_list[count][0], bg = "whitesmoke", fg = "grey", font = ("微軟正黑體", 28), width = 10, height = 3)
        question.place(x = 300, y = 200)
        if party_list[count][1] == "right":
            window.bind("<KeyPress>", answerRight)
        elif party_list[count][1] == "left":
            window.bind("<KeyPress>", answerLeft)
    print(wrongcount)


DPP_list = ["蔡英文", "謝長廷", "蘇貞昌", "賴清德", "陳菊", "林佳龍", "鄭文燦"]
KMT_list = ["馬英九", "朱立倫", "韓國瑜", "吳敦義", "王金平", "侯友宜", "盧秀燕"]
left_ans = ["left"]*7
right_ans = ["right"]*7
DPP_zip = list(zip(DPP_list, left_ans))
KMT_zip = list(zip(KMT_list, right_ans))
party_list = DPP_zip + KMT_zip
random.shuffle(party_list)
count = 0
wrongcount = 0
positive_list = ["真誠","卓越","進步","開明","友善","大方","機智","愛台","清廉", "勤政"]
negative_list = ["虛偽","拙劣","退步","獨裁","惡劣","小氣","愚昧","賣台","貪汙", "怠惰"]

DPP_reacttime_list = []
KMT_reacttime_list  = []
positive_reacttime_list  = []
negative_reacttime_list  = []





window = tk.Tk()
window.title("誠實包子")
window.geometry("800x600")
window.configure(background = "aquamarine")

image_file = tk.PhotoImage(file = "C:\\Users\\章倫\\Documents\\GitHub\\python-based-gui\\TW.png")
coverImg = tk.Label(window, bg = "aquamarine", image = image_file)

coverBtn = tk.Label(window, text = "Press \"b\" to start", bg = "whitesmoke", fg = "grey", font = ("微軟正黑體", 12), width = 18, height = 1)
coverIns= tk.Label(window, text = "按鍵盤\"b\"繼續", bg = "aquamarine", fg = "white", font = ("微軟正黑體", 12), width = 10, height = 2)
block01Ins = tk.Label(window, text = "民進黨E\n國民黨I", bg = "whitesmoke", fg = "grey", font = ("微軟正黑體", 28), width = 10, height = 3)
block01BtnLeft = tk.Label(window, text = "民進黨E", bg = "whitesmoke", fg = "grey", font = ("微軟正黑體", 12), width = 10, height = 2)
block01BtnRight = tk.Label(window, text = "國民黨I", bg = "whitesmoke", fg = "grey", font = ("微軟正黑體", 12), width = 10, height = 2)

coverImg.place(x = 0, y = 50)
coverBtn.place(x = 310, y = 500)
coverIns.place(x = 350, y = 540)

window.bind("<KeyPress>", bTo01)

window.mainloop()