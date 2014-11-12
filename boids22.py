__author__ = 'Sherif'
from boid import boid
import yaml
import random
import os
#from boids22 import Boids
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
from matplotlib import animation
class boids (type):
    def __init__(self):
        config = yaml.load(open(os.path.join(os.path.dirname(__file__), 'initial_config.yml')))
        self.number_boids = config["number_boids"]
        self.boids = [Boid(random.uniform(config['x_min'], config['x_max']),
                            random.uniform(config['y_min'], config['y_max']),
                            random.uniform(config['vx_min'], config['vx_max']),
                            random.uniform(config['vy_min'], config['vy_max'])) for x in range(self.number_boids)]

    def group_boids(self, data):
        self.boids= [Boid(data[0][i],data[1][i],data[2][i], data[3][i],) for i in range(self.num_boids)]
    def get_boids(self):
        return zip(*[[self.boids[i].x, self.boids[i].y, self.boids[i].vx, self.boids[i].vy] for i in range(self.num_boids)])

        # Flying towards the middle of the flak
    def fly_mid(self):
        for boid_i in self.boids:
            for boid_j in self.boids:
                boid_i.fly_mid(boid_j)

    def fly_away(self):
        for boid_i in self.boids:
            for boid_j in self.boids:
                boid_i.fly_away(boid_j)

    def velocity_match (self):
        for boid_i in self.boids:
            for boid_j in self.boids:
                boid_i.velocity_match(boid_j)

    def move (self):
        for boid_i in self.boids:
            boid_i.move()
    def update_boids(self):
        self.fly_mid()
        self.velocity_match()
        self.move()


# Load plot config from plot_config.yml
        plot_config = yaml.load(open(os.path.join(os.path.dirname(__file__), 'plot_config.yml')))
        xlim_max = plot_config["xlim_max"]
        xlim_min = plot_config["xlim_min"]
        ylim_max = plot_config["ylim_max"]
        ylim_min = plot_config["ylim_min"]
        framesT = plot_config["frames"]
        intervalT = plot_config["interval"]
    # construct flock of boids)
        my_boids = Boids()
# plot figure
        figure = plt.figure()
        axes = plt.axes(xlim=(xlim_min, xlim_max), ylim=(ylim_min, ylim_max))
        scatter = axes.scatter(my_boids.get_boids()[0], my_boids.get_boids()[1])
# Run the simulation and update the figure
    def animate(frame):
        my_boids.update_boids()
        scatter.set_offsets(zip(my_boids.get_boids()[0], my_boids.get_boids()[1]))
        anim = animation.FuncAnimation(figure, animate, frames=framesT, interval=intervalT)
