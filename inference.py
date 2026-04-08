from environment import WorkBenchEnv
from models import Action
from multi_agent import PlannerAgent, AnalystAgent, ExecutorAgent, CriticAgent
from rl_train import train

planner = PlannerAgent()
analyst = AnalystAgent()
executor = ExecutorAgent()
critic = CriticAgent()

# train RL agent once
agent = train(episodes=50)

def run(return_score=False):
    env = WorkBenchEnv()
    obs = env.reset()
    total = 0

    while True:
        analysis = analyst.analyze(obs)
        action_payload = executor.execute(obs, analysis)

        action = Action(action_type="multi_agent", payload=action_payload)

        obs, reward, done, _ = env.step(action)
        critic.review(reward)

        total += reward

        if done:
            break

    if return_score:
        return round(total, 2)

    print("Score:", total)