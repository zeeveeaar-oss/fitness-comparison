import matplotlib.pyplot as plt
import seaborn as sns

Ramesh = [168, 60 ]
Sandeep = [169, 68 ]
type = ['Ramesh','Sandeep']
color = ['b','r']
label = ['Ramesh', 'Sandeep']
plt.title('fitness comparision')
plt.xlabel('Person')
plt.ylabel('weight')
plt.bar(type, label=label, color=color, width=0.94, orientation = 'vertical', height = [Ramesh[1], Sandeep[1]])
plt.legend()
plt.show()