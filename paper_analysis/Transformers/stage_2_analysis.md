# Transformers: Karpathy-Style Analysis

> First-principles technical explanation

**TL;DR:** The Transformer is a new neural network architecture that does away with the recurrent and convolutional components prevalent in sequence models. Instead, it relies entirely on attention mechanisms to draw connections between different parts of the input and output sequences.

---

The Transformer is a new neural network architecture that does away with the recurrent and convolutional components prevalent in sequence models. Instead, it relies entirely on attention mechanisms to draw connections between different parts of the input and output sequences.

At its core, attention allows the model to look at the entire input sequence and learn the relevant parts to focus on for generating each output element. This is in contrast to RNNs which process the input sequentially, making it difficult to learn long-range dependencies.

The key innovation is self-attention - relating different positions of a single sequence to compute representations of that sequence. The self-attention layer looks at the sequence and for each position, computes attention weights over all other positions to get a representation enriched by relevant information spread throughout the sequence.

This self-attention is performed in parallel across all positions, allowing extreme parallelization compared to sequential RNNs. The self-attention layers are wrapped in an encoder-decoder architecture similar to previous seq2seq models.

In the encoder, self-attention layers process the input sequence. In the decoder, self-attention is used both to process the output up to a given position, as well as to attend to relevant parts of the input sequence.

The model achieves new state-of-the-art results in machine translation while being much more parallelizable and efficient to train than recurrent models. However, there are still open questions around generalizing self-attention to other modalities beyond text.

The Transformer elegantly replaces the venerable RNN with a more parallelizable alternative built on self-attention. While more remains to be explored, it provides a fresh perspective on sequence modeling grounded in a first-principles rethinking of the fundamentals.
---

### Other Perspectives

[Precision Analysis](stage_1_analysis.md) · **Karpathy-Style Analysis** · [Builder's Perspective](stage_3_analysis.md) · [Strategic Analysis](stage_4_analysis.md) · [Pseudocode](pseudocode.md)

---

[← Back to Transformers](.) · [Original Paper](https://arxiv.org/pdf/1706.03762) · [All Papers](../)
