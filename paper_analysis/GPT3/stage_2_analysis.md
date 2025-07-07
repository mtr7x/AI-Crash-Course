Here is a summary in the style of Andrej Karpathy on the paper "Language Models are Few-Shot Learners":

The core idea of this work is to train massively large language models in an unsupervised manner on broad data, allowing them to meta-learn the ability to perform a wide range of language tasks simply by being prompted with a few examples or instructions at inference time - a paradigm called "few-shot learning". 

Technically, they trained GPT-3, an autoregressive transformer language model with 175 billion parameters (10x larger than previous models) on a filtered subset of web crawl data. No task-specific architectures or fine-tuning datasets were used. Instead, tasks were specified purely via text interaction with the pre-trained model, providing a few examples as the prompt.

The key insight is that simply by scaling up the model and dataset massively, the capabilities of few-shot learning emerge in a surprising way. GPT-3 demonstrated strong few-shot performance on many NLP benchmarks like translation, question-answering, reading comprehension and even tasks requiring multi-step reasoning or domain adaptation unseen during training.

However, there were also many tasks where few-shot performance still struggled, exposing limitations. Additionally, training on broad web data raises concerns around factual accuracy, bias, and potential for misuse that need careful study.

The potential of this few-shot meta-learning capability is two-fold: 1) It enables language models to be flexibly applied to a vast range of tasks by simply communicating via prompts, without task-specific training. 2) It hints at the possibility of more general reasoning capabilities emerging at even larger scales.

But the work also highlights key open challenges - improving few-shot performance on harder tasks, mitigating harms from training on uncurated data, and developing safe deployment strategies as these models become more powerful and general. Getting this right will require responsible systems-level thinking beyond just model scaling.