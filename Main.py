import Space
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as anim


# The Interval in seconds, for which each new position of a planet get calculated. The smaller, the more accurate.
D_TIME = 100


def _append_locations(space_object_ist, iterations, step=250):
    """
    Creates a list of coordinates for each object in space_object_list for later plotting
    :param space_object_ist: filled with class objects from Space.Spaceobject
    :param iterations: amount of new positions calculated. The higher, the more time it takes to calculate.
    :param step: To save time and memory while plotting, it appends only every 'step'(default=250th) location.
    :return: three lists (x, y, z) with calculated coordinates of all objects
    """

    x = [[i.location[0] for i in space_object_ist]]
    y = [[i.location[1] for i in space_object_ist]]
    z = [[i.location[2] for i in space_object_ist]]

    for i in range(iterations):
        for body in space_object_ist:
            body.update_obj()
        if i % step == 0:
            x.append([body.location[0] for body in space_object_ist])
            y.append([body.location[1] for body in space_object_ist])
            z.append([body.location[2] for body in space_object_ist])

    return x, y, z


def show_plot(space_object_list, iterations=10 ** 5, save=None):
    """
    Plots the Space objects in an animated 3d graph.
    :param space_object_list: filled with class objects from Space.Spaceobject
    :param iterations: amount of new positions calculated. The higher, the more time it takes to calculate.
    :param save: enter name of the file to save it in current directory
    """

    # Setting up figure
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111, projection="3d")
    ax.set_xlabel("x (in m)")
    ax.set_ylabel("y (in m)")
    ax.set_zlabel("z (in m)")

    # x,y,z limits of graph
    graph_size = max([max(obj.location) for obj in space_object_list])
    xmin, xmax = -graph_size, +graph_size
    ax.set_xlim([xmin, xmax])
    ax.set_ylim([xmin, xmax])
    ax.set_zlim([xmin, xmax])

    # Plotting sun
    ax.scatter(0, 0, 0, c="#e6ac00", s=15)

    # Scatter and line plot
    x, y, z = _append_locations(space_object_list, iterations=iterations)
    sc = ax.scatter(x[0], y[0], z[0], c=[body.color for body in space_object_list], depthshade=0)

    # Animating the graph
    def animate_scatter(i):
        sc._offsets3d = (x[i], y[i], z[i])

    ani = anim.FuncAnimation(fig, animate_scatter, frames=len(x), interval=10, repeat=True)
    plt.show()

    if isinstance(save, str):
        ani.save(f"{save}.gif", writer="pillow")


def main():
    """
    Create the spaceobjects you want to plot and put them into the space_object_list.
    Name, location (hast to be float) and velocity are necessary. The rest is optional.
    """

    p1 = Space.Spaceobject(name="Mercury", mass=3.3*10**26, location=[58.*10**9, 0, 0],
                           D_TIME=D_TIME, velocity=[0, 172332/3.6, 0], color="#cc7a00")

    p2 = Space.Spaceobject(name="Venus", mass=4.867*10**27, location=[108.2*10**9, 0, 0],
                           D_TIME=D_TIME, velocity=[0, 126072/3.6, 0], color="#b34700")

    p3 = Space.Spaceobject(name="Earth", mass=5.972*10**27, location=[149.6*10**9, 0, 0],
                           D_TIME=D_TIME, velocity=[0, 107208/3.6, 0], color="blue")

    p4 = Space.Spaceobject(name="Mars", mass=6.42*10**26, location=[228.*10**9, 0, 0],
                           D_TIME=D_TIME, velocity=[0, 86868/3.6, 0], color="#ff751a")

    p5 = Space.Spaceobject(name="Jupiter", mass=1.9*10**27, location=[778.*10**9, 0, 0],
                           D_TIME=D_TIME, velocity=[0, 47052 / 3.6, 0], color="#ffb366")

    p6 = Space.Spaceobject(name="Saturn", mass=5.69*10**26, location=[1433. * 10 ** 9, 0, 0],
                           D_TIME=D_TIME, velocity=[0, 34884 / 3.6, 0], color="#ffcc99")

    p7 = Space.Spaceobject(name="Uranus", mass=8.68*10**25, location=[2872.*10**9, 0, 0],
                           D_TIME=D_TIME, velocity=[0, 24516/3.6, 0], color="#99b3ff")

    p8 = Space.Spaceobject(name="Neptune", mass=1.02*10**26, location=[4495. * 10 ** 9, 0, 0],
                           D_TIME=D_TIME, velocity=[0, 19548 / 3.6, 0], color="#0040ff")

    space_object_list = [p1, p2, p3, p4, p5, p6, p7, p8]

    # Plotting the space objects
    show_plot(space_object_list, iterations=250_000, save="Solar")


if __name__ == "__main__":
    main()
