
from matplotlib import pyplot as plt
#data tables
past_years_averages = [82, 84, 83, 86, 74, 84, 90]
years = [2000, 2001, 2002, 2003, 2004, 2005, 2006]
error = [1.5, 2.1, 1.2, 3.2, 2.3, 1.7, 2.4]

# Make your chart here
#create a 10x8 figure
fig= plt.figure(figsize = (10,8))
#create bar graph with error lines 
plt.bar(range(len(past_years_averages)),past_years_averages,yerr = error,capsize = 5)
#limit x and y axes
plt.xlim(-0.5,6.5)
plt.ylim(70,95)
#create axis object
ax = plt.subplot()
#set x ticks and labels to years
ax.set_xticks(range(len(years)))
ax.set_xticklabels(years)
#title graph and axes
plt.title('Final Exam Averages')
plt.xlabel('Year')
plt.ylabel('Test Average')
#save the figure
plt.savefig('my_bar_chart.png')
plt.show()
