import datetime

current_time = datetime.datetime.now()

formatted = current_time.strftime("%Y-%m-%d %H:%M:%S")

print(formatted)

class test:
    def __init__(self):
        a = int(input())
        b = int(input())
        print(a+b)

#a = test()


import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
print(y)
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.show() 