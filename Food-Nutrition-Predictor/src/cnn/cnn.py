"""Module to building convolutional neural network"""

import graphlab as gl


def build_cnn():   # Creating convolutional neural network
    """Build the Convolutional Neural Network
    Returns
    ______________
    Graphlab Neural Net object
    """


    layers = list()
    layers.append(gl.deeplearning.layers.ConvolutionLayer(kernel_size=3,
                                                          stride=2,
                                                          num_channels=64))
    layers.append(gl.deeplearning.layers.RectifiedLinearLayer())
    layers.append(gl.deeplearning.layers.MaxPooling(kernel_size=3, stride=2))
    layers.append(gl.deeplearning.layers.ConvolutionLayer(kernel_size=3,
                                                          stride=1,
                                                          num_channels=64))
    layers.append(gl.deeplearning.layers.RectifiedLinearLayer())
    layers.append(gl.deeplearning.layers.MaxPooling(kernel_size=3, stride=2))
    layers.append(gl.deeplearning.layers.FlattenLayer())
    layers.append(gl.deeplearning.layers.FullConnectionLayer(init_bias=0.0,
                                                             init_sigma=0.01,
                                                             num_hidden_units=64))
    layers.append(gl.deeplearning.layers.RectifiedLinearLayer())
    layers.append(gl.deeplearning.layers.DropoutLayer(threshold=0.5))
    layers.append(gl.deeplearning.layers.FullConnectionLayer(init_bias=0.0,
                                                             init_sigma=0.01,
                                                             num_hidden_units=8))
    layers.append(gl.deeplearning.layers.SoftmaxLayer())

    # Creating NeuralNet object to encapsulate layers
    net = gl.deeplearning.NeuralNet()
    net.layers = layers

    return net
