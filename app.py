import gradio as gr
# import time

def hello(i):
    return "Hello " + name + "!!"
#     classifier = pipeline("sentiment-analysis")
#     a = classifier(i)
    
#     return a
#     while True:
#         print('test')
#         time.sleep(1)
#     return "hello"
    
iface = gr.Interface(fn=hello, inputs="text", outputs="text")
iface.launch(server_name="0.0.0.0")
