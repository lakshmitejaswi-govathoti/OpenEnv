from models import Observation, Action
from graders.code_grader import grade_code

class CodeReviewTask:
    def __init__(self):
        self.code = [
            {"snippet": "x=1/0", "issues": ["division_by_zero"]},
            {"snippet": "print y", "issues": ["syntax_error"]}
        ]
        self.i = 0

    def reset(self):
        self.i = 0
        return Observation(task_id="code", content=self.code[self.i]["snippet"], metadata={})

    def step(self, action: Action):
        output = action.payload.get("issues", [])
        score = grade_code(output, self.code[self.i]["issues"])
        reward = score

        self.i += 1
        done = self.i >= len(self.code)

        obs = None if done else Observation(
            task_id="code",
            content=self.code[self.i]["snippet"],
            metadata={}
        )

        return obs, reward, done, {}