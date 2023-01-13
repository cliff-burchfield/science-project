# # importing the required module
# import matplotlib.pyplot as plt
  
# # x axis values
# x = range(1,10)

x2 = range(1,10)
y2 = [1,4,2,3,7,5,1,9,6]
# corresponding y axis values
y = range(1,10)
  
# # plotting the points 
# plt.plot(x, y, label='Average')
# plt.plot(x2,y2,label='Best')
# # naming the x axis
# plt.xlabel('x - axis')
# # naming the y axis
# plt.ylabel('y - axis')
  
# # giving a title to my graph
# plt.title('My first graph!')
  
# # function to show the plot
# plt.legend(loc='upper left')
# plt.show()

from matplotlib import pyplot as plt

plt.figure("Welcome to figure 1")
plt.plot(x2,y2)
plt.figure("Welcome to figure 2")
plt.plot([11, 13, 41])

plt.show()