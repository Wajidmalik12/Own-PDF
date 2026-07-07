import gradio as gr
from rag import process_pdf, chat

with gr.Blocks(title="PDF ChatBot") as demo:

    gr.Markdown("# 📄 PDF ChatBot")
    gr.Markdown("Upload a PDF and ask questions about it.")

    with gr.Row():
        pdf = gr.File(
            label="Upload PDF",
            file_types=[".pdf"]
        )

        upload = gr.Button("Upload")

    status = gr.Textbox(
        label="Status",
        interactive=False
    )

    upload.click(
        fn=process_pdf,
        inputs=pdf,
        outputs=status
    )

    question = gr.Textbox(
        label="Ask a Question",
        placeholder="Ask anything about the uploaded PDF..."
    )

    answer = gr.Textbox(
        label="Answer",
        lines=10
    )

    question.submit(
        fn=chat,
        inputs=question,
        outputs=answer
    )

demo.launch(
    server_name="0.0.0.0",
    server_port=7860
)