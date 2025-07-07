Based on the provided paper, here are the key insights, surprising elements, and relevant quotes:

Key Insights:

1. The AlphaZero algorithm can achieve superhuman performance across different complex games like chess, shogi, and Go, without any domain-specific knowledge or human expertise, solely through self-play reinforcement learning from the game rules.

2. AlphaZero challenges the conventional approach of using handcrafted evaluation functions and heuristics, instead learning entirely from self-play using deep neural networks and a general reinforcement learning algorithm.

3. The neural network architecture and training process are highly general, allowing AlphaZero to master different games with distinct characteristics like chess, shogi, and Go, revealing underlying principles of learning and search.

4. AlphaZero's performance suggests that general-purpose reinforcement learning algorithms may be able to master a wide range of complex domains without human knowledge or data.

5. The success of AlphaZero could lead to new approaches in artificial intelligence that rely more on general learning capabilities rather than domain-specific expertise.

Surprising Elements:

1. AlphaZero achieved superhuman performance in chess and shogi, which were thought to be less suited for neural network architectures due to their position-dependent, asymmetric rules, and long-range interactions.

2. AlphaZero convincingly defeated the world-champion programs in chess (Stockfish) and shogi (Elmo), which had been carefully engineered with human expertise over decades.

3. The algorithm achieved superhuman performance in all three games (chess, shogi, Go) within 24 hours of training from random initialization, without any human knowledge or data.

4. AlphaZero's success challenges the conventional wisdom that handcrafted evaluation functions and domain-specific heuristics are essential for achieving high performance in complex games like chess and shogi.

Relevant Quotes:

1. "AlphaZero achieved within 24 hours a superhuman level of play in the games of chess and shogi (Japanese chess) as well as Go, and convincingly defeated a world-champion program in each case."

2. "AlphaZero replaces the handcrafted knowledge and domain-specific augmentations used in traditional game-playing programs with deep neural networks and a tabula rasa reinforcement learning algorithm."

3. "AlphaZero utilises a deep neural network (p;v) =f(s) with parameters . This neural network takes the board position s as an input and outputs a vector of move probabilities p with components pa=Pr(ajs) for each action a, and a scalar value v estimating the expected outcome z from position s, v E[zjs]."

4. "AlphaZero learns these move probabilities and value estimates entirely from self-play; these are then used to guide its search."

5. "The AlphaZero algorithm described in this paper differs from the original AlphaGo Zero algorithm in several respects."