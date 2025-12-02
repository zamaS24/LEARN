from torch import nn, tensor
import torch


# This is a simple perceptron layer 
linear = nn.Linear(in_features=4, out_features=1)

# returns (output, h_t)
RNN = nn.RNN(input_size=4, hidden_size=6, num_layers=3 )

x = tensor([[1,2,3,4]], dtype=torch.float32)


print('linear(x)', linear(x))




# LORA Fine tuning, inject low rank learnable weight matrices over the network





