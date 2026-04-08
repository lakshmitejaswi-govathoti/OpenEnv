from models import Observation, Action
from graders.data_grader import grade_data

class DataCleaningTask:
    def __init__(self):
        self.raw = ["John,25", "Alice,", ",30"]
        self.cleaned = ["John,25", "Alice,0", "Unknown,30"]
        self.i = 0

    def reset(self):
        self.i = 0
        return Observation(task_id="data", content=self.raw[self.i], metadata={})

    def step(self, action: Action):
        output = action.payload.get("cleaned", "")
        score = grade_data(output, self.cleaned[self.i])
        reward = score

        self.i += 1
        done = self.i >= len(self.raw)

        obs = None if done else Observation(
            task_id="data",
            content=self.raw[self.i],
            metadata={}
        )

        return obs, reward, done, {}