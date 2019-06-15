import tkinter as tk
import random
import time

def controlcore(event):
    global count
    global question
    global wrongcount
    global t_start
    global block3_DPPtime_list
    global block3_KMTtime_list
    if stimulate_list[count][3] == "01":
        if event.keysym == "s":
            coverImg.destroy()
            block01Ins.place(x = 300, y = 200)
            block01BtnLeft.place(x = 180, y = 500)
            block01BtnRight.place(x = 540, y = 500)
            count += 1
            window.bind("<KeyPress>", controlcore)
    
    elif stimulate_list[count][3] == 1 and stimulate_list[count - 1][3] == "01":
        if event.keysym == "s":
            coverBtn.place_forget()
            coverIns.place_forget()
            block01Ins.destroy()
            question = tk.Label(window, text = stimulate_list[count][0], bg = "whitesmoke", fg = "grey", font = ("微軟正黑體", 28), width = 10, height = 3)
            question.place(x = 300, y = 200)
            count += 1
            window.bind("<KeyPress>", controlcore)

    elif stimulate_list[count][3] == 1:
        if event.keysym == "e" or event.keysym == "i":
            question.destroy()
            if event.keysym == "e":
                if stimulate_list[count - 1][1] == "right":
                   #錯
                    print("You are wrong!")
                else:
                    #對
                    print("You are right!")

            elif event.keysym == "i":
                if stimulate_list[count - 1][1] == "right":
                    #對
                    print("You are right!")
                else:
                    #錯
                    print("You are wrong!")
            question = tk.Label(window, text = stimulate_list[count][0], bg = "whitesmoke", fg = "grey", font = ("微軟正黑體", 28), width = 10, height = 3)
            question.place(x = 300, y = 200)
            count += 1
            window.bind("<KeyPress>", controlcore)

    elif stimulate_list[count][3] == 12 and stimulate_list[count - 1][3] == 1:
        if event.keysym == "e" or event.keysym == "i":
            question.destroy()
            if event.keysym == "e":
                if stimulate_list[count - 1][1] == "right":
                   #錯
                    print("You are wrong!")
                else:
                    #對
                    print("You are right!")

            elif event.keysym == "i":
                if stimulate_list[count - 1][1] == "right":
                    #對
                    print("You are right!")
                else:
                    #錯
                    print("You are wrong!")
            block02Ins.place(x = 300, y = 200)
            block02BtnLeft.place(x = 180, y = 500)
            block02BtnRight.place(x = 540, y = 500)
            coverBtn.place(x = 310, y = 500)
            coverIns.place(x = 350, y = 540)
            count += 1
            window.bind("<KeyPress>", controlcore)

    elif stimulate_list[count][3] == 2 and stimulate_list[count - 1][3] == 12:
        if event.keysym == "s":
            coverBtn.place_forget()
            coverIns.place_forget()
            block02Ins.destroy()
            question = tk.Label(window, text = stimulate_list[count][0], bg = "whitesmoke", fg = "grey", font = ("微軟正黑體", 28), width = 10, height = 3)
            question.place(x = 300, y = 200)
            count += 1
            window.bind("<KeyPress>", controlcore)

    elif stimulate_list[count][3] == 2:
        if event.keysym == "e" or event.keysym == "i":
            question.destroy()
            if event.keysym == "e":
                if stimulate_list[count - 1][1] == "right":
                   #錯
                    print("You are wrong!")
                else:
                    #對
                    print("You are right!")

            elif event.keysym == "i":
                if stimulate_list[count - 1][1] == "right":
                    #對
                    print("You are right!")
                else:
                    #錯
                    print("You are wrong!")
            question = tk.Label(window, text = stimulate_list[count][0], bg = "whitesmoke", fg = "grey", font = ("微軟正黑體", 28), width = 10, height = 3)
            question.place(x = 300, y = 200)
            count += 1
            window.bind("<KeyPress>", controlcore)

    elif stimulate_list[count][3] == 23 and stimulate_list[count - 1][3] == 2:
        if event.keysym == "e" or event.keysym == "i":
            question.destroy()
            if event.keysym == "e":
                if stimulate_list[count - 1][1] == "right":
                   #錯
                    print("You are wrong!")
                else:
                    #對
                    print("You are right!")

            elif event.keysym == "i":
                if stimulate_list[count - 1][1] == "right":
                    #對
                    print("You are right!")
                else:
                    #錯
                    print("You are wrong!")
            block03Ins.place(x = 300, y = 200)
            block03BtnLeft.place(x = 180, y = 500)
            block03BtnRight.place(x = 540, y = 500)
            coverBtn.place(x = 310, y = 500)
            coverIns.place(x = 350, y = 540)
            count += 1
            window.bind("<KeyPress>", controlcore)

    elif stimulate_list[count][3] == 3 and stimulate_list[count - 1][3] == 23:
        if event.keysym == "s":
            coverBtn.place_forget()
            coverIns.place_forget()
            block03Ins.destroy()
            question = tk.Label(window, text = stimulate_list[count][0], bg = "whitesmoke", fg = "grey", font = ("微軟正黑體", 28), width = 10, height = 3)
            question.place(x = 300, y = 200)
            count += 1
            t_start = time.time()
            window.bind("<KeyPress>", controlcore)

    elif stimulate_list[count][3] == 3:
        if event.keysym == "e" or event.keysym == "i":
            t_end = time.time()
            question.destroy()
            if event.keysym == "e":
                if stimulate_list[count - 1][1] == "right":
                    #錯
                    if stimulate_list[count - 1][2] == "c":
                        wrongcount += 1
                    print("You are wrong!")
                else:
                    if stimulate_list[count - 1][2] == "c":
                        time_span = t_end - t_start
                        block3_DPPtime_list.append(time_span)
                    #對
                    print("You are right!")

            elif event.keysym == "i":
                if stimulate_list[count - 1][1] == "right":
                    if stimulate_list[count - 1][2] == "c":
                        time_span = t_end - t_start
                        block3_KMTtime_list.append(time_span)
                    #對
                    print("You are right!")
                else:
                    #錯
                    if stimulate_list[count - 1][2] == "c":
                        wrongcount += 1
                    print("You are wrong!")
            print(block3_DPPtime_list, block3_KMTtime_list, wrongcount)
            question = tk.Label(window, text = stimulate_list[count][0], bg = "whitesmoke", fg = "grey", font = ("微軟正黑體", 28), width = 10, height = 3)
            question.place(x = 300, y = 200)
            count += 1
            t_start = time.time()
            window.bind("<KeyPress>", controlcore)




DPP_list = ["DPP/A.png", "DPP/B.jpg", "DPP/C.jpg", "DPP/D.jpg", "DPP/E.jpg", "DPP/F.jpg", "DPP/G.jpg", "DPP/H.jpg", "DPP/I.jpg", "DPP/J.jpg"]
KMT_list = ["KMT/A.png", "KMT/B.jpg", "KMT/C.jpg", "KMT/D.jpg", "KMT/E.jpg", "KMT/F.jpg", "KMT/G.jpg", "KMT/H.jpg", "KMT/I.png", "KMT/J.jpg"]
positive_list = ["真誠","卓越","進步","開明","友善","大方","機智","愛台","清廉", "勤政"]
negative_list = ["虛偽","拙劣","退步","獨裁","惡劣","小氣","愚昧","賣台","貪汙", "怠惰"]
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
stimulate_list = block01_list + block1_list + block12_list + block2_list + block23_list + block3_list + block34_list + block4_list + block45_list + block5_list


window = tk.Tk()
window.title("誠實包子")
window.geometry("800x600")
window.configure(background = "aquamarine")

image_file = tk.PhotoImage(file = "C:\\Users\\章倫\\Documents\\GitHub\\python-based-gui\\TW.png")
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

wrongcount = 0
count = 0
block3_DPPtime_list = []
block3_KMTtime_list = []
window.bind("<KeyPress>", controlcore)

window.mainloop()
