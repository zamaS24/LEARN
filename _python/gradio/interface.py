"""NOTE
l'idée globale


    chauque item il a  (inputs to get , and output to make, and callback function)
    callback prend les inputs et retourne dans les outputs 
    
    event trigger by callbacks


You can use the Interface, and the even trigger is the submit button

"""



import gradio as gr
from PIL import Image
import numpy as np 



# the input will have the name if the parameters I guess when specified only the type of it 
def greet(name, place_holder, value): 
    
    return 'hello world', value



# by default it uses: gr.Row() 

############################" componentes"
# pour image : gr.Image()
# 
#
#


# we give three 
# fn is for the global function I guess
# inputs and outputs 
# examples : des exemples de inputs et leur outputs: 
# BOOL: live: si quand un input change on doit executer
# title
# theme 
# demo = gr.Interface(

#     fn=greet, 

#     inputs=[
#         "text", 
#         gr.Textbox(label='My label (avant it was place_holder)',lines=2, placeholder="place holder.."),
#         gr.Slider(value=2, minimum=1, maximum=10, step=1)
#     ], # which Gradio component(s) to use for the input. The number of components should match the number of arguments in your function.

#     outputs = ["text", "number"]
# )


def func1(text, number): 

    if text == None or text =='' or text ==' ': 
        gr.Warning("Il faut introduire ")
        gr.Info('for more useful usage click on show messages ')
        return None, None

    # return '', None

    return text +'returned' , number + 10


haut_de_page = """# Gestion de ticket d'erreurs avec une analyse textuelle et visuelle
<img src"C:\Users\monms\Desktop\PFE\images" alt="Girl in a jacket" width="500" height="600">

 > made by [OMARI Hamza](https://www.linkedin.com/in/hamza-omari/) & [HAMZAOUI Thameur](https://www.linkedin.com/in/thameur-hamzaoui-881831179)
"""
with gr.Blocks() as demo: 


    gr.Markdown()


    with gr.Row(): 

        gr.Interface(

        fn=func1, 
        inputs = ['text', 'number'], 
        outputs=['text', 'number']
        ),
        


        gr.Interface(

        fn=func1, 
        inputs = ['text', 'number'], 
        outputs=['text', 'number']
        )
        
       



demo.launch()

