from fastapi import FastAPI
import gradio as gr

from app import ict

app = FastAPI()

@app.get('/')
async def root():
    return 'Gradio app is running at /app', 200

app = gr.mount_gradio_app(app, ict, path='/app')
