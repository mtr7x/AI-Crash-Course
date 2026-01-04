# Scaling Laws: Karpathy-Style Analysis

> First-principles technical explanation

**TL;DR:** This paper presents an extensive empirical study on how the performance of Transformer language models scales with three key factors - model size, dataset size, and compute used for training. The findings reveal some strikingly simple yet powerful scaling laws that govern these relationships over...

---

This paper presents an extensive empirical study on how the performance of Transformer language models scales with three key factors - model size, dataset size, and compute used for training. The findings reveal some strikingly simple yet powerful scaling laws that govern these relationships over many orders of magnitude.


### At the core, we see that model performance depends most crucially on scale - the number of model parameters, size of the training dataset, and compute budget. Within reasonable limits, other architectural details like network depth or width have minimal impact. The key results are


Power Law Scaling: Performance exhibits remarkably consistent power-law scaling trends with each of the three scale factors when the other two are not bottlenecked. These trends span over 6 orders of magnitude with no signs of saturation at the highest scales studied.

Overﬁtting Universality: There is a simple relationship between the degree of overﬁtting and the ratio of model size to dataset size. Increasing model size by 8x requires growing the dataset by only ~5x to maintain optimal performance.

Training Universality: The shape of the training loss curves is remarkably consistent across model sizes, enabling extrapolation of infinite-compute performance from the early phase.

Transfer Performance: Performance on a transfer distribution is tightly coupled to the trained model's validation loss, with just a constant offset.

Sample Efficiency: Larger models are significantly more sample-efficient, requiring fewer tokens and optimization steps to reach a target loss compared to smaller models.

Optimal Compute Allocation: For a fixed compute budget, the optimal strategy is to train extremely large models on a relatively modest dataset far from convergence. Data requirements grow slowly (D ~ C^0.27) while optimal model size increases rapidly with more compute.

The insights reveal a remarkable simplicity underlying the increasingly complex and powerful language models. Performance improvements appear to be predictably achievable just by scaling up model, data and compute resources in tandem according to these laws. The findings provide a clear roadmap for optimally allocating available resources in pursuit of more capable language models and understanding the limits of scaling.
---

### Other Perspectives

[Precision Analysis](stage_1_analysis.md) · **Karpathy-Style Analysis** · [Builder's Perspective](stage_3_analysis.md) · [Strategic Analysis](stage_4_analysis.md) · [Pseudocode](pseudocode.md)

---

[← Back to Scaling Laws](.) · [Original Paper](https://arxiv.org/pdf/2001.08361) · [All Papers](../)
