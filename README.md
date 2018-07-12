[![License](https://img.shields.io/badge/License-MIT-blue.svg)](/LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Tensorflow-orange.svg)](https://www.tensorflow.org/)
[![Python](https://img.shields.io/badge/Python-3.5-green.svg)]()
[![Docker](https://img.shields.io/badge/Docker-Available-FF69B4.svg)](https://hub.docker.com/r/ceruleanwang/personae/)

# Personae - RL & SL Methods and Envs For Quantitative Trading

Personae is a repo that implements papers proposed methods in Deep Reinforcement Learning & Supervised Learning and applies them to simulate future financial trends. 

Based on Ceruleanacg's repo Personae's framework, I've personalized it to support TD's mutual funds, which I am currently investing in. Currently retraining it to more accurately predict my funds of interest. As of July 10th, 2018, I've earned $378 off mutual funds! :)

# Implemented Models (by Ceruleanacg)

+ [Deep Deterministic Policy Gradient (DDPG)](algorithm/RL/DDPG.py)   
Implement of DDPG with TensorFlow.
    > arXiv:1509.02971: [Continuous control with deep reinforcement learning](https://arxiv.org/abs/1509.02971)

+ [Double DQN](algorithm/RL/DoubleDQN.py)    
Implement of Double-DQN with TensorFlow.   
    > arXiv:1509.06461: [Deep Reinforcement Learning with Double Q-learning](https://arxiv.org/abs/1509.06461)
    
+ [Dueling-DQN](algorithm/RL/DuelingDQN.py)     
Implement of Dueling-DQN with TensorFlow.    
    > arXiv:1511.06581: [Dueling Network Architectures for Deep Reinforcement Learning](https://arxiv.org/abs/1511.06581)     
+ [Policy Gradient](algorithm/RL/PolicyGradient.py)   
Implement of Policy Gradient with TensorFlow.
    > NIPS. Vol. 99. 1999: [Policy gradient methods for reinforcement learning with function approximation](https://papers.nips.cc/paper/1713-policy-gradient-methods-for-reinforcement-learning-with-function-approximation.pdf)

+ [DA-RNN (DualAttnRNN)](algorithm/SL/DualAttnRNN.py)      
Implement of arXiv:1704.02971, DA-RNN with TensorFlow.
    > arXiv:1704.02971: [A Dual-Stage Attention-Based Recurrent Neural Network for Time Series Prediction](https://arxiv.org/abs/1704.02971)

+ [TreNet (HNN)](algorithm/SL/TreNet.py)     
Implement of TreNet with TensorFlow.    
    > IJCAI 2017. [Hybrid Neural Networks for Learning the Trend in Time Series](https://www.ijcai.org/proceedings/2017/0316.pdf)

+ [Naive-LSTM (LSTM)](algorithm/SL/NaiveLSTM.py)    
Implement of simple LSTM based model with TensorFlow.    
    > arXiv:1506.02078: [Visualizing and Understanding Recurrent Networks](https://arxiv.org/abs/1506.02078)     


# Requirements

Before you start testing, following requirements are needed.

- Python3.5
- TensorFlow1.4
- numpy
- scipy
- pandas
- rqalpha
- sklearn
- tushare
- matplotlib
- mongoengine


The original repo had a GPU docker, but I've included a CPU dockerfile as well. 

# How to Use

### Running the model

### Retraining the model