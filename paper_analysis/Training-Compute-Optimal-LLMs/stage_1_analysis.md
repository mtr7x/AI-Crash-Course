Here is my analysis of the provided paper:

1. Key Insights:

- Current large language models are significantly undertrained relative to their model size, due to the recent focus on scaling up model parameters while keeping the amount of training data relatively constant.

- For compute-optimal training, the model size and number of training tokens should be scaled equally - doubling the model size should be accompanied by doubling the number of training tokens.

- By training a 70B parameter model (Chinchilla) on 1.4 trillion tokens using the same compute budget as Gopher (280B parameters, 300B tokens), Chinchilla outperforms not only Gopher but also larger models like GPT-3 and Megatron-Turing NLG across a wide range of tasks.

- Smaller but compute-optimally trained models like Chinchilla have substantially lower costs for downstream fine-tuning and inference, facilitating broader usage.

- The findings challenge the conventional approach of predominantly increasing model size when increasing compute, while undertrained relative to the optimal number of tokens.

2. Surprising/Shocking Elements:

- The authors estimate that current large language models should be trained on substantially more tokens (e.g. 4x for Gopher) rather than just increasing model size.

- Chinchilla, at 70B parameters, outperforms much larger models like Gopher (280B), GPT-3 (175B), and Megatron-Turing NLG (530B) across a wide range of tasks, contradicting expectations around simply scaling up model size.

- The optimal compute-scaling approach differs significantly from prior work (Kaplan et al., 2020), representing a potential disruption to current practices.

3. Key Quotes:

"We ﬁnd that current large language models are signiﬁcantly undertrained, a consequence of the recent focus on scaling language models whilst keeping the amount of training data constant."

"By training over 400 language models ranging from 70 million to over 16 billion parameters on 5 to 500 billion tokens, we ﬁnd that for compute-optimal training, the model size and the number of training tokens should be scaled equally: for every doubling of model size the number of training tokens should also be doubled."

"Chinchilla uniformly and signiﬁcantly outperforms Gopher (280B), GPT-3 (175B), Jurassic-1 (178B), and Megatron-Turing NLG (530B) on a large range of downstream evaluation tasks."

"As a highlight, Chinchilla reaches a state-of-the-art average accuracy of 67.5% on the MMLU benchmark, greater than a 7% improvement over Gopher."

"The drive to train larger and larger models is clear—so far increasing the size of language models has been responsible for improving the state-of-the-art in many language modelling tasks."