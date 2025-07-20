import os

PROJECT_PATH = '/content/drive/MyDrive/ames-housing-ml'
TRAIN_PATH = os.path.join(PROJECT_PATH, 'data/train.csv')
TEST_PATH = os.path.join(PROJECT_PATH, 'data/test.csv')

def load_train_test():
    import pandas as pd
    train = pd.read_csv(TRAIN_PATH)
    test = pd.read_csv(TEST_PATH)
    return train, test
