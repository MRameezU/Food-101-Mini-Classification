### 1. Imports and class names setup ###
import gradio as gr
import os
import torch

from model import create_effnetb2_model
from timeit import default_timer as timer
from typing import Tuple,Dict

# Setup class names
class_names=["pizza","steak","sushi"]
### 2. Model and transforms perparation ###
effnetb2,effnetb2_transforms=create_effnetb2_model(num_classes=len(class_names))

# Load save weights
effnetb2.load_state_dict(
    torch.load(
        f="effnetb2_feature_extractor_food101_mini.pth",
        map_location=torch.device("cpu") # load the model to the CPU
    )
)



### 3. Predict function ###
def predict(img)->Tuple[Dict,float]:
  # start a timer
  start_time = timer()

  # Transform the input image for use with EffNetB2
  img=effnetb2_transforms(img).unsqueeze(0) # unsqueeze = add batch dimension on 0th index

  # Put model into eval mode, make prediction
  effnetb2.eval()
  with torch.inference_mode():
    # Pass transformed image through the model and turn the prediction logits into probaiblities
    pred_probs=torch.softmax(effnetb2(img),dim=1)

  # Create a prediction label and prediction probability dictionary
  pred_labels_and_probs = {}

  # pred_labels_and_probs = {class_names[i]: float(pred_probs[0][i]) for i in range(len(class_names))}
  # comment loop below to un-comment line above
  for i,class_name in enumerate(class_names):
    pred_labels_and_probs[class_name]=pred_probs[0][i]

  # Calculate pred time
  end_time=timer()
  pred_time=round(end_time-start_time,4)

  # Return pred dict and pred time
  return pred_labels_and_probs,pred_time

### 4. Gradio app ###

# Create title, description and article

title="Food101 Big Classification"
description = "An [EfficientNetB2 feature extractor](https://pytorch.org/vision/stable/models/generated/torchvision.models.efficientnet_b2.html#torchvision.models.efficientnet_b2) computer vision model to classify images as pizza, steak or sushi."
article = "Created at [Food101 Mini Classification](https://github.com/MRameezU/Food-101-Mini-Classification.git)."

# Create example list
# Create example list
example_list = [["examples/" + example] for example in os.listdir("examples")]

# Create the Gradio demo
demo = gr.Interface(fn=predict, # maps inputs to outputs
                    inputs=gr.Image(type="pil"),
                    outputs=[gr.Label(num_top_classes=3, label="Predictions"),
                             gr.Number(label="Prediction time (s)")],
                    examples=example_list,
                    title=title,
                    description=description,
                    article=article)

# Launch the demo!
demo.launch()
