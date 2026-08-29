# PyTorch Learning

A hands-on learning repository for understanding the fundamentals of **PyTorch and Deep Learning** through practical Python implementations.

This repository documents my learning progression from basic PyTorch tensors and gradient descent to neural networks and CNN fundamentals.

## Topics Covered

### 1. Tensor Basics

**File:** `tensors_basics.py`

This file covers the fundamentals of PyTorch tensors and basic tensor operations.

Topics include:

* Creating tensors
* Tensor shapes and dimensions
* Tensor data types
* Tensor indexing and slicing
* Tensor operations
* Arithmetic operations
* Reshaping tensors
* Basic tensor manipulation

---

### 2. Gradient Descent

**File:** `gradient_descent.py`

This file explores the fundamentals of gradient-based optimization and how parameters are updated during model training.

Topics include:

* Gradient descent
* Loss calculation
* Gradients
* Learning rate
* Parameter updates
* Minimizing loss
* Understanding the optimization process

---

### 3. Basic Neural Network

**File:** `neural_network.py`

This file implements a simple fully connected neural network using PyTorch.

Topics include:

* `nn.Module`
* `__init__()`
* `forward()`
* `nn.Linear`
* `ReLU`
* `MSELoss`
* Adam optimizer
* Forward propagation
* Backpropagation
* `zero_grad()`
* `loss.backward()`
* `optimizer.step()`
* Training over multiple epochs

The model demonstrates the basic workflow of creating, training, and optimizing a neural network.

---

### 4. CNN Convolution & Pooling Basics

**File:** `cnn_visions.py`

This file introduces the fundamental operations used in Convolutional Neural Networks by working with image tensors and observing changes in their dimensions.

Topics include:

* Creating image tensors
* `nn.Conv2d`
* `in_channels`
* `out_channels`
* `kernel_size`
* `stride`
* `padding`
* Convolution output dimensions
* `nn.MaxPool2d`
* Pooling operations
* Feature maps
* Changes in tensor shapes

#### Convolution Example

```text
Input Image
(1, 1, 28, 28)
       ↓
    Conv2d
       ↓
Output Image
(1, 8, 26, 26)
```

A single-channel `28 × 28` image is passed through a convolution layer with **8 output channels**, producing 8 feature maps.

#### Pooling Example

```text
Before Pooling
(1, 8, 28, 28)
       ↓
   MaxPool2d(2)
       ↓
After Pooling
(1, 8, 14, 14)
```

Max pooling reduces the spatial dimensions while keeping the number of channels unchanged.

---

## Repository Structure

```text
PyTorch-Learning/
│
└── Tensors&Setup/
    │
    ├── tensors_basics.py
    ├── gradient_descent.py
    ├── neural_network.py
    └── cnn_visions.py
```

## Learning Progression

```text
PyTorch Fundamentals
        ↓
      Tensors
        ↓
 Gradient Descent
        ↓
Neural Networks
        ↓
Convolution
        ↓
    Pooling
        ↓
 CNN Fundamentals
```

## Technologies Used

* Python
* PyTorch
* Torchvision
* Matplotlib

## Purpose

The purpose of this repository is to build a strong practical foundation in PyTorch and understand the core concepts behind deep learning.

Each topic is implemented through small experiments and examples to understand how PyTorch components work rather than only studying the theory.

## Next Steps

* Build complete CNN architectures
* Work with PyTorch datasets and DataLoaders
* Train image classification models
* Learn model evaluation techniques
* Save and load trained models
* Explore GPU acceleration with CUDA
* Experiment with more advanced deep learning architectures
