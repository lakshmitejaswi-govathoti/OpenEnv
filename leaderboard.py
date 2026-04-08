import pandas as pd
import os

FILE = "leaderboard.csv"

def init_board():
    if not os.path.exists(FILE):
        df = pd.DataFrame(columns=["model", "score"])
        df.to_csv(FILE, index=False)

def add_score(model, score):
    df = pd.read_csv(FILE)
    df.loc[len(df)] = [model, score]
    df = df.sort_values(by="score", ascending=False)
    df.to_csv(FILE, index=False)

def get_leaderboard():
    return pd.read_csv(FILE)