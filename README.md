<p align="center">
 <img src="https://user-images.githubusercontent.com/34741145/81591141-99752900-93d9-11ea-9ef6-cc2c68daaa19.png" alt="Logo of NeuralPy" />
 <br />
 A Keras like library works on top of PyTorch
</p>

> Currently, this library is at a very early stage of development. README and Documentation is incomplete.

## Table of contents:
- [Introduction](#introduction)
- [Pytorch](#pytorch)
- [Install](#install)
- [Dependencies](#dependencies)
- [Get Started](#get-started)
- [Documentation](#documentation)
- [Examples](#examples)
- [Blogs and Tutorials](#blogs-and-tutorials)
- [Support](#support)
- [Contributing](#contributing)
- [Next Release Plan](#next-release-plan)
- [License](#license)

## Introduction
NeuralPy is a Keras like deep learning library that works on top of PyTorch.

## Pytorch

## Install

## Dependencies

## Get Started
Let's create a linear regression model in 100 seconds.

### Importing the dependencies
```python
import numpy as np

from neuralpy.models import Sequential
from neuralpy.layers import Dense
from neuralpy.optimizer import Adam
from neuralpy.loss_functions import MSELoss
```

### Making some random data
```python
# Random seed for numpy
np.random.seed(1969)

# Generating the data
X_train = np.random.rand(100, 1) * 10
y_train = X_train + 5 *np.random.rand(100, 1)

X_validation = np.random.rand(100, 1) * 10
y_validation = X_validation + 5 * np.random.rand(100, 1)

X_test = np.random.rand(10, 1) * 10
y_test = X_test + 5 * np.random.rand(10, 1)
```

### Making the model
```python
# Making the model
model = Sequential()
model.add(Dense(n_nodes=1, n_inputs=1, bias=True, name="Input Layer"))

# Compiling the model
model.compile(optimizer=Adam(), loss_function=MSELoss())

# Printing model summary
model.summary()
```

### Training the model
```python
model.fit(train_data=(X_train, y_train), test_data=(X_validation, y_validation), epochs=300, batch_size=4)
```

### Predicting using the trained model
```python
model.predict(X=X_test, batch_size=32)
```

## Documentation
The documentation for NeuralPy is available at [https://neuralpy.imdeepmind.com/](https://neuralpy.imdeepmind.com/)

## Examples 
Several examples for projects in NeuralPy are available at [github.com/imdeepmind/NeuralPy-Examples](github.com/imdeepmind/NeuralPy-Examples). Please check visit this link.

## Blogs and Tutorials
For now there are no blogs or tutorials available, I'll update once I post something. Please also have look at the examples currently available.

## Support
If you are facing any issues using NeuralPy, then please raise a issue on GitHub or contact with me. 

## Contributing
Feel free to contribute to this project. If you need some help to get started, then reach me or open an github issue.

## Next Release Plan
Here is a list if things that I want to add in the library before the `0.1.0-alpha` release.
  * [x] Models
    * [x] Sequential
  * [ ] Layers
    * [x] Linear
      * [x] Dense
  * [ ] Regulariziers
      * [ ] Dropout
  * [x] Activation Functions
      * [x] Softmax
      * [x] Sigmoid
      * [x] Tanh
      * [x] ReLU
      * [x] LeakyReLU
  * [x] Loss Functions
      * [x] MSELoss
      * [x] CrossEntropyLoss
      * [x] NLLLoss
      * [x] BCELoss
  * [ ] Optimizers
      * [x] Adam
      * [x] SGD
      * [x] Adagrad
      * [ ] RMSprop
  * [x] GPU Support
  * [ ] User input validation
  * [ ] Error handling
  * [ ] Documentation and Code Commenting
  * [ ] Sample code and Blogs
  * [ ] Proper README
  * [ ] Configure project for PyPI

## License
[MIT](https://github.com/imdeepmind/NeuralPy/blob/master/LICENSE)
