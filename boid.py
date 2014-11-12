__author__ = 'Sherif'
import random
import os
import yaml
class boid (object):
    def __init__(self, px, py, vx, vy):
        config = yaml.load(open(os.path.join(os.path.dirname(__file__), 'initial_config.yml')))
        self.number.boids= config["ran_boids"]
        self.fly_mid=config["fly_mid"]
        self.fly_away= config["fly_away"]
        self.velocity_match= config ["speed_match"]
        self.velocity_match2= config["speed_match2"]

        ## For each boid
        self.px=px
        self.py=py
        self.vx=vx
        self.vy=vy

        #Flying conditions
        #Fly towards the middle
    def fly_mid(self,boid):
        self.vx += (boid.x - self.x) * self.fly_mid / self.number_boids
        self.vy += (boid.y - self.y) * self.fly_mid / self.number_boids

        # Flying of each boid with respect to the other boids
    def fly_awy(self, boid):
        if self.distance(boid) < self.fly_away:
            self.vx+=(self.x- boid.x)
            self.vy+=(self.y -boid.y)

    def velocity_match(self, boid):
        if self.distance(boid)<self.velocity_match2(boid):
            self.vx += (boid.vx - self.vx) * self.velocity_match2 / self.number_boids
            self.vy += (boid.vy - self.vy) * self.velocity_match2 / self.number_boids
    # The distance between boids

    def distance(self, boid):
        dist= (boid.x - self.x) ** 2 + (boid.y - self.y) ** 2
        return  dist

    def mov(self):
        self.x+=self.vx
        self.y+=self.vy











