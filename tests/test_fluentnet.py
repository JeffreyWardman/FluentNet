import torch
from fluentnet.fluentnet import FluentNet


def test_FluentNet(input):
    model = FluentNet()
    outputs = model.forward(input)
    assert isinstance(outputs, tuple), "output is a tuple"
    for output in outputs:
        output = output.detach().numpy()
        assert output.shape == torch.Size([input.shape[0], 1]), "correct number of batches outputted"
        assert (output >= 0).all() and (output <= 1).all(), "sigmoid activation function included in model"
