import gradio as gr


def hello(i):
    # classifier = pipeline("sentiment-analysis")
    # a = classifier(i)
    # return a
    return "hello"

iface = gr.Interface(fn=hello, inputs="text", outputs="text")
iface.launch(server_name="0.0.0.0")
