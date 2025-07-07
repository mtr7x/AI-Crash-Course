Based on the paper, here are the key insights, surprising elements, and notable quotes:

Key Insights:

1. Scaling up language models to very large sizes (e.g. GPT-3 with 175 billion parameters) greatly improves few-shot learning performance across many NLP tasks, sometimes reaching competitiveness with prior state-of-the-art fine-tuning approaches.

2. Large language models can perform reasonably well on tasks that require on-the-fly reasoning or domain adaptation from just a few examples or instructions, challenging the conventional need for large task-specific training datasets.

3. Few-shot learning capabilities of large language models open up potential for models to generalize to a wide range of language tasks without task-specific fine-tuning.

4. There are still some tasks and datasets where GPT-3's few-shot performance struggles, suggesting room for further improvement.

5. Potential societal impacts of large language models include misuse (e.g. generating misinformation), bias/fairness issues from training data, and high energy usage.

Surprising Elements:

1. GPT-3 can generate news articles that human evaluators have difficulty distinguishing from human-written articles.

2. GPT-3 achieves strong performance on some datasets without any gradient updates or fine-tuning, purely via instruction + examples.

3. GPT-3 faces methodological issues related to potential memorization of some benchmark training sets from its large web crawl training data.

Notable Quotes:

"GPT-3 achieves strong performance on many NLP datasets, including translation, question-answering, and cloze tasks, as well as several tasks that require on-the-fly reasoning or domain adaptation, such as unscrambling words, using a novel word in a sentence, or performing 3-digit arithmetic."

"We find that GPT-3 can generate samples of news articles which human evaluators have difficulty distinguishing from articles written by humans."

"There exists a very wide range of possible useful language tasks, encompassing anything from correcting grammar, to generating examples of an abstract concept, to critiquing a short story. For many of these tasks it is difficult to collect a large supervised training dataset, especially when the process must be repeated for every new task."