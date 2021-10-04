'''
Sets up datasets for training and testing the neural network
'''

import os
import raw_datasets
import rhymes

if __name__ == '__main__':
    data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))
    dict_path = os.path.join(data_path, 'rhyme_dict.json')
    train_path = os.path.join(data_path, 'train.csv')
    test_path = os.path.join(data_path, 'test.csv')

    rhymes.build_rhyme_dict(dict_path)
    raw_datasets.generate_dataset(50000, dict_path, train_path)
    raw_datasets.generate_dataset(10000, dict_path, test_path)


