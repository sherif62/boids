from boids22 import Boids
from nose.tools import assert_almost_equal
import os
import yaml
def test_class_boids_regression():
      regression_data=yaml.load(open(os.path.join(os.path.dirname(__file__),'fixture.yml')))
        boid_data = regression_data["before"]
        model = Boids(50,100,0.01,10000,0.125)
        model.boid(boid_data)
        model.update_boids()
        model_after = [
        [ boid.x for boid in model.boids ], \
        [ boid.y for boid in model.boids ], \
        [ boid.xv for boid in model.boids ], \
        [ boid.yv for boid in model.boids ]]
     for after,before in zip(regression_data["after"],model_after):
        for after_value,before_value in zip(after,before):
            assert_almost_equal(after_value,before_value,delta=0.01)