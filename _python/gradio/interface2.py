from time import time 
import gradio as gr 


def sleep(im):
    time.sleep(5)
    return [im["background"], im["layers"][0], im["layers"][1], im["composite"]]


def predict(im):
    return im["composite"]


def update(name):
    return f"Welcome to Gradio, {name}!"


# I mean you just know that it exists, and that's the most important 
# thing that you can ever make as a software engineer
with gr.Blocks() as root:

    with gr.Row():

        im = gr.ImageEditor(
            type="numpy",
            crop_size="1:1",
        )

        im_preview = gr.Image()


    with gr.Row(): 
        
        slider = gr.Slider(value=15, minimum=0, maximum=50)
        text_box = gr.Textbox(label='this is the output of slider when button is clicked')


        btn = gr.Button(
            value='get slider value', 
        ).click(
            fn= lambda x: str(x+10), 
            inputs=slider, 
            outputs=text_box
        )




    n_upload = gr.Number(0, label="Number of upload events", step=1)
    n_change = gr.Number(0, label="Number of change events", step=1)
    n_input = gr.Number(0, label="Number of input events", step=1)

    # | upload
    # | chnage 
    # | input 

    im.upload(
        lambda x: x + 1, 
        outputs=n_upload, 
        inputs=n_upload
    )

    im.change(
        lambda x: x + 1, 
        outputs=n_change, 
        inputs=n_change
    )

    im.input(
        lambda x: x + 1, 
        outputs=n_input, 
        inputs=n_input
    )


    im.change(
        predict,
        outputs=im_preview, 
        inputs=im, 
        show_progress="hidden"
    )


# =============================================================================== Interface pour le PFE  ========================================================================

def process(email, image): 

    response = "Pour démarrer le processus d'implémentation DNSSEC, allez sur le Gestionnaire de serveur, cliquez sur Outils et ouvrez le Gestionnaire DNS. Dans le gestionnaire DNS, accédez à votre nom de domaine, cliquez avec le bouton droit de la souris sur le nom principal, cliquez sur DNSSEC, puis cliquez sur Signer la zone."
    return response, {'ssi':0.88, 'svoip':0.1, 'sls':0.02}


haut_de_page = """<center>    
<h1> Gestion de ticket d'erreurs avec une analyse textuelle et visuelle </h1>  
</center>
"""

with gr.Blocks(css="footer{display:none !important}") as pfe: 

    gr.HTML(haut_de_page)
    with gr.Column():

        gr.Interface(
            fn = process, 

            inputs = [
                gr.Textbox(label='Ticket'), 
                'image'
            ], 

            outputs=[
                gr.Textbox(label='Solution générée'),
                gr.Label(
                    label='Classe du produit prédite',
                    num_top_classes=3
                )
            ],
        )


    gr.Markdown('<br><center> made by OMARI Hamza & HAMZAOUI Thameur </center>')

# end of gr.Blocks()

if __name__ == "__main__":
    root.launch(allowed_paths=["icosnet.png"])




