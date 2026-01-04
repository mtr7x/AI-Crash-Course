# Transformers: Builder's Perspective

> What this means for developers shipping products

**TL;DR:** Attention all developers! Google Brain just dropped a bombshell paper that could radically change how we build sequence models and language applications.

---

The Transformer Upends Sequence Modeling 

Attention all developers! Google Brain just dropped a bombshell paper that could radically change how we build sequence models and language applications. The Transformer is a novel neural network architecture that ditches the beloved recurrent and convolutional layers we've been using for years. Instead, it's built entirely on attention mechanisms - relating different positions of the input to compute representations.


### This lightweight, parallelizable approach is blowing minds across the developer community


 It achieves new state-of-the-art results on machine translation tasks, while training way faster than previous models on hardware many of us can access.

 The Transformer is riding the wave of momentum around attention, unifying self-attention with sequence transduction into a beautiful, simple design.

 By shedding the sequential computation constraints of RNNs, it opens up opportunities for more efficient modeling of long-range dependencies.

But let's be real - shiny new tech is cool, but what do the Transformer's performance wins mean for practitioners?

🛠 For language model developers, a boost in translation quality enables better UX across AI assistants, chatbots, and language interfaces.

 The efficient parallelization could unlock higher quality for on-device translation, bypassing server round-trips.

 More broadly, the Transformer shows attention is a powerful primitive - perhaps a building block for modeling other sequential data like audio, video, and proteins.

Of course, the Transformer isn't a magic wand - its simplicity could limits its capabilities on more complex tasks involving tight coordination across the whole sequence. But by open-sourcing their work, Google is kickstarting a movement where devs everywhere can test, extend, and discover where attention can shine.

The Transformer embodies Google's AI principles: being socially beneficial and favoring simple solutions where possible. As we collectively learn more about this invention in the wild, I'm excited to see what innovative applications the resourceful dev community will create!
---

### Other Perspectives

[Precision Analysis](stage_1_analysis.md) · [Karpathy-Style Analysis](stage_2_analysis.md) · **Builder's Perspective** · [Strategic Analysis](stage_4_analysis.md) · [Pseudocode](pseudocode.md)

---

[← Back to Transformers](.) · [Original Paper](https://arxiv.org/pdf/1706.03762) · [All Papers](../)
