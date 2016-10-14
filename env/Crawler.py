import os,shutil,re,time
from tkinter import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from urllib import request
from bs4 import BeautifulSoup


chromeDefaultPath = r'C:\Users\Administrator\Downloads'
chromeDriver = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver'

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

# change file name
def changeFileName(path,order,searchName,year):
    newPath = '../'+ searchName
    filename = 'multiTimeline.csv'
    filelist = os.listdir(path)

    Olddir = os.path.join(path,filename)

   # for file in filelist:
    newfilename = order + str(year) + '-' + searchName + '.csv'
    Newdir = os.path.join(path,newfilename)
    os.rename(Olddir,Newdir)

#初始化 GUI
GUI = Tk()
GUI.title(' Google Trends Automation')
GUI.geometry('300x800')
GUI.resizable(width=False, height=False)

#Blank
blank_label = Label(GUI, text="  ", font=("Arial",20))
blank_label.pack(side=TOP)


#Title
title_label = Label(GUI, text="Google Trends", font=("Arial",20))
title_label.pack(side=TOP)

#Blank
blank_label = Label(GUI, text="  ", font=("Arial",10))
blank_label.pack(side=TOP)

#Input multiply label
multiply_input_labe = Label(GUI,text="Multiple Search",font=("Arial",12))
multiply_input_labe.pack(side=TOP)

#Input multiply Search
text = StringVar()
search_input_text = Text(GUI,height=10)
search_input_text.pack(side=TOP)

#Blank
blank_label = Label(GUI, text="  ", font=("Arial",10))
blank_label.pack(side=TOP)




#初始化 Frame
frame = Frame(GUI)

#左半部分
frame_L = Frame(frame)
# check input search

def checkInputSearch() :
    search_input_text.delete(0.0,END)
    search_input_text.insert(1.0, search_var.get())

# 检查Search的值
Button(frame_L, text='Check Searh', command=checkInputSearch).pack(side=TOP)


#search Label
search_label = Label(frame_L, text="Search", font=("Arial",11))
search_label.pack(side=TOP)

#Start Year Label
start_year_label = Label(frame_L, text="Start Year", font=("Arial",11))
start_year_label.pack(side=TOP)

#Eed Year Label
end_year_label = Label(frame_L, text="End Year", font=("Arial",11))
end_year_label.pack(side=TOP)

# World
world_label = Label(frame_L, text="World", font=("Arial",11))
world_label.pack(side=TOP)







frame_L.pack(side=LEFT)


#右半部分
frame_R = Frame(frame)

def cleanInputSearch() :
    search_input_text.delete(0.0,END)
    search_input.delete('0','end')
    print()


# 清空Search 的值
Button(frame_R, text= 'Clean Seach', command=cleanInputSearch).pack(side=TOP)


#Input search Name
search_var = StringVar()
search_input = Entry(frame_R, textvariable=search_var,bg = "pink")
search_input.pack(side = TOP)   # 这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM



#Input Start Year
start_year_var = StringVar()
start_year_input = Entry(frame_R, textvariable=start_year_var)
start_year_input.pack(side=TOP)

#Input End Year
end_year_var = StringVar()
end_year_input = Entry(frame_R, textvariable=end_year_var)
end_year_input.pack(side=TOP)

#Input World Year
world_var = StringVar()
world_input = Entry(frame_R,textvariable = world_var, bg = "yellow")
world_input.insert(0,'US')
world_input.pack(side=TOP)

frame_R.pack(side=RIGHT)

frame.pack(side=TOP)


# 下载 Single CSV function
def downloadCSV() :
    # Transformate
    world_str = world_var.get()
    search_str = search_var.get()
    start_year_int = int(start_year_var.get())
    end_year_int = int(end_year_var.get())


    # Select the browser




    options = webdriver.ChromeOptions()
    options.add_argument('--lang=en-us.utf-8')
    chrome = webdriver.Chrome(executable_path=chromeDriver, chrome_options=options)




    # Downloading
    while (start_year_int <= end_year_int):

        chrome.get('https://www.google.com.au/trends/explore?geo='+ world_str +'&date=' + str(start_year_int) + '-01-01%20' + str(
            start_year_int + 1) + '-12-31&q=' + search_str)

        chrome.implicitly_wait(30)

        chrome.find_element_by_xpath('/html/body/div[2]/div[2]/md-content/div/div/div[1]/trends-widget/ng-include/widget/div/div/div[1]/widget-actions/button').click()

        chrome.find_element_by_xpath('/html/body/div[2]/div[2]/md-content/div/div/div[1]/trends-widget/ng-include/widget/div/div/div[1]/widget-actions/div/button[3]').click()

        time.sleep(3)
        changeFileName(chromeDefaultPath,'single-',search_str,start_year_int)

        start_year_int = start_year_int + 1

    # Close Chrome
    chrome.close()

#下载 Mulitple CSV function
def downloadMultipleCSV():
    # Transformate
    world_str = world_var.get()
    search_str = search_var.get()
    start_year_int = int(start_year_var.get())
    end_year_int = int(end_year_var.get())
    original_year_int = int(start_year_var.get())

    search_input_text.insert(1.0,search_str)
    search_array = search_str.split(',')

    # Select the browser
    options = webdriver.ChromeOptions()
    options.add_argument('--lang=en-us.utf-8')
    chrome = webdriver.Chrome(executable_path=chromeDriver, chrome_options=options)

    for index in range(len(search_array)):
        # Downloading
        while (start_year_int <= end_year_int):
            chrome.get('https://www.google.com.au/trends/explore?geo=' + world_str + '&date=' + str(
                start_year_int) + '-01-01%20' + str(
                start_year_int + 1) + '-12-31&q=' + search_array[index])

            chrome.implicitly_wait(30)

            chrome.find_element_by_xpath(
                '/html/body/div[2]/div[2]/md-content/div/div/div[1]/trends-widget/ng-include/widget/div/div/div[1]/widget-actions/button').click()

            chrome.find_element_by_xpath(
                '/html/body/div[2]/div[2]/md-content/div/div/div[1]/trends-widget/ng-include/widget/div/div/div[1]/widget-actions/div/button[3]').click()

            time.sleep(3)


            changeFileName(chromeDefaultPath,str(index+1)+'-', search_array[index], start_year_int)

            start_year_int = start_year_int + 1
        start_year_int = original_year_int
        print(search_array[index])






#US
US_label = Label(GUI, text="America : US", font=("Arial",12))
US_label.pack(side=TOP)

#AU
AU_label = Label(GUI, text='Australia : AU', font=("Arial",12))
AU_label.pack(side=TOP)

#NZ
NZ_label = Label(GUI, text= 'New Zealand : NZ', font=("Arial",12))
NZ_label.pack(side=TOP)

#IN
IN_label = Label(GUI, text='India : IN', font=("Arial",12))
IN_label.pack(side=TOP)

#CN
CN_label = Label(GUI, text='China : CN', font=("Arial",12))
CN_label.pack(side=TOP)

def downloadFortune500():
    response = request.urlopen('http://www.barchart.com/stocks/sp500.php?_dtp1=0')
    soup = BeautifulSoup(response, "html.parser")
    table = soup.select('table#dt1')[0].get('data-info')
    company = table[8:]
    company_array = company.split(';')
    timeStr = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())
    file = open(timeStr + ' Fortune500.txt', 'w')
    file.write(company_array[0])


#下载 500 强股票代码
Button(GUI, text="Download Fortune500 ", command=downloadFortune500).pack(side=BOTTOM)

#Blank
blank_label = Label(GUI, text="  ", font=("Arial",5))
blank_label.pack(side=BOTTOM)
# 下载单一CSV文件 按钮
Button(GUI, text="Download Single CSV ", command=downloadCSV).pack(side=BOTTOM)

#Blank
blank_label = Label(GUI, text="  ", font=("Arial",5))
blank_label.pack(side=BOTTOM)
# 多重下载CSV文件 按钮
Button(GUI, text='Download Multiple CSV', command=downloadMultipleCSV).pack(side=BOTTOM)

#Blank
blank_label = Label(GUI, text=" ", font=("Arial",20))
blank_label.pack(side=BOTTOM)


GUI.mainloop()

