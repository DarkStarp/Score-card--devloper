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

