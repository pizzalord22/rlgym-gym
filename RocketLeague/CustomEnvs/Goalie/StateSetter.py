from rlgym.utils.state_setters import StateSetter, DefaultState, StateWrapper
from rlgym.utils import common_values
import numpy as np


class DefaultStateSetter(StateSetter):
    GOAL_CORNERS = [(-893, 5120, 642)]  # top right?

    def __init__(self):
        super().__init__()
        self.rng = np.random.RandomState(123)

    def reset(self, state_wrapper: StateWrapper):
        self._spawn_ball(state_wrapper)
        self._spawn_car(state_wrapper)
        return

    def _spawn_ball(self, state_wrapper: StateWrapper):
        start_point = (4096 - 1200, -5120 + 300, 93)
        # end_point = common_values.BLUE_GOAL_CENTER

        x_offset = self.rng.uniform(-893 + common_values.BALL_RADIUS, 893 - common_values.BALL_RADIUS)
        y_offset = 800
        z_offset = self.rng.uniform(-602.775 / 2, 602.775 / 2)
        # end_point = np.add(end_point, (x_offset, y_offset, z_offset))

        velocity_vector = [-2000, 0, 0]
        state_wrapper.ball.set_pos(*start_point)
        state_wrapper.ball.set_lin_vel(*velocity_vector)

    def _spawn_car(self, state_wrapper: StateWrapper):
        # todo set car in front of goal facing the goal
        x, y, _ = common_values.BLUE_GOAL_CENTER
        z = 0
        y += 120
        state_wrapper.cars[0].set_pos(x, y, z)
        state_wrapper.cars[0].set_rot(yaw=self.rng.uniform(0, np.pi * 2))
        state_wrapper.cars[0].boost = 100
