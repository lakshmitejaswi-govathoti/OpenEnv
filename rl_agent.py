import random

class SimpleRLAgent:
    def __init__(self):
        self.memory = {}

    def act(self, obs):
        if obs.content in self.memory:
            return self.memory[obs.content]
        return self.random_action(obs)

    def random_action(self, obs):
        if obs.task_id == "email":
            return {"label": random.choice(["important", "spam", "promotions"])}
        if obs.task_id == "data":
            return {"cleaned": obs.content}
        if obs.task_id == "code":
            return {"issues": []}
        return {}

    def update(self, obs, action, reward):
        if reward > 0:
            self.memory[obs.content] = action