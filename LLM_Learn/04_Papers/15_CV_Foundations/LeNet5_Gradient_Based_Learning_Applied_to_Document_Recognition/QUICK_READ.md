---
type: paper_note
title: Gradient-Based Learning Applied to Document Recognition
short_name: LeNet-5
authors: Yann LeCun, Leon Bottou, Yoshua Bengio, Patrick Haffner
venue: Proceedings of the IEEE, 1998
url: http://yann.lecun.com/exdb/publis/pdf/lecun-01a.pdf
local_pdf: ./LeNet5_Gradient_Based_Learning_Applied_to_Document_Recognition.pdf
track: CV foundations / CNN foundation
read_mode: Background Scan
status: downloaded
created: 2026-06-11
---

# LeNet-5 - QUICK READ

## Position

这是 CNN / LeNet-5 的经典入口论文，适合放在 `CNN Primer` 和 `AlexNet` 之间。

读它不是为了深挖手写数字识别系统，而是为了理解 CNN 的早期完整形态：

```text
input image
-> convolution
-> subsampling / pooling
-> more convolution
-> classifier
```

## Why Now

AlexNet、VGG、GoogLeNet、ResNet 都继承了 CNN 的基本语法。LeNet-5 能帮助先建立这些概念：

- local receptive field
- weight sharing
- feature map
- convolution + subsampling
- end-to-end gradient-based learning

## Core Question

能不能少做手工特征工程，让一个可微分模型直接从图像像素学出识别需要的层级特征？

## First-pass Reading Scope

第一轮只看：

- Abstract / Introduction：为什么要端到端学习 document recognition。
- LeNet-5 architecture：卷积层、subsampling、feature maps、classifier。
- 为什么 convolution / shared weights 适合图像。
- 和 AlexNet 的关系：LeNet-5 是小图像/手写数字 CNN；AlexNet 是大规模 ImageNet + GPU + 深 CNN。

第一轮跳过：

- Graph Transformer Networks 的系统细节。
- 银行票据 / 邮件识别生产系统细节。
- 大量实验表格和工程部署细节。

## One-sentence Takeaway

LeNet-5 展示了 CNN 可以通过局部连接、权重共享和端到端梯度学习，从原始图像中学出层级视觉特征，是 AlexNet 之前最清晰的 CNN foundation。

## Section 2 - CNN for Isolated Character Recognition

### Key Architecture

```text
INPUT: 32x32x1
-> C1: 6@28x28 convolution, 5x5 kernels
-> S2: 6@14x14 subsampling, 2x2 stride 2
-> C3: 16@10x10 convolution, 5x5 kernels over selected S2 maps
-> S4: 16@5x5 subsampling, 2x2 stride 2
-> C5: 120@1x1 convolution, 5x5 kernels over all 16 S4 maps
-> F6: 84 fully connected
-> OUTPUT: 10 classes
```

### Shape Intuition

- `32 -> 28`: valid `5x5` convolution gives `32 - 5 + 1 = 28`.
- `28 -> 14`: subsampling halves spatial resolution with `2x2` windows.
- `14 -> 10`: valid `5x5` convolution gives `14 - 5 + 1 = 10`.
- `10 -> 5`: another `2x2` subsampling.
- `16@5x5 -> 120@1x1`: `C5` uses `5x5` kernels across all 16 maps, so it is equivalent to flattening `16 * 5 * 5 = 400` values and projecting to 120 features.

### Concept Clarifications

- A convolution kernel is not a whole MLP. It is a small shared linear filter, plus bias/nonlinearity, applied at every spatial location.
- A convolution layer is equivalent to a sparse linear layer with tied/shared weights.
- The dot product between a convolution kernel and an image patch can be read as a learned template response. It is not the same mechanism as Transformer attention: attention computes data-dependent token-token compatibility, while convolution applies the same learned filter at every spatial position.
- One kernel produces one output feature map; multiple kernels produce multiple feature maps.
- The `16` in `C3` is an architecture choice: 16 output feature maps. It is not computed as `6 x 6`.
- In LeNet-5, each `C3` feature map connects only to a subset of the 6 `S2` maps. Different `C3` maps look at different subsets, such as several selected input maps or all 6 maps. This partial connectivity reduces parameters, breaks symmetry, and lets different maps learn different combinations.
- Subsampling means spatial downsampling: feature maps become smaller while preserving coarse evidence that a feature exists nearby.

### Multi-channel Convolution Toy Example

For an input `14x14x6`, one `C3` detector might choose only 3 of the 6 input maps.

That detector is not a `14x14x3` kernel. It has three small kernels:

```text
K1: 5x5 for selected input map 1
K2: 5x5 for selected input map 2
K3: 5x5 for selected input map 3
```

At each spatial location:

```text
5x5 patch from map 1 dot K1
+ 5x5 patch from map 2 dot K2
+ 5x5 patch from map 3 dot K3
+ bias
= one scalar output
```

Sliding over `14x14` with valid `5x5` convolution gives `10x10`, so this one detector produces one `10x10` output map. Sixteen detectors produce `16@10x10`.

The cross-map sum is the feature fusion step. If a detector connects to 3 input maps, it is asking whether a local pattern composed from those 3 lower-level features is present at the same spatial location. Keeping three separate `10x10` maps would preserve the three separate evidences but would not create one higher-level detector response. Summing learned channel-specific responses plus bias turns several lower-level feature maps into one higher-level feature map.

### Section 2 Summary

- CNN replaces hand-designed character features with a trainable visual feature extractor.
- Its key prior knowledge is architectural: local receptive fields, shared weights, subsampling, and hierarchical composition.
- A convolution output map is a detector response map; a deeper convolution map is a learned fusion of lower-level response maps.
- Subsampling reduces spatial resolution and makes the representation more stable to small shifts and deformations.
- LeNet-5 is best read as `feature extractor + classifier`: `C1/S2/C3/S4/C5` build visual features, `F6/OUTPUT` maps them to digit classes.

### Worth Looking At In Section 2

- `Fig. 2`: LeNet-5 architecture. This is the most important figure for the first pass.
- The C/S notation: `C` means convolution, `S` means subsampling.
- The shape flow: `32x32 -> 6@28x28 -> 6@14x14 -> 16@10x10 -> 16@5x5 -> 120 -> 84 -> 10`.
- The partial connectivity in `C3`: it shows early CNNs already used selective structure instead of fully connecting everything.

Fig. 2 mental model:

```text
local detection
-> spatial downsampling
-> cross-map feature fusion
-> repeated local detection
-> global classification head
```

CNN can be read as a local-to-global feature hierarchy: repeated local checks produce feature maps, subsampling reduces spatial resolution, deeper convolution fuses lower-level maps into higher-level maps, and the final fully connected layers classify the accumulated representation.

### Rest-of-Paper Map

- Section 3: results and comparison on isolated handwritten digit recognition. This is mostly benchmark comparison against other methods of that era.
- Section 4: multi-module systems and Graph Transformer Networks. This generalizes backprop from a single CNN to heterogeneous systems.
- Section 5/6 region: multiple object recognition / heuristic over-segmentation. This moves from isolated characters to strings, candidate cuts, segmentation graphs, recognition transformers, and Viterbi paths.
- Section 7: global training for GTNs. This argues that a whole multi-module recognizer can be trained at the string level without requiring manual labels for each character segment.
- Section 8: Space Displacement Neural Network. This is an alternative to explicit heuristic segmentation: sweep a recognizer across possible locations.
- Later sections: GTN formalization, online handwriting systems, bank-check reading, deployment-oriented document recognition examples, and supporting derivations.

First-pass priority after Section 2: skim Section 3 for why CNN won, then read Section 4 conceptually for GTN/global training. Skip most tables and production-system details unless needed.

### Next Session Plan

Stop point: Section 2 is conceptually complete enough for first pass.

Next morning 60-75m plan:

- 10-15m: skim Section 3. Goal: understand what CNN beats and why this matters historically; skip most tables.
- 40-45m: read Section 4. Goal: understand GTN as a multi-module/global-training framework, not as modern Transformer attention.
- 10-15m: write a short bridge note: `LeNet-5 CNN local feature learning -> GTN global trainable system -> AlexNet scale-up`.

## Section 3 - Results and Comparison

### Section Role

Section 3 is evidence, not a new architecture. It answers:

```text
If CNNs can learn features directly from normalized pixel images,
do they actually beat the feature/classifier pipelines of that era?
```

The authors explicitly use isolated handwritten digit recognition as a benchmark for shape recognition methods, while acknowledging that it is only one subproblem in a practical document-recognition system.

### A. Database: Modified NIST / MNIST

- The dataset is built from NIST Special Database 3 and Special Database 1.
- The original split was problematic because one split was cleaner/easier than the other.
- The authors rebuild the split by mixing sources and separating writers, producing the Modified NIST / MNIST setup.
- Regular MNIST in this paper is `60,000` training examples and `10,000` test examples, size-normalized and centered.

Why it matters:

```text
They are careful about benchmark hygiene:
training/test should not differ just because one source is easier.
```

### B. Results

- Several LeNet-5 variants are trained on regular MNIST.
- Without distortions, LeNet-5 stabilizes around `0.95%` test error.
- Training error continues lower than test error, but they report not observing classic overtraining in this setup.
- Training-set size matters: experiments with `15k`, `30k`, and `60k` examples show that more training data improves accuracy.
- They then use artificial distortions to increase effective training data: translations, scaling, squeezing, and horizontal shearing.
- With distorted training data, test error drops to about `0.8%`.

Why it matters:

```text
CNN structure is important, but data coverage is also important.
Augmentation is already a central idea here.
```

### C. Comparison With Other Classifiers

The paper compares LeNet-style CNNs against a wide spread of methods:

- linear / pairwise linear classifiers
- k-nearest-neighbor over pixels
- PCA + polynomial classifier
- RBF networks
- one-hidden-layer and two-hidden-layer fully connected MLPs
- earlier CNNs such as LeNet-1 and LeNet-4
- boosted LeNet-4
- tangent-distance classifiers
- support vector machines and variants

First-pass interpretation:

- Pixel-space linear methods are weak because the decision boundary is too simple.
- KNN and tangent-distance methods can be strong, but memory and runtime become expensive.
- Fully connected MLPs help, but do not exploit image structure as efficiently as CNNs.
- SVMs are strong and historically important, but expensive and not image-structured in the same way.
- CNNs are competitive because they bake in image priors while keeping the feature extractor trainable.

### D. Discussion

The paper does not claim LeNet-5 is the only good method. Its discussion is more nuanced:

- Boosted LeNet-4 performs best in their comparison, around `0.7%`.
- Distorted LeNet-5 is close, around `0.8%`.
- Accuracy is not the only metric: rejection behavior, multiply-add operations, memory, and training time matter for practical document-recognition systems.
- CNNs are attractive because they combine accuracy, compact memory, regular computation, and hardware-friendly structure.
- Training time can be long for the designer, but inference-time accuracy, speed, and memory matter more to end users.
- Larger recognizers become feasible as compute and data grow; this is a pre-AlexNet version of the scale-up story.

### Core Takeaways For Us

- The paper uses isolated digit recognition as a controlled benchmark, not as the final document-recognition goal.
- It intentionally focuses on adaptive methods that operate directly on size-normalized images, rather than systems that depend heavily on handcrafted features.
- CNNs work because the architecture matches image structure: local fields, shared weights, subsampling, and trainable hierarchy.
- Data augmentation / distortion matters: adding plausible affine distortions improves robustness and tests whether learned features generalize to shifted, scaled, squeezed, or sheared digits.
- The historical message is stronger than the exact table numbers: LeNet-style CNNs made learned feature extraction competitive with the best methods of the era while remaining compact and practical.

### What To Skip

- Do not memorize every classifier and error rate in Fig. 9 / comparison tables.
- Do not spend time on exact optimization details yet; those are support for the result, not the core idea.
- Use Section 3 only to answer: `Why did people take CNNs seriously before AlexNet?`

## Section 4 - Multi-Module Systems and GTN

### Section Role

Section 4 is the conceptual bridge from a single trainable recognizer to a trainable document-recognition system.

```text
Section 2: a CNN can recognize one isolated character.
Section 4: a full document system needs many modules, and those modules should still be trainable together.
```

### 1. Backprop Is More General Than MLPs

The paper first argues that classical backprop is only one instance of gradient-based learning. Gradients can be propagated through any arrangement of functional modules, as long as each module can pass derivatives backward.

This means a trainable system does not need to be a plain stack of linear layers and sigmoids. LeNet-5 is already multi-module:

```text
convolution
subsampling
fully connected layers
RBF / output layer
```

The bigger claim:

```text
large trainable systems should be built from simple specialized modules,
but optimized with a larger task-level objective.
```

### 2. Why Multi-Module Systems?

Real document recognition has more structure than isolated digit classification:

```text
image
-> candidate segmentation
-> candidate characters
-> candidate strings / words
-> best interpretation
```

The system may need to segment and recognize at the same time, and it may not be given the correct segmentation during training.

This is the motivation for modular systems:

- one module proposes candidates
- one module scores characters
- one module combines candidates into possible strings
- one module selects the best interpretation

### 3. Why Graphs Instead of Fixed Vectors?

Traditional neural networks and simple multi-module systems pass fixed-size vectors between layers. That is too limited for:

- variable-length inputs, such as character strings or words
- multiple possible segmentations
- alternative interpretations
- relations among a variable number of objects or features

GTN replaces fixed-size vector communication with directed graphs:

```text
nodes: positions / states / candidate boundaries
arcs: candidate segments, labels, penalties, vectors, or scores
paths: possible interpretations
```

A graph can compactly represent many possible sequences or interpretations at once.

### 4. What Is A Graph Transformer?

A Graph Transformer is a module that takes one or more graphs as input and produces a graph as output.

```text
input graph(s)
-> Graph Transformer module
-> output graph
```

A Graph Transformer Network is a composition of these modules:

```text
Graph Transformer
-> Graph Transformer
-> Graph Transformer
-> loss / best path / interpretation
```

This is not modern self-attention Transformer. Here, `Transformer` means a module that transforms graphs.

### 5. How Does Backprop Work Through GTN?

Modules in a GTN communicate both forward states and backward gradients through graphs.

Forward:

```text
input graph numerical data
-> module parameters
-> output graph numerical data
```

Backward:

```text
gradient on output graph data
-> gradient on input graph data
-> gradient on module parameters
```

The paper's condition is pragmatic: as long as the numerical data on graph arcs are produced by differentiable functions of input graph data and parameters, gradient-based learning can be applied.

### One-Sentence Takeaway

GTN is LeCun's attempt to generalize end-to-end gradient learning from `one CNN classifier` to `a whole structured recognition pipeline` whose intermediate states are graphs of candidates and interpretations.

### Why It Matters For The Roadmap

GTN is historically relevant because it anticipates a problem we still care about:

```text
perception module
-> candidate states / objects / actions
-> structured decision
-> task-level loss
```

For robotics, the analogy is:

```text
camera / sensors
-> perception candidates
-> policy / planner candidates
-> action selection
-> task success / failure
```

The details are old, but the system idea is still useful: do not optimize every module only locally if the final task can provide a better objective.

### Complete Mental Model

Problem:

```text
isolated character recognition:
  one image -> one label

real document recognition:
  one image/string field -> many candidate cuts -> many candidate characters
  -> many candidate strings -> one final interpretation
```

The hard part is not just recognizing a clean character. The hard part is that the system may not know the correct segmentation and may need to compare many possible interpretations.

Graph:

```text
node = a state, position, or candidate boundary
arc = a candidate transition/segment with numerical data
path = one possible interpretation
```

For handwriting, a segmentation graph can represent many possible ways to cut a word or digit string. Each complete path through the graph is one possible segmentation/reading.

Graph Transformer:

```text
input graph
-> module transforms it
-> output graph
```

Examples:

```text
segmentation graph
-> recognition transformer
-> interpretation / recognition graph
-> Viterbi transformer
-> best path
```

The recognition transformer applies a recognizer such as LeNet to candidate image segments on arcs, then attaches class labels and penalties/scores to output arcs.

The Viterbi transformer chooses the best path through the interpretation graph. In this paper's language, lower penalty means a better interpretation.

Training idea:

```text
final loss / penalty
-> gradients on output graph numeric data
-> gradients through graph transformers
-> gradients on recognizer/module parameters
```

The key is that the graph structure can represent variable-length and multi-hypothesis outputs, while the numeric data on graph arcs can still be differentiated.

Toy example:

```text
input image: handwritten "12"

candidate cuts:
  [1][2]
  [12]
  [1?][?2]

segmentation graph:
  arcs correspond to candidate image pieces

recognition transformer:
  each arc image piece -> LeNet scores for 0..9
  output graph arcs carry labels and penalties

Viterbi transformer:
  select the lowest-penalty path
  output: "12"

training:
  if target is "12", penalize paths that do not match
  send gradients back into recognition scores and recognizer parameters
```

### Graph Toy Example In Detail

The graph is not a drawing of the model pipeline. It is a compact representation of many candidate interpretations of the same input.

Suppose an image contains a handwritten `"12"`. A segmentation heuristic proposes possible cut positions:

```text
0 ---- a ---- b ---- end
```

The segmentation graph has nodes for cut positions and arcs for candidate image segments:

```text
0 -> a      maybe the first digit
a -> end    maybe the second digit
0 -> end    maybe the whole ink blob is one digit
0 -> b      maybe a wider first candidate
b -> end    maybe a narrower second candidate
```

Each path from `0` to `end` covers the ink in one possible way:

```text
path 1: 0 -> a -> end      two segments
path 2: 0 -> end           one segment
path 3: 0 -> b -> end      alternative two-segment cut
```

Then a recognition transformer applies LeNet-like recognition to each candidate segment. It replaces each segment arc with labeled arcs carrying penalties:

```text
0 -> a:
  label "1", penalty 0.1
  label "7", penalty 1.4

a -> end:
  label "2", penalty 0.2
  label "3", penalty 1.1

0 -> end:
  label "8", penalty 2.8
  label "2", penalty 3.2
```

A complete path in the interpretation graph now means both a segmentation and a string:

```text
0 -> a("1") -> end("2")     string "12", total penalty 0.3
0 -> end("8")               string "8", total penalty 2.8
0 -> a("7") -> end("3")     string "73", total penalty 2.5
```

The Viterbi transformer chooses the path with the lowest total penalty. If the target is `"12"`, training should lower the penalty of the `"12"` path and/or raise the penalties of competing paths.

This is why a graph is useful: it stores many possible segmentations and label sequences at once, without forcing the system to make a hard segmentation decision before recognition.

### Connection: GTN vs LLM Self-Consistency

GTN has a useful analogy with `Self-Consistency Improves Chain of Thought Reasoning`.

```text
GTN:
  build an explicit graph of candidate segmentations / interpretations
  score paths with trainable modules
  choose the lowest-penalty path, often with Viterbi-style search
  can train module scores with a global objective

Self-Consistency:
  sample multiple reasoning paths from an LLM
  extract final answers
  aggregate / vote / marginalize over answers
  usually no parameter update; it is a test-time decoding strategy
```

Shared idea:

```text
Do not trust a single path.
Generate or keep multiple candidate paths.
Use an aggregation / scoring rule to pick a more reliable final answer.
```

Key difference:

```text
GTN represents candidates explicitly as a graph and can propagate gradients through numeric path scores.
Self-Consistency samples implicit language reasoning paths and selects by answer consistency, usually without backprop.
```

Why this is a real-system idea:

- It avoids requiring perfect hard segmentation before recognition.
- It can train a recognizer to reject bad segments, not only classify clean hand-segmented characters.
- It lets the final task objective influence earlier module scores.
- It generalizes fixed-vector neural nets to variable-size, structured candidate spaces.

## Section 5 - Heuristic Over-Segmentation and Figures 17/18

Section 5 moves from isolated character recognition to character strings. The central problem is segmentation:

```text
clean isolated digit:
  one image crop -> one label

real handwritten string:
  one image strip -> unknown cuts -> unknown number of characters -> one string
```

The important idea is not to make one hard cut too early. Instead, the system deliberately over-segments the input: it proposes many candidate cut points, including wrong ones, and then lets recognition plus global path search choose the best interpretation.

### Fig. 17 - Whole GTN String Recognition Flow

Fig. 17 shows the full string-recognition GTN:

```text
input handwritten string image
-> segmentation graph
-> recognition transformer
-> interpretation / recognition graph
-> Viterbi transformer
-> best path / final string
```

The segmentation graph stores possible candidate cuts and candidate image pieces. Each path through that graph is one possible segmentation of the same handwriting.

The recognition transformer applies a character recognizer to each candidate segment and turns the segmentation graph into an interpretation graph. In that interpretation graph, arcs carry both a class label and a penalty.

The Viterbi transformer then finds the lowest-penalty path. Reading the labels on that path gives the final recognized string.

So Fig. 17 is the global picture: multiple possible segmentations and labels are kept alive until the system can choose the best complete path.

### Fig. 18 - Local Operation of the Recognition Transformer

Fig. 18 zooms into one arc of the segmentation graph.

One segmentation arc means:

```text
this candidate image segment might be one character
```

The recognition transformer runs the character recognizer on that candidate image segment and expands it into many labeled arcs:

```text
candidate segment image
-> recognizer
-> label "0" with penalty p0
-> label "1" with penalty p1
-> ...
-> label "9" with penalty p9
```

Low penalty means the recognizer thinks that label is plausible. High penalty means unlikely. The key is that the segment is not immediately collapsed into a single label; the graph can preserve several alternatives, and later Viterbi/path search chooses the best full sequence.

Toy example:

```text
segmentation arc: image piece x

after recognition transformer:
  x -> "1", penalty 0.2
  x -> "7", penalty 1.6
  x -> "4", penalty 3.1
```

If neighboring arcs make `"12"` much more plausible than `"72"` or `"42"`, global path search can choose the full `"12"` path even if one local decision is ambiguous.

### What Section 5 Is Teaching

The section is worth learning because it teaches a pattern that keeps reappearing in ML systems:

```text
Do not make brittle early decisions.
Represent ambiguity explicitly.
Score alternatives.
Use global search / global objective to select the best interpretation.
```

For this paper, the concrete version is:

```text
candidate cuts
-> segmentation DAG
-> candidate segments
-> recognizer penalties
-> interpretation DAG
-> Viterbi shortest path
-> output string
```

This is very close in spirit to speech recognition, OCR, structured prediction, CTC-style sequence learning, beam search, and even some LLM decoding ideas: keep multiple hypotheses alive, then choose or marginalize using a global score.

For first-pass reading, the must-understand items are:

- hard segmentation is unreliable;
- over-segmentation intentionally produces extra candidate cuts;
- a segmentation graph is a DAG where paths are possible segmentations;
- Fig. 18 explains how each candidate segment becomes labeled alternatives with penalties;
- Fig. 17 explains how the whole graph is decoded by Viterbi into one final string;
- this prepares Section 7, where the paper asks how to train the whole graph system with string-level supervision.

## Section 7 - Global Training for GTN / Fig. 20

This is the section that most directly matches the modern "train the whole system toward the final task" intuition.

Previous sections assumed the recognizer already knows how to give:

```text
correct segment + correct label -> low penalty
bad segment or wrong label -> high penalty
```

But in real data, we may only have a string-level label:

```text
input image: handwritten "34"
target label: "34"
```

We usually do not know which exact image segment is the `3`, which exact image segment is the `4`, or which candidate cuts are wrong. Section 7 asks: can the system learn from the final string label without manually labeled character segments?

The answer is yes, by doing global training over the graph.

### Ordinary Viterbi Training

First idea:

```text
1. Build segmentation graph.
2. Recognition transformer creates interpretation graph.
3. Use target string to keep only paths compatible with the correct label sequence.
4. Among those correct paths, use Viterbi to find the lowest-penalty path.
5. Minimize that path penalty.
```

This is already global because the training target is the whole string, not each isolated character.

But it has a weakness: it only tells the correct path to become better. It does not explicitly punish a dangerous wrong path that already has very low penalty.

This can cause the collapse problem: the model may reduce many penalties at once, making everything look plausible instead of making the correct answer clearly better than wrong competitors.

### Fig. 20 - Discriminative Viterbi Training

Fig. 20 fixes this by comparing two paths:

```text
correct best path:
  best path among paths compatible with the target label, e.g. "34"

unconstrained best path:
  best path among all paths, whether correct or wrong
```

The loss is:

```text
E_dvit = penalty(best correct path) - penalty(best unconstrained path)
```

Because the unconstrained graph includes the correct path, the best unconstrained penalty is always less than or equal to the best correct penalty.

So:

```text
if model already predicts the correct path:
  best correct path == best unconstrained path
  E_dvit = 0

if a wrong path beats the correct path:
  best correct penalty > best unconstrained penalty
  E_dvit > 0
```

Minimizing this loss does two things at once:

```text
lower penalty of the best correct path
raise penalty of the best competing path
```

That is why it is called discriminative: it does not just model the correct answer; it makes the correct answer win against its strongest competitor.

### How to Read the Fig. 20 Big Diagram

Read Fig. 20 from bottom/left to top/right conceptually:

```text
input handwritten image
-> Segmenter
-> segmentation graph
-> Recognition Transformer
-> interpretation graph
```

Then the graph branches into two training paths.

Branch A: constrained/correct branch

```text
interpretation graph + desired answer "34"
-> Path Selector
-> constrained interpretation graph
-> Viterbi Transformer
-> best constrained path
-> constrained Viterbi penalty
```

The path selector removes paths whose label sequence is not the desired answer. If the target is `"34"`, only paths that read as `"34"` remain.

Branch B: unconstrained/competitor branch

```text
interpretation graph
-> Viterbi Transformer
-> best unconstrained path
-> Viterbi penalty
```

This branch asks: what would the recognizer currently output if nobody forced it to be correct?

Loss function:

```text
constrained Viterbi penalty
- unconstrained Viterbi penalty
```

### What the Brackets and Parentheses Mean

The caption says:

```text
[ ... ] = penalties computed during forward propagation
( ... ) = partial derivatives computed during backward propagation
```

So an arc like:

```text
3 [0.1] (+1)
```

means:

```text
label: 3
forward penalty: 0.1
backward derivative: +1
```

Why `+1`? Because this arc is on the best correct/constrained path, and the loss contains:

```text
+ penalty(correct path)
```

When doing gradient descent, a `+1` derivative pushes the model to lower this penalty.

An arc like:

```text
1 [0.1] (-1)
```

means this arc is on the best unconstrained competing path. The loss contains:

```text
- penalty(best unconstrained path)
```

So the derivative is `-1`. Under gradient descent, this pushes the model to raise the penalty of that wrong competing path.

If an arc appears in both paths, the gradients can cancel:

```text
(+1) + (-1) = 0
```

That makes sense: shared evidence used by both correct and competing paths is not the discriminative boundary. The useful learning signal is concentrated on the arcs that distinguish the correct answer from the dangerous wrong answer.

### Toy Example

Input image looks like `"34"`, but the current recognizer is confused.

Best correct path:

```text
"3" penalty 0.1
"4" penalty 0.6
total = 0.7
```

Best unconstrained path:

```text
"4" penalty 0.4
"3" penalty 0.1
"1" penalty 0.1
total = 0.6
```

The model currently prefers the wrong `"431"` path because `0.6 < 0.7`.

Discriminative Viterbi loss:

```text
E = 0.7 - 0.6 = 0.1
```

Training will:

```text
decrease penalties on the correct "34" path
increase penalties on the competing "431" path
```

After training, we want:

```text
penalty("34") < penalty(any competing string)
```

### Why This Matters

This is one of the most modern-feeling ideas in the paper:

```text
Do not only train local modules with local labels.
Train the whole structured system so the final output beats alternatives.
```

In current language:

- `segmentation graph` is the latent structure;
- `path` is a latent alignment / latent explanation;
- `recognizer penalties` are trainable scores;
- `Viterbi` is structured decoding;
- `discriminative Viterbi training` is a margin-like global objective over correct vs competing structures.

This is not fully end-to-end in the modern raw-data-to-answer sense, because the segmenter is still heuristic. But it is end-to-end across the trainable scoring parts of the structured recognition pipeline.

### What Else in Section 7 Matters

After Fig. 20, there are three more ideas worth keeping.

#### 1. Discriminative Viterbi Still Has a Limitation

Discriminative Viterbi training only compares the best correct path with the single best unconstrained path.

This is a hard-best-path objective:

```text
correct side: only the best correct path matters
wrong side: only the best competing path matters
```

That is useful, but it can ignore the fact that there may be many nearly-good paths. If the correct path barely wins, the gradient can already become zero, even though wrong paths are dangerously close.

So the next move is to replace hard best-path scoring with a softer graph-level score.

#### 2. Forward Scoring / Forward Training

Viterbi asks:

```text
What is the single lowest-penalty path?
```

Forward scoring asks:

```text
What is the combined score of all paths that produce this interpretation?
```

If penalties are interpreted as negative log scores:

```text
score(path) = exp(-penalty(path))
```

then:

```text
Viterbi:
  use max / min over paths

Forward:
  sum scores over all compatible paths
```

Intuition:

```text
Viterbi = only the best explanation matters
Forward = all plausible explanations contribute
```

This gives a smoother training signal. Arcs on very good paths get large gradients, but other plausible paths can still contribute. The paper describes this as a soft version of backpropagating through Viterbi.

#### 3. Discriminative Forward Training

This is the strongest version in the section.

It compares:

```text
all paths compatible with the correct interpretation
vs
all paths in the unconstrained graph
```

Instead of:

```text
best correct path
vs
best competing path
```

So the objective is closer to:

```text
increase posterior mass of all correct paths
decrease posterior mass of incorrect competing paths
```

This is why the paper connects it to probabilistic ideas, HMM forward algorithms, and Boltzmann-machine-like clamped/free phases.

The modern translation:

```text
Viterbi training:
  hard latent alignment

Forward training:
  soft latent alignment / marginalization over paths

Discriminative forward training:
  contrast correct-path mass against all-path mass
```

#### 4. The Probability Point Is Subtle

The paper gives a probabilistic interpretation, but it does not require every internal arc penalty to be a perfectly normalized probability.

This matters because some candidate segments are garbage: they may not correspond to any real character. Forcing every recognizer output to be a clean probability distribution over valid character classes can be awkward.

The author's practical stance is:

```text
use penalties / energies internally
postpone normalization as far as possible
optimize a discriminative objective directly
```

So the right mental model is:

```text
penalty ~= energy / negative log-score
global loss makes correct structured interpretations beat incorrect ones
```

not:

```text
every intermediate value must be a clean calibrated probability
```

### Section 7 Takeaway

Section 7 is a progression:

```text
Viterbi training:
  lower the best correct path

Discriminative Viterbi training:
  lower the best correct path and raise the best competitor

Forward training:
  use all compatible paths, not only the single best path

Discriminative forward training:
  make the total mass of correct interpretations dominate the competing mass
```

This is the paper's mature global-training idea: learn from final string labels, treat segmentation/alignment as latent structure, and send credit/blame back through the graph to the recognizer.

## VLM / VLA / Robot Observation Connection

机器人相机输入同样是图像：

```text
camera image
-> CNN / ViT visual encoder
-> visual feature / visual token
-> policy / VLA / planner
-> action
```

LeNet-5 帮助理解 `visual encoder` 的基本思想：不是人工写边缘/纹理特征，而是让网络自己学习 feature hierarchy。

## Current Status

- [x] PDF downloaded
- [ ] Background scan
- [ ] 写 3 句 CNN takeaway
