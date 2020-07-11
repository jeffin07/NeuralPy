import pytest
from torch.nn import AvgPool2d as _AvgPool2D
from neuralpy.layers import AvgPool2D


def test_AvgPool2D_should_throws_type_error():
    with pytest.raises(TypeError) as ex:
        x = AvgPool2D()


@pytest.mark.parametrize(
    'kernel_size, stride, padding, dilation, return_indices, \
    ceil_mode, name',
    [
        # Checking kernel size validation
        ("invalid", 3, 3, 3,  False, False, "test"),
        (("", 3), 3, 3, 3,  False, False, "test"),
        ((3, ""), 3, 3, 3,  False, False, "test"),

        # Checking stride validation
        ((3, 3), "invalid", 3, 3,  False, False, "test"),
        ((3, 3), ("", 3), 3, 3,  False, False, "test"),
        ((3, 3), (3, ""), 3, 3,  False, False, "test"),

        # Checking padding validation
        ((3, 3), (3, 3), "invalid", 3,  False, False, "test"),
        ((3, 3), (3, 3), ("", 3), 3,  False, False, "test"),
        ((3, 3), (3, 3), (3, ""), 3,  False, False, "test"),

        # Checking dilation validation
        ((3, 3), (3, 3), (3, 3), "invalid",  False, False, "test"),
        ((3, 3), (3, 3), (3, 3), ("", 3), False, False, "test"),
        ((3, 3), (3, 3), (3, 3), (3, ""), False, False, "test"),

        # Checking return indices validation
        ((3, 3), (3, 3), (3, 3), (3, 3), "invalid", False, "test"),
        ((3, 3), (3, 3), (3, 3), (3, 3), 12.5, False, "test"),

        # Checking ceil mode validation
        ((3, 3), (3, 3), (3, 3), (3, 3), False, "test", "test"),
        ((3, 3), (3, 3), (3, 3), (3, 3), False, 23.4, "test"),

        # Checking name validation
        ((3, 3), (3, 3), (3, 3), (3, 3), False, False, False),
        ((3, 3), (3, 3), (3, 3), (3, 3), False, False, 12),
    ]
)
def test_AvgPool2D_throws_value_error(
    kernel_size, stride, padding, dilation,
    return_indices, ceil_mode, name):
        with pytest.raises(ValueError) as ex:
            x = AvgPool2D(
                    kernel_size=kernel_size, stride=stride,
                    padding=padding, dilation=dilation,
                    return_indices=return_indices,
                    ceil_mode=ceil_mode, name=name)

# Possible values
kernel_sizes = [3, (1,1)]
strides = [2, (2,2), None]
paddings = [1, (1,1)]
dilations = [1]
return_indicess = [False]
ceil_modes = [True]
names = [None, 'Test']


@pytest.mark.parametrize(
    "kernel_size, stride, padding, dilation, return_indices, \
    ceil_mode, name",
    [(kernel_size, stride, padding, dilation, return_indices,\
    ceil_mode, name)
    for kernel_size in kernel_sizes
    for stride in strides
    for padding in paddings
    for dilation in dilations
    for return_indices in return_indicess
    for ceil_mode in ceil_modes
    for name in names]
)
def test_AvgPool2D_get_layer_method(
    kernel_size, stride, padding, dilation,
    return_indices, ceil_mode, name):


        x = AvgPool2D(
                kernel_size=kernel_size, stride=stride,
                padding=padding, dilation=dilation,
                return_indices=return_indices,
                ceil_mode=ceil_mode, name=name
        )

        prev_dim = (3, 6, (6, 18, 32) )
        layer_details = x.get_input_dim(prev_dim, "conv2d")

        details = x.get_layer()

        assert isinstance(details, dict) == True

        assert details['name'] == name

        assert issubclass(details['layer'], _AvgPool2D) == True

        assert isinstance(
                details['keyword_arguments'], dict) == True

        assert details['keyword_arguments']['kernel_size'] == kernel_size

        if stride is None:
            assert details['keyword_arguments']['stride'] == kernel_size
        else:    
            assert details['keyword_arguments']['stride'] == stride

        assert details['keyword_arguments']['padding'] == padding

        assert details['keyword_arguments']['dilation'] == dilation

        assert details['keyword_arguments']['return_indices'] == return_indices

        assert details['keyword_arguments']['ceil_mode'] == ceil_mode
