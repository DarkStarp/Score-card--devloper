import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from reportlab.platypus import Paragraph,SimpleDocTemplate,Table,TableStyle,Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import letter
from reportlab.graphics.shapes import Drawing
from reportlab.lib import colors
from reportlab.graphics.charts.barcharts import(VerticalBarChart)
from reportlab.graphics.charts.piecharts import(Pie)
from reportlab.graphics.shapes import String
from reportlab.graphics.charts.legends import Legend
from reportlab.lib.colors import Color, PCMYKColor
from reportlab.graphics.shapes import Drawing, _DrawingEditorMixin
from reportlab.lib.colors import black, red, purple, green, maroon, brown, pink, white, HexColor
from reportlab.lib.validators import Auto
pd.set_option("max_rows", None)
pd.set_option('max_columns', None)
df=pd.read_csv(r'file\pop.csv',header=3)
df['What you marked'].fillna(9999999,inplace=True)
#df=df.drop([50,51,52,53,54,55])
df.dropna(axis=1,inplace=True)
df=df.replace(to_replace =[9999999],value=" ")  
pd.set_option("max_rows", None)
pd.set_option('max_columns', None)
selected_columns=df[['Student No ','Name of Candidate','Registration','Grade ','Gender','Name of school ','Date of Birth ', 
'City of Residence','Date and time of test','Country of Residence','Extra time assistance','Score if correct','Score if incorrect']]
df2= selected_columns.copy()   
for i in range(0,100):
    if i%5!=0:
        df2= df2.drop(i) 
df2=df2.reset_index()
Attempt_status_q1=[]
Attempt_status_q2 = []
Attempt_status_q3=[]
Attempt_status_q4=[]
Attempt_status_q5=[]
j=0
for i in range (0,100):
    if j==0:
        Attempt_status_q1.append(df._get_value(i,15,takeable=True))
        j=1
        continue
    if j==1:
        Attempt_status_q2.append(df._get_value(i,15,takeable=True))
        j=2
        continue
    if j==2:
        Attempt_status_q3.append(df._get_value(i,15,takeable=True))
        j=3
        continue
    if j==3:
        Attempt_status_q4.append(df._get_value(i,15,takeable=True))
        j=4
        continue
    if j==4:
        Attempt_status_q5.append(df._get_value(i,15,takeable=True))
        j=0
        continue
df2=df2.assign(**{'Attempt_status_q1' :Attempt_status_q1 , 'Attempt_status_q2' : Attempt_status_q2,'Attempt_status_q3':Attempt_status_q3,
             'Attempt_status_q4':Attempt_status_q4,'Attempt_status_q5':Attempt_status_q5})

What_you_marked_q1=[]
What_you_marked_q2=[]
What_you_marked_q3=[]
What_you_marked_q4=[]
What_you_marked_q5=[]
j=0
for i in range (0,100):
    if j==0:
        What_you_marked_q1.append(df._get_value(i,16,takeable=True))
        j=1
        continue
    if j==1:
        What_you_marked_q2.append(df._get_value(i,16,takeable=True))
        j=2
        continue
    if j==2:
        What_you_marked_q3.append(df._get_value(i,16,takeable=True))
        j=3
        continue
    if j==3:
        What_you_marked_q4.append(df._get_value(i,16,takeable=True))
        j=4
        continue
    if j==4:
        What_you_marked_q5.append(df._get_value(i,16,takeable=True))
        j=0
        continue
df2=df2.assign(**{'What_you_marked_q1' :What_you_marked_q1 , 'What_you_marked_q2' : What_you_marked_q2,'What_you_marked_q3':What_you_marked_q3,
             'What_you_marked_q4':What_you_marked_q4,'What_you_marked_q5':What_you_marked_q5})

Correct_Answer_q1=[]
Correct_Answer_q2=[]
Correct_Answer_q3=[]
Correct_Answer_q4=[]
Correct_Answer_q5=[]
j=0
for i in range (0,100):
    if j==0:
        Correct_Answer_q1.append(df._get_value(i,17,takeable=True))
        j=1
        continue
    if j==1:
        Correct_Answer_q2.append(df._get_value(i,17,takeable=True))
        j=2
        continue
    if j==2:
        Correct_Answer_q3.append(df._get_value(i,17,takeable=True))
        j=3
        continue
    if j==3:
        Correct_Answer_q4.append(df._get_value(i,17,takeable=True))
        j=4
        continue
    if j==4:
        Correct_Answer_q5.append(df._get_value(i,17,takeable=True))
        j=0
        continue
df2=df2.assign(**{'Correct_Answer_q1' :Correct_Answer_q1 , 'Correct_Answer_q2' :Correct_Answer_q2,'Correct_Answer_q3':Correct_Answer_q3,
             'Correct_Answer_q4':Correct_Answer_q4,'Correct_Answer_q5':Correct_Answer_q5})
Outcome_q1=[]
Outcome_q2=[]
Outcome_q3=[]
Outcome_q4=[]
Outcome_q5=[]
j=0
for i in range (0,100):
    if j==0:
        Outcome_q1.append(df._get_value(i,18,takeable=True))
        j=1
        continue
    if j==1:
        Outcome_q2.append(df._get_value(i,18,takeable=True))
        j=2
        continue
    if j==2:
        Outcome_q3.append(df._get_value(i,18,takeable=True))
        j=3
        continue
    if j==3:
        Outcome_q4.append(df._get_value(i,18,takeable=True))
        j=4
        continue
    if j==4:
        Outcome_q5.append(df._get_value(i,18,takeable=True))
        j=0
        continue
df2=df2.assign(**{'Outcome_q1' :Outcome_q1 , 'Outcome_q2' :Outcome_q2,'Outcome_q3':Outcome_q3,
             'Outcome_q4':Outcome_q4,'Outcome_q5':Outcome_q5})
Your_score_q1=[]
Your_score_q2=[]
Your_score_q3=[]
Your_score_q4=[]
Your_score_q5=[]
j=0
for i in range (0,100):
    if j==0:
        Your_score_q1.append(df._get_value(i,19,takeable=True))
        j=1
        continue
    if j==1:
        Your_score_q2.append(df._get_value(i,19,takeable=True))
        j=2
        continue
    if j==2:
        Your_score_q3.append(df._get_value(i,19,takeable=True))
        j=3
        continue
    if j==3:
        Your_score_q4.append(df._get_value(i,19,takeable=True))
        j=4
        continue
    if j==4:
        Your_score_q5.append(df._get_value(i,19,takeable=True))
        j=0
        continue
df2=df2.assign(**{'Your_score_q1' :Your_score_q1 , 'Your_score_q2' :Your_score_q2,'Your_score_q3':Your_score_q3,
             'Your_score_q4':Your_score_q4,'Your_score_q5':Your_score_q5})
Time_Spent_on_question_q1=[]
Time_Spent_on_question_q2=[]
Time_Spent_on_question_q3=[]
Time_Spent_on_question_q4=[]
Time_Spent_on_question_q5=[]
j=0
for i in range (0,100):
    if j==0:
        Time_Spent_on_question_q1.append(df._get_value(i,12,takeable=True))
        j=1
        continue
    if j==1:
        Time_Spent_on_question_q2.append(df._get_value(i,12,takeable=True))
        j=2
        continue
    if j==2:
        Time_Spent_on_question_q3.append(df._get_value(i,12,takeable=True))
        j=3
        continue
    if j==3:
        Time_Spent_on_question_q4.append(df._get_value(i,12,takeable=True))
        j=4
        continue
    if j==4:
        Time_Spent_on_question_q5.append(df._get_value(i,12,takeable=True))
        j=0
        continue
df2=df2.assign(**{'Time_Spent_on_question_q1' :Time_Spent_on_question_q1 , 'Time_Spent_on_question_q2' :Time_Spent_on_question_q2,'Time_Spent_on_question_q3':Time_Spent_on_question_q3,
             'Time_Spent_on_question_q4':Time_Spent_on_question_q4,'Time_Spent_on_question_q5':Time_Spent_on_question_q5})
pd.set_option("max_rows", None)
pd.set_option('max_columns', None)

df2=df2.drop(["index"], axis=1)

convert_dict = {'Registration': int, 
                'Grade ': int,
                'Student No ':int,
                'Score if correct':int,
                'Score if incorrect':int,
                'Your_score_q1':int,
                'Your_score_q2':int,
                'Your_score_q3':int,
                'Your_score_q4':int,
                'Your_score_q5':int,
                'Time_Spent_on_question_q1':int,
                'Time_Spent_on_question_q2':int,
                'Time_Spent_on_question_q3':int,
                'Time_Spent_on_question_q4':int,
                'Time_Spent_on_question_q5':int,
                
               }
  
df2 = df2.astype(convert_dict) 

l=[]
for j in range(0,20):
    a=df2.iloc[j,33]
    b=df2.iloc[j,34]
    c=df2.iloc[j,35]
    d=df2.iloc[j,36]
    e=df2.iloc[j,37]
    t=a+b+c+d+e
    l.append(t)
u=0
asd=[]
for k in range(0,20):
    for j in l:
        if l[k]>j:
            u=u+1
    d=u*100/20
    asd.append(d)
    u=0
df2['percentile']=asd

for i in range(0,20):
    performance = pd.DataFrame()
    Question=['Question No.','Q1','Q2','Q3','Q4','Q5']
    Time_Spent_on_Question = ['Time Spent (sec)']
    Score_if_Correct = ['Score if Correct',2,2,2,2,2]
    Score_if_Incorrect = ['Score if Incorrect',-1,-1,-1,-1,-1]
    Attempt_Status = ['Attempt Status']
    What_You_Marked = ['What You Marked']
    Correct_Answer = ['Correct Answer']
    Outcome = ['Outcome']
    Your_Score = ['Your Score']
    tq = 38
    ats = 13
    wym = 18
    caa = 23
    ot = 28
    ysa = 33
    for j in range(0,5):
        Time_Spent_on_Question.append(df2._get_value(i,tq,takeable=True))
        Attempt_Status.append(df2._get_value(i,ats,takeable=True))
        What_You_Marked.append(df2._get_value(i,wym,takeable = True))
        Correct_Answer.append(df2._get_value(i,caa,takeable = True))
        Outcome.append(df2._get_value(i,ot,takeable = True))
        Your_Score.append(df2._get_value(i,ysa,takeable = True))
        tq=tq+1
        ats=ats+1
        wym=wym+1
        caa=caa+1
        ot=ot+1
        ysa=ysa+1
        
    performance = performance.assign(**{'Question No.':Question,'Time Spent (sec)':Time_Spent_on_Question,'Score if Correct':Score_if_Correct,'Score if Incorrect': Score_if_Incorrect, 'Attempt Status':Attempt_Status,
                                        'What you Marked': What_You_Marked, 'Correct Answer':Correct_Answer, 'Outcome':Outcome,'Your_Score':Your_Score})
    
    poi = []
    poiuy = []
    poi.append(df2._get_value(i,1,takeable = True))
    poi.append(df2._get_value(i,3,takeable = True))
    poi.append(df2._get_value(i,5,takeable = True))
    poi.append(df2._get_value(i,7,takeable = True))
    poi.append(df2._get_value(i,9,takeable = True))
    poiuy.append(df2._get_value(i,2,takeable = True))
    poiuy.append(df2._get_value(i,4,takeable = True))
    poiuy.append(df2._get_value(i,6,takeable = True))
    poiuy.append(df2._get_value(i,8,takeable = True))
    poiuy.append(df2._get_value(i,10,takeable = True))
    lst = [['Name of Candidate', 'Grade','School Name','City of Residence','Country of Residence'],poi,['Registration No.','Gender','Date of Birth','Date of test','Extra time assistance'],poiuy]
    details=pd.DataFrame(lst)
    details =details.T

    qwe=str(i)
    qwe=qwe+'.pdf'
    
    pdf=SimpleDocTemplate(qwe,pagesize=letter, rightMargin=30,leftMargin=30, topMargin=5,bottomMargin=18)
    #pdf.translate(inch,inch)
    flow_obj=[]
    dataa = [['Report Card']]
    t=Table(dataa)
    style=TableStyle([('TEXTCOLOR',(0,0),(-1,-1),colors.red),('FONTNAME',(0,0),(-1,-1),'Courier-Bold'),('ALIGN',(0,0),(-1,-1),'CENTER'),('FONTSIZE',(0,0),(-1,-1),30),('BOTTOMPADDING',(0,0),(-1,-1),20)] )
    t.setStyle(style)
    kl= 'pics' + "\\" + str(i+1)
    # kl = kl + str(i+1)
    kl=kl+'.jpg'
    #gh='C:\Users\hp\Downloads\Pics\Pics\'+kl+'.jpg'
    im = Image(r'pics\logo.png',100,100)
    m = Image(kl,100,120)
    T=Table([[im,m]],colWidths=[335,230])
    sst = TableStyle([('ALIGN',(0,0),(-1,-1),'RIGHT'),('BOTTOMPADDING',(0,0),(-1,-1),22)])
    T.setStyle(sst)


    Tab = Table(np.array(details).tolist())
    st = TableStyle([('ALIGN',(0,0),(-1,-1),'LEFT'),('FONTNAME',(0,0),(0,-1),'Times-BoldItalic'),('FONTSIZE',(0,0),(-1,-1),11),('FONTNAME',(2,0),(2,-1),'Times-BoldItalic'),('BOTTOMPADDING',(0,0),(-1,-1),10),
                    ('TOPPADDING',(0,0),(-1,-1),14),('LEFTPADDING',(0,0),(-1,-1),55),('BOX',(0,0),(-1,-1),2,colors.black),('RIGHTPADDING',(0,0),(-1,-1),45),('BOX',(0,0),(1,-1),2,colors.black)])
    Tab.setStyle(st)


    tab1 = Table([['Student Performance']])
    style4 = TableStyle([('FONTNAME',(0,0),(-1,-1),'Courier-Bold'),('FONTSIZE',(0,0),(-1,-1),16), ('TOPPADDING',(0,0),(-1,-1),25),('TEXTCOLOR',(0,0),(-1,-1),colors.orange),('BOTTOMPADDING',(0,0),(-1,-1),25)])
    tab1.setStyle(style4)


    tab2 = Table(np.array(performance).tolist())
    style5 = TableStyle([('ALIGN',(0,0),(-1,-1),'CENTER'),('FONTNAME',(0,0),(-1,0),'Times-BoldItalic'),('FONTSIZE',(0,0),(-1,-1),8.5),('TOPPADDING',(0,0),(-1,-1),15),('BOX',(0,0),(-1,-1),1.5,colors.black),('BOTTOMPADING',(0,0),(-1,-1),50),
                    ('GRID',(0,1),(-1,-1),2,colors.black),('BACKGROUND',(0,0),(8,0),colors.green) ])
    tab2.setStyle(style5)
    rownum = len(performance)
    for k in range(1, rownum):
        if k%2 == 0:
            bc = colors.burlywood
        else:
            bc = colors.beige
        ts = TableStyle([('BACKGROUND',(0,k),(-1,k),bc)])
        tab2.setStyle(ts)

        

    tab3 = Table([['']])
    style6 = TableStyle([('BACKGROUND',(0,0),(-1,-1),colors.transparent),('TOPPADDING',(0,0),(-1,-1),10),('BOTTOMPADDING',(0,0),(-1,-1),10)])
    tab3.setStyle(style6)


    a=df2.iloc[i,33]
    b=df2.iloc[i,34]
    c=df2.iloc[i,35]
    d=df2.iloc[i,36]
    e=df2.iloc[i,37]
    tosc=a+b+c+d+e
    #total score
    ds=df2.iloc[i,43]


    tab4 = Table([['Total Score',tosc],['Your Overall\n Percentile',ds]],colWidths = [100,100])
    style7 = TableStyle([('BACKGROUND',(0,0),(-1,-1),colors.pink),('TOPPADDING',(0,0),(-1,-1),10),('BOTTOMPADDING',(0,0),(-1,-1),10),('LEFTPADDING',(0,0),(-1,-1),40),('RIGHTPADDING',(0,0),(-1,-1),1)])
    tab4.setStyle(style7)


    flow_obj.append(t)
    flow_obj.append(T)
    flow_obj.append(Tab)
    flow_obj.append(tab1)
    flow_obj.append(tab2)
    flow_obj.append(tab3)
    flow_obj.append(tab4)
    pdf.build(flow_obj)
