import os
from tkinter import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


#初始化 GUI
GUI = Tk()
GUI.title(' Google Trends Automation')
GUI.geometry('300x400')
GUI.resizable(width=False, height=True)

#Blank
blank_label = Label(GUI, text="  ", font=("Arial",30))
blank_label.pack(side=TOP)

#Title
title_label = Label(GUI, text="Google Trends", font=("Arial",20))
title_label.pack(side=TOP)

#Blank
blank_label = Label(GUI, text="  ", font=("Arial",30))
blank_label.pack(side=TOP)


#初始化 Frame
frame = Frame(GUI)

#左半部分
frame_L = Frame(frame)

#Company Label
company_label = Label(frame_L, text="Compnay", font=("Arial",18))
company_label.pack(side=TOP)

#Start Year Label
start_year_label = Label(frame_L, text="Start Year", font=("Arial",18))
start_year_label.pack(side=TOP)

#Eed Year Label
end_year_label = Label(frame_L, text="End Year", font=("Arial",18))
end_year_label.pack(side=TOP)



frame_L.pack(side=LEFT)


#右半部分
frame_R = Frame(frame)

#Input Company Name
company_var = StringVar()
company_input = Entry(frame_R, textvariable=company_var,bg = "pink")
company_input.pack(side = TOP)   # 这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM

#Input Start Year
start_year_var = StringVar()
start_year_input = Entry(frame_R, textvariable=start_year_var, bg = "green")
start_year_input.pack(side=TOP)

#Input End Year
end_year_var = StringVar()
end_year_input = Entry(frame_R, textvariable=end_year_var, bg = "green")
end_year_input.pack(side=TOP)

frame_R.pack(side=RIGHT)

frame.pack(side=TOP)


# 下载 CSV function
def downloadCSV() :
    # Transformate
    company_str = company_var.get()
    start_year_int = int(start_year_var.get())
    end_year_int = int(end_year_var.get())


    # Select the browser
    chrome = webdriver.Chrome()

    # Downloading
    while (start_year_int <= end_year_int):

        chrome.get('https://www.google.com.au/trends/explore?date=' + str(start_year_int) + '-01-01%20' + str(
            start_year_int) + '-12-31&q=' + company_str)

        chrome.implicitly_wait(20)

        chrome.find_element_by_xpath('/html/body/div[2]/div[2]/md-content/div/div/div[1]/trends-widget/ng-include/widget/div/div/div[1]/widget-actions/button').click()

        chrome.find_element_by_xpath('/html/body/div[2]/div[2]/md-content/div/div/div[1]/trends-widget/ng-include/widget/div/div/div[1]/widget-actions/div/button[3]').click()

        start_year_int = start_year_int + 1






# 按钮
Button(GUI, text="Download CSV ", command=downloadCSV).pack(side=BOTTOM)

#Blank
blank_label = Label(GUI, text="  ", font=("Arial",20))
blank_label.pack(side=BOTTOM)





GUI.mainloop()



# define Create a folder function
def mkdir(path):
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")

    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        print
        path + ' 创建成功'
        # 创建目录操作函数
        os.makedirs(path)
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print
        path + ' 目录已存在'
        return False


# Select the Company and Year
#company = input("Please input company name: ")
#start_year = input("Please input Start year: ")
#end_year = input("Please input End year: ")



# Create a foler
#mkdir('../' + company)










# close chrome browser
chrome.close()

