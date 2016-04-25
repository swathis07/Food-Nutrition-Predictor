# Food Nutrition Predictor

## Motivation

Fitness apps allow users to log their calorie intake. To do this, the user has to manually type in each item of food they had and the serving size of each of the item after each meal. This can be a somewhat tedious process. This was the motivation for my project. Can we automate this process? Can an app identify what a food item is, from an image? Can it determine the serving size from the image? Being a prototype, I decided to focus on the question of identifying the food item from an image.

## Data

I looked at classifying eight different food items.

![Food Classes](/Food-Nutrition-Predictor/data/fooditems.png "Food classes")

I scraped images from Google using Google Custom Search API. I scraped around 6000 images for all eight classes. Images that were not relevant to the search query had to manually be deleted from the dataset. The images were resized to 256 x 256 pixels for processing by the model.


## Model

I built a Convolutional Neural Network using Graphlab. A convolutional network convolves several small filters on the input image. The space of filter activations in downsized and this step is repeated over till sufficiently high level features are extracted from the images. The features are then fed into the Feed Forward Neural Network that carries out the classification task at hand. In this case it classifies into the eight different categories.

![CNN](/Food-Nutrition-Predictor/data/convolution_rep.png "Representation of Convolutional Neural Network")

The Convolutional Neural Network I built has two convolutional layers and two fully connected layers. Both convolutional layers have 64 filters each and both are downsampled using a Maxpool layer. I augmented my dataset by randomly mirroring and randomly cropping some of the images. I used L2 regularization to reduce overfitting. Momentum was set to 0.9. The activation function used was rectifier.

## Results

The accuracy of my model was 73.38%. I also looked at other metrics like top 2 accuracy and top 3 accuracy.
Top 2 and top 3 accuracy is calculated by looking at how often the true label is present in the top 2 and 3 predictions returned by the model respectively.
* **Top 1 accuracy: 73.38%**
* **Top 2 accuracy: 84.13%**
* **Top 3 accuracy: 91.27%**

The normalized confusion matrix below summarizes true labels vs. the predicted labels.

![cm_values](/Food-Nutrition-Predictor/data/cm_values.png "Confusion matrix values" = 100x100)

![Confusion_Matrix](/Food-Nutrition-Predictor/data/confusion_matrix.png "Normalized confusion Matrix")

As can be seen from the figure above, the darker blocks represent a higher percent of prediction. The values that lie on the diagonal represent the values whose predicted values were the same as the true value of the label. The figure shows that model performs fairly well in predicting the true label correctly.
