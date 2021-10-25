import random
import sys
from tkinter import *
import tkinter.messagebox#提示框
import tkinter.simpledialog#对话框
class MainForm:
    def __init__(self):
        self.root = Tk()
        self.gett = 0
        self.root.title("一百以内加-减-乘法练习软件")#界面标题
        self.root.geometry("415x280")#窗口大小
        self.label_text = Label(self.root, text="加-减练习软件", font=("楷体",25))
        self.label_text.pack()
        self.label_text_start = Label(self.root, text="请点击任意按钮开始", font=("楷体",15),fg="blue")
        self.label_text_start.pack()
        self.right_times=0
        self.error_times=0
        self.firsttime=1
        self.num=0
        self.num_now=0
        self.resu = 0
        self.wind2_exist=0
        self.input_frame()
        self.button_frame()
        self.root.mainloop()

    def get_total_num(self):

        while self.num==0:
            num = self.Enum.get()
            self.num = int(num)
            if self.num==0:
                tkinter.messagebox.showinfo(title="提示",message="总题数不能为0！")
                self.wind2_exist=0
                break
        self.num_now=self.num
        self.label_text_start.destroy()
        self.wind2.destroy()

    def choice_total_num(self):
        self.wind2 = Tk()
        self.wind2.title("设置总题数")#界面标题
        self.wind2.geometry("331x80+400+200")#窗口大小
        self.label_text2 = Label(self.wind2, text="设置本次练习总题量", font=("楷体",15))
        self.label_text2.pack()
        self.Fget_num = tkinter.Frame(self.wind2, width=10)# 创建内部容器
        self.content2 = tkinter.StringVar() # 标签的显示
        #单行的输入使用entry
        self.Enum = tkinter.Entry(self.Fget_num, width=10, font=("consolas",15), textvariable=self.content)
        self.Enum.pack(fill="x", expand=1)
        self.Fget_num.pack(side="top")
        Button(self.wind2, text='确定', command=self.get_total_num).pack(side="top")


    def make_formula(self):# 显示计算式
        num1 = random.randint(0,100)# 产生0到100的随机数
        num2 = random.randint(0,100-num1)
        sign = random.randint(0,2)# 随机产生符号
        sign1 = ""
        if sign == 0:
            sign1 = "+"
            self.resu = num1 + num2
            formula = str(num1) +" "+ sign1 + " " + str(num2) + " " + "="
        elif sign==2:
            sign1="*"
            num1=random.randint(0,10)
            num2=int(99/num1)
            self.resu=num1*num2
            formula = str(num1) +" "+ sign1 + " " + str(num2) + " " + "="
        else :
            sign1 = "-"
            if num1 > num2:
                self.resu = num1 - num2
                formula = str(num1) +" "+ sign1 + " " + str(num2) + " " + "="
            else :
                self.resu = num2 - num1
                formula = str(num2) +" "+ sign1 + " " + str(num1) + " " + "="
        self.label_text2 = Label(self.root, text=formula, font=("楷体",12))
        self.label_text2.pack(fill="x",expand=1)
        self.gett = 1

    def input_frame(self):# 输入框显示
        self.input_frame = tkinter.Frame(self.root, width=20)# 创建内部容器
        self.content = tkinter.StringVar() # 标签的显示
        #单行的输入使用entry
        self.entry = tkinter.Entry(self.input_frame, width=14, font=("consolas",15), textvariable=self.content)
        self.entry.pack(fill="x", expand=1)
        self.clean = False# 每次输入结束之后要清除数字
        self.input_frame.pack(side="top")
    
    def button_frame(self):#　定义按钮
        self.button_frame = tkinter.Frame(self.root, width=100)
        self.button_list = [[],[],[],[]]
        self.button_list[0].append(tkinter.Button(self.button_frame, text="1", fg="white", width=4, font=("consolas",15),bg="#778899"))
        self.button_list[0].append(tkinter.Button(self.button_frame, text="2", fg="white", width=4, font=("consolas",15),bg="#778899"))
        self.button_list[0].append(tkinter.Button(self.button_frame, text="3", fg="white", width=4, font=("consolas",15),bg="#778899"))
        self.button_list[1].append(tkinter.Button(self.button_frame, text="4", fg="white", width=4, font=("consolas",15),bg="#778899"))
        self.button_list[1].append(tkinter.Button(self.button_frame, text="5", fg="white", width=4, font=("consolas",15),bg="#778899"))
        self.button_list[1].append(tkinter.Button(self.button_frame, text="6", fg="white", width=4, font=("consolas",15),bg="#778899"))
        self.button_list[2].append(tkinter.Button(self.button_frame, text="7", fg="white", width=4, font=("consolas",15),bg="#778899"))
        self.button_list[2].append(tkinter.Button(self.button_frame, text="8", fg="white", width=4, font=("consolas",15),bg="#778899"))
        self.button_list[2].append(tkinter.Button(self.button_frame, text="9", fg="white", width=4, font=("consolas",15),bg="#778899"))
        self.button_list[3].append(tkinter.Button(self.button_frame, text="0", fg="white", width=4, font=("consolas",15),bg="#778899"))
        self.button_list[3].append(tkinter.Button(self.button_frame, text="ok", fg="black", width=4, font=("consolas",15),bg="yellow"))
        self.button_list[3].append(tkinter.Button(self.button_frame, text="start", fg="black", width=4, font=("consolas",15),bg="orange"))
        self.row = 0
        for group in self.button_list:
            self.column = 0
            for button in group:
                button.bind("<Button-1>",lambda event : self.button_handle(event))
                button.grid(row=self.row, column=self.column)
                self.column += 1
            self.row += 1
        self.button_frame.pack(side="bottom")
    

    def right_times_count(self):
        print("正确题数: ",self.right_times)
        self.L_count=tkinter.Label(self.root,text=("正确题数:",self.right_times),fg="blue",  font=("consolas",12))
        self.L_count.place(x=300,y=210)
        self.L_error=tkinter.Label(self.root,text=("错误次数:",self.error_times),fg="red",  font=("consolas",12))
        self.L_error.place(x=300,y=230)
        self.L_num_now=tkinter.Label(self.root,text=("剩余题数:",self.num_now),fg="black", wraplength=200, font=("consolas",12))
        self.L_num_now.place(x=300,y=250)

    def button_handle(self, event):# 按键事件绑定
        
        oper = event.widget["text"]
        if self.clean:
            self.content.set("")#清除数据
            self.clean = False
        if self.num==0 and self.wind2_exist==0:
                self.wind2_exist=1
                self.choice_total_num()
                    
        for i in range(100):
            if oper != "ok" and oper != "start" and self.num!=0:
                self.entry.insert("end", oper)
            elif oper == "ok" and self.num!=0:
                exp = self.entry.get()
                result = int(exp)
            elif oper == "start":
                if self.firsttime==1 and self.num!=0:
                    self.content.set("")
                    self.make_formula()
                    self.right_times_count()
                    self.firsttime=0
                
            if result == self.resu:
                tkinter.messagebox.showinfo(title="提示",message="计算正确")
                self.clean = True
                self.right_times+=1
                self.num_now-=1
                if self.gett == 1:
                    self.label_text2.destroy()
                    self.L_count.destroy()
                    self.L_error.destroy()
                    self.L_num_now.destroy()
                    self.gett == 0 
                self.content.set("")#清除数据
                self.clean = False
                if(self.num_now==0):
                    if(self.error_times==0):
                        tkinter.messagebox.showinfo(title="恭喜",message="本次练习完毕！共答题 %d 道，全部回答正确,非常棒！"%(self.num))
                    else:
                        tkinter.messagebox.showinfo(title="恭喜",message="本次练习完毕！共答题 %d 道，其中计算错误 %d 次,继续加油臭猪"%(self.num,self.error_times))
                    self.root.destroy()
                self.make_formula()
                self.right_times_count()
                self.gett=1
                break
            else :
                self.error_times+=1
                self.L_error.destroy()
                self.L_count.destroy()
                self.L_num_now.destroy()
                self.right_times_count()
                tkinter.messagebox.showinfo(title="提示",message="计算错误请重新计算")
                self.content.set("")

        

        

def main():
    MainForm()
if __name__ == "__main__":
    main()






