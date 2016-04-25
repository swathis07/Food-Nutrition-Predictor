# Food Nutrition Predictor

## Motivation

Fitness apps allow users to log their calorie intake. To do this, the user has to manually type in each item of food they had and serving size for each item they had after each meal. This can be a somewhat tedious process. This was the motivation for my project. Can we automate this process? Can an app identify what a food item is, from an image? Can it determine the serving size from the image? Being a prototype, I decided to focus on the question of identifying the food item from an image.

## Data

I looked at classifying eight different food items.

![Food Classes](/Food-Nutrition-Predictor/data/fooditems.png "Food classes")

I scraped images from Google using Google Custom Search API. I scraped around 6000 images for all eight classes. Images that were not relevant to the search query had to manually be deleted from the dataset. The images were resized to 256 x 256 pixels for processing by the model.


## Model

I built a Convolutional Neural Network using Graphlab. A convolutional network convolves several small filters on the input image. The space of filter activations in downsized and this step is repeated over till sufficiently high level features are extracted from the images. The features are then fed into the Feed Forward Neural Network that carries out the classification task at hand. In this case it classifies into the eight different categories.

![CNN](/Food-Nutrition-Predictor/data/convolution_rep.png "Representation of Convolutional Neural Network")

The Convolutional Neural Network I built has two convolutional layers and two full connected layers. Both convolutional layers have 64 filters each and both are downsampled using a Maxpool layer. A summary of the layers is below

### network layers ###
layer[0]: ConvolutionLayer
  init_random = gaussian
  padding = 0
  stride = 2
  num_channels = 64
  num_groups = 1
  kernel_size = 3
layer[1]: RectifiedLinearLayer
layer[2]: MaxPoolingLayer
  padding = 0
  stride = 2
  kernel_size = 3
layer[3]: ConvolutionLayer
  init_random = gaussian
  padding = 0
  stride = 1
  num_channels = 64
  num_groups = 1
  kernel_size = 3
layer[4]: RectifiedLinearLayer
layer[5]: MaxPoolingLayer
  padding = 0
  stride = 2
  kernel_size = 3
layer[6]: FlattenLayer
layer[7]: FullConnectionLayer
  init_sigma = 0.01
  init_random = gaussian
  init_bias = 0
  num_hidden_units = 64
layer[8]: RectifiedLinearLayer
layer[9]: DropoutLayer
  threshold = 0.5
layer[10]: FullConnectionLayer
  init_sigma = 0.01
  init_random = gaussian
  init_bias = 0
  num_hidden_units = 8
layer[11]: SoftmaxLayer
### end network layers ###

### network parameters ###
learning_rate = 0.001
random_mirror = 1
random_crop = 1
l2_regularization = 0.0005
metric = accuracy,recall@2
momentum = 0.9
