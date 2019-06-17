import tkinter as tk
from PIL import ImageTk, Image
import random
import time

def controlcore(event):
    global count
    if stimulate_list[count][3] == "01":
        if (event.keysym == "s" or event.keysym == "S") and detect_key == True:
            coverImg.destroy()
            coverBtn.place_forget()
            coverIns.place_forget()
            showinstruction(block01Ins, block01BtnLeft, block01BtnRight)
    
    elif stimulate_list[count][3] == 1 and stimulate_list[count - 1][3] == "01":
        showfirstquestion(event, block01Ins)

    elif stimulate_list[count][3] == 1:
        main(event)

    elif stimulate_list[count][3] == 12:
        main_instruction(event, showinstruction, block02Ins, block02BtnLeft, block02BtnRight)

    elif stimulate_list[count][3] == 2 and stimulate_list[count - 1][3] == 12:
        showfirstquestion(event, block02Ins)

    elif stimulate_list[count][3] == 2:
        main(event)

    elif stimulate_list[count][3] == 23:
        main_instruction(event, showinstruction, block03Ins, block03BtnLeft, block03BtnRight)

    elif stimulate_list[count][3] == 3 and stimulate_list[count - 1][3] == 23:
        showfirstquestion(event, block03Ins)

    elif stimulate_list[count][3] == 3:
        main(event)

    elif stimulate_list[count][3] == 34:
        main_instruction(event, showinstruction, block04Ins, block04BtnLeft, block04BtnRight)

    elif stimulate_list[count][3] == 4 and stimulate_list[count - 1][3] == 34:
        showfirstquestion(event, block04Ins)

    elif stimulate_list[count][3] == 4:
        main(event)

    elif stimulate_list[count][3] == 45:
        main_instruction(event, showinstruction, block05Ins, block05BtnLeft, block05BtnRight)

    elif stimulate_list[count][3] == 5 and stimulate_list[count - 1][3] == 45:
        showfirstquestion(event, block05Ins)

    elif stimulate_list[count][3] == 5:
        main(event)

    elif stimulate_list[count][3] == 56:
        main(event)
        printresult()

    else:
        pass

def main(event):
    global detect_key
    global block3_practice
    global block5_practice
    global block3_wrongcount
    global block5_wrongcount
    global block3_DPPtime_list
    global block3_KMTtime_list
    global block5_DPPtime_list
    global block5_KMTtime_list
    if (event.keysym == "e" or event.keysym == "i" or event.keysym == "E" or event.keysym == "I") and detect_key == True:
        detect_key = False
        if stimulate_list[count][3] == 3:
            t_end = time.time()
            block3_practice += 1
        elif stimulate_list[count][3] == 5 or stimulate_list[count][3] == 56:
            t_end = time.time()
            block5_practice += 1
        question.destroy()
        
        if event.keysym == "e" or event.keysym == "E":
            if stimulate_list[count - 1][1] == "right":
                if stimulate_list[count][3] == 3 and block3_practice >= 8:
                    block3_wrongcount += 1
                elif (stimulate_list[count][3] == 5 or stimulate_list[count][3] == 56) and block5_practice >= 8:
                    block5_wrongcount += 1
                showwronganswer()
                if stimulate_list[count][3] == 56:
                    window.after(500, wronganswer.destroy)
                else:
                    window.after(500, showquestion)
            else:
                if stimulate_list[count][3] == 3 and block3_practice >= 8:
                    if stimulate_list[count - 1][2] == "c":
                        time_span = t_end - t_start
                        block3_DPPtime_list.append(time_span)
                elif (stimulate_list[count][3] == 5 or stimulate_list[count][3] == 56) and block5_practice >= 8:
                    if stimulate_list[count - 1][2] == "c":
                        time_span = t_end - t_start
                        block5_KMTtime_list.append(time_span)
                if stimulate_list[count][3] != 56:
                    showquestion()

        elif event.keysym == "i" or event.keysym == "I":
            if stimulate_list[count - 1][1] == "right":
                if stimulate_list[count][3] == 3 and block3_practice >= 8:
                    if stimulate_list[count - 1][2] == "c":
                        time_span = t_end - t_start
                        block3_KMTtime_list.append(time_span)
                elif (stimulate_list[count][3] == 5 or stimulate_list[count][3] == 56) and block5_practice >= 8:
                    if stimulate_list[count - 1][2] == "c":
                        time_span = t_end - t_start
                        block5_DPPtime_list.append(time_span)
                if stimulate_list[count][3] != 56:
                    showquestion()
            else:
                if stimulate_list[count][3] == 3 and block3_practice >= 8:
                    block3_wrongcount += 1
                elif (stimulate_list[count][3] == 5 or stimulate_list[count][3] == 56) and block5_practice >= 8:
                    block5_wrongcount += 1
                showwronganswer()
                if stimulate_list[count][3] == 56:
                    window.after(500, wronganswer.destroy)
                else:
                    window.after(500, showquestion)

def main_instruction(event, showinstruction, Ins, BtnLeft, BtnRight):
    global detect_key
    global block3_practice
    global block3_wrongcount
    global block3_DPPtime_list
    global block3_KMTtime_list
    if (event.keysym == "e" or event.keysym == "i" or event.keysym == "E" or event.keysym == "I") and detect_key == True:
        detect_key = False
        if stimulate_list[count][3] == 3:
            t_end = time.time()
        question.destroy()
        
        if event.keysym == "e" or event.keysym == "E":
            if stimulate_list[count - 1][1] == "right":
                if stimulate_list[count - 1][3] == 3:
                    block3_wrongcount += 1
                showwronganswer()
                window.after(500, showinstruction(Ins, BtnLeft, BtnRight))
            else:
                if stimulate_list[count - 1][3] == 3:
                    if stimulate_list[count - 1][2] == "c":
                        time_span = t_end - t_start
                        block3_DPPtime_list.append(time_span)
                showinstruction(Ins, BtnLeft, BtnRight)

        elif event.keysym == "i" or event.keysym == "I":
            if stimulate_list[count - 1][1] == "right":
                if stimulate_list[count - 1][3] == 3:
                    if stimulate_list[count - 1][2] == "c":
                        time_span = t_end - t_start
                        block3_KMTtime_list.append(time_span)
                showinstruction(Ins, BtnLeft, BtnRight)
            else:
                if stimulate_list[count - 1][3] == 3:
                    block3_wrongcount += 1
                showwronganswer()
                window.after(500, showinstruction(Ins, BtnLeft, BtnRight))

def showquestion():
    global count
    global question
    global t_start
    global image_file
    global detect_key
    global have_wronganswer
    if have_wronganswer == True:
        wronganswer.destroy()
        have_wronganswer = False
    image_file = ImageTk.PhotoImage(Image.open(stimulate_list[count][0]))
    question = tk.Label(window, image = image_file)
    question.place(x = 200, y = 50)
    count += 1
    t_start = time.time()
    detect_key = True
    window.bind("<KeyPress>", controlcore)

def showinstruction(ins, btnLeft, btnRight):
    global count
    global detect_key
    global have_wronganswer
    if have_wronganswer == True:
        wronganswer.destroy()
        have_wronganswer = False
    ins.place(x = 300, y = 200)
    btnLeft.place(x = 180, y = 500)
    btnRight.place(x = 540, y = 500)
    coverBtn.place(x = 310, y = 500)
    coverIns.place(x = 350, y = 540)
    count += 1
    detect_key = True
    window.bind("<KeyPress>", controlcore) 

def showwronganswer():
    global wronganswer
    global have_wronganswer
    have_wronganswer = True
    wronganswer = tk.Label(window, text = "Wrong Answer!", bg = "whitesmoke", fg = "red", font = ("微軟正黑體", 28), width = 20, height = 3)
    wronganswer.place(x = 200, y = 200)

def showfirstquestion(event, ins):
    global question
    global count
    global t_start
    global image_file
    global detect_key
    if (event.keysym == "s" or event.keysym == "S") and detect_key == True:
        detect_key = False
        coverBtn.place_forget()
        coverIns.place_forget()
        ins.destroy()
        image_file = ImageTk.PhotoImage(Image.open(stimulate_list[count][0]))
        question = tk.Label(window, image = image_file)
        question.place(x = 200, y = 50)
        count += 1
        t_start = time.time()
        detect_key = True
        window.bind("<KeyPress>", controlcore)

def printresult():
    global block3_DPPtime_total
    global block3_KMTtime_total
    global block5_DPPtime_total
    global block5_KMTtime_total
    global count
    count += 1
    if len(block3_DPPtime_list) != 0 and len(block3_KMTtime_list) != 0 and len(block5_DPPtime_list) != 0 and len(block3_KMTtime_list) != 0 and block3_wrongcount < 16 and block5_wrongcount < 16:
        for i in range(len(block3_DPPtime_list)):
            block3_DPPtime_total += block3_DPPtime_list[i]
        for i in range(len(block3_KMTtime_list)):
            block3_KMTtime_total += block3_KMTtime_list[i]
        for i in range(len(block5_DPPtime_list)):
            block5_DPPtime_total += block5_DPPtime_list[i]
        for i in range(len(block5_KMTtime_list)):
            block5_KMTtime_total += block5_KMTtime_list[i]
        block3_DPPtime_average = round((block3_DPPtime_total / len(block3_DPPtime_list)), 4)
        block3_KMTtime_average = round((block3_KMTtime_total / len(block3_KMTtime_list)), 4)
        block5_DPPtime_average = round((block5_DPPtime_total / len(block5_DPPtime_list)), 4)
        block5_KMTtime_average = round((block5_KMTtime_total / len(block5_KMTtime_list)), 4)
        block3_average = round(((block3_DPPtime_total + block3_KMTtime_total) / (len(block3_DPPtime_list) + len(block3_KMTtime_list))), 4)
        block5_average = round(((block5_DPPtime_total + block5_KMTtime_total) / (len(block5_DPPtime_list) + len(block5_KMTtime_list))), 4)
        if block3_average < block5_average - 0.05:
            block_result = tk.Label(window, text = "You are DPPer!", bg = "whitesmoke", fg = "grey", font = ("微軟正黑體", 28), width = 20, height = 3)
            block_result.place(x = 200, y = 200)
        elif block3_average - 0.03 > block5_average:
            block_result = tk.Label(window, text = "You are KMTer!", bg = "whitesmoke", fg = "grey", font = ("微軟正黑體", 28), width = 20, height = 3)
            block_result.place(x = 200, y = 200)
        else:
            block_result = tk.Label(window, text = "You are Neutral!", bg = "whitesmoke", fg = "grey", font = ("微軟正黑體", 28), width = 20, height = 3)
            block_result.place(x = 200, y = 200)
        print("block3 average DPP time: ", block3_DPPtime_average)
        print("block3 average KMT time: ", block3_KMTtime_average)
        print("block3 average time    : ", block3_average)
        print()
        print("block5 average DPP time: ", block5_DPPtime_average)
        print("block5 average KMT time: ", block5_KMTtime_average)
        print("block5 average time    : ", block5_average)
    else:
        block_result = tk.Label(window, text = "Too many wrong answers!", bg = "whitesmoke", fg = "grey", font = ("微軟正黑體", 28), width = 20, height = 3)
        block_result.place(x = 200, y = 200)
        print("No result")

DPP_list = ["DPP/A.png", "DPP/B.jpg", "DPP/C.jpg", "DPP/D.jpg", "DPP/E.jpg", "DPP/F.jpg", "DPP/G.jpg", "DPP/H.jpg", "DPP/I.jpg", "DPP/J.jpg"]
KMT_list = ["KMT/A.png", "KMT/B.jpg", "KMT/C.jpg", "KMT/D.jpg", "KMT/E.jpg", "KMT/F.jpg", "KMT/G.jpg", "KMT/H.jpg", "KMT/I.png", "KMT/J.jpg"]
positive_list = ['POS/' + str(i) + '.png' for i in range(1, 11)]
negative_list = ['NEG/' + str(i) + '.png' for i in range(1, 11)]
left_ans = ["left"]*10
right_ans = ["right"]*10
cnpts = ["c"]*10
attrs = ["a"]*10
block1 = [1]*10
block2 = [2]*10
block3 = [3]*10
block4 = [4]*10
block5 = [5]*10


block1_DPP_zip = list(zip(DPP_list, left_ans, cnpts, block1))
block1_KMT_zip = list(zip(KMT_list, right_ans, cnpts, block1))
block2_positive_zip = list(zip(positive_list, left_ans, attrs, block2))
block2_negative_zip = list(zip(negative_list, right_ans, attrs, block2))
block3_DPP_zip = list(zip(DPP_list, left_ans, cnpts, block3))
block3_KMT_zip = list(zip(KMT_list, right_ans, cnpts, block3))
block3_positive_zip = list(zip(positive_list, left_ans, attrs, block3))
block3_negative_zip = list(zip(negative_list, right_ans, attrs, block3))
block4_KMT_zip = list(zip(KMT_list, left_ans, cnpts, block4))
block4_DPP_zip = list(zip(DPP_list, right_ans, cnpts, block4))
block5_KMT_zip = list(zip(KMT_list, left_ans, cnpts, block5))
block5_DPP_zip = list(zip(DPP_list, right_ans, cnpts, block5))
block5_positive_zip = list(zip(positive_list, left_ans, attrs, block5))
block5_negative_zip = list(zip(negative_list, right_ans, attrs, block5))


block1_list = block1_DPP_zip + block1_KMT_zip
block2_list = block2_positive_zip + block2_negative_zip
block3_cnpts_list = block3_DPP_zip + block3_KMT_zip
block3_attrs_list = block3_positive_zip + block3_negative_zip
block4_list = block4_KMT_zip + block4_DPP_zip
block5_cnpts_list = block5_KMT_zip + block5_DPP_zip
block5_attrs_list = block5_positive_zip + block5_negative_zip


random.shuffle(block1_list)
random.shuffle(block2_list)
random.shuffle(block3_cnpts_list)
random.shuffle(block3_attrs_list)
random.shuffle(block4_list)
random.shuffle(block5_cnpts_list)
random.shuffle(block5_attrs_list)

block3_list = []
block5_list = []

for i in range(20):
    block3_list.append(block3_attrs_list[i])
    block3_list.append(block3_cnpts_list[i])
    block5_list.append(block5_attrs_list[i])
    block5_list.append(block5_cnpts_list[i])

block01_list = [("民進黨E\n國民黨I", "s", "ins", "01")]
block12_list = [("正面E\n負面I", "s", "ins", 12)]
block23_list = [("民進黨 正面E\n國民黨 負面I", "s", "ins", 23)]
block34_list = [("國民黨E\n民進黨I", "s", "ins", 34)]
block45_list = [("國民黨 正面E\民進黨 負面I", "s", "ins", 45)]
block56_list = [(0,0,0,56)]
block_end = [(0,0,0,6)]
stimulate_list = block01_list + block1_list + block12_list + block2_list + block23_list + block3_list + block34_list + block4_list + block45_list + block5_list + block56_list + block_end


window = tk.Tk()
window.iconbitmap("包子.ico")
window.title("誠實包子")
window.geometry("800x600")
window.configure(background = "aquamarine")

image_file = tk.PhotoImage(file = "TW.png")
coverImg = tk.Label(window, bg = "aquamarine", image = image_file)

coverBtn = tk.Label(window, text = "Press \"s\" to start", bg = "whitesmoke", fg = "grey", font = ("微軟正黑體", 12), width = 18, height = 1)
coverIns= tk.Label(window, text = "按鍵盤\"s\"繼續", bg = "aquamarine", fg = "white", font = ("微軟正黑體", 12), width = 10, height = 2)
coverImg.place(x = 0, y = 50)
coverBtn.place(x = 310, y = 500)
coverIns.place(x = 350, y = 540)

block01Ins = tk.Label(window, text = "民進黨E\n國民黨I", bg = "whitesmoke", fg = "grey", font = ("微軟正黑體", 28), width = 10, height = 3)
block01BtnLeft = tk.Label(window, text = "民進黨E", bg = "whitesmoke", fg = "grey", font = ("微軟正黑體", 12), width = 10, height = 2)
block01BtnRight = tk.Label(window, text = "國民黨I", bg = "whitesmoke", fg = "grey", font = ("微軟正黑體", 12), width = 10, height = 2)
block02Ins = tk.Label(window, text = "正面E\n負面I", bg = "whitesmoke", fg = "grey", font = ("微軟正黑體", 28), width = 10, height = 3)
block02BtnLeft = tk.Label(window, text = "正面E", bg = "whitesmoke", fg = "grey", font = ("微軟正黑體", 12), width = 10, height = 2)
block02BtnRight = tk.Label(window, text = "負面I", bg = "whitesmoke", fg = "grey", font = ("微軟正黑體", 12), width = 10, height = 2)
block03Ins = tk.Label(window, text = "民進黨 正面E\n國民黨 負面I", bg = "whitesmoke", fg = "grey", font = ("微軟正黑體", 28), width = 10, height = 3)
block03BtnLeft = tk.Label(window, text = "民進黨 正面E", bg = "whitesmoke", fg = "grey", font = ("微軟正黑體", 12), width = 10, height = 2)
block03BtnRight = tk.Label(window, text = "國民黨 負面I", bg = "whitesmoke", fg = "grey", font = ("微軟正黑體", 12), width = 10, height = 2)
block04Ins = tk.Label(window, text = "國民黨E\n民進黨I", bg = "whitesmoke", fg = "grey", font = ("微軟正黑體", 28), width = 10, height = 3)
block04BtnLeft = tk.Label(window, text = "國民黨E", bg = "whitesmoke", fg = "grey", font = ("微軟正黑體", 12), width = 10, height = 2)
block04BtnRight = tk.Label(window, text = "民進黨I", bg = "whitesmoke", fg = "grey", font = ("微軟正黑體", 12), width = 10, height = 2)
block05Ins = tk.Label(window, text = "國民黨 正面E\n民進黨 負面I", bg = "whitesmoke", fg = "grey", font = ("微軟正黑體", 28), width = 10, height = 3)
block05BtnLeft = tk.Label(window, text = "國民黨 正面E", bg = "whitesmoke", fg = "grey", font = ("微軟正黑體", 12), width = 10, height = 2)
block05BtnRight = tk.Label(window, text = "民進黨 負面I", bg = "whitesmoke", fg = "grey", font = ("微軟正黑體", 12), width = 10, height = 2)

count = 0
block3_DPPtime_list = []
block3_KMTtime_list = []
block5_DPPtime_list = []
block5_KMTtime_list = []
block3_wrongcount = 0
block5_wrongcount = 0
block3_practice = 0
block5_practice = 0
detect_key = True
have_wronganswer = False
window.bind("<KeyPress>", controlcore)

block3_DPPtime_total = 0
block3_KMTtime_total = 0
block5_DPPtime_total = 0
block5_KMTtime_total = 0

window.mainloop()