# AIM- make an Pie chart and plot hours spent in different things during the day

# importing the required module
import matplotlib.pyplot as plt

days = [1,2,3,4,5,6,7]
	
# different activities you do during the day and number of hours spent on them per day
activities='sleep','reading','leisure','excercising','At work','eating'

hours=[8,1,4,1,8,2]              #respective hours
#you can also use a dictionary and use keys and values function for specifying them later on in code.


# plotting the points, give appropriate labels
fig1, ax1 = plt.subplots()
ax1.pie(hours,labels=activities,shadow=True)	


# giving a title to my graph
ax1.set_title('Everyday Activities')	

# function to show the plot
plt.show()


#print your name , college name , year of graduation at the end of the program
print('Tarun Sevada , IIT BHU , Year of Graduation: 2024 ')
