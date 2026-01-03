# The Karpathy Guide to Modern AI
*From zero to the frontier, explained simply*

---

## Part 1: What Even Is a Neural Network?

Okay, forget everything you think you know. A neural network is just a function. That's it. It takes numbers in, does some math, spits numbers out.

```
input → [bunch of matrix multiplies + nonlinearities] → output
```

The "learning" part? We have a loss function that says "how wrong were you?" and we use calculus (backpropagation) to nudge all the numbers (weights) in the direction that makes us less wrong. Do this a billion times. Congratulations, you've trained a neural network.

The magic isn't in any individual piece. The magic is that **this works at all**. And it works unreasonably well.

---

## Part 2: The Transformer - The Only Architecture You Need

Before 2017, we had RNNs. They processed sequences one token at a time, like reading a book word by word while trying to remember everything. Problem: information gets lost. The 50th word has basically forgotten the 1st word.

**Transformers said: "What if we just look at everything at once?"**

Here's the core idea - **self-attention**:

```
For each word, ask: "How much should I pay attention to every other word?"

"The cat sat on the mat because it was tired"
                                    ↑
                          What does "it" refer to?
```

The model learns to compute attention scores. "it" learns to attend strongly to "cat" and weakly to "mat". This is learned, not programmed.

The actual math:

```
Q = input × W_q  (what am I looking for?)
K = input × W_k  (what do I contain?)
V = input × W_v  (what do I actually say?)

Attention = softmax(Q × K^T / √d) × V
```

That's it. That's the paper that changed everything. Three matrix multiplies and a softmax.

**Why does this work so well?**

1. **Parallelization**: Unlike RNNs, you can process all tokens simultaneously. GPUs love this.
2. **Long-range dependencies**: Token 1 can directly talk to token 1000. No telephone game.
3. **It's differentiable**: Backprop works. We can train it.

---

## Part 3: Language Models - Prediction is All You Need

Here's the dumbest idea that turned out to be genius:

**Just predict the next word. Over and over. On the entire internet.**

```
"The cat sat on the" → predict "mat"
"The capital of France is" → predict "Paris"
"def fibonacci(n):" → predict "\n    if n <= 1:"
```

You do this trillions of times across all of human text. What emerges?

- Grammar? Learned.
- Facts? Learned.
- Reasoning? Somehow... learned?
- Code? Learned.
- Multiple languages? Learned.

**This is the GPT approach.** Stack transformer layers, make it predict next tokens, scale it up.

The loss function is embarrassingly simple:

```
loss = -log(probability model assigned to the correct next token)
```

Lower loss = model is more confident about the right answer. That's the entire training objective.

---

## Part 4: The Scaling Revelation

The 2020 Scaling Laws paper showed something that should have been surprising but in hindsight makes total sense:

**Performance scales predictably with compute, data, and parameters.**

Plot loss against compute on a log-log scale. It's a straight line. A *predictable* straight line.

This means:
- Want a better model? Spend 10x more compute.
- Want to know how good your model will be? Check where it lands on the scaling curve.

GPT-3 was basically: "What if we actually believe this and just... scale up?"

| Model | Parameters |
|-------|-----------|
| GPT-2 | 1.5B |
| GPT-3 | 175B |
| GPT-4 | ~1.8T (rumored) |

Each jump = qualitatively new capabilities emerge. This is called "emergent behavior" and honestly we don't fully understand why it happens. The model just... starts being able to do things it couldn't do before.

---

## Part 5: RLHF - Teaching the Model to Be Helpful

Here's the problem with raw GPT-3: it's trained to predict text, not to be helpful.

Ask it a question, it might:
- Answer the question
- Continue the question with another question
- Write something completely unrelated but statistically plausible

**RLHF (Reinforcement Learning from Human Feedback) fixes this.**

The recipe:

```
Step 1: Supervised Fine-Tuning (SFT)
        - Collect examples of good assistant responses
        - Fine-tune the model on these

Step 2: Train a Reward Model
        - Show humans two responses, ask which is better
        - Train a model to predict human preferences

Step 3: RL Fine-Tuning
        - Use PPO to optimize the language model
        - Maximize reward from the reward model
        - Add KL penalty so it doesn't drift too far from original
```

This is the InstructGPT → ChatGPT transition. Same base model. Totally different behavior.

**DPO (2023)** simplified this further: skip the reward model entirely, just optimize directly on the preference pairs. Mathematically equivalent, practically simpler.

---

## Part 6: Making Models Think - Chain of Thought

This one is almost embarrassing in its simplicity.

**Before CoT:**
```
Q: Roger has 5 tennis balls. He buys 2 cans of 3. How many does he have?
A: 11
```
Model just guesses. Often wrong.

**After CoT:**
```
Q: Roger has 5 tennis balls. He buys 2 cans of 3. How many does he have?
   Let's think step by step.
A: Roger starts with 5 balls.
   He buys 2 cans, each with 3 balls.
   2 × 3 = 6 new balls.
   5 + 6 = 11 total balls.
```

Same model. Just prompted differently. Accuracy jumps dramatically.

**Why does this work?**

The model's "reasoning" happens in the forward pass. More tokens = more compute = more "thinking". By forcing it to show its work, you're literally giving it more computation to solve the problem.

This is why o1 and DeepSeek R1 generate long chains of reasoning. It's not theater. The thinking IS the compute.

---

## Part 7: The ReAct Pattern - Thought + Action

Pure reasoning hits a wall. The model can think, but it can't *do* anything.

**ReAct interleaves reasoning with actions:**

```
Question: What is the elevation of the birthplace of the inventor of the telephone?

Thought 1: I need to find who invented the telephone.
Action 1: Search[inventor of telephone]
Observation 1: Alexander Graham Bell invented the telephone.

Thought 2: Now I need to find where Bell was born.
Action 2: Search[Alexander Graham Bell birthplace]
Observation 2: Bell was born in Edinburgh, Scotland.

Thought 3: Now I need the elevation of Edinburgh.
Action 3: Search[Edinburgh elevation]
Observation 3: Edinburgh's elevation is 47 meters.

Answer: 47 meters
```

The model learns to use tools. Search engines. Calculators. Code interpreters. APIs. This is the foundation of all modern AI agents.

---

## Part 8: The DeepSeek R1 Moment

Okay this paper (January 2025) is wild. Let me explain why.

**The old way to make models reason:**
1. Collect tons of human-written reasoning traces
2. Supervised fine-tuning on these traces
3. Maybe some RLHF on top

**DeepSeek R1's approach:**
1. Start with base model
2. Pure RL. No SFT. No reward model.
3. Just let it learn to maximize correctness on reasoning tasks

What emerged?

The model spontaneously developed:
- Chain of thought reasoning
- Self-verification ("let me check this")
- Backtracking ("wait, that's wrong, let me try again")
- Breaking problems into subproblems

**Nobody programmed these behaviors.** They emerged from pure optimization pressure.

This is the AlphaZero moment for language. AlphaZero learned superhuman Go with no human games. DeepSeek R1 learned sophisticated reasoning with no human reasoning traces.

---

## Part 9: The Practical Stack (Llama 3)

If you want to understand how to actually build one of these things, read the Llama 3 paper. It's the most transparent look at a frontier model.

Key details:

```
Architecture: Standard transformer (boring but it works)
Parameters: 8B, 70B, 405B variants
Context: 128K tokens
Training data: 15T tokens
Training compute: 3.8 × 10^25 FLOPs (for 405B)

Secret sauce:
- Careful data curation (quality > quantity)
- Extensive post-training (SFT + DPO + more)
- Multi-stage training curriculum
- Careful hyperparameter tuning at each scale
```

The lesson: there's no magic. It's engineering. Careful, meticulous engineering at scale.

---

## Part 10: What Actually Matters

Here's my ranking of what to understand deeply:

1. **Transformers** - The architecture. Learn it cold.
2. **Scaling** - Bigger = better, predictably. This drives everything.
3. **RLHF/DPO** - How we align models to human intent.
4. **Chain of Thought** - How we get models to reason.
5. **RL for reasoning** - The frontier (DeepSeek R1, o1).

Everything else is details.

---

## The Meta-Lesson

Here's what I want you to take away:

**The core ideas are simple.** Attention. Next-token prediction. Scaling. Human feedback. Step-by-step reasoning.

**The magic is in the scale.** These simple ideas, applied at massive scale, produce capabilities that surprise even the people building them.

**We don't fully understand why.** Emergent capabilities. Scaling laws. The unreasonable effectiveness of next-token prediction. We have theories, but no complete explanation.

**The field moves fast.** The DeepSeek R1 paper is from *January 2025*. By the time you read this, there will be new breakthroughs.

---

## How to Actually Learn This

1. **Watch 3Blue1Brown** - Get the visual intuition for neural nets
2. **Read the Transformer paper** - With pencil and paper. Implement it.
3. **Build something** - Train a tiny GPT on Shakespeare. See it work.
4. **Read papers actively** - Don't just read. Ask "why did they do this?"
5. **Stay current** - Follow arXiv, Twitter, Discord communities

The best way to learn is to build. Go train a model. Break things. That's how you develop intuition.

---

## Key Papers

- [Transformers](https://arxiv.org/pdf/1706.03762) - The architecture (2017)
- [GPT-3 / Scaling Laws](https://arxiv.org/pdf/2005.14165) - Scale is all you need (2020)
- [RLHF / InstructGPT](https://arxiv.org/pdf/2203.02155) - Making models helpful (2022)
- [Chain of Thought](https://arxiv.org/pdf/2201.11903) - Let's think step by step (2022)
- [DeepSeek R1](https://arxiv.org/pdf/2501.12948v1) - RL for reasoning (2025)

---

*Now go read the Transformer paper. Actually read it. Implement it from scratch. That's worth more than reading 100 summaries.*

*Good luck. This stuff is genuinely exciting.*
