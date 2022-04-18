import numpy as np
from rlgym.utils import common_values
from rlgym.utils.gamestates import PlayerData, GameState
from rlgym.utils.reward_functions import RewardFunction, CombinedReward
from rlgym.utils.reward_functions.common_rewards import VelocityPlayerToBallReward, VelocityBallToGoalReward, \
    EventReward


class DefaultRewardFunction(RewardFunction):
    def __init__(self):
        self.x_threshold = 4096+500
        self.vel_rew = VelocityPlayerToBallReward()
        self.event_rew = EventReward(touch=1, goal=10)

    def reset(self, initial_state: GameState):
        self.vel_rew.reset(initial_state)
        self.event_rew.reset(initial_state)

    def get_reward(self, player: PlayerData, state: GameState, previous_action: np.ndarray) -> float:
        rew = 0
        rew += self.vel_rew.get_reward(player, state, previous_action) / common_values.CAR_MAX_SPEED
        rew += self.event_rew.get_reward(player, state, previous_action)
        if state.ball.position[0] < self.x_threshold:
            rew = -1
        return rew
