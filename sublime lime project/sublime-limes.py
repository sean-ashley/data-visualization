
import codecademylib
from matplotlib import pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

visits_per_month = [9695, 7909, 10831, 12942, 12495, 16794, 14161, 12762, 12777, 12439, 10309, 8724]




# numbers of limes of different species sold each month
key_limes_per_month = [92.0, 109.0, 124.0, 70.0, 101.0, 79.0, 106.0, 101.0, 103.0, 90.0, 102.0, 106.0]
persian_limes_per_month = [67.0, 51.0, 57.0, 54.0, 83.0, 90.0, 52.0, 63.0, 51.0, 44.0, 64.0, 78.0]
blood_limes_per_month = [75.0, 75.0, 76.0, 71.0, 74.0, 77.0, 69.0, 80.0, 63.0, 69.0, 73.0, 82.0]


# create your figure here
#Create a figure of width 12 and height 8.
fig = plt.figure(figsize= (12,8))
ax1 = plt.subplot(1,2,1)
x_values = range(len(months))
#plot website visits vs month of visit
ax1.plot(x_values,visits_per_month,marker = 'o')
#label axes
plt.xlabel('Month')
plt.ylabel('Visits')
#change x ticks to months
ax1.set_xticks(x_values)
#change x tick labels to month names
ax1.set_xticklabels(months)
#title the plot
plt.title('Website Visits vs Month')
#define second subplot
ax2 = plt.subplot(1,2,2)
#plot all 3 types of lime sales vs month
ax2.plot(x_values,key_limes_per_month,color = 'purple',marker = 'v')
ax2.plot(x_values,persian_limes_per_month,color = 'blue',marker = '1')
ax2.plot(x_values,blood_limes_per_month,color = 'red',marker = '*')
#create a legend with all 3 limes 
ax2.legend(['Key Limes','Persian Limes','Blood Limes'])
#label axes
plt.xlabel('Month')
plt.ylabel('Sales')
#change x ticks to month values and label as month names
ax2.set_xticks(x_values)
ax2.set_xticklabels(months)
#title the second subplot
plt.title('Lime Sales (per type) vs Month')
#save the figure as a png
plt.savefig('Sublime_Limes_visit_and_sale_graphs.png')
plt.show()
