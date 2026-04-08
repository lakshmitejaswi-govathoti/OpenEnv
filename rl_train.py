from environment import WorkBenchEnv
from models import Action
from rl_agent import SimpleRLAgent

def train(episodes=50):
    agent = SimpleRLAgent()

    for _ in range(episodes):
        env = WorkBenchEnv()
        obs = env.reset()

        while True:
            action_payload = agent.act(obs)
            action = Action(action_type="rl", payload=action_payload)

            next_obs, reward, done, _ = env.step(action)
            agent.update(obs, action_payload, reward)

            obs = next_obs

            if done:
                break

    return agent