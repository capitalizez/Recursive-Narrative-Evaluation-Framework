
import os
from datetime import datetime
from llama_cpp import Llama
import gradio as gr

# Preload available models
model_paths = {
    "mythomax-l2-13b": r"C:\AI\models\MythoMaxL2\mythomax-l2-13b.Q4_K_M.gguf",
}
llm_models = {}
for name, path in model_paths.items():
    try:
        llm_models[name] = Llama(model_path=path, n_gpu_layers=-1, n_ctx=4096, verbose=False)
    except Exception:
        llm_models[name] = None

SYSTEM_PROMPT = (
    "You are a helpful AI model. Respond clearly, respectfully, and intelligently to the user's questions.\n"
    "Use structured reasoning when needed and end each response with [StopSignal]."
)

def retrieve_context_snippet(file_path: str, query: str, window: int = 2) -> str:
    try:
        lines = open(file_path, encoding="utf-8").read().splitlines()
    except Exception:
        return ""
    collected = []
    for idx, line in enumerate(lines):
        if query.lower() in line.lower():
            start = max(0, idx - window)
            end = min(len(lines), idx + window + 1)
            collected.extend(lines[start:end])
    snippet = []
    seen = set()
    for ln in collected:
        if ln not in seen:
            seen.add(ln)
            snippet.append(ln)
    return "\n".join(snippet)

def build_prompt(history_pairs, context_snippet, latest_user):
    """history_pairs: list of [user, assistant]"""
    parts = [SYSTEM_PROMPT]
    if context_snippet:
        parts.append(f"[Context snippet]:\n{context_snippet}")
    for usr, ai in history_pairs:
        parts.append(f"[User prompt]: {usr}")
        parts.append(ai)
    parts.append(f"[User prompt]: {latest_user}")
    parts.append("[Assistant response]:")
    return "\n".join(parts)

def generate_response(history_pairs, user_message, temperature, max_tokens, model_name, context_snippet):
    prompt = build_prompt(history_pairs, context_snippet, user_message)
    llm = llm_models.get(model_name)
    if not llm:
        raise RuntimeError(f"Model '{model_name}' failed to load.")
    resp = llm(
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=temperature,
        echo=False,
        stop=["[StopSignal]", "\n[User prompt]:"]
    )
    text = resp['choices'][0]['text'].strip()
    if not text.endswith('[StopSignal]'):
        text += ' [StopSignal]'
    return text

def chat(user_message, history, temperature, max_tokens, model_name, context_file):
    history = history or []  # list of [user, assistant]
    snippet = retrieve_context_snippet(context_file.name, user_message) if context_file else ""
    reply = generate_response(history, user_message, temperature, max_tokens, model_name, snippet)
    history.append([user_message, reply])
    with open('chat_log.txt', 'a', encoding='utf-8') as f:
        ts = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        f.write(f"[{ts}] USER: {user_message}\n[{ts}] ASSISTANT: {reply}\n\n")
    return history, snippet, ""

dark_css = "body {background-color: #121212; color: #fff;}"
with gr.Blocks(css=dark_css) as demo:
    gr.Markdown("# Recursive Narrative Evaluation Chat")
    with gr.Row():
        with gr.Column(scale=3):
            chatbot = gr.Chatbot(label="Chat", height=400)
            user_input = gr.Textbox(placeholder="Type your message here...", label="Your message")
            send_btn = gr.Button("Send")
            snippet_box = gr.Textbox(label="Context Snippet", lines=4, interactive=False)
        with gr.Column(scale=1):
            gr.Markdown("## Settings")
            model_selector = gr.Dropdown(list(model_paths.keys()), value=list(model_paths.keys())[0], label="Model")
            temp_slider = gr.Slider(0.1, 1.0, value=0.7, label="Temperature")
            token_slider = gr.Slider(50, 1024, value=150, step=50, label="Max Tokens")
            context_file = gr.File(label="Upload Context File")

    send_btn.click(
        chat,
        inputs=[user_input, chatbot, temp_slider, token_slider, model_selector, context_file],
        outputs=[chatbot, snippet_box, user_input]
    )
    user_input.submit(
        chat,
        inputs=[user_input, chatbot, temp_slider, token_slider, model_selector, context_file],
        outputs=[chatbot, snippet_box, user_input]
    )

    demo.launch(share=True)
