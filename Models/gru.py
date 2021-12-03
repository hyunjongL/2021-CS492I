import torch
import torch.nn as nn


class GRUNet(nn.Module):
    """
    Usage:

    gru = GRUNet(in_channels, hid_channels, out_channels, num_layers, drop_prob=0.2)
    pred = gruNet(x)
    음성 파일의 길이가 서로 다르기 때문에 recurrent 한 모델을 사용해야함. 따라서 GRU를 사용함.


    """
    def __init__(self, in_channels, hid_channels, out_channels, num_layers, drop_prob=0.2):
        super(GRUNet, self).__init__()

        self.in_channels = in_channels
        self.hid_channels = hid_channels
        self.num_layers = num_layers
        
        self.relu = nn.ReLU()
        self.gru = nn.GRU(in_channels, hid_channels, num_layers, batch_first=True, dropout=drop_prob)
        self.fc = nn.Linear(hid_channels, out_channels)

    def _get_init_states(self, batch_size):
        weight = next(self.parameters()).data
        init_states = weight.new(self.num_layers, batch_size, self.hid_channels).zero_().to(device)
        return init_states
            
    def forward(self, x):
        # Usage example: GRULayer(x, NUM_FEATURES)
        # x.shape = NUM_BATCHES x 10 x 128

        # batch_size, time_length, num_features = x.shape
        # init_states = self._get_init_states(batch_size)
        # out, h = self.gru(x, init_states)
        out = self.fc(self.relu(self.gru(x)))
        
        return out
    
