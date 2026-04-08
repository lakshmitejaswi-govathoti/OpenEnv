from models import Observation, Action
from graders.email_grader import grade_email

class EmailTask:
    def __init__(self):
        self.data = [
            {"text": "Meeting at 10am", "label": "important"},
            {"text": "Win money now", "label": "spam"},
            {"text": "Big sale today", "label": "promotions"}
        ]
        self.i = 0

    def reset(self):
        self.i = 0
        return Observation(task_id="email", content=self.data[self.i]["text"], metadata={})

    def step(self, action: Action):
        correct = grade_email(action.payload, self.data[self.i]["label"])
        reward = 1.0 if correct else -0.2

        self.i += 1
        done = self.i >= len(self.data)

        obs = None if done else Observation(
            task_id="email",
            content=self.data[self.i]["text"],
            metadata={}
        )

        return obs, reward, done, {}