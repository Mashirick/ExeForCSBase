import tkinter as tk
from tkinter import filedialog
from tkinter import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl
from tkinter.filedialog import *
import math
import csv
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk
#设置字体
mpl.rcParams['font.sans-serif'] = ['simhei']
mpl.rcParams['axes.unicode_minus'] = False
#初始界面
def jm1():
    def open_file():#导入文件
        filename = filedialog.askopenfilename(title='导入文件', filetypes=[('csv', '*.csv')])
        en.set(filename)
    def return_file():#获取文件
        global place
        place = str(entry_filename.get()) #用get提取entry中的内容
        window.destroy()
        jm2() 
    #界面初始化
    window=tk.Tk()
    window.title("请先输入文件")
    texttop=tk.Text(window,height=10,width=40)
    window.geometry('720x540')
    
    en=StringVar()
    en.set('(请保证输入的文件地址无汉字)')
    button_import = tk.Button(window, text="请导入csv格式的文件", command=open_file).pack()
    entry_filename = tk.Entry(window, width=30, font=("宋体", 10, 'bold'),textvariable=en)
    entry_filename.pack()   
    button_return = tk.Button(window, text="确认导入", command=return_file).pack()
    
    window.mainloop()
#结果输出界面
def jm2():
    global data
    #界面初始化
    window2=tk.Tk()
    texttop=tk.Text(window2,height=10,width=40)
    window2.title("请选择您需要输出的数据")
    window2.geometry('720x540')
    label_window2=Label(window2,text="请选择您需要输出的数据")
    #获取学生总数
    data=pd.read_csv(place)
    row,columns=map(int,data.shape)
    student_number=row
    var=StringVar()
    display_label=Label(window2,textvariable=var,relief=RIDGE)
    var.set("学生总数为:"+str(student_number))
    #获取列表各项数据
    def gender():#性别数据
        global male, female,gender_flag
        gender_flag=1        
        gender=list(data.gender)
        male=gender.count('M')
        female=gender.count('F')
        window2.destroy()
        jm3()
    def nationality():#国家数据
        global nation,nation_amount,nations_flag
        nations_flag=1
        nations=list(data.Nationality)
        nation=list(set(nations))
        nation_amount=[]
        for name in nation:
            nation_amount.append(nations.count(name))
        window2.destroy()
        jm3()
    def birthplace():#出生地数据
        global birthplace,birthplace_amount,birthplace_flag
        birthplace_flag=1
        placeS=list(data.PlaceofBirth)
        birthplace=list(set(placeS))
        birthplace_amount=[]
        for name in birthplace:
            birthplace_amount.append(placeS.count(name))
        window2.destroy()
        jm3()
    def stage():
        global stage,stage_amount,stage_flag
        stage_flag=1
        stages=list(data.StageID)
        stage=list(set(stages))
        stage_amount=[]
        for name in stage:
            stage_amount.append(stages.count(name))
        window2.destroy()
        jm3()
    def grade():
        global grade,grade_amount,grade_flag
        grade_flag=1
        grades=list(data.GradeID)
        grade=list(set(grades))
        grade_amount=[]
        for name in grade:
            grade_amount.append(grades.count(name))
        window2.destroy()
        jm3()
    def relation():
        global relation,relation_amount,relation_flag
        relation_flag=1
        relations=list(data.Relation)
        relation=list(set(relations))
        relation_amount=[]
        for name in relation:
            relation_amount.append(relations.count(name))
        window2.destroy()
        jm3()
    def section():
        global section,section_amount,section_flag
        section_flag=1
        sections=list(data.SectionID)
        section=list(set(sections))
        section_amount=[]
        for name in section:
            section_amount.append(sections.count(name))
        window2.destroy()
        jm3()
    def theme():
        global theme,theme_amount,theme_flag
        theme_flag=1
        themes=list(data.Topic)
        theme=list(set(themes))
        theme_amount=[]
        for name in theme:
            theme_amount.append(themes.count(name))
        window2.destroy()
        jm3()
    def semeter():
        global semeter,semeter_amount,semeter_flag
        semeter_flag=1
        semeters=list(data.Semester)
        semeter=list(set(semeters))
        semeter_amount=[]
        for name in semeter:
            semeter_amount.append(semeters.count(name))
        window2.destroy()
        jm3()
    def PAS():
        global PAS,PAS_amount,PAS_flag
        PAS_flag=1
        PASs=list(data.ParentAnsweringSurvey)
        PAS=list(set(PASs))
        PAS_amount=[]
        for name in PAS:
            PAS_amount.append(PASs.count(name))
        window2.destroy()
        jm3()
    def PSS():
        global PSS,PSS_amount,PSS_flag
        PSS_flag=1
        PSSs=list(data.ParentschoolSatisfaction)
        PSS=list(set(PSSs))
        PSS_amount=[]
        for name in PSS:
            PSS_amount.append(PSSs.count(name))
        window2.destroy()
        jm3()
    def class_hml():
        global hml,class_flag
        class_flag=1
        class_hml=list(data.Class)
        hml=[class_hml.count(1),class_hml.count(2),class_hml.count(3)]
        window2.destroy()
        jm3()
    def find_cj():
        window2.destroy()
        jm4()
    #设置按键
    global gender_flag,nations_flag,birthplace_flag,stage_flag,grade_flag,relation_flag
    global section_flag,theme_flag,semeter_flag,PAS_flag,PSS_flag
    lis=[0,0,0,0,0,0,0,0,0,0,0,0]
    class_flag,gender_flag,nations_flag,birthplace_flag,stage_flag,grade_flag,relation_flag,section_flag,theme_flag,semeter_flag,PAS_flag,PSS_flag=map(int,lis)
    button_gender = tk.Button(window2, text="显示性别数据", command=gender)
    button_nations=tk.Button(window2,text='显示学生国籍数据', command=nationality)
    button_birthplace=tk.Button(window2,text='显示学生出生地数据', command=birthplace)
    button_stage= tk.Button(window2, text="显示教育阶段数据", command=stage)
    button_grade= tk.Button(window2, text="显示年级数据", command=grade)
    button_relation= tk.Button(window2, text="显示对学生的负责人情况数据", command=relation)
    button_section= tk.Button(window2, text="显示班级分布数据", command=section)
    button_theme= tk.Button(window2, text="显示学生所选主题数据", command=theme)
    button_semeter= tk.Button(window2, text="显示学期分布数据", command=semeter)
    button_PAS= tk.Button(window2, text="显示家长回答问卷情况数据", command=PAS)
    button_PSS= tk.Button(window2, text="显示家长对学校印象数据", command=PSS)
    button_find_cj=tk.Button(window2,text="查询成绩",command=find_cj)
    button_hml=tk.Button(window2,text="学生总体成绩图表",command=class_hml)
    display_label.grid(row=0,column=0,rowspan=1,columnspan=4,sticky='w')
    button_gender.grid(row=4,column=0,rowspan=1,columnspan=4,sticky='w')
    button_nations.grid(row=8,column=0,rowspan=1,columnspan=4,sticky='w')
    button_birthplace.grid(row=9,column=0,rowspan=1,columnspan=4,sticky='w')
    button_stage.grid(row=5,column=0,rowspan=1,columnspan=4,sticky='w')
    button_grade.grid(row=3,column=0,rowspan=1,columnspan=4,sticky='w')
    button_relation.grid(row=13,column=0,rowspan=1,columnspan=4,sticky='w')
    button_section.grid(row=6,column=0,rowspan=1,columnspan=4,sticky='w')
    button_theme.grid(row=10,column=0,rowspan=1,columnspan=4,sticky='w')
    button_semeter.grid(row=7,column=0,rowspan=1,columnspan=4,sticky='w')
    button_PAS.grid(row=12,column=0,rowspan=1,columnspan=4,sticky='w')
    button_PSS.grid(row=11,column=0,rowspan=1,columnspan=4,sticky='w')
    button_find_cj.grid(row=1,column=0,rowspan=1,columnspan=4,sticky='w')
    button_hml.grid(row=2,column=0,rowspan=1,columnspan=4,sticky='w')
    window2.mainloop()
def jm3():
    class From:
        def __init__(self): 
            self.root=tk.Tk()                    #创建主窗体
            self.canvas=tk.Canvas()              #创建一块显示图形的画布
            if gender_flag:#性别
                self.figure=self.gender_matplotlib() #返回matplotlib所画图形的figure对象
            elif nations_flag:#国籍
                self.figure=self.nations_matplotlib()
            elif birthplace_flag:#出生地
                self.figure=self.birthplace_matplotlib()
            elif stage_flag:#教育阶段
                self.figure=self.stage_matplotlib()
            elif grade_flag:#年级
                self.figure=self.grade_matplotlib()
            elif relation_flag:#对学生负责情况
                self.figure=self.relation_matplotlib()
            elif section_flag:#班级分布
                self.figure=self.section_matplotlib()
            elif theme_flag:#主题情况
                self.figure=self.theme_matplotlib()
            elif semeter_flag:#学期分布
                self.figure=self.semeter_matplotlib()
            elif PAS_flag:#家长是否回答
                self.figure=self.PAS_matplotlib()
            elif PSS_flag:#家长是否满意
                self.figure=self.PSS_matplotlib()
            elif class_flag:
                self.figure=self.hml_matplotlib()
            self.create_form(self.figure)        #将figure显示在tkinter窗体上面
            self.root.mainloop()
        #绘图函数  
        def gender_matplotlib(self):
            picture=plt.figure(num=2,figsize=(16,12),dpi=80,facecolor="pink",edgecolor='green',frameon=True)
            pie_male=float(male*100/(male+female))
            pie_female=float(female*100/(male+female))
            pie_gender=[pie_male,pie_female]
            name_gender=['Male','Female']
            patches,name_text,gender_text=plt.pie(pie_gender,labels=name_gender,autopct='%2.2f%%',radius=0.6,startangle=0)
            plt.title('男女比例饼图',fontsize=28)
            plt.legend(['male','female'],fontsize=20)
            for t in name_text:  
                t.set_size(20)       
            for t in gender_text:    
                t.set_size(20)           
            return picture
        def nations_matplotlib(self):
            picture=plt.figure(num=2,figsize=(16,12),dpi=80,facecolor="pink",edgecolor='green',frameon=True)
            nation_name=['']*len(nation)
            patches,name_text,nation_text=plt.pie(nation_amount,labels=nation_name,autopct='%2.2f%%',radius=0.6,pctdistance=1.1,startangle=100)
            plt.title('来自不同国家的学生占比',fontsize=28)
            plt.legend(nation,fontsize=14)
            for t in name_text:  
                t.set_size(20)       
            for t in nation_text:    
                t.set_size(8)
            return picture
        def birthplace_matplotlib(self):
            picture=plt.figure(num=2,figsize=(16,12),dpi=80,facecolor="pink",edgecolor='green',frameon=True)
            birthplace_name=['']*len(birthplace)
            patches,name_text,birthday_text=plt.pie(birthplace_amount,labels=birthplace_name,autopct='%2.2f%%',radius=0.8,startangle=100,pctdistance=1.1)
            plt.title('出生自不同国家的学生占比',fontsize=28)
            plt.legend(birthplace,fontsize=14)
            for t in name_text:  
                t.set_size(20)       
            for t in birthday_text:    
                t.set_size(8)           
            return picture
        def stage_matplotlib(self):
            picture=plt.figure(num=2,figsize=(16,12),dpi=80,facecolor="pink",edgecolor='green',frameon=True)
            stage_name=stage
            patches,name_text,stage_text=plt.pie(stage_amount,labels=stage_name,autopct='%2.2f%%',radius=0.8,startangle=0)
            plt.title('每个教育阶段的学生占比',fontsize=28)
            plt.legend(stage,fontsize=14)
            for t in name_text:  
                t.set_size(25)       
            for t in stage_text:    
                t.set_size(25)           
            return picture
        def grade_matplotlib(self):
            picture=plt.figure(num=2,figsize=(16,12),dpi=80,facecolor="pink",edgecolor='green',frameon=True)
            grade_name=['']*len(grade)
            patches,name_text,grade_text=plt.pie(grade_amount,labels=grade_name,autopct='%2.2f%%',radius=0.8,startangle=0,pctdistance=1.1)
            plt.title('每个年级的学生占比',fontsize=28)
            plt.legend(grade,fontsize=14)
            for t in name_text:  
                t.set_size(20)       
            for t in grade_text:    
                t.set_size(16)           
            return picture
        def relation_matplotlib(self):
            picture=plt.figure(num=2,figsize=(16,12),dpi=80,facecolor="pink",edgecolor='green',frameon=True)
            relation_name=relation
            patches,name_text,relation_text=plt.pie(relation_amount,labels=relation_name,autopct='%2.2f%%',radius=0.8,startangle=0)
            plt.title('学生家庭教育负责人',fontsize=28)
            plt.legend(relation,fontsize=18)
            for t in name_text:  
                t.set_size(20)       
            for t in relation_text:    
                t.set_size(20)           
            return picture
        def section_matplotlib(self):
            picture=plt.figure(num=2,figsize=(16,12),dpi=80,facecolor="pink",edgecolor='green',frameon=True)
            section_name=section
            patches,name_text,section_text=plt.pie(section_amount,labels=section_name,autopct='%2.2f%%',radius=0.8,startangle=0)
            plt.title('不同班级学生占比',fontsize=28)
            plt.legend(section,fontsize=18)
            for t in name_text:  
                t.set_size(20)       
            for t in section_text:    
                t.set_size(20)           
            return picture
        def theme_matplotlib(self):
            picture=plt.figure(num=2,figsize=(16,12),dpi=80,facecolor="pink",edgecolor='green',frameon=True)
            theme_name=['']*len(theme)
            patches,name_text,theme_text=plt.pie(theme_amount,labels=theme_name,
                                                 colors=['tomato', 'lightskyblue', 'goldenrod', 'green', 'y','c','m','slategray','linen','palegreen','olive','r'],
                                                 autopct='%2.2f%%',radius=0.8,startangle=0,pctdistance=0.8)
            plt.title('学生所选的主题在全部主题中占比',fontsize=28)
            plt.legend(theme,fontsize=18)
            for t in name_text:  
                t.set_size(20)       
            for t in theme_text:    
                t.set_size(16)           
            return picture
        def semeter_matplotlib(self):
            picture=plt.figure(num=2,figsize=(16,12),dpi=80,facecolor="pink",edgecolor='green',frameon=True)
            semeter_name=semeter
            patches,name_text,semeter_text=plt.pie(semeter_amount,labels=semeter_name,autopct='%2.2f%%',radius=0.8,startangle=0)
            plt.title('在不同学期的学生占比',fontsize=28)
            plt.legend(semeter,fontsize=20)
            for t in name_text:  
                t.set_size(20)       
            for t in semeter_text:    
                t.set_size(20)           
            return picture
        def PAS_matplotlib(self):
            picture=plt.figure(num=2,figsize=(16,12),dpi=80,facecolor="pink",edgecolor='green',frameon=True)
            PAS_name=PAS
            patches,name_text,PAS_text=plt.pie(PAS_amount,labels=PAS_name,autopct='%2.2f%%',radius=0.8,startangle=0)
            plt.title('家长是否回复了学校调查问卷',fontsize=28)
            plt.legend(PAS,fontsize=14)
            for t in name_text:  
                t.set_size(20)       
            for t in PAS_text:    
                t.set_size(20)           
            return picture
        def PSS_matplotlib(self):
            picture=plt.figure(num=2,figsize=(16,12),dpi=80,facecolor="pink",edgecolor='green',frameon=True)
            PSS_name=PSS
            patches,name_text,PSS_text=plt.pie(PSS_amount,labels=PSS_name,autopct='%2.2f%%',radius=0.8,startangle=0)
            plt.title('已收集的调查问卷中家长的印象',fontsize=28)
            plt.legend(PSS,fontsize=18)
            for t in name_text:  
                t.set_size(20)       
            for t in PSS_text:    
                t.set_size(20)
            return picture
        def hml_matplotlib(self):
            picture=plt.figure(num=2,figsize=(14,10),dpi=70,facecolor="pink",edgecolor='green',frameon=True)
            y=hml
            x=[100,80,60]
            p=np.polyfit(x,y,2)
            x2=np.linspace(60,100,80)
            y2=np.polyval(p,x2)
            plt.bar(x,y,width=3.0,label='柱状图')
            plt.plot(x, y,'*:r',label='折线图')
            plt.plot(x2,y2,'g-',label='拟合曲线')
            plt.xlabel('Class')
            plt.xlim(40,120)
            plt.xticks(np.linspace(60,100,5,endpoint=True))
            plt.ylabel('Numbers')
            plt.ylim(0,250)
            plt.yticks(np.linspace(0,250,6,endpoint=True))
            plt.title('拟合曲线表达式：y='+str(round(p[0],2))+'x^2+'+str(round(p[1],2))+'x'+str(round(p[2],2)))
            plt.legend()
            return picture
        #tk.canvas绘图
        def create_form(self,figure):
            #把绘制的图形显示到tkinter窗口上
            self.canvas=FigureCanvasTkAgg(figure,self.root)
            self.canvas.draw() 
            self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)        
            #把matplotlib绘制图形的导航工具栏显示到tkinter窗口上
            toolbar =NavigationToolbar2Tk(self.canvas, self.root) 
            toolbar.update()
            self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
     
    if __name__=="__main__":
        form=From()
def jm4():
    #获取年级、性别成绩数据
    def cj_G1():
        global flag1,df
        if 'G-01' in df_grade:
            flag1=1
            df=data.query("GradeID == 'G-01'")
            thesame()
        else:
            window4.destroy()
            jm5()
    def cj_G2():
        global flag2,df
        if 'G-02' in df_grade:
            flag2=1
            df=data.query("GradeID == 'G-02'")
            thesame()
        else:
            window4.destroy()
            jm5()
    def cj_G3():
        global flag3,df
        if 'G-03' in df_grade:
            flag3=1
            df=data.query("GradeID == 'G-03'")
            thesame()
        else:
            window4.destroy()
            jm5()
    def cj_G4():
        global flag4,df
        if 'G-04' in df_grade:
            flag4=1
            df=data.query("GradeID == 'G-04'")
            thesame()
        else:
            window4.destroy()
            jm5()
    def cj_G5():
        global flag5,df
        if 'G-05' in df_grade:
            flag5=1
            df=data.query("GradeID == 'G-05'")
            thesame()
        else:
            window4.destroy()
            jm5()
    def cj_G6():
        global flag6,df
        if 'G-06' in df_grade:
            flag6=1
            df=data.query("GradeID == 'G-06'")
            thesame()
        else:
            window4.destroy()
            jm5()
    def cj_G7():
        global flag7,df
        if 'G-07' in df_grade:
            flag7=1
            df=data.query("GradeID == 'G-07'")
            thesame()
        else:
            window4.destroy()
            jm5()
    def cj_G8():
        global flag8,df
        if 'G-08' in df_grade:
            flag8=1
            df=data.query("GradeID == 'G-08'")
            thesame()
        else:
            window4.destroy()
            jm5()
    def cj_G9():
        global flag9,df
        if 'G-09' in df_grade:
            flag9=1
            df=data.query("GradeID == 'G-09'")
            thesame()
        else:
            window4.destroy()
            jm5()
    def cj_G10():
        global flag10,df
        if 'G-10' in df_grade:
            flag10=1
            df=data.query("GradeID == 'G-10'")
            thesame()
        else:
            window4.destroy()
            jm5()
    def cj_G11():
        global flag11,df
        if 'G-11' in df_grade:
            flag11=1
            df=data.query("GradeID == 'G-11'")
            thesame()
        else:
            window4.destroy()
            jm5()
    def cj_G12():
        global flag12,df
        if 'G-12' in df_grade:
            flag12=1
            df=data.query("GradeID == 'G-12'")
            thesame()
        else:
            window4.destroy()
            jm5()
    def cj_male():
        global flag_male,df
        if 'M' in df_gender:
            flag_male=1
            df=data.query("gender == 'M'")
            thesame()
        else:
            window4.destroy()
            jm5()
    def cj_female():
        global flag_female,df
        if 'F' in df_gender:
            flag_female=1
            df=data.query("gender == 'F'")
            thesame()
        else:
            window4.destroy()
            jm5()
    #获取三个班级的各项指标数据
    def thesame():
        global PSS,classes,raisehands,announcementsview,visitedresources,discussion,amt
        df_a=df.query("SectionID == 'A'")
        df_b=df.query("SectionID == 'B'")
        df_c=df.query("SectionID == 'C'")
        amt,z=map(int,df.shape)
        raisehands=[sum(list(df_a.raisedhands)),sum(list(df_b.raisedhands)),sum(list(df_c.raisedhands))]
        announcementsview=[sum(list(df_a.AnnouncementsView)),sum(list(df_b.AnnouncementsView)),sum(list(df_c.AnnouncementsView))]
        visitedresources=[sum(list(df_a.VisitedResources)),sum(list(df_b.VisitedResources)),sum(list(df_c.VisitedResources))]
        discussion=[sum(list(df_a.Discussion)),sum(list(df_b.Discussion)),sum(list(df_c.Discussion))]
        PSS=[list(df_a.ParentschoolSatisfaction).count('Good'),list(df_a.ParentschoolSatisfaction).count('Bad'),
                 list(df_b.ParentschoolSatisfaction).count('Good'),list(df_b.ParentschoolSatisfaction).count('Bad'),
                 list(df_c.ParentschoolSatisfaction).count('Good'),list(df_c.ParentschoolSatisfaction).count('Bad')]
        classes=[list(df_a.Class).count(1),list(df_a.Class).count(2),list(df_a.Class).count(3),
                   list(df_b.Class).count(1),list(df_b.Class).count(2),list(df_b.Class).count(3),
                   list(df_c.Class).count(1),list(df_c.Class).count(2),list(df_c.Class).count(3)]
        window4.destroy()
        jm5()
    #计算相关系数
    def cal_relation(x,y):
        n=len(x)
        sum1=sum(list(x))
        sum2=sum(list(y))
        gene1,gene2,gene3=map(int,[0,0,0])
        for i in range(n):
            gene1+=(x[i]-sum1/n)*(y[i]-sum2/n)
            gene2+=(x[i]-sum1/n)**2
            gene3+=(y[i]-sum2/n)**2
        r=gene1/(gene2*gene3)**0.5
        return r
    #对相关系数所需值进行初始化，并计算出相关系数
    def relation():
        global r_raisedhands,r_StudentAbsenceDays,r_gender,r_relation,r_VisitedResources,r_AnnouncementsView,r_Discussion
        
        list_raisedhands=list(data.raisedhands)
        list_StudentAbsenceDays=list(data.StudentAbsenceDays)
        list_gender=list(data.gender)
        list_Relation=list(data.Relation)
        list_Class=list(data.Class)
        list_VisitedResources=list(data.VisitedResources)
        list_AnnouncementsView=list(data.AnnouncementsView)
        list_Discussion=list(data.Discussion)
        
        list_gender=[1 if x=='M' else 0 for x in list_gender]
        list_relation=[1 if x=='Father' else 0 for x in list_Relation]
        list_StudentAbsenceDays=[1 if x=='Above-7' else 0 for x in list_StudentAbsenceDays]
        
        
        r_raisedhands=cal_relation(list_raisedhands,list_Class)
        r_StudentAbsenceDays=cal_relation(list_StudentAbsenceDays,list_Class)
        r_gender=cal_relation(list_gender,list_Class)
        r_relation=cal_relation(list_relation,list_Class)
        r_VisitedResources=cal_relation(list_VisitedResources,list_Class)
        r_AnnouncementsView=cal_relation(list_AnnouncementsView,list_Class)
        r_Discussion=cal_relation(list_Discussion,list_Class)
        
        window4.destroy()
        jm6()
    #界面初始化
    window4=tk.Tk()
    texttop=tk.Text(window4,height=10,width=40)
    window4.title("请选择您需要查看的数据")
    window4.geometry('720x540')
    label_window4=Label(window4,text="请选择您需要查看的数据")
    #设置按键
    global flag1,df_grade,flag2,flag3,flag4,flag5,flag6,flag7,flag8,flag9,flag10,flag11,flag12,flag_male,flag_female,flag_relation
    df_grade=set(list(data.GradeID))
    df_gender=set(list(data.gender))
    lis=[0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    flag1,flag2,flag3,flag4,flag5,flag6,flag7,flag8,flag9,flag10,flag11,flag12,flag_male,flag_female=map(int,lis)
    button_G1=tk.Button(window4,text="查询Grade01成绩",command=cj_G1)
    button_G2=tk.Button(window4,text="查询Grade02成绩",command=cj_G2)
    button_G3=tk.Button(window4,text="查询Grade03成绩",command=cj_G3)
    button_G4=tk.Button(window4,text="查询Grade04成绩",command=cj_G4)
    button_G5=tk.Button(window4,text="查询Grade05成绩",command=cj_G5)
    button_G6=tk.Button(window4,text="查询Grade06成绩",command=cj_G6)
    button_G7=tk.Button(window4,text="查询Grade07成绩",command=cj_G7)
    button_G8=tk.Button(window4,text="查询Grade08成绩",command=cj_G8)
    button_G9=tk.Button(window4,text="查询Grade09成绩",command=cj_G9)
    button_G10=tk.Button(window4,text="查询Grade10成绩",command=cj_G10)
    button_G11=tk.Button(window4,text="查询Grade11成绩",command=cj_G11)
    button_G12=tk.Button(window4,text="查询Grade12成绩",command=cj_G12)
    button_relation=tk.Button(window4,text="  成绩相关性展示 ",command=relation)
    button_male=tk.Button(window4,text="查询男性学生成绩",command=cj_male)
    button_female=tk.Button(window4,text="查询女性学生成绩",command=cj_female)
    button_G1.grid(row=0,column=0,rowspan=1,columnspan=4,sticky='w')
    button_G2.grid(row=1,column=0,rowspan=1,columnspan=4,sticky='w')
    button_G3.grid(row=2,column=0,rowspan=1,columnspan=4,sticky='w')
    button_G4.grid(row=3,column=0,rowspan=1,columnspan=4,sticky='w')
    button_G5.grid(row=4,column=0,rowspan=1,columnspan=4,sticky='w')
    button_G6.grid(row=5,column=0,rowspan=1,columnspan=4,sticky='w')
    button_G7.grid(row=6,column=0,rowspan=1,columnspan=4,sticky='w')
    button_G8.grid(row=7,column=0,rowspan=1,columnspan=4,sticky='w')
    button_G9.grid(row=8,column=0,rowspan=1,columnspan=4,sticky='w')
    button_G10.grid(row=9,column=0,rowspan=1,columnspan=4,sticky='w')
    button_G11.grid(row=10,column=0,rowspan=1,columnspan=4,sticky='w')
    button_G12.grid(row=11,column=0,rowspan=1,columnspan=4,sticky='w')
    button_male.grid(row=12,column=0,rowspan=1,columnspan=4,sticky='w')    
    button_female.grid(row=13,column=0,rowspan=1,columnspan=4,sticky='w')
    button_relation.grid(row=14,column=0,rowspan=1,columnspan=4,sticky='w')   
    window4.mainloop()
def jm5():
    #设置展示数据的函数
    def g_show():
        var_column=StringVar()
        var_raise=StringVar()
        var_announce=StringVar()      
        var_visited=StringVar()
        var_discussion=StringVar()
        var_PSS=StringVar()
        var_class=StringVar()        
        
        column_label=Label(window5,textvariable=var_column,relief=RIDGE)
        raise_label=Label(window5,textvariable=var_raise,relief=RIDGE)
        announce_label=Label(window5,textvariable=var_announce,relief=RIDGE)
        visited_label=Label(window5,textvariable=var_visited,relief=RIDGE)
        discussion_label=Label(window5,textvariable=var_discussion,relief=RIDGE)
        PSS_label=Label(window5,textvariable=var_PSS,relief=RIDGE)
        class_label=Label(window5,textvariable=var_class,relief=RIDGE)
        
        var_column.set("数据展示格式：数据标题：Section A   Section B  Section C（括号内为数据的平均值）")
        var_raise.set("全部学生举手的次数为："
                      +str(raisehands[0])+str('(')+str(round(raisehands[0]/amt,2))+str(')')+'     '
                      +str(raisehands[1])+str('(')+str(round(raisehands[1]/amt,2))+str(')')+'     '
                      +str(raisehands[2])+str('(')+str(round(raisehands[2]/amt,2))+str(')'))
        var_announce.set("所有学生浏览学校公告的次数："
                         +str(announcementsview[0])+str('(')+str(round(announcementsview[0]/amt,2))+str(')')+'     '
                         +str(announcementsview[1])+str('(')+str(round(announcementsview[1]/amt,2))+str(')')+'     '
                         +str(announcementsview[2])+str('(')+str(round(announcementsview[2]/amt,2))+str(')'))
        var_visited.set("全部学生浏览在线课件的次数："
                        +str(visitedresources[0])+str('(')+str(round(visitedresources[0]/amt,2))+str(')')+'     '
                        +str(visitedresources[1])+str('(')+str(round(visitedresources[1]/amt,2))+str(')')+'     '
                        +str(visitedresources[2])+str('(')+str(round(visitedresources[2]/amt,2))+str(')'))
        var_discussion.set("全部学生参与课堂讨论的次数 ："
                        +str(discussion[0])+str('(')+str(round(discussion[0]/amt,2))+str(')')+'     '
                        +str(discussion[1])+str('(')+str(round(discussion[1]/amt,2))+str(')')+'     '
                        +str(discussion[2])+str('(')+str(round(discussion[2]/amt,2))+str(')'))
        var_PSS.set("家长对于学校的满意度（好/不好）："
                        +str(PSS[0])+str(' / ')+str(PSS[1])+'     '
                        +str(PSS[2])+str(' / ')+str(PSS[3])+'     '
                        +str(PSS[4])+str(' / ')+str(PSS[5]))
        var_class.set("每个等级学生人数（高/中/低）："
                        +str(classes[0])+str(' / ')+str(classes[1])+str(' / ')+str(classes[2])+'     '
                        +str(classes[3])+str(' / ')+str(classes[4])+str(' / ')+str(classes[5])+'     '
                        +str(classes[6])+str(' / ')+str(classes[7])+str(' / ')+str(classes[8]))
        
        column_label.grid(row=0,column=0,sticky='w')
        raise_label.grid(row=1,column=0,sticky='w')
        announce_label.grid(row=2,column=0,sticky='w')
        visited_label.grid(row=3,column=0,sticky='w')
        discussion_label.grid(row=4,column=0,sticky='w')
        PSS_label.grid(row=5,column=0,sticky='w')
        class_label.grid(row=6,column=0,sticky='w')
    #定义“选择目录”函数
    def outputFile():
        outputFilePath = askdirectory()   # 选择目录，返回目录名
        outputpath.set(outputFilePath)   # 设置变量outputpath的值  
    #定义“保存文件”函数
    def fileSave():
        filenewpath = asksaveasfilename(defaultextension='.csv')   # 设置保存文件，并返回文件名
        filenewname.set(str(filenewpath))  # 设置变量filenewname的值
        outputplace=str(filenewpath)
        f=open(outputplace,'w', encoding='utf-8',newline='')
        csv_write = csv.writer(f)
        for row in excel_grade:
            curr = ','.join(map(str, row))
            curr=list(curr.split(','))
            csv_write.writerow(curr)
        f.close()
    #定义“退出程序”函数
    def quit_grade():
        window5.destroy()
    #界面初始化
    window5=tk.Tk()
    texttop=tk.Text(window5,height=8,width=16)
    window5.title("展示Section A, Section B, Section C三班级的成绩")
    window5.geometry('720x540')
    
    if flag1 or flag2 or flag3 or flag4 or flag5 or flag6 or flag7 or flag8 or flag9 or flag10 or flag11 or flag12 or flag_male or flag_female:
        global excel_grade
        #将需要输出的数据编排进列表中
        excel_grade=[['Title','Section A','Section A(Average Value)','Section B','Section B(Average Value)','Section C','Section C(Average Value)'],
                 ['Raisehands',raisehands[0],round(raisehands[0]/amt,2),raisehands[1],round(raisehands[1]/amt,2),raisehands[2],round(raisehands[2]/amt,2)],
                 ['Announcementsview',announcementsview[0],round(announcementsview[0]/amt,2),announcementsview[1],round(announcementsview[1]/amt,2),announcementsview[2],round(announcementsview[2]/amt,2)],
                 ['Visitedresources',visitedresources[0],round(visitedresources[0]/amt,2),visitedresources[1],round(visitedresources[1]/amt,2),visitedresources[2],round(visitedresources[2]/amt,2)],
                 ['Discussion',discussion[0],round(discussion[0]/amt,2),discussion[1],round(discussion[1]/amt,2),discussion[2],round(discussion[2]/amt,2)],
                 ['Classes(H/M/L)',str(classes[0])+str('/')+str(classes[1])+str('/')+str(classes[2]),'',str(classes[3])+str('/')+str(classes[4])+str('/')+str(classes[5]),'',str(classes[6])+str('/')+str(classes[7])+str('/')+str(classes[8]),''],
                 ['ParentschoolSatisfaction','Section A(Good)','Section A(Bad)','Section B(Good)','Section B(Bad)','Section C(Good)','Section C(Bad)'],
                 ['',PSS[0],PSS[1],PSS[2],PSS[3],PSS[4],PSS[5]]]
        #用于展示数据的函数
        g_show()
        #用于“保存文件”
        outputpath = tk.StringVar()
        filenewname = tk.StringVar()
        # 构建“选择目录”这一行的标签、输入框以及启动按钮
        tk.Label(window5, text='选择目录').grid(row=7, column=0, padx=5, pady=5,sticky='W')
        tk.Entry(window5, textvariable=outputpath).grid(row=7, column=0, padx=5, pady=5,)
        tk.Button(window5, text='点击选择', command=outputFile).grid(row=7, column=0, padx=5, pady=5,sticky='E')
        # 构建“保存文件”这一行的标签、输入框以及启动按钮
        tk.Label(window5, text='保存文件').grid(row=8, column=0, padx=5, pady=5,sticky='w')
        tk.Entry(window5, textvariable=filenewname).grid(row=8, column=0, padx=5, pady=5)
        tk.Button(window5, text='输入名称并保存', command=fileSave).grid(row=8, column=0, padx=5, pady=5,sticky='E')
        #构建“推出程序”按钮
        tk.Button(window5,text='退出程序',command=quit_grade).grid(row=9, column=0, padx=5, pady=5,sticky='w')
    else:#当没有数据时，输出此项
        var=StringVar()
        var_label=Label(window5,textvariable=var,relief=RIDGE)
        var.set('您所需要的班级数据因列表数据不足而无法提供')
        var_label.grid(row=0,column=0)

def jm6():
    #定义展示“相关系数”的函数
    def relation_show():
        var_raisedhands=StringVar()
        var_StudentAbsenceDays=StringVar()
        var_VisitedResources=StringVar()      
        var_gender=StringVar()
        var_relation=StringVar()
        var_AnnouncementsView=StringVar()
        var_Discussion=StringVar()   
        
        raisedhands_label=Label(window6,textvariable=var_raisedhands,relief=RIDGE)
        StudentAbsenceDays_label=Label(window6,textvariable=var_StudentAbsenceDays,relief=RIDGE)
        VisitedResources_label=Label(window6,textvariable=var_VisitedResources,relief=RIDGE)
        gender_label=Label(window6,textvariable=var_gender,relief=RIDGE)
        relation_label=Label(window6,textvariable=var_relation,relief=RIDGE)
        AnnouncementsView_label=Label(window6,textvariable=var_AnnouncementsView,relief=RIDGE)
        Discussion_label=Label(window6,textvariable=var_Discussion,relief=RIDGE)
        
        var_raisedhands.set('上课举手次数与成绩的相关系数：'+str(r_raisedhands))
        var_StudentAbsenceDays.set('缺勤次数与成绩的相关系数：'+str(r_StudentAbsenceDays))
        var_VisitedResources.set('浏览在线课件次数与成绩的相关系数：'+str(r_VisitedResources))   
        var_gender.set('性别与成绩的相关系数：'+str(r_gender))
        var_relation.set('父或母陪伴学习与成绩的相关系数：'+str(r_relation))
        var_AnnouncementsView.set('浏览学校公告次数与成绩的相关系数：'+str(r_AnnouncementsView))
        var_Discussion.set('参与课堂讨论次数与成绩的相关系数：'+str(r_Discussion))
        
        raisedhands_label.grid(row=0,column=0,sticky='w')
        StudentAbsenceDays_label.grid(row=1,column=0,sticky='w')
        VisitedResources_label.grid(row=2,column=0,sticky='w')
        gender_label.grid(row=3,column=0,sticky='w')
        relation_label.grid(row=4,column=0,sticky='w')
        AnnouncementsView_label.grid(row=5,column=0,sticky='w')
        Discussion_label.grid(row=6,column=0,sticky='w')
    #定义“选择目录”函数    
    def outputFile():        
        outputFilePath_r = askdirectory()   # 选择目录，返回目录名
        outputpath.set(outputFilePath_r)   # 设置变量outputpath的值 
    #定义“保存文件”函数
    def fileSave():
        filenewpath = asksaveasfilename(defaultextension='.csv')   # 设置保存文件，并返回文件名
        filenewname.set(str(filenewpath))  # 设置变量filenewname的值
        outputplace=str(filenewpath)
        f=open(outputplace,'w', encoding='utf-8',newline='')
        csv_write = csv.writer(f)
        for row in excel_r:
            curr = ','.join(map(str, row))
            curr=list(curr.split(','))
            csv_write.writerow(curr)
        f.close()
    #定义“退出程序”函数
    def quit_r():
        window6.destroy()

    global excel_r
    #将需要输出的数据编排进列表中    
    excel_r=[['Correlation Factor','r'],['Raisedhands',r_raisedhands],['StudentAbsenceDays',r_StudentAbsenceDays],
             ['VisitedResources',r_VisitedResources],['Gender',abs(r_gender)],['Relation',abs(r_relation)],
             ['AnnouncementsView',r_AnnouncementsView],['Discussion',r_Discussion]]
    #界面初始化
    window6=tk.Tk()
    texttop=tk.Text(window6,height=8,width=16)
    window6.title("成绩相关性展示")
    window6.geometry('720x540')
    #用于“保存文件”      
    outputpath = tk.StringVar()
    filenewname = tk.StringVar()
    # 构建“选择目录”这一行的标签、输入框以及启动按钮
    tk.Label(window6, text='选择目录').grid(row=7, column=0, padx=5, pady=5,sticky='W')
    tk.Entry(window6, textvariable=outputpath).grid(row=7, column=0, padx=5, pady=5,)
    tk.Button(window6, text='点击选择', command=outputFile).grid(row=7, column=0, padx=5, pady=5,sticky='E')
    # 构建“保存文件”这一行的标签、输入框以及启动按钮
    tk.Label(window6, text='保存文件').grid(row=8, column=0, padx=5, pady=5,sticky='w')
    tk.Entry(window6, textvariable=filenewname).grid(row=8, column=0, padx=5, pady=5)
    tk.Button(window6, text='输入名称并保存', command=fileSave).grid(row=8, column=0, padx=5, pady=5,sticky='E')
    tk.Button(window6,text='退出程序',command=quit_r).grid(row=9, column=0, padx=5, pady=5,sticky='w')
    #数据展示
    relation_show()
    
jm1()
