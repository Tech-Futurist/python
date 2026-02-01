### when to use the .equals() method specifically. to compare to objects 

###### in free fall if there is no friction then it will reach at the same height ,
# but if you are providing some velocity then it will move above the position you had started.
# then why at here it is not moving the position above it like has the initial velocity.
# may be coz here there is no deformation so may be
# or may be I am wrong coz then how it will move , I have to add the deformation.
# ceiling doesn't make any sense like ball is moving in the influence of gravity.
#
####### Ball falling in the influence of gravity having some velocity.
#
from vpython import *

scene.range = 20
red_ball = sphere(color = color.red , make_trail = True )
# ceiling = box(pos = vector(40,0.8,0),size = vector(100,0.5,10) , color = color.blue)
Floor = box(pos = vector(40,-8,0),size = vector(100,0.5,10))

dt = 0.01
time = 0.0
velocity = vector(5,0,0)
acceleration = vector(0,-9.8,0)
vec_arrow = arrow(color = color.blue, shaftwidth = 0.5)
# sleep(1)
while(time < 10.0):
    rate(1/dt)## 100 loops per second according to dt which is kind of nearly to normal.

    red_ball.pos = red_ball.pos + velocity * dt
    velocity = velocity + acceleration * dt
    vec_arrow.pos = red_ball.pos
    vec_arrow.axis = velocity
    if red_ball.pos.y < Floor.pos.y:
    # if red_ball.pos.equals(Floor.pos):# just trying
        ### why red_ball.pos.y == Floor. pos.y is reduntant means it won't do anything. Like here above you don't have to put <=
        # print(red_ball.pos)
        # print("velocity is ",velocity)
        velocity.y = velocity.y*-1
        if (red_ball.color.equals(color.red)):
            red_ball.color = color.blue
        elif (red_ball.color.equals(color.blue)):
            red_ball.color = color.green
        else:
            red_ball.color = color.red

    time = time + dt


########## Free fall of a ball and it's bounce back
## but it's not like the actual one coz it depend on time to stop and there are other things so it is not seem like actual physics
# from vpython import *
#
# scene.range = 20
# red_ball = sphere(color = color.red , make_trail = True )
# Floor = box(pos = vector(0,-10,0),size = vector(10,0.5,10), color = color.blue)
#
# dt = 0.01
# time = 0.0
# velocity = vector(0,0,0)
# acceleration = vector(0,-9.8,0)
# while (time<10.0):
#     rate(1/dt)
#     red_ball.pos = red_ball.pos + velocity *dt
#     velocity = velocity + acceleration*dt
#
#     if red_ball.pos.y < Floor.pos.y:
### why red_ball.pos.y == Floor.pos.y is reduntant means it won't do anything. Like here above you don't have to put <=
#         velocity = velocity * -1
#
#     time = time + dt



