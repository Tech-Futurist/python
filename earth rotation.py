### radians is nothing but angle swapped by radius of circle in one second or dt amount of time
# One radian is the angle made at the center of a circle by an arc whose length is equal to the radius of the circle
####### shaftwidth = 0.5 is considered fine or amazing.

##### just add subtitle to the axis and planes and that it is moving about -x and +ve z axis.
### *********** try to add night sky view using canva scene or just create so many small balls which will look like star.
from vpython import *

# scene.background = color.white

earth = sphere(radius = 6.378e6) ########### 10e6 is same as e6
scene.title = ('Earth rotation')
earth.texture = textures.earth
axial_direction = cylinder(radius = 50000,axis = vector(4*6.378e6,0,0),pos= vector(-2*6.378e6,0,0) ,color = color.cyan)
equitorial_direction= cylinder(radius = 50000,axis = vector(0,4*6.378e6,0),pos = vector(0,-2*6.378e6,0),color= color.green ,opacity = 0.5)
oblique_direction= cylinder(radius = 50000,axis = vector(0,0,4*6.378e6),pos = vector(0,0,-2*6.378e6),color = color.red )
dt = 1000 # instantenous time
time_in_one_second = 24*60*60 # seconds
angular_speed = 2*pi/time_in_one_second
xy_plane = box(size = vector(4*6.378e6,4*6.378e6,0),opacity = 0.5)
# xyz_plane = box(size = vector(4*6.378e6,4*6.378e6,4*6.378e6),opacity = 0.5,color = color.orange) # it form a 3d square.
# yz_plane = box(size = vector(0,4*6.378e6,4*6.378e6),opacity = 0.5,color= color.red)### why I am unable to form the yz plane.

xz_plane = box(size = vector(4*6.378e6,0,4*6.378e6), opacity = 0.5)
# angular_speed_vector = arrow(shaftwidth = 0.5,color = color.red ,pos =vector(3*earth.radius,0,0) )
while(True):
    rate(100)
    # earth.rotate(angle = angular_speed*dt,axis = vector(0,40,40))#### unable to fix the exact angle or close to exact angle.
    earth.rotate(angle = angular_speed*dt,axis = vector(-40,0,40))#### unable to fix the exact angle or close to exact angle.

    # angular_speed_vector.pos = vector(3*earth.radius,0,0)
    # angular_speed_vector.axis = vector(0,angular_speed/1000,0)
