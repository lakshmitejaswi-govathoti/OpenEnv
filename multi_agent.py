from tools import search_tool, code_analysis_tool

class PlannerAgent:
    def plan(self, obs):
        return ["analyze", "execute"]

class AnalystAgent:
    def analyze(self, obs):
        return {"tokens": obs.content.lower().split()}

class ExecutorAgent:
    def execute(self, obs, analysis):
        text = obs.content.lower()

        if obs.task_id == "email":
            for word in analysis["tokens"]:
                label = search_tool(word)
                if label != "unknown":
                    return {"label": label}
            return {"label": "promotions"}

        if obs.task_id == "data":
            parts = text.split(",")
            name = parts[0] if parts[0] else "Unknown"
            age = parts[1] if len(parts) > 1 and parts[1] else "0"
            return {"cleaned": f"{name},{age}"}

        if obs.task_id == "code":
            return {"issues": code_analysis_tool(text)}

class CriticAgent:
    def review(self, reward):
        return reward > 0