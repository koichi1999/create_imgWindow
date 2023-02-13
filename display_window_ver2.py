import sys
import tkinter as tk
import createImg_ver2 as ci
import cv2
import unicodedata

#テキストボックス内に2文字までしか入力できないように文字制限
def limit_char(string):
    characterNum = 2
    return len(string) <= characterNum

class txtBox_Behavior:
    #コンストラクタ
    def __init__(self, input:tk.Entry):
        self.input = input
    
    #入力された文字が全角か半角か判定
    def typeCharacter(self):
        char_flag = False
        
        getVal = self.input.get()
        for c in getVal:
            valType = unicodedata.east_asian_width(c)
            if('Na' == valType):
                #print(valType)
                pass
            else:
                char_flag = True
                #print("半角以外が含まれている")
                break
        return char_flag
    
    #入力された文字列が数値かどうか判定、さらに整数かどうかも判定
    def str_value(self):
        str_flag = False
        #オブジェクトの値を取得して、str型に変換
        getVal = str(self.input.get())
        Int_value = getVal.isdecimal()
        #print(Int_value)
        if(Int_value == True):
            pass
        else:
            str_flag = True
        return str_flag
    
    #文字列をint型に変換
    def getValue(self):
        #オブジェクトの値を取得して、int型に変換
        getVal = int(self.input.get())
        #入力された値をint型に変換
        #print(getVal)
        #print(type(getVal))
        return getVal

def txtBox_value(txtBox:tk.Entry):
    txtBox_behavior = txtBox_Behavior(txtBox)
    fill_value = None
    valType = txtBox_behavior.typeCharacter()
    minValue = 0
    maxValue = 50
    #print(valType)
    if(not valType):
        stringValue = txtBox_behavior.str_value()
        #print(stringValue)
        if(not stringValue):
            fill_value = txtBox_behavior.getValue()
            if (fill_value <= minValue):
                fill_value = None
                txtBox.delete(minValue, tk.END)
                #txtBox.insert(tk.END, str(fill_value))
                #print(fill_value)
            elif (fill_value > maxValue):
                fill_value = None
                txtBox.delete(minValue, tk.END)
                #txtBox.insert(tk.END, str(fill_value))
                #print(fill_value)
        else:
            txtBox.delete(minValue, tk.END)
    else:
        txtBox.delete(minValue, tk.END)
    return fill_value

window_width = 400
window_height = 400
# ボタンのクリックイベント
def clickColorRow():
    fill_value = txtBox_value(txtBox)
    if(fill_value is None):
        #print("Null")
        pass
    else:
        #print(fill_value)
        color_window = ci.Color_Window(width=window_width, height=window_height)
        img_rowColor = color_window.create_rowWindow(fill_area=fill_value)
        cv2.imshow("img_rowColor", img_rowColor)

# ボタンのクリックイベント
def clickColorColumn():
    fill_value = txtBox_value(txtBox2)
    if(fill_value is None):
        #print("Null")
        pass
    else:
        #print(fill_value)
        color_window = ci.Color_Window(width=window_width, height=window_height)
        img_columnColor = color_window.create_columnWindow(fill_area=fill_value)
        cv2.imshow("img_columnColor", img_columnColor)

# ボタンのクリックイベント
def clickColorCross():
    fill_value = txtBox_value(txtBox6)
    if(fill_value is None):
        #print("Null")
        pass
    else:
        color_window = ci.Color_Window(width=window_width, height=window_height)
        img_crossColor = color_window.create_crossWindow(fill_area=fill_value)
        cv2.imshow("img_crossColor", img_crossColor)

# ボタンのクリックイベント
def clickGrayRow():
    fill_value = txtBox_value(txtBox1)
    if(fill_value is None):
        #print("Null")
        pass
    else:
        gray_window = ci.GrayScale_Window(width=window_width, height=window_height)
        img_row = gray_window.create_rowWindow(fill_area=fill_value)
        cv2.imshow("img_row", img_row)

# ボタンのクリックイベント
def clickGrayColumn():
    fill_value = txtBox_value(txtBox3)
    if(fill_value is None):
        #print("Null")
        pass
    else:
        gray_window = ci.GrayScale_Window(width=window_width, height=window_height)
        img_column = gray_window.create_columnWindow(fill_area=fill_value)
        cv2.imshow("img_column", img_column)

def clickGrayCross():
    fill_value = txtBox_value(txtBox5)
    if(fill_value is None):
        #print("Null")
        pass
    else:
        gray_window = ci.GrayScale_Window(width=window_width, height=window_height)
        img_corss = gray_window.create_crossWindow(fill_area=fill_value)
        cv2.imshow("img_corss", img_corss)

#全てのウィンドウを閉じる
def clickCloseWindows():
    cv2.destroyAllWindows()

#プログラムを終了
def clickQuit():
    sys.exit()

# メインウィンドウを作成
baseGround = tk.Tk()

# ウィンドウのサイズを設定
baseGround.geometry("750x750")

#現在のアプリ画面の横幅、縦幅を取得

# ウィンドウのタイトルを設定
baseGround.title("画像を描画します")

#ボタンを作成して配置
buttonColor_row = tk.Button(baseGround, text= "Color:Row", font=("",18), fg="green"
                    , width= 16, height=2, command=clickColorRow).place(x = 10, y=10)
buttonColor_column = tk.Button(baseGround, text= "Color:Column", font=("",18), fg="green"
                    , width=16, height=2, command=clickColorColumn).place(x= 10, y=220)
buttonColor_cross = tk.Button(baseGround, text= "Color:Cross", font=("",18), fg="green"
                    , width=16, height=2, command=clickColorCross).place(x= 10, y=440)
buttonGray_row = tk.Button(baseGround, text= "GrayScale:Row", font=("",18), fg="green"
                    , width=16, height=2, command=clickGrayRow).place(x = 300, y=10)
buttonGray_column = tk.Button(baseGround, text= "GrayScale:Column", font=("",18), fg="green"
                    , width=16, height=2, command=clickGrayColumn).place(x=300, y=220)
buttonGray_cross = tk.Button(baseGround, text= "GrayScale:Cross", font=("",18), fg="green"
                    , width=16, height=2, command=clickGrayCross).place(x=300, y=440)
buttonCloseWindows = tk.Button(baseGround, text= "Close All Windows", font=("",18), fg="blue"
                    , width=16, height=2, command=clickCloseWindows).place(x=80, y=630)
buttonQuit = tk.Button(baseGround, text= "Quit", font=("",18), fg="blue"
                    , width=12, height=2, command=clickQuit).place(x=360, y=630)

# ラベル
label = tk.Label(text='Filled Width')
label.place(x=80, y=90)

label1 = tk.Label(text='Filled Width')
label1.place(x=380, y=90)

label2 = tk.Label(text='Filled Width')
label2.place(x=80, y=300)

label3 = tk.Label(text='Filled Width')
label3.place(x=380, y=300)

labal5 = tk.Label(text='Filled Width')
labal5.place(x=380, y=520)

labal6 = tk.Label(text='Filled Width')
labal6.place(x=80, y=520)

vc = baseGround.register(limit_char)

# テキストボックス
txtBox = tk.Entry(width=20, validate="key", validatecommand=(vc, "%P"))
txtBox.place(x=50, y=120)

txtBox1 = tk.Entry(width=20, validate="key", validatecommand=(vc, "%P"))
txtBox1.place(x=350, y=120)

txtBox2 = tk.Entry(width=20, validate="key", validatecommand=(vc, "%P"))
txtBox2.place(x=50, y=330)

txtBox3 = tk.Entry(width=20, validate="key", validatecommand=(vc, "%P"))
txtBox3.place(x=350, y=330)

txtBox5 = tk.Entry(width=20, validate="key", validatecommand=(vc, "%P"))
txtBox5.place(x=350, y=550)

txtBox6 = tk.Entry(width=20, validate="key", validatecommand=(vc, "%P"))
txtBox6.place(x=50, y=550)

baseGround.mainloop()