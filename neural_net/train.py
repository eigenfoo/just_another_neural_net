'''
train.py
'''

import neural_net as nn

NEURAL_NET_FILENAME = input('Neural network init filename: ')
NUM_INPUT, NUM_HIDDEN, NUM_OUTPUT, WEIGHTS = \
    nn.read_neural_net_file(NEURAL_NET_FILENAME)

TRAIN_FILENAME = input('Neural network training data filename: ')
TRAINING_DATA = nn.read_data_file(TRAIN_FILENAME)

LEARNING_RATE = float(input('Learning rate: '))
EPOCHS = int(input('Number of epochs: '))
WEIGHTS = nn.train(WEIGHTS, TRAINING_DATA, LEARNING_RATE, EPOCHS)

TRAINED_FILENAME = input('Neural network trained filename: ')
nn.write_trained_file(TRAINED_FILENAME, NUM_INPUT, NUM_HIDDEN, NUM_OUTPUT,
                      WEIGHTS)
