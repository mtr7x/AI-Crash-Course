Based on the provided paper, here are the key insights, surprising elements, and notable quotes:

Key Insights:

1. The Transformer model proposes a novel neural network architecture that relies solely on attention mechanisms, dispensing with recurrence and convolutions entirely. This challenges the conventional use of recurrent or convolutional neural networks in sequence transduction models.

2. The model achieves state-of-the-art performance on machine translation tasks while being more parallelizable and requiring significantly less training time compared to existing models.

3. The self-attention mechanism allows the model to effectively capture long-range dependencies within sequences, addressing a limitation of previous approaches.

4. The multi-head attention mechanism and positional encoding enable the model to learn dependencies between different positions in the input and output sequences without relying on sequential computation.

5. The Transformer architecture generalizes well to other tasks, such as English constituency parsing, demonstrating its versatility.

Surprising or Shocking Elements:

1. The paper presents a sequence transduction model that entirely discards recurrence and convolutions, which have been fundamental components of state-of-the-art models in this domain.

2. The Transformer achieves superior performance on machine translation tasks compared to existing models, including ensembles, despite its simplicity and parallelizability.

3. The model establishes a new single-model state-of-the-art BLEU score on the WMT 2014 English-to-French translation task after training for only 3.5 days on eight GPUs, significantly reducing the training costs compared to previous best models.

Notable Quotes:

1. "We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely."

2. "Experiments on two machine translation tasks show these models to be superior in quality while being more parallelizable and requiring significantly less time to train."

3. "Our model achieves 28.4 BLEU on the WMT 2014 English-to-German translation task, improving over the existing best results, including ensembles, by over 2 BLEU."

4. "On the WMT 2014 English-to-French translation task, our model establishes a new single-model state-of-the-art BLEU score of 41.8 after training for 3.5 days on eight GPUs, a small fraction of the training costs of the best models from the literature."

5. "We show that the Transformer generalizes well to other tasks by applying it successfully to English constituency parsing both with large and limited training data."