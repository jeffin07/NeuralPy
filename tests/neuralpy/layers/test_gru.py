import pytest
from torch.nn import GRU as _GRU
from neuralpy.layers import GRU


def test_GRU_should_throws_type_error():
    with pytest.raises(TypeError) as ex:
        x = GRU()


@pytest.mark.parametrize(
    "hidden_size, num_layers, input_size,\
    bias, batch_first, dropout, bidirectional,name",
    [
        # Checking hidden_size validation
        (False, 1, 5, False, False, 0, False, "test"),
        (345.6, 1, 5, False, False, 0, False, "test"),
        ("this", 1, 5, False, False, 0, False, "test"),

        # Checking num_layers validation
        (128, -3, 5, False, False, 0, False, "test"),
        (128, 43.4, 5, False, False, 0, False, "test"),
        (128, False, 5, False, False, 0, False, "test"),
        (128, "test", 5, False, False, 0, False, "test"),

        # Checking input_size validation
        (128, 1, "test", False, False, 0, False, "test"),
        (128, 1, False, False, False, 0, False, "test"),
        (128, 1, 5.5, False, False, 0, False, "test"),
        (128, 1, -56, False, False, 0, False, "test"),

        # Checking bias validation
        (128, 1, 5, "test", False, 0, False, "test"),
        (128, 1, 5, 345, False, 0, False, "test"),
        (128, 1, 5, 45.64, False, 0, False, "test"),

        # Checking batch_first
        (128, 1, 5, False, "test", 0, False, "test"),
        (128, 1, 5, False, 4.53, 0, False, "test"),
        (128, 1, 5, False, 23, 0, False, "test"),

        # Checking dropout validation
        (128, 1, 5, False, False, "test", False, "test"),
        (128, 1, 5, False, False, "", False, "test"),
        (128, 1, 5, False, False, 45.43, 234.43, "test"),

        # Checking bidirectional validation
        (128, 1, 5, False, False, 0, "test", "test"),
        (128, 1, 5, False, False, 0, 234.2, "test"),
        (128, 1, 5, False, False, 0, 34, "test"),

        # Checking name validation
        (128, 1, 5, False, False, 0, False, False),
        (128, 1, 5, False, False, 0, False, ""),
        (128, 1, 5, False, False, 0, False, 234),
    ]
)
def test_GRU_should_throw_value_error(
        hidden_size, num_layers, input_size,
        bias, batch_first, dropout, bidirectional, name):
    with pytest.raises(ValueError) as ex:
        x = GRU(
            hidden_size=hidden_size, input_size=input_size,
            num_layers=num_layers, bias=bias,
            batch_first=batch_first, dropout=dropout,
            bidirectional=bidirectional, name=name)


# Possible values
input_sizes = [1, 2, None]
hidden_sizes = [2, 2]
num_layerses = [1,  4]
biases = [False, True]
batch_firsts = [False, True]
dropouts = [1, 2]
bidirectionals = [False, True]
names = ['Test', None]


@pytest.mark.parametrize(
    "input_size, hidden_size, num_layers,\
    bias, batch_first, dropout, bidirectional,name",
    [(input_size, hidden_size, num_layers,
      bias, batch_first, dropout, bidirectional, name)
     for input_size in input_sizes
     for hidden_size in hidden_sizes
     for num_layers in num_layerses
     for bias in biases
     for batch_first in batch_firsts
     for dropout in dropouts
     for bidirectional in bidirectionals
     for name in names]
)
def test_GRU_layer_get_method(
        input_size, hidden_size, num_layers,
        bias, batch_first, dropout, bidirectional, name):

    x = GRU(
        input_size=input_size, hidden_size=hidden_size,
        num_layers=num_layers, bias=bias,
        batch_first=batch_first, dropout=dropout,
        bidirectional=bidirectional, name=name)

    prev_dim = (6,)

    if input_size is None:
        x.get_input_dim(prev_dim, "GRU")

    details = x.get_layer()

    assert isinstance(details, dict) == True

    assert details['layer_details'] == (hidden_size, )

    assert details['name'] == name

    assert issubclass(details['layer'], _GRU) == True

    assert isinstance(details['keyword_arguments'], dict) == True

    if input_size:
        assert details['keyword_arguments']['input_size'] == input_size
    else:
        assert details['keyword_arguments']['input_size'] == prev_dim[0]

    assert details['keyword_arguments']['hidden_size'] == hidden_size

    assert details['keyword_arguments']['num_layers'] == num_layers

    assert details['keyword_arguments']['hidden_size'] == hidden_size

    assert details['keyword_arguments']['num_layers'] == num_layers

    assert details['keyword_arguments']['bias'] == bias

    assert details['keyword_arguments']['batch_first'] == batch_first

    assert details['keyword_arguments']['dropout'] == dropout

    assert details['keyword_arguments']['bidirectional'] == bidirectional


def test_GRU_with_invalid_layer():
    with pytest.raises(ValueError) as ex:
        x = GRU(hidden_size=128, num_layers=1, input_size=None)

        x.get_input_dim((64, ), "dense")
