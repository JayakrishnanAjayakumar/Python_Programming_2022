from ipywidgets import widgets
import pandas as pd

class QuestionWidgetHelper:
    def __init__(self,qNo):
        self.qNo = qNo
        data = pd.read_csv('qtest.csv')
        question = data.loc[data.qNo==self.qNo]
        choice = question.Values.values[0].split('|')
        self.qWidget = widgets.RadioButtons(
            options=choice,
            value = choice[question.Answer.values[0]],
            description='Your Answer:',
            disabled=False
        )
        self.qWidget.observe(self.valueChanged, names=['value'])
    
    def valueChanged(self,changed):
        data = pd.read_csv('qtest.csv')
        question = data.loc[data.qNo==self.qNo]
        choice = question.Values.values[0].split('|')
        data.loc[data.qNo==self.qNo,'Answer'] = choice.index(changed['new'])
        data.to_csv('qtest.csv',index=False)
        
    def display(self):
        return self.qWidget