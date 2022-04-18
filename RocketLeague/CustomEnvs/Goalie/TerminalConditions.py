from rlgym.utils.gamestates import GameState
from rlgym.utils.terminal_conditions.common_conditions import TimeoutCondition, GoalScoredCondition
from rlgym.utils.terminal_conditions import TerminalCondition


class DefaultTerminalConditions(TerminalCondition):
    def __init__(self):
        super().__init__()
        self.conditions = [TimeoutCondition(100), GoalScoredCondition()]

    def reset(self, initial_state: GameState):
        for condition in self.conditions:
            condition.reset(initial_state)

    def is_terminal(self, current_state: GameState) -> bool:
        print("ball position 0", current_state.ball.position[0])
        print("ball position 1", current_state.ball.position[1])
        print("ball position 2", current_state.ball.position[2])
        if current_state.ball.position[0] <= 3000:
            return True

        for condition in self.conditions:
            if condition.is_terminal(current_state):
                return True
        return False
