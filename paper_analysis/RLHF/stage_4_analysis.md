Here is a strategic business-focused summary on instructing language models with human feedback, in the style of Elad Gil:

As large language models become more capable, aligning them with user intent is a critical challenge. OpenAI's work on InstructGPT demonstrates a promising approach - fine-tuning models like GPT-3 with human feedback to better follow instructions across a wide range of tasks. 

The core insight is using reinforcement learning from human preferences as a reward signal during fine-tuning. By collecting datasets of humans ranking different model outputs, they can train a reward model to predict which outputs are preferred. Then using proximal policy optimization, they fine-tune the base model to maximize that predicted reward.

From a strategic perspective, this line of research could unlock major value by making large language models dramatically more controllable and aligned with user objectives. The ability to reliably execute on instructions while exhibiting desirable traits like truthfulness and avoiding toxic outputs is a key bottleneck in deploying language AI products at scale.

The results are highly promising - their 1.3B parameter InstructGPT model, with over 100x fewer parameters than GPT-3, produces outputs preferred by human raters over GPT-3's 175B model. It exhibits marked improvements in truthfulness on benchmarks while reducing hallucinated and toxic outputs.

However, major challenges remain in scaling this approach. Collecting high-quality human feedback at the scale required for models with billions of parameters is extremely labor-intensive. Techniques for better leveraging this data, like reward modeling and better reinforcement learning algorithms, will be critical.

Ultimately, this line of work could shape the competitive landscape by giving pioneers like OpenAI an edge in controllable and scalable language AI capabilities. But executing on the remaining technical hurdles around data efficiency, model alignment, and robust oversight will be key to fully realizing the potential. Players who can productize these advances first may be able to create defensible positions.

For AI-focused founders, investors, and executives, these developments reinforce the strategic importance of aligning powerful language models with robust oversight and human feedback. Unlocking instructable and controllable language AI could create immense value, if the remaining scaling challenges can be overcome. Closely tracking the technical progress while staying mindful of the societal implications will be paramount.