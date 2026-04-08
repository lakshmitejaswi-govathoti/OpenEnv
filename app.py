import gradio as gr
from inference import run
from leaderboard import init_board, add_score, get_leaderboard

init_board()

def evaluate_model(model_name):
    score = run(return_score=True)
    add_score(model_name, score)
    return str(score), get_leaderboard()

with gr.Blocks() as demo:
    gr.Markdown("# 🏆 WorkBenchAI Leaderboard")

    model_input = gr.Textbox(label="Model Name")
    run_btn = gr.Button("Run Evaluation")

    score_output = gr.Textbox(label="Score")
    leaderboard_output = gr.Dataframe()

    run_btn.click(
        fn=evaluate_model,
        inputs=model_input,
        outputs=[score_output, leaderboard_output]
    )

demo.launch()