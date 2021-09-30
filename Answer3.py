import pandas as pd

url = 'https://raw.githubusercontent.com/Bungeetech/internship-test2/master/input/question-3/main.csv'  
data = pd.read_csv(url)



a = data.sort_values(["Red Cards", "Yellow Cards"], ascending=False)
# a = list(a)
a[['Team','Red Cards','Yellow Cards']]