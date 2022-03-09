from typing import List

import torch
from torch import nn
from fluentnet.seresnet import SEResNet, SEBasicBlock
from fluentnet.attention import Attention


class FluentNetOneModel(nn.Module):
    def __init__(
        self,
        resnet_layers: List[int] = [2] * 8,
        resnet_block=SEBasicBlock,
        bilstm_dropout: float = 0.2,
        attention_dropout: float = 0.0,
        attention_dim_head: int = 128,
        hidden_size: int = 512,  # As per paper
    ):
        super().__init__()
        self.seresnet = SEResNet(resnet_block, layers=resnet_layers, num_classes=1)
        self.bilstm_layer = nn.LSTM(input_size=64, hidden_size=hidden_size, bidirectional=True, num_layers=2, dropout=bilstm_dropout)
        self.attention_layer = Attention(dim=1024, dim_head=attention_dim_head, heads=1, dropout=attention_dropout)  # Global attention
        self.fc = nn.Linear(in_features=1024 * hidden_size, out_features=1)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x: torch.Tensor):
        out = self.seresnet(x)
        out, _ = self.bilstm_layer(out.flatten(-2, -1))
        out = self.attention_layer(out)
        out = out.flatten(1)
        out = self.fc(out)
        out = self.sigmoid(out)
        return out


class FluentNet:
    def __init__(self):
        self.sound_rep_model = FluentNetOneModel()
        self.word_rep_model = FluentNetOneModel()
        self.phrase_rep_model = FluentNetOneModel()
        self.revision_model = FluentNetOneModel()
        self.interjection_model = FluentNetOneModel()
        self.prolongation_model = FluentNetOneModel()

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        sound_rep = self.sound_rep_model(x)
        word_rep = self.word_rep_model(x)
        phrase_rep = self.phrase_rep_model(x)
        revision = self.revision_model(x)
        interjection = self.interjection_model(x)
        prolongation = self.prolongation_model(x)

        return sound_rep, word_rep, phrase_rep, revision, interjection, prolongation
