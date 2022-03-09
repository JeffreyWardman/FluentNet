from pytest import fixture
import torch


@fixture
def input():
    return torch.rand((1, 3, 256, 256))
