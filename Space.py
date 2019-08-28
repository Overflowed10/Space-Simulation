import numpy as np


class Spaceobject:
    def __init__(self, name, location, velocity=(1, 1, 1), D_TIME=100, mass=1, color="blue"):
        self.name = name                        # name of the space object
        self.mass = mass                        # in kg
        self.location = location                # (x, y, z)
        self.velocity = velocity                # velocity (x, y, z)
        self.D_TIME = D_TIME                    # amount of seconds taken for the calculation of the next
                                                # position of the space object
        self.G = 6.6743*10**-11                 # gravitational constant in m³/(kg * s²)
        self.color = color                      # color of the space object

        self.sun = {"mass": 1.989*10**30,       # Dict with values for the sun
                    "location": [0, 0, 0],
                    "velocity": [1, 1, 1]}

    def calc_vector_planet_to_sun(self, vec2):
        """ Takes the suns location as vec2 and returns the vector of the object towards the sun.
            Is used in self.calc_vector_towards_sun.
        """
        vec_x = vec2[0] - self.location[0]
        vec_y = vec2[1] - self.location[1]
        vec_z = vec2[2] - self.location[2]
        return vec_x, vec_y, vec_z

    @staticmethod
    def calc_vector_length(vector):
        """ Takes a vector and returns its length.
            Is used in self.calc_vector_towards_sun.
        """
        return np.sqrt((vector[0]**2+vector[1]**2+vector[2]**2))

    def calc_vector_towards_sun(self):
        """ Returns the direction of the space object towards the sun
        """
        top = self.calc_vector_planet_to_sun(self.sun["location"])
        mass = self.sun["mass"]
        factor = (mass * self.G * self.D_TIME) / (self.calc_vector_length(top))**3

        vec_x = top[0] * factor
        vec_y = top[1] * factor
        vec_z = top[2] * factor

        return vec_x, vec_y, vec_z

    def calc_new_velocity(self):
        """ Returns the new velocity of the object.
        """
        vel_towards_sun = self.calc_vector_towards_sun()
        vec_x = self.velocity[0] + vel_towards_sun[0]
        vec_y = self.velocity[1] + vel_towards_sun[1]
        vec_z = self.velocity[2] + vel_towards_sun[2]
        return vec_x, vec_y, vec_z

    def calc_velocity_planet(self):
        """ Calculates velocity of the planet in a certain time frame.
        Is used in self.calc_new_position.
        """
        vec_x = self.velocity[0] * self.D_TIME
        vec_y = self.velocity[1] * self.D_TIME
        vec_z = self.velocity[2] * self.D_TIME
        return vec_x, vec_y, vec_z

    def calc_movement_towards_sun(self):
        """ Calculates the planets movement towards the sun.
        Is used in self.calc_new_position.
        """
        vel_towards_sun = self.calc_vector_towards_sun()
        vec_x = vel_towards_sun[0] * (self.D_TIME / 2)
        vec_y = vel_towards_sun[1] * (self.D_TIME / 2)
        vec_z = vel_towards_sun[2] * (self.D_TIME / 2)
        return vec_x, vec_y, vec_z

    def calc_new_position(self):
        """ Calculates the new location of the object.
        """
        vel_planet = self.calc_velocity_planet()
        mov_towards_sun = self.calc_movement_towards_sun()
        vec_x = self.location[0] + vel_planet[0] + mov_towards_sun[0]
        vec_y = self.location[1] + vel_planet[1] + mov_towards_sun[1]
        vec_z = self.location[2] + vel_planet[2] + mov_towards_sun[2]
        return vec_x, vec_y, vec_z

    def update_obj(self):
        """ Updates self.location and  self.direction of an object
        """
        new_position = self.calc_new_position()
        new_velocity = self.calc_new_velocity()

        self.location[0] = new_position[0]
        self.location[1] = new_position[1]
        self.location[2] = new_position[2]

        self.velocity[0] = new_velocity[0]
        self.velocity[1] = new_velocity[1]
        self.velocity[2] = new_velocity[2]
