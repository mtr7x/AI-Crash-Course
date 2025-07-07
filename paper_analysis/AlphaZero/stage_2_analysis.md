Here is a summary in the style of Andrej Karpathy:

The paper describes AlphaZero, a general reinforcement learning algorithm that achieves superhuman performance across the games of chess, shogi, and Go, starting from just the game rules. Let's break this down:

At its core, AlphaZero uses a neural network f(s) that takes a game position s as input and outputs:
1) p - A vector of move probabilities for each possible action a 
2) v - A scalar value estimating the expected outcome from position s

This (p, v) output is all AlphaZero uses to play - no handcrafted evaluation functions or heuristics.

To actually search for the best move, AlphaZero runs Monte Carlo tree search (MCTS) using the neural network outputs to guide the search. It plays out many simulated games, selecting moves proportionally to p and the visit counts, to construct a tree representing the search probabilities.

The neural network f is trained from scratch solely by self-play reinforcement learning on games of chess/shogi/Go. After each game, it adjusts the network weights to: 
1) Predict accurate final outcomes v compared to the game result z
2) Match the search probabilities p to the actual search visit counts

So in essence, AlphaZero learns to accurately evaluate positions and predict good moves, all from playing against itself according to a simple RL loss.

What's remarkable is that this generic, self-learning algorithm can reach superhuman performance across such different domains as chess, shogi and Go, with no human knowledge except the rules. The potential is clear - general RL methods that can tackle complex domains from first principles.

However, the algorithm is incredibly computationally expensive, running millions of self-play games. And the performance likely relies on fortunate properties of these perfect information games. Extending this to imperfect information or unbounded domains remains an open challenge for future work.

Overall, AlphaZero takes an important step towards general game-playing AI by replacing domain heuristics with a powerful RL framework that can learn directly from the rules. The results push the boundaries of what we thought possible with brute force learning from first principles.