"""Module to load and resize images"""


import graphlab as gl
import os

# gl.product_key.set_product_key('your key')


def load(path):
    """
    Loads images into an SFrame. Each image file name in the directory should
    start with the name of the class that it belongs to.

    Parameters
    ------------------
    path: Directory to load images from.

    Returns
    __________________
    SFrame with images and path
    """

    train_dir = path
    train_sf = gl.image_analysis.load_images(train_dir, random_order=True)
    return train_sf


def resize(train):
    """
    Resizes the image to 256x256.

    Parameters
    _________________
    train_sf: SFrame with images that need to be resized

    Returns
    _________________
    SFrame with resized image
    """

    train['image'] = gl.image_analysis.resize(train['image'], 256, 256)
    return train


def set_label(train):
    """
    Sets labels for training the images. Each image file name should start with
    the class that it belongs to followed by underscore. Eg. burger_01.jpg

    Parameters
    __________________
    train_sf: SFrame with images and path name

    Returns
    __________________
    SFrame with additional columns 'label' and 'category'
    'label' contains the name of the category. 'category' is numerical representation
    of the categories.
    """
    train['label'] = train['path'].apply(lambda x: x.split('/')[-1].split('_')[0])
    unique_labels = train['label'].unique().sort()
    class_map = {}

    for i in range(len(unique_labels)):
        class_map[unique_labels[i]] = i

    train['category'] = train['label'].apply(lambda x: class_map[x])
    return train, class_map
