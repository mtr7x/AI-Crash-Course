Based on the paper, here are the key insights, surprising elements, and relevant quotes I've identified:

Key Insights:

1. Fine-tuning large language models with human feedback can significantly improve their ability to follow instructions and user intent, even outperforming much larger models trained on just text data.

2. The InstructGPT models showed improvements in truthfulness, reduced toxicity, and better adherence to constraints compared to the original GPT-3 models.

3. Reinforcement learning from human preferences can help align language model behavior with desired attributes like helpfulness, honesty, and harmlessness.

4. Collecting datasets of human demonstrations and preferences enables fine-tuning large language models in a targeted way on specific capabilities.

5. Even with fine-tuning, language models still make mistakes, highlighting the need for further research into aligning them with human values.

Surprising Elements:

1. The 1.3B parameter InstructGPT model produced outputs preferred by human raters over the 175B GPT-3 model, despite being over 100x smaller.

2. On the TruthfulQA benchmark, InstructGPT generated truthful and informative answers about twice as often as GPT-3.

3. Fine-tuning reduced toxic output generation compared to the original GPT-3 models.

Relevant Quotes:

"In human evaluations on our prompt distribution, outputs from the 1.3B parameter InstructGPT model are preferred to outputs from the 175B GPT-3, despite having 100x fewer parameters."

"InstructGPT models show improvements in truthfulness and reductions in toxic output generation while having minimal performance regressions on public NLP datasets."

"Even though InstructGPT still makes simple mistakes, our results show that ﬁne-tuning with human feedback is a promising direction for aligning language models with human intent."