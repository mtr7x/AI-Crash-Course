# Llama3: Builder's Perspective

> What this means for developers shipping products

**TL;DR:** clears throat* What's up, devs? Your resident AI watcher Swyx here with the hottest scoop on Llama 3 - Meta's new herd of beefy language models here to shake things up.

---

*clears throat* What's up, devs? Your resident AI watcher Swyx here with the hottest scoop on Llama 3 - Meta's new herd of beefy language models here to shake things up. 


### Let's start with the hard nums


- 405B params in the flagship - we're talking DENSE Transformer, 128k context window. No skimping!
- 15T token pre-training data across 100+ languages. Multilingual and poly-talented, just how we like it.
- Eval results are  - basically on par with GPT-4 across coding, reasoning, multi-task benchmarks.  


### But the real spice is in the *how* they got there


- **Scaling Responsibly**: Rather than a bloated MoE, they kept it simple with dense Transformers and smart tweaks. Scaled pre-training flops by 50x over Llama 2 in a stable way.
- **Data Quality >>>> Data Quantity**: Heavy investment in data filtering, curation and quality assurance pipelines. They know good data is the real secret sauce.
- **SFT + Reward Modeling FTW**: Sticking to tried-and-true supervised finetuning with safety tech like rejection sampling + direct pref optimization. Keeping it stable at scale.

Now for my take: This is a HUGE milestone for open, democratized AI capabilities. Meta is putting their flagship 405B model out there under an updated open license. The floodgates are open for off-the-shelf AGI capabilities accessible to anyone working on AI products and services.

That said, there's still work to do on the safety front - even with Llama Guard 3, more robustness is needed. And there are still open questions around the environmental impact of such massively scaled models.

But the potential upside is immense - a wave of innovation from indie devs, startups, and the open source community building on top of AGI foundations rather than proprietary black boxes. This could be a pivotal step towards actually putting "AI" into every software product.

So get hyped, but stay aware of the challenges. Hop into those model weights, crank up the prompts, and build something amazing - the doors are wide open! Let's take this for a spin. 🧵
---

### Other Perspectives

[Precision Analysis](stage_1_analysis.md) · [Karpathy-Style Analysis](stage_2_analysis.md) · **Builder's Perspective** · [Strategic Analysis](stage_4_analysis.md) · [Pseudocode](pseudocode.md)

---

[← Back to Llama3](.) · [Original Paper](https://arxiv.org/pdf/2407.21783) · [All Papers](../)
