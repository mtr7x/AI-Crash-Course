# Scaling Laws: Precision Analysis

> Key insights, surprising findings, and quotable moments

**TL;DR:** Based on the paper, here are the key insights, surprising elements, and relevant quotes

---

### Based on the paper, here are the key insights, surprising elements, and relevant quotes



### Key Insights


- Language model performance improves in predictable power-law relationships with model size, dataset size, and compute used for training, spanning over 6 orders of magnitude without signs of deviation.

- Within reasonable limits, performance depends weakly on architectural details like depth vs width - scale factors of model size, data, and compute are most important.

- Large models are more sample-efficient, reaching the same performance with fewer optimization steps and data points compared to smaller models.

- For a fixed compute budget, optimal performance is achieved by training very large models and stopping significantly before full convergence, being far more sample-efficient than training small models to convergence.

- The ideal batch size scales as a power-law with the loss only, being around 1-2 million tokens for the largest models.

- Transfer performance to different data distributions is strongly correlated with performance on the training set, with a roughly constant offset penalty.

- There is a universal overﬁtting pattern where increasing model size requires increasing data sub-linearly (N^0.74/D) to avoid diminishing returns.


### Surprising Elements


- The smooth power-law scaling relationships spanning over 6 orders of magnitude with no deviations even at the largest scales studied.

- The relative unimportance of architectural hyperparameters like depth vs width compared to the scale factors.

- The finding that for a fixed compute budget, it is optimal to train very large models but stop far before convergence.

- The universal N^0.74/D overﬁtting relationship between model size and data requirements.


### Relevant Quotes


"Performance has a power-law relationship with each of the three scale factors N, D, C when not bottlenecked by the other two, with trends spanning more than six orders of magnitude." 

"Within reasonable limits, performance depends very weakly on other architectural hyperparameters such as depth vs. width."

"Large models are more sample-efficient than small models, reaching the same level of performance with fewer optimization steps (Figure 2) and using fewer data points (Figure 4)."

"Maximally compute-efficient training would therefore be far more sample efficient than one might expect based on training small models to convergence, with data requirements growing very slowly as D~C^0.27 with training compute."

"The ideal batch size for training these models is roughly a power of the loss only, and continues to be determinable by measuring the gradient noise scale; it is roughly 1-2 million tokens at convergence for the largest models we can train."
---

### Other Perspectives

**Precision Analysis** · [Karpathy-Style Analysis](stage_2_analysis.md) · [Builder's Perspective](stage_3_analysis.md) · [Strategic Analysis](stage_4_analysis.md) · [Pseudocode](pseudocode.md)

---

[← Back to Scaling Laws](.) · [Original Paper](https://arxiv.org/pdf/2001.08361) · [All Papers](../)
