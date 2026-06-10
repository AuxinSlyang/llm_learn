---
type: paper_note
title: ImageNet Classification with Deep Convolutional Neural Networks
short_name: AlexNet
url: https://proceedings.neurips.cc/paper_files/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf
local_pdf: ./AlexNet_ImageNet_Classification_with_Deep_CNNs.pdf
track: CV foundation
read_mode: Background Scan
status: downloaded
created: 2026-06-09
---

# AlexNet - QUICK READ

## Position

AlexNet 是现代深度 CNN 在 ImageNet 上爆发的标志性论文。它不是我们近期精读重点，但它解释了为什么深度卷积网络成为视觉 backbone 的起点。

前置概念：先看 `../00_CNN_Primer.md` 和 `../LeNet5_Gradient_Based_Learning_Applied_to_Document_Recognition/QUICK_READ.md`，理解 convolution、local receptive field、weight sharing、feature map、pooling 和早期 CNN 架构。

## Key Ideas

- 大规模 ImageNet 分类推动视觉表征学习。
- 深 CNN + ReLU + dropout + data augmentation + GPU training。
- 视觉模型从手工特征转向端到端学习特征。

## Quick Understanding

This paper is not trying to invent CNN from scratch. LeNet already showed that convolutional networks can learn visual features for small, clean digit images.

AlexNet asks a bigger question:

```text
Can a deep CNN scale to real natural images, large datasets, and 1000-way object classification?
```

The answer is yes, if several things come together:

```text
ImageNet-scale data
+ a much deeper / wider CNN
+ GPU training
+ ReLU for faster optimization
+ data augmentation to reduce overfitting
+ dropout in fully connected layers
```

So the paper is best read as a scale-up moment:

```text
LeNet:
  small grayscale digits -> CNN works

AlexNet:
  large RGB natural images -> deep CNN becomes a serious visual backbone
```

The main task is ImageNet classification:

```text
input: natural image
output: one of 1000 object categories
metric: top-1 / top-5 classification error
```

The architecture is roughly:

```text
image
-> convolution / pooling stack
-> fully connected classifier
-> 1000-way softmax
```

For first-pass reading, focus on:

- why large-scale supervised data changed vision;
- why deeper CNNs became useful after GPU / ReLU / regularization;
- how learned visual features replaced hand-engineered feature pipelines;
- why this became the starting point for later visual backbones.

Skip on first pass:

- exact local response normalization details;
- two-GPU split engineering;
- every hyperparameter in the training section.

## Abstract + Introduction Understanding

Yes, this can be understood as a very large/deep CNN for 1000-way ImageNet classification.

More precisely, the paper trains a large CNN on the ImageNet LSVRC-2010 subset:

```text
data: about 1.2M training images
classes: 1000 object categories
model: 5 convolutional layers + 3 fully connected layers
output: 1000-way softmax
scale: about 60M parameters
```

The abstract's main claim is:

```text
large deep CNN + ImageNet-scale data + GPU implementation
beats previous state of the art by a large margin
```

The Introduction gives the logic:

1. Object recognition already depends on machine learning, but small datasets are not enough for realistic objects.
2. Real-world objects vary by pose, background, lighting, texture, scale, and viewpoint, so models need much more data.
3. ImageNet provides the scale: millions of labeled images and many categories.
4. A high-capacity model is needed, but the model also needs image-specific inductive bias.
5. CNNs provide that bias through locality and stationarity: local pixels are related, and similar visual patterns can appear anywhere.
6. Historically, CNNs were too expensive for high-resolution large-scale images; GPUs made this practical.

So the paper's key insight is not simply "make CNN deeper". It is:

```text
large supervised visual dataset
+ high-capacity CNN with the right image priors
+ enough GPU compute
+ training/regularization tricks
= scalable learned visual representation
```

The core contributions named in the introduction:

- trained one of the largest CNNs of that time on ImageNet competition data;
- used a highly optimized GPU implementation;
- used architectural/training choices such as ReLU, multi-GPU training, local response normalization, overlapping pooling;
- used data augmentation and dropout to control overfitting;
- showed depth mattered: removing convolutional layers hurt performance.

For our reading path, the most important bridge is:

```text
LeNet proves CNN works for small clean digits.
AlexNet proves deep CNN works for large natural-image recognition.
ResNet later solves how to make deep CNNs much deeper and easier to train.
ViT later asks whether image patches can be treated as tokens instead of using CNN locality bias.
```

## Dataset - ImageNet / ILSVRC

The dataset in this paper is ImageNet, more specifically the ILSVRC-2010 ImageNet classification benchmark.

ImageNet itself is a large labeled image database organized around object categories, originally much larger than the specific competition subset:

```text
ImageNet:
  many object categories
  millions of labeled natural images
  labels organized around WordNet-style object concepts
```

The paper uses the competition subset:

```text
ILSVRC-2010:
  1000 object classes
  about 1.2M training images
  50K validation images
  150K test images
```

Each example is:

```text
input: one natural RGB image
label: one object category out of 1000
```

The classification target is single-label 1000-way classification, even though real images may contain multiple objects. The model is trained to output a probability distribution over 1000 classes through a final softmax.

The images have variable resolutions, so the paper resizes them before training:

```text
resize so the shorter side is 256 pixels
train on fixed-size crops from the resized image
subtract the mean image / mean pixel activity
```

Why this dataset mattered:

```text
small datasets:
  models can overfit and may not need strong learned visual features

ImageNet-scale dataset:
  enough variation to train high-capacity CNNs
  enough categories to force general visual feature learning
  large enough benchmark to reveal the advantage of deep learned representations
```

For our roadmap, ImageNet is the supervised vision pretraining ancestor of later visual backbones:

```text
ImageNet:
  image -> object category

CLIP:
  image -> aligned with natural language text

VLM / VLA:
  image / video / robot observation -> language/action-conditioned representation
```

## Section Map

Recommended reading mode for this paper: structured quick read.

```text
Abstract:
  claim the result and scale: 1.2M images, 1000 classes, large CNN, much lower error.

1. Introduction:
  why large-scale object recognition needs large data, high-capacity models, CNN priors, and GPU compute.

2. The Dataset:
  ImageNet / ILSVRC setup: 1000 classes, train/val/test split, preprocessing.

3. The Architecture:
  the core method section. Read all subsections conceptually.

  3.1 ReLU Nonlinearity:
    faster training than saturating activations.

  3.2 Training on Multiple GPUs:
    engineering solution for compute/memory limits; not conceptually central today.

  3.3 Local Response Normalization:
    historical normalization trick; understand as lateral competition / brightness normalization, then move on.

  3.4 Overlapping Pooling:
    max-pooling windows overlap; slightly improves generalization.

  3.5 Overall Architecture:
    5 conv + 3 fully connected layers + 1000-way softmax.

4. Reducing Overfitting:
  data augmentation and dropout. Important because the model has about 60M parameters.

5. Details of Learning:
  SGD, momentum, weight decay, learning-rate schedule, initialization. Useful but first pass can skim.

6. Results:
  ImageNet competition results and ablations. Read top-1/top-5 improvement and depth importance.

7. Discussion:
  why scale/depth mattered and why more compute/data could improve further.
```

First-pass priority:

```text
must understand:
  Section 1, 2, 3.1, 3.5, 4, 6

can skim:
  3.2, 3.3, 3.4, 5
```

## Architecture Understanding

Yes, this section is mainly the network architecture.

But for AlexNet, "architecture" should be understood at two levels:

```text
network architecture:
  how layers are connected

training / system architecture:
  what tricks make this large CNN trainable on ImageNet
```

The network itself is:

```text
input image crop
-> conv1
-> pooling / normalization
-> conv2
-> pooling / normalization
-> conv3
-> conv4
-> conv5
-> pooling
-> fc6
-> fc7
-> fc8
-> 1000-way softmax
```

The paper summarizes it as:

```text
5 convolutional layers
+ 3 fully connected layers
= 8 learned layers
```

Mental model:

```text
early conv layers:
  detect local low-level visual patterns such as edges, colors, textures

middle conv layers:
  combine low-level patterns into object parts / motifs

late conv layers:
  produce higher-level spatial visual features

fully connected layers:
  integrate features globally and classify into 1000 categories
```

Compared with LeNet:

```text
LeNet:
  small grayscale input
  shallow CNN
  10 digit classes

AlexNet:
  RGB natural images
  much larger/deeper CNN
  1000 object classes
  much more data and compute
```

Important architecture/training components:

```text
ReLU:
  non-saturating activation; speeds up training compared with tanh/sigmoid

max pooling:
  reduces spatial resolution and gives some local translation robustness

local response normalization:
  historical trick; not essential for first-pass understanding

dropout:
  used in fully connected layers to reduce overfitting

data augmentation:
  random crops / flips / color perturbations to increase effective data

GPU split:
  engineering necessity at the time; two GPUs split the network/model
```

For first-pass reading, the core is not the exact layer dimensions. The core is:

```text
large natural image dataset
-> deep convolutional feature extractor
-> global classifier
-> regularized and accelerated enough to train
```

This is why AlexNet becomes the ancestor of the modern visual encoder idea:

```text
image
-> visual backbone
-> feature representation
-> downstream classifier / detector / VLM / policy
```

## Section 3 - Detailed Architecture Breakdown

Section 3 is the core method section. It is partly network architecture and partly training/infrastructure architecture.

### 3.1 ReLU Nonlinearity

Problem:

```text
large neural nets with tanh / sigmoid train slowly
```

Reason:

```text
sigmoid / tanh can saturate
-> gradients become small
-> training slows down
```

AlexNet uses ReLU:

```text
f(x) = max(0, x)
```

Formula reminders:

```text
sigmoid(x) = 1 / (1 + exp(-x))
tanh(x) = (exp(x) - exp(-x)) / (exp(x) + exp(-x))
ReLU(x) = max(0, x)
```

Intuition:

```text
positive activation:
  pass through directly

negative activation:
  clamp to zero
```

Why it mattered:

```text
faster optimization
less saturation
sparser activations
made large/deep CNN training more practical
```

What to remember:

```text
ReLU is not just a minor activation choice here.
It is one of the reasons the large CNN trains fast enough to be useful.
```

Why nonlinearity is critical:

```text
linear layer:
  z = W x + b

activation:
  a = phi(z)

next layer:
  z2 = W2 a + b2
```

If there is no nonlinear activation, stacking layers does not buy much:

```text
z1 = W1 x
z2 = W2 z1 = W2 W1 x
```

The two layers collapse into one linear layer:

```text
W_combined = W2 W1
z2 = W_combined x
```

So without nonlinearities, a deep network is still basically one big linear transformation. It cannot build complex decision boundaries or hierarchical feature composition.

With nonlinearities, each layer can transform the representation:

```text
edge response
-> ReLU gate
-> combine active edges into corners/textures
-> ReLU gate
-> combine into parts
-> combine into object-level features
```

For CNNs, convolution itself is also a linear operation:

```text
kernel dot image patch + bias
```

ReLU turns the convolution response into a nonlinear feature detector:

```text
if feature is present strongly:
  keep the positive response

if feature is absent / negative:
  clamp to zero
```

Why ReLU is better than sigmoid/tanh for AlexNet:

```text
sigmoid / tanh:
  saturate for large positive or negative inputs
  derivative becomes very small
  gradients shrink through many layers

ReLU:
  positive side does not saturate
  derivative is 1 for x > 0
  active units pass gradients more directly
```

This is why ReLU mattered for training a much larger/deeper CNN on ImageNet.

More precise comparison:

```text
sigmoid:
  output range: (0, 1)
  derivative max: 0.25
  problem 1: saturates on both sides
  problem 2: not zero-centered, so optimization can zig-zag

tanh:
  output range: (-1, 1)
  derivative max: 1 near zero
  better than sigmoid because it is zero-centered
  still saturates for large positive/negative inputs

ReLU:
  output range: [0, infinity)
  derivative: 1 for x > 0, 0 for x < 0
  positive side does not saturate
  cheap to compute
  creates sparse activations
```

The key issue for deep networks is the chain rule:

```text
gradient through many layers
= product of many local derivatives
```

If many local derivatives are small, the product becomes tiny:

```text
0.25 * 0.25 * 0.25 * ... -> vanishing gradient
```

ReLU keeps the derivative as `1` on active units, so gradients can pass through active paths much more easily. This is why AlexNet reports much faster training with ReLU than with equivalent tanh units.

So the right conclusion is:

```text
sigmoid/tanh are not impossible.
They are just a poor fit for training a large, deep ImageNet CNN quickly.
ReLU is a simpler optimization-friendly activation.
```

### 3.2 Training on Multiple GPUs

Problem:

```text
the model is too large / expensive for one GPU of that era
```

AlexNet splits the network across two GPUs. Each GPU stores and computes part of the feature maps / kernels, and the GPUs communicate only at certain layers.

Why this matters:

```text
this is an early example of model parallelism
```

In modern terms:

```text
one model is partitioned across devices
because compute / memory on one device is not enough
```

For first-pass reading:

```text
understand the infra reason
do not memorize the exact GPU connection pattern
```

Roadmap connection:

```text
AlexNet already shows that model architecture and hardware constraints co-evolve.
This later becomes central in LLM training/inference infra.
```

More complete view:

AlexNet's two-GPU training is not data parallelism. It is closer to model parallelism.

Data parallelism would be:

```text
GPU 1:
  full model copy, batch shard A

GPU 2:
  full model copy, batch shard B

after backward:
  synchronize gradients
```

AlexNet does something different:

```text
GPU 1:
  stores/computes one part of the model

GPU 2:
  stores/computes another part of the model

selected layers:
  exchange activations across GPUs
```

The reason was practical:

```text
single GTX 580:
  limited memory and compute

AlexNet:
  about 60M parameters
  large conv activations
  ImageNet-scale training
```

The paper's split can be remembered as:

```text
split channels / kernels across two GPUs
communicate only where needed
avoid all-to-all communication at every layer
```

In CNN terms:

```text
some layers:
  grouped connections within each GPU

some layers:
  cross-GPU connections to mix information

fully connected layers:
  eventually integrate global information
```

Why this is historically interesting:

```text
not the first use of GPUs for neural networks
not the first distributed training idea
but a very visible proof that GPU-trained deep CNNs could win at ImageNet scale
```

Earlier related examples include GPU-accelerated deep learning and GPU CNN work before AlexNet. AlexNet's importance is that it combined:

```text
large supervised vision data
+ large CNN
+ GPU implementation
+ engineering-aware model split
-> breakthrough ImageNet result
```

Modern connection:

```text
AlexNet two-GPU split:
  early model parallelism due to memory/compute limits

modern LLM training:
  data parallelism + tensor parallelism + pipeline parallelism + ZeRO/FSDP

same theme:
  model scale is constrained by hardware,
  so architecture and systems design must co-evolve
```

### 3.3 Local Response Normalization

Problem they were trying to solve:

```text
encourage competition between nearby feature maps
make strong activations stand out
improve generalization slightly
```

The rough operation:

```text
activation of one channel
is divided by a function of neighboring channels' squared activations
at the same spatial location
```

Intuition:

```text
if several nearby feature maps fire strongly at the same location,
normalization makes them compete
```

This was inspired by biological / lateral inhibition style intuition.

Modern reading:

```text
historical trick
not the main transferable idea
mostly replaced by BatchNorm / LayerNorm / better training recipes later
```

For first pass:

```text
know that LRN is a normalization / competition mechanism
do not spend time memorizing the formula
```

### 3.4 Overlapping Pooling

Pooling does two things:

```text
reduce spatial resolution
keep strong local responses
add some local translation robustness
```

Non-overlapping pooling:

```text
pool size = stride
windows do not overlap
```

Overlapping pooling:

```text
pool size > stride
neighboring pooling windows overlap
```

AlexNet uses overlapping max pooling. The point is not conceptually huge, but it slightly improves performance and reduces overfitting.

Mental model:

```text
regular pooling:
  summarize disjoint local blocks

overlapping pooling:
  summarize local blocks with smoother coverage
```

For first pass:

```text
understand it as a small regularization/generalization trick
not the main contribution
```

### 3.5 Overall Architecture

This is the part that matters most.

High-level architecture:

```text
input image crop
-> conv1
-> max-pool / LRN
-> conv2
-> max-pool / LRN
-> conv3
-> conv4
-> conv5
-> max-pool
-> fc6
-> fc7
-> fc8
-> 1000-way softmax
```

Layer-level rough shape:

```text
conv1:
  96 filters, large receptive field, early low-level features

conv2:
  256 filters, richer local combinations

conv3:
  384 filters, higher-level visual features

conv4:
  384 filters

conv5:
  256 filters

fc6 / fc7:
  4096-dimensional global feature layers

fc8:
  1000-way classifier
```

The important architecture pattern:

```text
spatial feature extraction:
  convolution + pooling stack

global decision:
  fully connected classifier
```

This is still the template of many later supervised vision models:

```text
visual backbone
-> feature vector / feature map
-> task head
```

What changed later:

```text
VGG:
  simpler, deeper small-conv stack

ResNet:
  residual connections make much deeper CNNs trainable

ViT:
  replace CNN locality bias with patch tokens + Transformer

CLIP / VLM:
  replace 1000-way closed-label classifier with image-text representation learning
```

### AlexNet Core Format / Shape Intuition

The core format is:

```text
image tensor
-> repeated conv feature extraction
-> spatial downsampling
-> flatten
-> fully connected classification head
-> 1000-way softmax
```

Using the common `227 x 227 x 3` shape convention for intuition:

```text
input:
  227 x 227 x 3 RGB image crop

conv1:
  11 x 11 kernels, stride 4, 96 output channels
  -> 55 x 55 x 96

max pool:
  3 x 3, stride 2
  -> 27 x 27 x 96

conv2:
  5 x 5 kernels, 256 output channels
  -> 27 x 27 x 256

max pool:
  3 x 3, stride 2
  -> 13 x 13 x 256

conv3:
  3 x 3 kernels, 384 output channels
  -> 13 x 13 x 384

conv4:
  3 x 3 kernels, 384 output channels
  -> 13 x 13 x 384

conv5:
  3 x 3 kernels, 256 output channels
  -> 13 x 13 x 256

max pool:
  3 x 3, stride 2
  -> 6 x 6 x 256

flatten:
  6 * 6 * 256 = 9216

fc6:
  4096

fc7:
  4096

fc8:
  1000

softmax:
  probability distribution over 1000 ImageNet classes
```

The exact shape convention can vary slightly across implementations because of the historical `224` vs `227` crop detail. For first-pass reading, the important structure is:

```text
large early receptive field
-> progressively richer channels
-> progressively smaller spatial map
-> global classifier
```

Toy example with smaller numbers:

```text
input:
  8 x 8 x 3 toy RGB image

conv1:
  four 3 x 3 x 3 filters
  -> each filter slides over the image
  -> output: 6 x 6 x 4 feature maps

ReLU:
  negative responses become 0
  -> still 6 x 6 x 4

max pool:
  2 x 2 window, stride 2
  -> output: 3 x 3 x 4

conv2:
  eight 3 x 3 x 4 filters
  -> output: 1 x 1 x 8

flatten:
  8 numbers

fc:
  8 -> 5 toy classes

softmax:
  probabilities for 5 classes
```

This toy network has the same conceptual pattern as AlexNet:

```text
local patch detectors
-> nonlinearity
-> downsampling
-> deeper feature combination
-> classifier
```

### Multi-GPU Split Intuition

AlexNet's multi-GPU design is model parallelism.

Instead of copying the whole model to two GPUs, it splits feature maps / filters across them:

```text
GPU 1:
  handles one group of channels / kernels

GPU 2:
  handles another group of channels / kernels
```

Some layers communicate across GPUs, and some layers mostly stay within each GPU's own channel group.

Toy example:

```text
conv1 output:
  96 channels

split:
  GPU 1 gets channels 1..48
  GPU 2 gets channels 49..96
```

Then a grouped convolution can do:

```text
GPU 1:
  conv filters only look at GPU 1's 48 channels

GPU 2:
  conv filters only look at GPU 2's 48 channels
```

At selected layers, the groups communicate so the network can mix information across GPUs.

Modern interpretation:

```text
not data parallel:
  each GPU does not have a full copy of the model

model parallel:
  the model itself is split across GPUs
```

This was necessary because the model and activations were large for the hardware of the time.

### Overlapping Pooling Toy Example

Max pooling takes the largest value in a local window.

Non-overlapping pooling:

```text
pool size = 2
stride = 2
```

Example 4 x 4 feature map:

```text
1  3  2  4
5  6  1  2
0  2  8  1
3  1  4  7
```

Non-overlap 2 x 2 pooling gives:

```text
max(1,3,5,6)=6    max(2,4,1,2)=4
max(0,2,3,1)=3    max(8,1,4,7)=8

=> 6 4
   3 8
```

Overlapping pooling means:

```text
pool size > stride
```

For example:

```text
pool size = 3
stride = 2
```

Windows overlap because the next window starts before the previous one fully ends. On a larger feature map, this makes the summary smoother and gives nearby features more shared context.

AlexNet uses overlapping max pooling as a small generalization improvement, not as the main architectural idea.

### Pool vs Norm

Pooling and normalization are doing different things.

Pooling operates mainly over the spatial dimensions:

```text
height x width
```

Normalization in AlexNet's LRN operates mainly across nearby channels at the same spatial location:

```text
channels / feature maps
```

#### What Pooling Does

Max pooling asks:

```text
In this small spatial neighborhood, what is the strongest response?
```

Example:

```text
2 x 2 patch:

1  3
5  2

max pool -> 5
```

So pooling compresses local spatial information:

```text
many nearby activations -> one representative activation
```

Why useful:

```text
1. reduce spatial resolution
   less compute and smaller feature maps

2. preserve strongest local evidence
   if an edge/texture detector fires strongly nearby, keep it

3. add small translation tolerance
   if the object/edge shifts slightly inside the pooling window,
   the pooled output may stay similar
```

Toy example:

```text
feature detector fires here:

0 0 0 0
0 9 0 0
0 0 0 0
0 0 0 0

if it shifts slightly:

0 0 0 0
0 0 9 0
0 0 0 0
0 0 0 0
```

After pooling, both may produce a similar strong local summary. This makes the model less fragile to tiny shifts.

The tradeoff:

```text
pooling loses exact position detail
but gains compactness and robustness
```

#### What AlexNet's Norm Does

AlexNet's `norm` is Local Response Normalization, not modern LayerNorm.

It asks:

```text
At this same spatial position, are several channels firing strongly?
If yes, make them compete.
```

Toy channel example at one pixel location:

```text
channel activations:
  c1 = 1
  c2 = 10
  c3 = 2
  c4 = 8
  c5 = 1
```

LRN divides each activation by a term based on nearby channels' squared activations. Strong neighbors increase the denominator, so responses are suppressed relative to each other.

Intuition:

```text
pooling:
  choose strong response over nearby spatial positions

LRN:
  make nearby feature channels compete at the same spatial position
```

Your "numerical stability" intuition is closer to modern normalization layers such as BatchNorm / LayerNorm. AlexNet's LRN can help scale activations, but the paper's motivation is more about local competition / lateral inhibition and slightly better generalization.

Modern shortcut:

```text
pool:
  spatial downsampling / local invariance

LRN:
  historical channel-wise response competition

BatchNorm / LayerNorm:
  more directly about stabilizing distributions and optimization
```

### Full Toy Flow: Conv -> ReLU -> LRN -> Pool -> Classifier

Use a tiny grayscale image to see the whole flow. Real AlexNet is RGB and much larger, but the mechanics are the same.

Input:

```text
5 x 5 x 1 image

1  1  0  0  0
1  1  0  2  2
0  0  0  2  2
0  3  3  0  0
0  3  3  0  0
```

Suppose `conv1` has two `3 x 3` filters:

```text
filter A: detects upper-left block-ish pattern
filter B: detects lower-left block-ish pattern
```

After convolution, we get two `3 x 3` feature maps:

```text
channel A:
  4   2  -1
  1   0  -2
 -1  -2  -3

channel B:
 -2  -1  -1
  1   3   1
  2   6   3
```

Then ReLU:

```text
negative values -> 0
positive values stay
```

```text
channel A after ReLU:
  4  2  0
  1  0  0
  0  0  0

channel B after ReLU:
  0  0  0
  1  3  1
  2  6  3
```

Now LRN. At each spatial location, LRN looks across channels.

For example, at center position `(row=2, col=2)`:

```text
channel A value = 0
channel B value = 3
```

If channel B fires strongly and nearby channels also fire, LRN reduces the response by a denominator based on nearby channel activations.

The AlexNet-style formula is:

```text
b_i(x, y) =
  a_i(x, y) /
  (k + alpha * sum_j a_j(x, y)^2) ^ beta
```

Where:

```text
a_i:
  activation of channel i before normalization

b_i:
  activation after normalization

sum_j:
  nearby channels around i at the same spatial position

k, alpha, beta:
  constants controlling how strong the normalization is
```

AlexNet uses this across nearby channels, not across nearby spatial pixels.

Simplified numeric intuition:

```text
same spatial location, five channels:

c1 = 1
c2 = 2
c3 = 10
c4 = 2
c5 = 1
```

If we normalize `c3`, nearby channels have large squared activity:

```text
sum squares = 1^2 + 2^2 + 10^2 + 2^2 + 1^2
            = 110
```

The denominator becomes larger, so:

```text
c3 after norm < 10
```

The exact number is less important than the effect:

```text
strong activation remains strong,
but is damped when neighboring channels also fire strongly.
```

Then pooling. Suppose after ReLU/LRN one channel is:

```text
4  2  0
1  0  0
0  0  0
```

Using `2 x 2` max pooling with stride `1` for a tiny overlapping example:

```text
window 1:
4 2
1 0
max = 4

window 2:
2 0
0 0
max = 2

window 3:
1 0
0 0
max = 1

window 4:
0 0
0 0
max = 0
```

Output:

```text
4 2
1 0
```

This is pooling's job:

```text
keep the strongest local evidence
reduce / summarize spatial layout
```

Finally, after several conv/ReLU/norm/pool blocks:

```text
feature maps
-> flatten into a vector
-> fully connected layers
-> class scores
-> softmax probabilities
```

Toy classifier output:

```text
cat: 0.05
dog: 0.80
car: 0.10
bird: 0.03
ship: 0.02
```

The whole flow is:

```text
conv:
  detect local patterns

ReLU:
  keep positive evidence, remove negative responses

LRN:
  make nearby channels compete at the same spatial position

pool:
  keep strongest evidence over nearby spatial positions

FC/softmax:
  turn learned visual features into class probabilities
```

### Section 3 Takeaway

Section 3 is not just "the network has 8 layers".

It says:

```text
To scale CNNs to ImageNet, you need:
  architecture depth/capacity
  fast nonlinearity
  pooling/downsampling
  regularization-ish normalization tricks
  hardware-aware parallel training
```

This is why you correctly noticed that some of this is infra: AlexNet is a vision paper, but its success depends heavily on compute and implementation.

### Architecture Correction Checkpoint

Your high-level summary is right:

```text
large image crop
-> conv / ReLU / LRN / pooling feature extractor
-> fully connected classifier
-> softmax over 1000 ImageNet classes
```

The details to keep straight:

```text
input:
  original images have variable sizes
  AlexNet trains on fixed-size crops after resizing
  common clean mental model: 227 x 227 x 3

conv1:
  filters: 96 filters, each 11 x 11 x 3
  stride: 4
  output: 55 x 55 x 96
  then ReLU / LRN / max pool -> 27 x 27 x 96

conv2:
  input: 27 x 27 x 96
  filters: 256 filters, spatial size 5 x 5
  simplified filter depth: 96
  AlexNet grouped two-GPU detail: each group sees part of the channels
  padding: 2
  stride: 1
  output: 27 x 27 x 256
  then pool -> 13 x 13 x 256

conv3:
  filters: 384 filters, spatial size 3 x 3
  padding: 1
  output: 13 x 13 x 384
  no pooling here

conv4:
  filters: 384 filters, spatial size 3 x 3
  padding: 1
  output: 13 x 13 x 384
  no pooling here

conv5:
  filters: 256 filters, spatial size 3 x 3
  padding: 1
  output: 13 x 13 x 256
  then pool -> 6 x 6 x 256

classifier:
  flatten -> 9216
  fc6 -> 4096
  fc7 -> 4096
  fc8 -> 1000 logits
  softmax -> 1000 class probabilities
```

The common mistake is to forget padding. Without padding, `27 x 27` through a `5 x 5` kernel would become `23 x 23`. AlexNet uses padding in conv2, conv3, conv4, and conv5, so the spatial size stays stable through those convolution layers.

Formula:

```text
out = floor((H + 2P - K) / S) + 1
```

For conv2:

```text
H = 27, P = 2, K = 5, S = 1
out = floor((27 + 4 - 5) / 1) + 1 = 27
```

Why later kernel sizes get smaller:

```text
kernel spatial size:
  11 x 11, 5 x 5, 3 x 3

number of filters / output channels:
  96, 256, 384, 384, 256
```

These are different axes. Spatial kernels get smaller because:

```text
early layer:
  feature map is high resolution
  raw pixels are low-level
  large 11 x 11 stride-4 kernel quickly reduces resolution and sees a larger initial patch

later layers:
  feature maps are already lower resolution
  each location already corresponds to a larger receptive field in the original image
  3 x 3 is enough to combine local high-level features
```

Channels increase because higher layers need more detectors:

```text
edges / colors / simple textures
-> corners / motifs / parts
-> object-level visual patterns
```

Compute also matters. A convolution layer's parameter count is roughly:

```text
K x K x C_in x C_out
```

So if later layers used huge spatial kernels while `C_in` and `C_out` were already large, compute and parameters would explode. This is the bridge to VGG later: stack many small `3 x 3` convolutions instead of using very large kernels everywhere.

## Section 4 Preview - Reducing Overfitting

After Section 3, the next natural section is Section 4.

Why it matters:

```text
AlexNet has about 60M parameters
ImageNet is large for 2012, but still finite
large model + finite labeled dataset -> overfitting risk
```

Section 4 has two main tools:

```text
data augmentation:
  create more effective training variation from existing images
  random crops / flips / color perturbation

dropout:
  regularize fully connected layers
  prevent co-adaptation of hidden units
```

For first pass, Section 4 is more important than LRN. It explains why AlexNet could use a high-capacity model without simply memorizing ImageNet.

## Final Takeaways

AlexNet can be understood as an engineering-heavy scale-up of CNNs:

```text
LeNet-style CNN idea
-> much larger natural-image dataset
-> deeper / wider CNN
-> GPU-aware model split
-> ReLU / augmentation / dropout / SGD recipe
-> ImageNet-scale visual representation
```

It is not important because it invented every component from scratch. It is important because it assembled the right components at the right scale:

```text
data scale:
  ImageNet / ILSVRC 1000-way natural image classification

model scale:
  5 convolutional layers + 3 fully connected layers
  about 60M parameters

systems scale:
  two GTX 580 GPUs
  channel / kernel split across GPUs
  cross-GPU communication in selected layers

optimization:
  mini-batch SGD
  momentum
  weight decay
  learning rate decay

regularization:
  data augmentation
  dropout
```

The minimal sentence:

```text
AlexNet proves that a large, GPU-trained CNN can learn useful visual features from ImageNet-scale supervised data.
```

For our VLM / VLA route, the main concept is:

```text
image
-> visual backbone
-> learned visual feature
-> classifier / detector / VLM connector / robot policy input
```

## Follow-up CV Reading Path

Do not expand into a full CV survey. The current path should only support `robot observation -> visual backbone / visual tokens -> VLM / VLA`.

Recommended order:

```text
1. VGG:
   why small 3 x 3 convolutions can be stacked deeper
   bridge from AlexNet's large kernels to cleaner CNN depth

2. GoogLeNet / Inception:
   multi-scale feature extraction and compute-aware architecture
   useful for understanding depth / width / compute tradeoffs

3. ResNet:
   residual connection solves deep CNN optimization difficulty
   most important CNN backbone concept after AlexNet

4. ViT:
   image patches as tokens
   bridge from CNN visual features to Transformer visual tokens

5. Vision Transformers Need Registers:
   attention / feature map artifact and interpretability caution
   support line, not a main backbone paper

6. CLIP:
   image-text contrastive alignment
   turns visual features into open-vocabulary semantic features

7. BLIP-2 / LLaVA:
   connect frozen visual encoders to LLMs
   bridge from VLM to VLA-style systems

8. YOLO:
   real-time object detection awareness
   useful for robot perception / labeling / failure analysis, but not the main VLA path

9. Diffusion vision papers:
   awareness scan only
   mainly to connect image generation intuition with Diffusion Policy later
```

## Why For VLM/VLA

后续所有 vision encoder 都继承了一个基本观念：图像可以先通过深度模型抽成 feature，再接到别的任务上。
