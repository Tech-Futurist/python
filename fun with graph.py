
"""sample of how to make a graph using numpy to take datasets
f1 = gcurve(color = color.cyan)
for x in arange(0,8.05,0.1):
    f1.plot(x,5*cos(2*x)*exp(-0.2*x))"""


# it just stop atlast but it must not be the case coz in order to stop it will take time otherwise you will face an accident.
### means it will decelerate first then will stop.

# using graph() you just give the parameters like its title , size basically the structure.
# using gcurve() , here you give above graph as parameter and color by which we wanna draw this graph.
# plot() , in plot() we give the actual point of x and y axis that we want to draw.
#  Which will be inside the while loop or one by one point draw karega.

# position time graph of non-uniform velocity
#
# for making velocity vs time graph , just change the pos to velocity and specified velocity to the ball i.e. redball.velocity
## and it will be a straight line coz speed is increasing continously.

from vpython import *
scene.height =200
scene.range = 20
redBall = sphere(color = color.red , radius = 0.5)
greenball = sphere(color = color.green , pos = vector(0,2,0))

time = 0.0
dt = 0.01
redBall.speed = 10# 0.2 original # if it is 0.5 then your slope will be larger from the initial itself and it means that you are covering more distance in a less amount of time.
acc = 0.6 ## if acceleration is large , it just mean that uski speed jyada jaldi increase ho jaayegi.

myGraph = graph(xtitle = "Time[s]", ytitle = "Position [m]",height = 250 ,title = "position time graph of non- uniform velocity ")
myPlot = gcurve(graph = myGraph,color = color.red)

while(time < 8.0):
    rate(100)
    # redBall.pos.x = redBall.pos.x - speed*dt # it means -ve direction main move karke decelerate ho raha hai.
    redBall.pos.x = redBall.pos.x + redBall.speed*dt
    # speed = speed - acc*dt# it means decelerate hokar stop hua hai.
    redBall.speed = redBall.speed + acc * dt
    time = time + dt
# #
# # # # here by changing x to y it just changes the motion graph is same

    myPlot.plot(time,redBall.speed)  # it is taking two coordinates coz you are making graph in 2d  and so it takes two parameter.

#### velocity vs time graph




# position time graph of uniform velocity

# from vpython import *
#
# scene.height = 100
# scene.range = 10
# redball = sphere(color = color.red, radius = 0.5)
# greenball = sphere(color = color.green , pos = vector(0,2,0))
#
# time = 0.0
# dt = 0.01
# velocity = 0.5 # m/s
# mygraph = graph(title = "Uniform velocity graph", xtitle = "Position[m]", ytitle = "Time[s]")
# myPlot = gcurve(color = color.blue, graph = mygraph)
#
# while(time < 15.0):
#     rate(100)
#     redball.pos.x = redball.pos.x + velocity*dt
#     time = time + dt
#     myPlot.plot(time , redball.pos.x )









