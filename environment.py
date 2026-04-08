from models import Action
from tasks.email_task import EmailTask
from tasks.data_cleaning_task import DataCleaningTask
from tasks.code_review_task import CodeReviewTask

class WorkBenchEnv:

    def __init__(self):
        self.tasks = [EmailTask(), DataCleaningTask(), CodeReviewTask()]
        self.idx = 0
        self.current = self.tasks[self.idx]

    def reset(self):
        self.idx = 0
        self.current = self.tasks[self.idx]
        return self.current.reset()

    def step(self, action: Action):
        obs, reward, done, info = self.current.step(action)

        if done and self.idx < len(self.tasks) - 1:
            self.idx += 1
            self.current = self.tasks[self.idx]
            obs = self.current.reset()
            done = False

        return obs, reward, done, info

    def state(self):
        return {
            "task_index": self.idx,
            "task_name": type(self.current).__name__
        }