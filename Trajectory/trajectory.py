#Imports
import matplotlib.pyplot as plt

#Variables
g = -9.8
axisY = []

#Functions 
def sy(b, t): #Given an initial velocity and a time,  find how high the particle is. 
    global g
    height = b*t + 0.5*g*t**2
    print('Height is: ', height, 'm')
    return height

def sx(q, t): #Given an initial velocity and a time,  find how far the particle is from the starting point. 
    global g
    print('Distance in the x axis from the starting point is: ', q*t, 'm')

def vy(b, t): #Given an initial velocity and a time, find the velocity in the y axis
    global g
    print('Velocity in the y axis is: ', b + g*t, 'm/s')

def vx(q, t): #Given an initial velocity and a time, find the velocity in the x axis
    global g
    print('Velocity at any time is: ', q, 'm/s')

def range(b, q): #Given initial velocity in both x and y axis, find the range
    t = -((b*2)/-9.8)
    print('Particle will land on floor after ', t, ' seconds')
    print('The range of the particle is: ', q*t, 'm')

def highPoint(b): #Highest point
    global g

    t = b/-(g)
    print(t)

    print('Highest point is: ', b*t + 0.5*g*t**2, ' m')

def maxTime(b): #time when sy = 0
    return b/4.9
def plotting(b, t):
    return b*t + 0.5*g*t**2

#Run code
print('By entering the initial speed in the x and y axis, you can find the highest point, the range, velocity in the x and y axis at any given time and range at any given time in both the x and y axis')
q = float(input('Enter x axis initial speed: '))
b = float(input('Enter y axis initial speed: '))
t = float(input('Enter time: '))

print('')
print('')

print('After ', t, ' seconds: ')
sy(b, t)
sx(q, t)
vy(b, t)
vx(q, t)
print('')
range(b, q)
highPoint(b)

#Pot sy

landTime = maxTime(b)
i = 0
while i < landTime:
    axisY.append(plotting(b, i))
    i = i + 0.1


plt.plot(axisY)
plt.ylabel('Height in meters')
plt.xlabel('Time in seconds')
plt.show()
