import gradio as gr
# import time
# import os
def hello(i):

    return "Hello " + "!!"
#     classifier = pipeline("sentiment-analysis")
#     a = classifier(i)
    
#     return a
#     while True:
#         print('test')
#         time.sleep(1)
#     return "hello"
    
# tryghgmjhkk,:




    iface = gr.Interface(fn=hello, inputs="text", outputs="text")
    iface.launch(server_name="0.0.0.0")
# except:
#     print('err')
#     os.exit(-1)
