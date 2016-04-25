"""Training the model"""

import graphlab as gl
import argparse as ap
import os
import loadimages as li
import cnn
import pickle


parser = ap.ArgumentParser()
parser.add_argument("-t", "--trainingSet", help="Path to Training Set", required="True")
args = vars(parser.parse_args())

path = args["trainingSet"]

train = li.load(path)
train = li.resize(train)
train, class_map = li.set_label(train)

# Scale the image
mean_image = train['image'].mean()

# Splitting data into training and test set
training_data, validation_data = train.random_split(0.8, seed=1)

net = net.build_cnn()
model = gl.neuralnet_classifier.create(training_data['image', 'category'],
                                       target='category',
                                       network=net,
                                       validation_set=validation_data['image',
                                       'category'],
                                       metric=['accuracy', 'recall@2'],
                                       max_iterations=50,
                                       mean_image=mean_image,
                                       random_crop=True,
                                       input_shape=(3, 200, 200),
                                       random_mirror=True,
                                       class_weights='auto',
                                       l2_regularization=.0005)

model.save('74per_model')
validation_data.save('test_data.csv', format='csv')
with open('class_map.pickle', 'wb') as fhand:
    pickle.dump(a, fhand)
