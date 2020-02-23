#encoding:utf-8
import tkinter as tk
from tkinter import ttk
import numpy as  np
import sys
from main import HotelPipeline
import threading
import pymysql
import xlwt
import datetime
from tkinter import filedialog
from tkinter import END

class GUI(object):
    def __init__(self):        
        # 建立窗口
        self.window = tk.Tk()
        # 窗口名字
        self.window.title('携程')
        # 设定窗口大小
        self.window.geometry('800x400')
        # 字符类型函数，接收hit_me传过来的字符串
        self.var = tk.StringVar()
        # 添加一个标签
        self.l1 = tk.Label(self.window, text='请选择所在城市',  font=('Arial', 12), width=30, height=2)
        # l = tk.Label(self.window, textvariable=var, bg='white', fg='red', font=('Arial', 12), width=30, height=2)
        self.l2 = tk.Label(self.window, text='请选择酒店星级', font=('Arial', 12), width=30, height=2)
        self.l5 = tk.Label(self.window, text='请选择并发数量', font=('Arial', 12), width=30, height=2)
        self.l4 = tk.Label(self.window, text='请选择最低评分', font=('Arial', 12), width=30, height=2)
        self.l3 = tk.Label(self.window, text='请选择评论数量', font=('Arial', 12), width=30, height=2)
        self.l6 = tk.Label(self.window, text='选择路径并保存', font=('Arial', 12), width=30, height=2)

        # self.l4 = tk.Label(self.window, text='请选择', bg='green', font=('Arial', 12), width=30, height=2)
        
        
        # 添加下拉框
        self.cmb1 = ttk.Combobox(self.window, height=4)
        # 设置下拉菜单中的值
        self.cmb1['value'] = ('请选择','湖南省','长沙','怀化','娄底','邵阳','衡阳','岳阳','郴州','湘西','株洲','湘潭','衡阳','常德','张家界','永州')
        self.cmb1.current(0)

        self.cmb2 = ttk.Combobox(self.window, height=4)
        # 设置下拉菜单中的值
        self.cmb2['value'] = ('请选择','All','二星级及以下','三星级','四星级','五星级')
        self.cmb2.current(0)


        self.cmb5 = ttk.Combobox(self.window,height=4)
        # 设置下拉菜单中的值
        tp1 = tuple(i for i in range(1,11))
        self.cmb5['value'] = tp1
        self.cmb5.current(2)

        xx = ['请选择']
        x = np.arange(2.0,5.1,0.5)
        tp =  list(round(i,1) for i in x)
        tp = tuple(xx + tp)
        self.cmb4 = ttk.Combobox(self.window,height=4)
        # 设置下拉菜单中的值
        self.cmb4['value'] = tp
        self.cmb4.current(0)

        self.cmb3 = ttk.Combobox(self.window,height=4)
        # 设置下拉菜单中的值
        self.cmb3['value'] = ('请选择','100','200','500','1000')
        self.cmb3.current(0)


        # 酒店评分
        # e1=tk.Entry(self.window,width=100,height=2)
        # 评论数量

        # e1=tk.Entry(self.window,width=100,height=2)


        # 创建滚动条
        scroll = tk.Scrollbar()
        self.t = tk.Text(self.window, width=52, height=22, font=('Arial', 12))
        scroll.pack(side=tk.RIGHT,fill=tk.Y)
        scroll.config(command=self.t.yview)
        self.t.config(yscrollcommand=scroll.set)
        txt = 'Please select the conditions before clicking start>>>>>>>'
        # 将文本内容插入文本框
        self.t.insert('insert',txt)
        self.t.see(END);
        self.on_hit = False
        self.HotelPipeline = HotelPipeline(self.t,)
        self.b1 = tk.Button(self.window, text='开始', font=('Arial', 12), width=9, height=1, command=lambda :self.thread_it(self.HotelPipeline.thread_pool,self.cmb1.get(),self.cmb2.get(),self.cmb3.get(),self.cmb4.get(),int(self.cmb5.get())))
        # self.b2 = tk.Button(self.window, text='停止', font=('Arial', 12), width=9, height=1, command=self.stop)
        self.b3 = tk.Button(self.window, text='关闭', font=('Arial', 12), width=9, height=1, command=self.close)
        self.b4 = tk.Button(self.window, text='SAVE_EXCLE', font=('Arial', 12), width=12, height=1, command=self.save_as_excel)

        # 放置标签  l.pack()  l.place()
        self.l1.place(x=410, y=25, anchor='nw')
        self.cmb1.place(x=620, y=35, anchor='nw')
        self.l2.place(x=410, y=75, anchor='nw')
        self.cmb2.place(x=620, y=85, anchor='nw')
        self.l3.place(x=410, y=125, anchor='nw')
        self.cmb3.place(x=620, y=135, anchor='nw')
        self.l4.place(x=410, y=175, anchor='nw')
        self.cmb4.place(x=620, y=185, anchor='nw')
        self.l5.place(x=410, y=225, anchor='nw')
        self.cmb5.place(x=620, y=235, anchor='nw')
        self.l6.place(x=435, y=285,anchor='nw')
        self.b1.place(x=490, y=350, anchor='nw')
        # self.b2.place(x=590, y=350, anchor='nw')
        self.b3.place(x=690, y=350, anchor='nw')
        self.b4.place(x=660, y=290,anchor='nw')
        self.t.place(x=0, y=0, anchor='nw')
        # 主窗口循环显示,点一下会刷新
        # print(self.cmb1.get())
        self.window.resizable(0, 0)
        self.window.mainloop()

    @staticmethod
    def thread_it(func, *args):
        t = threading.Thread(target=func, args = args)
        t.setDaemon(True)  # 守护--就算主界面关闭，线程也会留守后台运行（不对!）
        t.start()

    # def thread_it(func, *args):
    #     '''将函数打包进线程'''
    #     # 创建
    #     t = threading.Thread(target=func, args=args)
    #     # 守护 !!!
    #     t.setDaemon(True)
    #     # 启动
    #     t.start()
    #     # 阻塞--卡死界面！
    #     # t.join()

    def hit_me(self):
        if self.on_hit == False:
            self.on_hit = True
            self.t.insert('insert','\n'+self.cmb1.get())
        else:
            self.on_hit = False
            self.var.set('')
    def start(self):
        self.HotelPipeline.thread_pool(self.cmb1.get())
    def stop(self):
        self.HotelPipeline.__del__()
    def close(self):
        sys.exit()


    def save_as_excel(self):
        dictName = filedialog.askdirectory()
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='', database='demo', charset='utf8')
        cursor = conn.cursor()
        sql = 'select * from hotel'
        cursor.execute(sql)
        li_single_hotel = cursor.fetchall()
        cursor.scroll(0, mode='absolute')
        # 搜取所有结果
        results = cursor.fetchall()

        # 获取MYSQL里面的数据字段名称
        fields = cursor.description
        workbook = xlwt.Workbook()
        date = str(datetime.date.today()).replace('-','')
        sheet = workbook.add_sheet('table_' + date, cell_overwrite_ok=True)

        # 写上字段信息
        for field in range(0, len(fields)):
            sheet.write(0, field, fields[field][0])

        # 获取并写入数据段信息
        row = 1
        col = 0
        for row in range(1, len(results) + 1):
            for col in range(0, len(fields)):
                sheet.write(row, col, u'%s' % results[row - 1][col])

        workbook.save('{}/{}.xlsx'.format(dictName,date))



class MyThread(threading.Thread):
    def __init__(self, func, *args):
        super().__init__()
        self.HotelPipeline = HotelPipeline()

        self.func = self.HotelPipeline.thread_pool
        self.args = args

        self.setDaemon(True)
        self.start()  # 在这里开始

    def run(self):
        self.func(*self.args)


if __name__ == '__main__':
    GUI = GUI()

