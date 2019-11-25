# Space-Simulation

![Sun and 3 Planets](https://media.giphy.com/media/iI4EpDohs3jDcW0CWM/giphy.gif)
<br>A simplified simulation of our solar system where the only forces at work are those between the sun and the individual space object.


Create new Spaceobjects and insert them into the space_object_list in main() to add them to the simulation:

```
meteor1 = Space.Spaceobject(name="Meteor1", location=[100. * 10 ** 9, 100. * 10 ** 9, 0], velocity=[-20000 / 3.6, -1948 / 3.6, 0], color="red")

meteor2 = Space.Spaceobject(name="Meteor2", location=[-100. * 10 ** 9, 70. * 10 ** 4, 0], velocity=[20000 / 3.6, -19548 / 3.6, 0], color="black")
                           
space_object_list = [meteor1, meteor2]                                              
```

When executing main(), you can zoom by clicking and moving your right mouse button. 
