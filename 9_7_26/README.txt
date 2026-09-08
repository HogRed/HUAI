# Building a GAN From Scratch

**Harding University AI Club**  
**Meeting date:** September 7, 2026

## Watch the Meeting

[Watch the full lecture on YouTube](https://youtu.be/A_1UH0RmsLc?si=DBqqAK4mMcsRzCr6)

## Meeting Overview

How does generative AI learn to create something new?

In this meeting, we built a **Generative Adversarial Network (GAN) from scratch** and trained it to generate 8×8 handwritten digits. Instead of relying on a deep-learning framework, we used Python and NumPy to implement the machinery ourselves.

**No PyTorch. No autograd. No GPU.**

The goal was not merely to make a GAN run. We wanted to open the machinery and understand how the model learns.

## What We Built

Our GAN contains two neural networks that learn through competition:

- The **generator** begins with random noise and attempts to create convincing handwritten digits.
- The **discriminator** examines real and generated images and tries to determine which are authentic.

The discriminator learns to become a better detective. The generator receives gradients through the discriminator and learns to create more convincing images. As training continues, initially meaningless noise gradually develops recognizable, digit-like structure.

## What Students Practiced

During the meeting, students explored how to:

- Represent an image as a vector of pixel values
- Normalize image data for neural-network training
- Build a multilayer neural network with NumPy
- Implement forward propagation and backpropagation
- Calculate gradients for weights, biases, and network inputs
- Use Leaky ReLU, sigmoid, and tanh activation functions
- Train with randomized minibatches
- Implement the Adam optimizer from scratch
- Derive the discriminator and generator gradients
- Pass a gradient through the discriminator to train the generator
- Alternate between training two competing neural networks
- Use fixed-noise snapshots to observe learning over time
- Evaluate generated images for structure, quality, and variety

## The Data

We used the handwritten digits dataset included with scikit-learn. Each image is an 8 x 8 grid, giving the network 64 pixel values per example.

Although the dataset includes labels identifying each digit, the GAN does not use them. It is never told whether an image represents a zero, one, seven, or any other digit. It simply studies the collection and learns what handwritten digits tend to look like.

For this instructional demonstration, the complete dataset is used for training. The purpose is to study the GAN training process rather than measure predictive performance on labeled test examples.

## Training at a Glance

Each training step has two parts:

1. **Train the discriminator:** Show it real images and generated images, then update it to become better at telling them apart.
2. **Train the generator:** Create new images, pass them through the discriminator, and send the resulting gradient backward through both networks. Only the generator is updated during this phase.

This alternating process creates the adversarial game at the heart of a GAN.

## Tools Used

- Python
- NumPy
- Matplotlib
- scikit-learn, used only to load the digits dataset
- Google Colab

## Why Build It From Scratch?

Modern frameworks can build a GAN with far less code, but they also hide many of the most interesting ideas. Implementing the system ourselves allowed us to see exactly how batches move through a network, how gradients are calculated, and how one neural network can provide the learning signal for another.

AI Club is not only a place to use artificial intelligence. It is a place to take it apart, examine how it works, and build it ourselves.