Here are the key insights, surprising elements, and important quotes from the paper:

Key Insights:

1. Large language models can develop powerful reasoning capabilities purely through reinforcement learning without supervised fine-tuning, as demonstrated by DeepSeek-R1-Zero. This challenges the conventional thinking that supervised data is necessary.

2. DeepSeek-R1-Zero naturally emerged with intriguing reasoning behaviors like self-verification, reflection, and generating long chains-of-thought through the reinforcement learning process. This reveals an underlying capability of large models to self-evolve reasoning skills.

3. Combining a small amount of cold-start data, multi-stage training (including rejection sampling and supervised fine-tuning after RL), and additional RL allows further refinement of the reasoning capabilities, as seen in DeepSeek-R1 matching OpenAI's reasoning performance.

4. Distillation from a large reasoning-focused model like DeepSeek-R1 to smaller dense models transfers the discovered reasoning patterns better than applying RL directly on the smaller model. This has practical implications for developing capable but efficient reasoning models.

5. The results suggest that very large language models have an innate potential for advanced reasoning that can be unlocked and guided through carefully designed reinforcement learning objectives and curricula.

Surprising Elements:

1. DeepSeek-R1-Zero achieved super performance on numerous reasoning benchmarks like AIME 2024 (71% pass@1) purely through reinforcement learning on a base model, without any supervised fine-tuning. This contradicts established expectations.

2. The remarkable self-evolution of DeepSeek-R1-Zero, naturally developing advanced reasoning behaviors like self-verification and reflection, represents a significant deviation from typical language model capabilities.

3. The success of distillation in transferring reasoning skills from a large model to much smaller dense models (e.g. 14B outperforming 32B state-of-the-art) is an unexpected and potentially disruptive result.

Key Quotes:

1. "DeepSeek-R1-Zero naturally emerged with numerous powerful and intriguing reasoning behaviors."
2. "DeepSeek-R1-Zero exhibits super performance on reasoning benchmarks. For instance, the pass@1 score on AIME 2024 increases from 15.6% to 71.0%."
3. "We directly apply RL to the base model without relying on supervised fine-tuning (SFT) as a preliminary step. This approach allows the model to explore chain-of-thought (CoT) for solving complex problems, resulting in the development of DeepSeek-R1-Zero."
4. "Notably, it is the first open research to validate that reasoning capabilities of LLMs can be incentivized purely through RL, without the need for SFT."
5. "Distillation from DeepSeek-R1 to smaller dense models. Using Qwen2.5-32B as the base model, direct distillation from DeepSeek-R1 outperforms applying RL on it."