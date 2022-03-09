import torch
from fluentnet.fluentnet import FluentNet


def test_FluentNet(input):
    model = FluentNet()
    output = model.forward(input)
    output = output.detach().numpy()
    assert output.shape == torch.Size([input.shape[0], 1, 6]), "correct number of batches and classes outputted"
    assert (output >= 0).all() and (output <= 1).all(), "sigmoid activation function included in model"
