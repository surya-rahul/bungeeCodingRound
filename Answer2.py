import pandas as pd

url = 'https://raw.githubusercontent.com/Bungeetech/internship-test2/master/input/question-2/main.csv'
data = pd.read_csv("main.csv")

data.groupby('occupation').agg({'age': ['max','min']})
