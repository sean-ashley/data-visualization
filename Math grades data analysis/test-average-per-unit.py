import codecademylib
from matplotlib import pyplot as plt
#data
unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
middle_school_a = [80, 85, 84, 83, 86]
middle_school_b = [73, 78, 77, 82, 86]
#create lists to make multiple bars per unit on bar graph
#t = number of datasets
#w = bar width
#n = which set of data we are on
#d = the number of data points
def create_x(t, w, n, d):
    return [t*x + w*n for x in range(d)]
# Make your chart here

#create both x values for the bar graphs
school_a_x = create_x(2,0.8,1,5)
school_b_x = create_x(2,0.8,2,5)
#create 10x8 figure
fig = plt.figure(figsize = (10,8))
#create axis object
ax = plt.subplot()
#plot both school bar graphs
plt.bar(school_a_x,middle_school_a)
plt.bar(school_b_x,middle_school_b)
#calculate middle point between both x values for tick values
middle_x = [(a+b)/2.0 for a,b in zip(school_a_x,school_b_x)]
#set x ticks to that middle index and the tick labels to the unit names
ax.set_xticks(middle_x)
ax.set_xticklabels(unit_topics)
#create legend and titles
plt.legend(['Middle School A','Middle School B'])
plt.title("Test Averages on Different Units")
plt.xlabel('Unit')
plt.ylabel('Test Average')
plt.savefig('my_side_by_side.png')
plt.show()