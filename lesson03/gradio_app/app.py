from fastai.vision.all import *  # Importing the necessary fastai modules
import gradio as gr  # Importing Gradio for creating the web interface
import timm  # Importing timm for model management

# Load the pre-trained model
learn = load_learner('model.pkl')

# Extract categories (class labels) from the DataLoader
categories = learn.dls.vocab

# Function to classify an image
def classify_image(img):
    _, _, probs = learn.predict(img)
    return dict(zip(categories, map(float, probs)))  # Map categories to their probabilities

# Define Gradio input and output components 
image = gr.Image(width=224, height=224)  # Image input
label = gr.Label()  # Output label to display classification
examples = ['test_image1.jpg', 'test_image2.jpg']  # Example images for demonstration

# Create and launch the Gradio interface
intf = gr.Interface(fn=classify_image, inputs=image, outputs=label, examples=examples)
intf.launch()