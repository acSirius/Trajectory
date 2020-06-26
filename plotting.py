#imports
import matplotlib.pyplot as plt

#variables
g = -9.8
landTime = 0

axisY = []

#y axis is height, x axis is height
def sy(b, t): #x axis to plot
    global g
    height = (b*t + 0.5*g*t**2)
    print(height)
    return height

def maxTime(b): #time when sy = 0
    return b/4.9

landTime = maxTime(28)


i = 0
while i < landTime:
    axisY.append(sy(28, i))
    i = i + 0.1


#plot
plt.plot(axisY)
plt.ylabel('some numbers')
plt.show()
print(axisY)