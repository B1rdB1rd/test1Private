import gradio as gr

def greet(name):
    return "Hello " + name + "!!"
    # return 123/0

iface = gr.Interface(fn=greet, inputs="text", outputs="text")
iface.launch()
