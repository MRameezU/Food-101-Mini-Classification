# Food-101 Mini Classification with EfficientNetB2

This repository aims to replicate and improve upon the results of the research paper titled ["Food-101 - Mining Discriminative Components with Random Forests"](https://data.vision.ee.ethz.ch/cvl/datasets_extra/food-101/) by Lukas Bossard, Matthieu Guillaumin, and Luc Van Gool. The original paper reported a test accuracy of 56.4% on the Food-101 dataset. Using minimal resources, we have achieved significantly higher accuracy with modern deep learning models.

## Project Overview

In this project, I focused on the **EfficientNet B2** model, training it on a subset of the Food-101 dataset containing three classes: **pizza, steak, and sushi**. The goal was to achieve better accuracy with minimal resources.

### Model Performance

| Model           | Test Loss | Test Accuracy | Number of Parameters | Model Size (MB) | Time per Prediction (CPU) |
|-----------------|-----------|---------------|----------------------|-----------------|---------------------------|
| EfficientNet B2 | 0.281287   | 96.88%        | 7,705,221            | 29 MB           | 0.0269 seconds             |

> **Note:** The experiment code and performance results for the **ViT Base** model will be hosted in a separate repository. This repository will be linked here once available.

### Gradio App

To make this model accessible and easy to use, I have deployed a simple Gradio app on Hugging Face Spaces. The app allows users to upload an image and get a prediction for one of the three food classes.

[Hugging Face Spaces URL](https://huggingface.co/spaces/urameez/foodvision_mini)

## Repository Structure

- **`food101_mini_classification.ipynb`**: Jupyter notebook containing the code for training and evaluating the EfficientNet B2 model.
- **`food101_mini_classification/`**:
  - **`effnetb2_feature_extractor_food101_mini.pth`**: Pretrained weights for the EfficientNet B2 model.
  - **`app.py`**: Script to launch the Gradio app.
  - **`examples/`**:
    - **`example_1.jpg`**: Sample image for prediction.
    - **`example_2.jpg`**: Sample image for prediction.
    - **`example_3.jpg`**: Sample image for prediction.
  - **`model.py`**: Python module containing the model definitions and utilities.
  - **`requirements.txt`**: List of dependencies required to run the project.

## How to Use

1. Clone the repository:
    ```bash
    git clone https://github.com/MRameezU/Food-101-Mini-Classification.git
    cd Food-101-Mini-Classification
    ```

    

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the Gradio app locally:
    ```bash
    python app.py
    ```

4. Alternatively, you can use the app directly on Hugging Face Spaces via the provided URL.

## Acknowledgments

This project was inspired by the work of [Daniel Bourke](https://github.com/mrdbourke). I also acknowledge the research conducted by Lukas Bossard, Matthieu Guillaumin, and Luc Van Gool, as well as the open-source community for their tools and resources.

## License

This project is licensed under the MIT License.
