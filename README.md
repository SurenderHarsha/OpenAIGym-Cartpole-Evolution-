# OpenAIGym-Cartpole-Evolution-
This is an effecient implementation of the OpenAI gym's cartpole AI using a NeuroEvolution Algorithm (Similar to NEAT) which outperforms the traditional RL Techniques.

This is based on https://blog.openai.com/evolution-strategies/ 
But the cartpole environment is too simple to find significant difference between ES and RL techniques.
Therefore the maximum reward and steps have been increased to 15000. The reason for this is that Evolution strategies may get lucky and converge to a solution in just 2 episodes as tested. Hence I have increased the time of gameplay.

On performing tests, the Algorithm takes approximately on an average of 75 episodes to converge to a solution of 15000.

It is based on the evolution of weights of a perceptron using genetic algorithms.
For now to Solve for a score of 195, it takes about 1-40 Episodes randomly.
