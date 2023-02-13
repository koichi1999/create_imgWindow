import copy
import numpy as np
from numpy.random import *
import cv2
import random

class  GrayScale_Window:
    #コンストラクタ
    def __init__(self, width, height):
        self.width = width #幅
        self.height = height #高さ
    
    def create_columnWindow(self, fill_area):
        #グレースケールのイメージ画像を作成し、ウィンドウに表示する
        #行を縞模様に塗りつぶす.第一象限、第二象限、第三象限、第四象限ごとに輝度を変えられる
        img = np.zeros((self.height, self.width), np.uint8)
        
        row,column = img.shape[:2]
        
        #用意する色
        #参考文献(Pythonでランダムな小数・整数を生成する, https://note.nkmk.me/python-random-randrange-randint/)
        #参考文献(NumPy, randomで様々な種類の乱数の配列を生成, https://note.nkmk.me/python-numpy-random/)
        fill_color = randint(0, 256, 8) #0〜255 の整数を8個生成
        
        for i in range(row):
            if i < row / 2:
                b = 1
                c = 0
                flag = False
                for j in range(column):
                    if j < column / 2:
                        column_pos = column - column
                        if column_pos+(fill_area*c) <= j < column_pos+(fill_area*b):
                            if flag == True:
                                brightness = fill_color[0]
                            else:
                                brightness = fill_color[1]
                            img[i,j] = brightness
                        else:
                            flag = not flag
                            if flag == True:
                                brightness = fill_color[0]
                            else:
                                brightness = fill_color[1]
                            img[i,j] = brightness
                            b = b + 1
                            c = c + 1
                    else:
                        column_pos = int(column / 2)
                        if j != column_pos:
                            pass
                        else:
                            b = 1
                            c = 0
                            flag = False
                        
                        if column_pos+(fill_area*c) <= j < column_pos+(fill_area*b):
                            if flag == True:
                                brightness = fill_color[2]
                            else:
                                brightness = fill_color[3]
                            img[i,j] = brightness
                        else:
                            flag = not flag
                            if flag == True:
                                brightness = fill_color[2]
                            else:
                                brightness = fill_color[3]
                            img[i,j] = brightness
                            b = b + 1
                            c = c + 1
            else:
                b = 1
                c = 0
                flag = False
                for j in range(column):
                    if j < column / 2:
                        column_pos = column - column
                        if column_pos+(fill_area*c) <= j < column_pos+(fill_area*b):
                            if flag == True:
                                brightness = fill_color[4]
                            else:
                                brightness  = fill_color[5]
                            img[i,j] = brightness
                        else:
                            flag = not flag
                            if flag == True:
                                brightness = fill_color[4]
                            else:
                                brightness = fill_color[5]
                            img[i,j] = brightness
                            b = b + 1
                            c = c + 1
                    else:
                        column_pos = int(column / 2)
                        if j != column_pos:
                            pass
                        else:
                            b = 1
                            c = 0
                            flag = False
                        if column_pos+(fill_area*c) <= j < column_pos+(fill_area*b):
                            if flag == True:
                                brightness = fill_color[6]
                            else:
                                brightness = fill_color[7]
                            img[i,j] = brightness
                        else:
                            flag = not flag
                            if flag == True:
                                brightness = fill_color[6]
                            else:
                                brightness = fill_color[7]
                            img[i,j] = brightness
                            b = b + 1
                            c = c + 1
        return img                   
    
    def create_rowWindow(self, fill_area):
        #グレースケールのイメージ画像を作成し、ウィンドウに表示する
        #行を縞模様に塗りつぶす.第一象限、第二象限、第三象限、第四象限ごとに輝度を変えられる
        img = np.zeros((self.height, self.width), np.uint8)
        
        row,column = img.shape[:2]
        
        #用意する色
        fill_color = randint(0, 256, 8) #0〜255 の整数を8個生成
        
        b = 1 #変数
        c = 0 #変数
        flag = False
        
        for i in range(row):
            if i < row / 2:
                row_pos = row - row
                if row_pos+(fill_area*c) <= i < row_pos+(fill_area*b):
                    pass
                else:
                    flag = not flag
                    b = b + 1
                    c = c + 1
                for j in range(column):
                    if j < column / 2:
                        if flag == True:
                            brightness = fill_color[0]
                        else:
                            brightness = fill_color[1]
                        img[i,j] = brightness
                    else:
                        if flag == True:
                            brightness = fill_color[2]
                        else:
                            brightness = fill_color[3]
                        img[i,j] = brightness
            else:
                row_pos = int(row / 2)
                if i != row_pos:
                    pass
                else:
                    b = 1
                    c = 0
                    flag = False
                    
                if row_pos+(fill_area*c) <= i < row_pos+(fill_area*b):
                    pass
                else:
                    flag = not flag
                    b = b + 1
                    c = c + 1     
                for j in range(column):
                    if j < column / 2:
                        if flag == True:
                            brightness = fill_color[4]
                        else:
                            brightness = fill_color[5]
                        img[i,j] = brightness
                    else:
                        if flag == True:
                            brightness = fill_color[6]
                        else:
                            brightness = fill_color[7]
                        img[i,j] = brightness
        return img
    
    def create_crossWindow(self, fill_area):
        #グレースケールのイメージ画像を作成し、ウィンドウに表示する
        #行を縞模様に塗りつぶす.第一象限、第二象限、第三象限、第四象限ごとに輝度を変えられる
        img = np.zeros((self.height, self.width), np.uint8)
        
        row,column = img.shape[:2]
        
        #用意する色
        #参考文献(Pythonでランダムな小数・整数を生成する, https://note.nkmk.me/python-random-randrange-randint/)
        #参考文献(NumPy, randomで様々な種類の乱数の配列を生成, https://note.nkmk.me/python-numpy-random/)
        fill_color = randint(0, 256, 8) #0〜255 の整数を8個生成
        fill_color2 = randint(0,256,4) #0〜255 の整数を4個生成
        b = 1 #変数
        c = 0 #変数
        flag = False
        
        for i in range(row):
            if i < row / 2:
                row_pos = row - row
                
                if row_pos+(fill_area*c) <= i < row_pos+(fill_area*b):
                    pass
                else:
                    flag = not flag
                    b = b + 1
                    c = c + 1
                for j in range(column):
                    if j < column / 2:
                        if flag == True:
                            brightness = fill_color[0]
                        else:
                            brightness = fill_color[1]
                        img[i,j] = brightness
                    else:
                        if flag == True:
                            brightness = fill_color[2]
                        else:
                            brightness = fill_color[3]
                        img[i,j] = brightness
            else:
                row_pos = int(row / 2)
                if i != row_pos:
                    pass
                else:
                    b = 1
                    c = 0
                    flag = False
                    
                if row_pos+(fill_area*c) <= i < row_pos+(fill_area*b):
                    pass
                else:
                    flag = not flag
                    b = b + 1
                    c = c + 1     
                for j in range(column):
                    if j < column / 2:
                        if flag == True:
                            brightness = fill_color[4]
                        else:
                            brightness = fill_color[5]
                        img[i,j] = brightness
                    else:
                        if flag == True:
                            brightness = fill_color[6]
                        else:
                            brightness = fill_color[7]
                        img[i,j] = brightness
        
        for i in range(row):
            if i < row / 2:
                b = 1
                c = 0
                flag = False
                for j in range(column):
                    if j < column / 2:
                        column_pos = column - column
                        if column_pos+(fill_area*c) <= j < column_pos+(fill_area*b):
                            if flag == True:
                                brightness = fill_color2[0]
                                img[i,j] = brightness
                            else:
                                pass
                        else:
                            flag = not flag
                            if flag == True:
                                brightness = fill_color2[0]
                                img[i,j] = brightness
                            else:
                                pass
                            b = b + 1
                            c = c + 1
                    else:
                        column_pos = int(column / 2)
                        if j != column_pos:
                            pass
                        else:
                            b = 1
                            c = 0
                            flag = False
                        
                        if column_pos+(fill_area*c) <= j < column_pos+(fill_area*b):
                            if flag == True:
                                brightness = fill_color2[1]
                                img[i,j] = brightness
                            else:
                                pass
                        else:
                            flag = not flag
                            if flag == True:
                                brightness = fill_color2[1]
                                img[i,j] = brightness
                            else:
                                pass
                            b = b + 1
                            c = c + 1
            else:
                b = 1
                c = 0
                flag = False
                for j in range(column):
                    if j < column / 2:
                        column_pos = column - column
                        if column_pos+(fill_area*c) <= j < column_pos+(fill_area*b):
                            if flag == True:
                                brightness = fill_color2[2]
                                img[i,j] = brightness
                            else:
                                pass
                        else:
                            flag = not flag
                            if flag == True:
                                brightness = fill_color2[2]
                                img[i,j] = brightness
                            else:
                                pass
                            b = b + 1
                            c = c + 1
                    else:
                        column_pos = int(column / 2)
                        if j != column_pos:
                            pass
                        else:
                            b = 1
                            c = 0
                            flag = False
                        if column_pos+(fill_area*c) <= j < column_pos+(fill_area*b):
                            if flag == True:
                                brightness = fill_color2[3]
                                img[i,j] = brightness
                            else:
                                pass
                        else:
                            flag = not flag
                            if flag == True:
                                brightness = fill_color2[3]
                                img[i,j] = brightness
                            else:
                                pass
                            b = b + 1
                            c = c + 1
        return img
    
class  Color_Window:
    #コンストラクタ
    def __init__(self, width, height):
        self.width = width #幅
        self.height = height #高さ
        self.channel = 3 #チャンネル数
    
    def create_columnWindow(self, fill_area):
        #カラーのイメージ画像を作成し、ウィンドウに表示する
        #行を縞模様に塗りつぶす.第一象限、第二象限、第三象限、第四象限ごとに輝度を変えられる
        img = np.zeros((self.height, self.width, self.channel), np.uint8)
        
        row,column = img.shape[:2]
        
        #用意する色
        #参考文献(Pythonでランダムな小数・整数を生成する, https://note.nkmk.me/python-random-randrange-randint/)
        fill_color = np.random.randint(0,256,(8,3)) # 0以上256未満の8行3列の配列の整数乱数
        
        for i in range(row):
            if i < row / 2:
                b = 1
                c = 0
                flag = False
                for j in range(column):
                    if j < column / 2:
                        column_pos = column - column
                        if column_pos+(fill_area*c) <= j < column_pos+(fill_area*b):
                            if flag == True:
                                color = fill_color[0,:]
                            else:
                                color = fill_color[1,:]
                            img[i,j] = color
                        else:
                            flag = not flag
                            if flag == True:
                                color = fill_color[0,:]
                            else:
                                color = fill_color[1,:]
                            img[i,j] = color
                            b = b + 1
                            c = c + 1
                    else:
                        column_pos = int(column / 2)
                        if j != column_pos:
                            pass
                        else:
                            b = 1
                            c = 0
                            flag = False
                        
                        if column_pos+(fill_area*c) <= j < column_pos+(fill_area*b):
                            if flag == True:
                                color = fill_color[2,:]
                            else:
                                color = fill_color[3,:]
                            img[i,j] = color
                        else:
                            flag = not flag
                            if flag == True:
                                color = fill_color[2,:]
                            else:
                                color = fill_color[3,:]
                            img[i,j] = color
                            b = b + 1
                            c = c + 1
            else:
                b = 1
                c = 0
                flag = False
                for j in range(column):
                    if j < column / 2:
                        column_pos = column - column
                        if column_pos+(fill_area*c) <= j < column_pos+(fill_area*b):
                            if flag == True:
                                color = fill_color[4,:]
                            else:
                                color = fill_color[5,:]
                            img[i,j] = color
                        else:
                            flag = not flag
                            if flag == True:
                                color = fill_color[4,:]
                            else:
                                color = fill_color[5,:]
                            img[i,j] = color
                            b = b + 1
                            c = c + 1
                    else:
                        column_pos = int(column / 2)
                        if j != column_pos:
                            pass
                        else:
                            b = 1
                            c = 0
                            flag = False
                        if column_pos+(fill_area*c) <= j < column_pos+(fill_area*b):
                            if flag == True:
                                color = fill_color[6,:]
                            else:
                                color = fill_color[7,:]
                            img[i,j] = color
                        else:
                            flag = not flag
                            if flag == True:
                                color = fill_color[6,:]
                            else:
                                color = fill_color[7,:]
                            img[i,j] = color
                            b = b + 1
                            c = c + 1
        return img                   
    
    def create_rowWindow(self, fill_area):
        #カラーのイメージ画像を作成し、ウィンドウに表示する
        #行を縞模様に塗りつぶす.第一象限、第二象限、第三象限、第四象限ごとに輝度を変えられる
        img = np.zeros((self.height, self.width, self.channel), np.uint8)
        
        row,column = img.shape[:2]
        
        fill_color = np.random.randint(0,256,(8,3)) # 0以上256未満の8行3列の配列の整数乱数
        
        b = 1 #変数
        c = 0 #変数
        flag = False
        
        for i in range(row):
            if i < row / 2:
                row_pos = row - row
                if row_pos+(fill_area*c) <= i < row_pos+(fill_area*b):
                    pass
                else:
                    flag = not flag
                    b = b + 1
                    c = c + 1
                for j in range(column):
                    if j < column / 2:
                        if flag == True:
                            color = fill_color[0,:]
                        else:
                            color = fill_color[1,:]
                        img[i,j] = color
                    else:
                        if flag == True:
                            color = fill_color[2,:]
                        else:
                            color = fill_color[3,:]
                        img[i,j] = color
            else:
                row_pos = int(row / 2)
                if i != row_pos:
                    pass
                else:
                    b = 1
                    c = 0
                    flag = False
                    
                if row_pos+(fill_area*c) <= i < row_pos+(fill_area*b):
                    pass
                else:
                    flag = not flag
                    b = b + 1
                    c = c + 1     
                for j in range(column):
                    if j < column / 2:
                        if flag == True:
                            color = fill_color[4,:]
                        else:
                            color = fill_color[5,:]
                        img[i,j] = color
                    else:
                        if flag == True:
                            color = fill_color[6,:]
                        else:
                            color = fill_color[7,:]
                        img[i,j] = color
        return img
    
    def create_crossWindow(self, fill_area):
        #カラーのイメージ画像を作成し、ウィンドウに表示する
        #行を縞模様に塗りつぶす.第一象限、第二象限、第三象限、第四象限ごとに輝度を変えられる
        img = np.zeros((self.height, self.width, self.channel), np.uint8)
        
        row,column = img.shape[:2]
        
        #用意する色
        #参考文献(Pythonでランダムな小数・整数を生成する, https://note.nkmk.me/python-random-randrange-randint/)
        #参考文献(NumPy, randomで様々な種類の乱数の配列を生成, https://note.nkmk.me/python-numpy-random/)
        fill_color = np.random.randint(0,256,(8,3)) # 0以上256未満の8行3列の配列の整数乱数
        fill_color2 = np.random.randint(0,256,(4,3)) # 0以上256未満の4行3列の配列の整数乱数
        b = 1 #変数
        c = 0 #変数
        flag = False
        
        for i in range(row):
            if i < row / 2:
                row_pos = row - row
                
                if row_pos+(fill_area*c) <= i < row_pos+(fill_area*b):
                    pass
                else:
                    flag = not flag
                    b = b + 1
                    c = c + 1
                for j in range(column):
                    if j < column / 2:
                        if flag == True:
                            color = fill_color[0,:]
                        else:
                            color = fill_color[1,:]
                        img[i,j] = color
                    else:
                        if flag == True:
                            color = fill_color[2,:]
                        else:
                            color = fill_color[3,:]
                        img[i,j] = color
            else:
                row_pos = int(row / 2)
                if i != row_pos:
                    pass
                else:
                    b = 1
                    c = 0
                    flag = False
                    
                if row_pos+(fill_area*c) <= i < row_pos+(fill_area*b):
                    pass
                else:
                    flag = not flag
                    b = b + 1
                    c = c + 1     
                for j in range(column):
                    if j < column / 2:
                        if flag == True:
                            color = fill_color[4,:]
                        else:
                            color = fill_color[5,:]
                        img[i,j] = color
                    else:
                        if flag == True:
                            color = fill_color[6,:]
                        else:
                            color = fill_color[7,:]
                        img[i,j] = color
        
        for i in range(row):
            if i < row / 2:
                b = 1
                c = 0
                flag = False
                for j in range(column):
                    if j < column / 2:
                        column_pos = column - column
                        if column_pos+(fill_area*c) <= j < column_pos+(fill_area*b):
                            if flag == True:
                                color = fill_color2[0,:]
                                img[i,j] = color
                            else:
                                pass
                        else:
                            flag = not flag
                            if flag == True:
                                color = fill_color2[0,:]
                                img[i,j] = color
                            else:
                                pass
                            b = b + 1
                            c = c + 1
                    else:
                        column_pos = int(column / 2)
                        if j != column_pos:
                            pass
                        else:
                            b = 1
                            c = 0
                            flag = False
                        
                        if column_pos+(fill_area*c) <= j < column_pos+(fill_area*b):
                            if flag == True:
                                color = fill_color2[1,:]
                                img[i,j] = color
                            else:
                                pass
                        else:
                            flag = not flag
                            if flag == True:
                                color = fill_color2[1,:]
                                img[i,j] = color
                            else:
                                pass
                            b = b + 1
                            c = c + 1
            else:
                b = 1
                c = 0
                flag = False
                for j in range(column):
                    if j < column / 2:
                        column_pos = column - column
                        if column_pos+(fill_area*c) <= j < column_pos+(fill_area*b):
                            if flag == True:
                                color = fill_color2[2,:]
                                img[i,j] = color
                            else:
                                pass
                        else:
                            flag = not flag
                            if flag == True:
                                color = fill_color2[2,:]
                                img[i,j] = color
                            else:
                                pass
                            b = b + 1
                            c = c + 1
                    else:
                        column_pos = int(column / 2)
                        if j != column_pos:
                            pass
                        else:
                            b = 1
                            c = 0
                            flag = False
                        if column_pos+(fill_area*c) <= j < column_pos+(fill_area*b):
                            if flag == True:
                                color = fill_color2[3,:]
                                img[i,j] = color
                            else:
                                pass
                        else:
                            flag = not flag
                            if flag == True:
                                color = fill_color2[3,:]
                                img[i,j] = color
                            else:
                                pass
                            b = b + 1
                            c = c + 1
        return img

#----------test code----------
#gray_window = GrayScale_Window(400, 400)
#img_column = gray_window.create_columnWindow(50)
#img_row = gray_window.create_rowWindow(50)
#img_cross = gray_window.create_crossWindow(20)

#color_window = Color_Window(400, 400)
#img_columnColor = color_window.create_columnWindow(20)
#img_rowColor = color_window.create_rowWindow(20)
#img_crossColor = color_window.create_crossWindow(20)

#cv2.imshow("img_column", img_column)
#cv2.imshow("img_row", img_row)
#cv2.imshow("img_cross", img_cross)
#cv2.imshow("img_columnColor", img_columnColor)
#cv2.imshow("img_rowColor", img_rowColor)
#cv2.imshow("img_crossColor", img_crossColor)
#cv2.waitKey(0)
#cv2.destroyAllWindows()