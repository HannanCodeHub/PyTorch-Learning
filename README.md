# Tensors & Setup

This folder contains my PyTorch fundamentals and hands-on practice while learning the basics of deep learning with PyTorch.

## Topics Covered

### 1. PyTorch Tensor Basics

**File:** `tensors_basics.py`

Covers the fundamentals of PyTorch tensors, including:

* Creating tensors
* Tensor shapes and dimensions
* Tensor data types
* Tensor indexing and slicing
* Tensor operations
* Reshaping tensors
* Basic tensor manipulation

### 2. Gradient Descent

**File:** `gradient_descent.py`

Covers the fundamentals of optimization and gradient-based learning, including:

* Gradient descent
* Loss calculation
* Gradients
* Parameter updates
* Learning rate
* Understanding how a model minimizes its loss

### 3. Basic Neural Network

**File:** `neural_network.py`

Implements a simple neural network using PyTorch and covers:

* `nn.Module`
* `__init__()`
* `forward()`
* `nn.Linear`
* `MSELoss`
* Adam optimizer
* Forward propagation
* Backpropagation
* `zero_grad()`
* `loss.backward()`
* `optimizer.step()`
* Training over multiple epochs

The neural network is trained to learn a simple relationship between input and output.

## Files

```text
Tensors&Setup/
│
├── tensors_basics.py
├── gradient_descent.py
├── neural_network.py
└── README.md
```

## Purpose

The purpose of this folder is to build a strong foundation in PyTorch by understanding tensors, optimization, gradients, and the basic workflow of training neural networks.

## Learning Progression

```text
PyTorch Setup
      ↓
Tensors
      ↓
Gradient Descent
      ↓
Neural Networks
      ↓
MNIST Classifier
      ↓
CNNs & Advanced Deep Learning
```

This folder represents the foundational stage of my PyTorch learning journey before moving on to complete deep learning projects.

## Next Steps

* Datasets and DataLoaders
* Convolutional Neural Networks (CNNs)
* Model evaluation
* Model saving and loading
* GPU acceleration
* Advanced neural network architectures
