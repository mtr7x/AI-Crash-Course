Here are the key insights, surprising elements, and notable quotes from the paper:

Key Insights:
1. Traditional language model benchmarks do not effectively measure alignment with human preferences for open-ended conversational abilities.
2. Using strong language models like GPT-4 as judges to evaluate other language models can approximate human preferences in a scalable and explainable way. 
3. LLM judges exhibit some biases like position bias and verbosity preference, but techniques can mitigate these biases.
4. The authors' new benchmarks MT-Bench and Chatbot Arena aim to evaluate open-ended conversational abilities aligned with human preferences.
5. LLM judges like GPT-4 achieve over 80% agreement with human preferences on these benchmarks, similar to agreement between humans.
6. Traditional and open-ended conversational benchmarks provide complementary evaluation of language models' capabilities.

Surprising Elements:
- Strong language models used as judges can match human preferences as well as humans agree with each other (over 80% agreement).
- Language models exhibit biases like preferring longer/more verbose responses and self-enhancing by rating their own responses highly.
- Open-ended conversational benchmarks differentiate between base language models and fine-tuned models better aligned with human preferences.

Notable Quotes:

"We argue that this discrepancy primarily arises due to existing evaluation that only measures LLMs' core capability on a confined set of tasks (e.g., multi-choice knowledge or retrieval questions), without adequately assessing its alignment with human preference in open-ended tasks, such as the ability to accurately adhere to instructions in multi-turn dialogues."

"Despite the base LLaMA models showing competitive performance on conventional benchmarks (Table 8), its answers to open-ended questions are often not preferred by humans."

"We call this approach "LLM-as-a-judge". This approach has been tried in our earlier blog post and other concurrent or follow-up work. However, there has not been a systematic study of this approach."