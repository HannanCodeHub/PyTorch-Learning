# MNIST Classifier

A PyTorch-based deep learning project for classifying handwritten digits from the MNIST dataset. This project implements and compares a fully connected neural network and a Convolutional Neural Network (CNN).

## Overview

The project starts with a basic fully connected neural network and then extends the implementation to a CNN to improve image classification performance.

Both models are trained and evaluated on the MNIST dataset containing handwritten digits from **0 to 9**.

## Technologies Used

* Python
* PyTorch
* Torchvision
* Matplotlib

## Models

### 1. Fully Connected Neural Network

**File:** `mnist_classifier.py`

Architecture:

```text
28 × 28 Image
     ↓
Flatten
     ↓
784 → 128
     ↓
ReLU
     ↓
128 → 64
     ↓
ReLU
     ↓
64 → 10
```

**Test Accuracy: 97.55%**

### 2. Convolutional Neural Network

**File:** `cnn_classifier.py`

Architecture:

```text
28 × 28 Image
     ↓
Conv2d (1 → 32)
     ↓
ReLU
     ↓
MaxPool
     ↓
Conv2d (32 → 64)
     ↓
ReLU
     ↓
MaxPool
     ↓
Flatten
     ↓
3136 → 128
     ↓
ReLU
     ↓
128 → 10
```

**Test Accuracy: 99.29%**

## Model Comparison

| Model                          | Architecture                   | Test Accuracy |
| ------------------------------ | ------------------------------ | ------------: |
| Fully Connected Neural Network | Linear layers                  |    **97.55%** |
| CNN                            | Convolution + Pooling + Linear |    **99.29%** |

The CNN achieved a **1.74 percentage-point improvement** over the fully connected neural network.

## Training Configuration

Both models were trained using:

* Dataset: MNIST
* Batch Size: 64
* Epochs: 5
* Optimizer: Adam
* Learning Rate: 0.001
* Loss Function: Cross Entropy Loss
* Device: CPU

## Example Prediction

The models can also be used to predict individual handwritten digits from the MNIST test dataset.

Example:

```text
Actual Label: 6
Model Prediction: 6
```

## Project Structure

```text
MNIST-Classifier/
│
├── mnist_classifier.py
├── cnn_classifier.py
├── README.md
├── requirements.txt
└── .gitignore
```

The MNIST dataset and trained model weights are excluded from the repository using `.gitignore`.

## How to Run

Install the required dependencies:

```bash
pip install torch torchvision matplotlib
```

Run the fully connected neural network:

```bash
python mnist_classifier.py
```

Run the CNN:

```bash
python cnn_classifier.py
```

The MNIST dataset will be downloaded automatically when the scripts are executed.

## Key Learning Outcomes

Through this project, I practiced:

* Loading and preprocessing image datasets
* Using PyTorch `Dataset` and `DataLoader`
* Building neural networks with `nn.Module`
* Working with `Linear` layers
* Understanding `Conv2d`
* Using `ReLU` and `MaxPool2d`
* Implementing training loops
* Forward propagation and backpropagation
* Loss calculation and optimization
* Model evaluation and accuracy
* Saving trained model weights
* Comparing different neural network architectures

## Future Improvements

* Experiment with different CNN architectures
* Increase training epochs
* Add data augmentation
* Visualize model predictions
* Build a handwritten digit prediction interface
* Experiment with GPU acceleration
