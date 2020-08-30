import codecademylib
from matplotlib import pyplot as plt
import numpy as np
#data
unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
As = [6, 3, 4, 3, 5]
Bs = [8, 12, 8, 9, 10]
Cs = [13, 12, 15, 13, 14]
Ds = [2, 3, 3, 2, 1]
Fs = [1, 0, 0, 3, 0]


#the bottom of c will be at the As + Bs, and so on and so forth for each other grade
c_bottom = np.add(As, Bs)
#create d_bottom and f_bottom here
d_bottom = np.add(c_bottom,Cs)
f_bottom = np.add(d_bottom,Ds)
#create your plot here
#create figure 
fig= plt.figure(figsize=(10,8))

#plot the grades on top of each other
plt.bar(range(len(unit_topics)),As)
plt.bar(range(len(unit_topics)),Bs,bottom =As)
plt.bar(range(len(unit_topics)),Cs,bottom =c_bottom)
plt.bar(range(len(unit_topics)),Ds,bottom =d_bottom)
plt.bar(range(len(unit_topics)),Fs,bottom =f_bottom)
#create axis object
ax = plt.subplot()
#set and label the xticks
ax.set_xticks(range(len(unit_topics)))
ax.set_xticklabels(unit_topics)
#title , label the axes , and create a legtend
plt.title('Grade Distribution')
plt.ylabel('Number of Students')
plt.xlabel('Unit')
plt.legend(['A','B','C','D','F'])
plt.savefig("my_stacked_bar.png")
plt.show()