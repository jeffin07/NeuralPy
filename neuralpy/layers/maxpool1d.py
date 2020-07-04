""" MaxPool1D for NeuralPy """

from torch.nn import MaxPool1d as _MaxPool1d


class MaxPool1d:
    """
        MaxPool1d Applies a 1D max pooling over an input
        To learn more about MaxPool1d, please check pytorch
        documentation at https://pytorch.org/docs/stable/nn.html#maxpool1d

        Supported Arguments:

            kernel_size: (Integer) the size of the window to take a max over
            stride: (Integer) the stride of the window.
                Default value is kernel_size
            padding: (Integer) implicit zero padding to be
                added on both sides
            dilation: (Integer) a parameter that controls the
                stride of elements in the window
            return_indices: (Boolean) if True, will return the
                max indices along with the outputs
            ceil_mode: (Boolean) when True, will use ceil instead
                of floor to compute the output shape
    """

    def __init__(
            self, kernel_size, stride=None, padding=0, dilation=1,
            return_indices=False, ceil_mode=False, name=None
            ):
        """
            __init__ method for MaxPool1d

            Supported Arguments:

            kernel_size: (Integer) the size of the window to take a max over
            stride: (Integer) the stride of the window.
                Default value is kernel_size
            padding: (Integer) implicit zero padding to be
                added on both sides
            dilation: (Integer) a parameter that controls the
                stride of elements in the window
            return_indices: (Boolean) if True, will return the
                max indices along with the outputs
            ceil_mode: (Boolean) when True, will use ceil instead
                of floor to compute the output shape
        """

        # Checking the kernel_size
        if not kernel_size and not isinstance(kernel_size, int):
            raise ValueError(
                "Please provide a valid value for kernel_size")

        # Checking the stride
        if stride and not isinstance(stride, int):
            raise ValueError(
                "Please provide a valid value for stride")

        # Checking the padding,  it is an optional filed
        if padding and not isinstance(padding, int):
            raise ValueError(
                "Please provide a valid value for padding")

        # Checking the dilation, it is an optional filed
        if dilation and not isinstance(dilation, int):
            raise ValueError(
                "Please provide a valid value for dialtion")

        # Checking the return_indices, it is an optional filed
        if return_indices and not isinstance(return_indices, bool):
            raise ValueError(
                "Please provide a valid value for return_indices")

        # Checking the ceil_mode, it is an optional filed
        if ceil_mode and not isinstance(ceil_mode, bool):
            raise ValueError(
                "Please provide a valid value for ceil_mode")

        # Checking the name, it is an optional filed
        if name is not None and not (isinstance(name, str) and name):
            raise ValueError("Please provide a valid name")

        # Storing the data
        self.__kernel_size = kernel_size
        self.__stride = stride

        self.__padding = padding
        self.__dilation = dilation
        self.__return_indices = return_indices
        self.__ceil_mode = ceil_mode
        self.__name = name

    def get_input_dim(self, prev_input_dim, prev_layer_type):
        """
            This method calculates the input shape for layer based on previous output layer.

            This method is used by the NeuralPy Models, for building the models.
            No need to call this method for using NeuralPy.
        """
        # MaxPool1d does not need to n_input, so returning None
        return None

    def get_layer(self):
        """
            This method returns the details as dict of the layer.

            This method is used by the NeuralPy Models, for building the models.
            No need to call this method for using NeuralPy.
        """
        # Returning all the details of the layer
        return{
            'layer_details': self.__kernel_size,
            'name': self.__name,
            'type': 'MaxPool1D',
            'layer': _MaxPool1d,
            'keyword_arguments': {
                    'kernel_size': self.__kernel_size,
                    'stride': self.__stride,
                    'padding': self.__padding,
                    'dilation': self.__dilation,
                    'return_indices': self.__return_indices,
                    'ceil_mode': self.__ceil_mode
            }
        }
