import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np


#input : distance between 2 pipes bird position
# e.g : [birdx, birdy, pipe1_x, pipe1_y, pipe2_x, pipe2_y] : 6

#output : jump or no jump
# e.g [jump] 1
dataset = [([1,2,3,4,5,6],0)]

class Simple_Net(nn.Module):
    def __init__(self):
        super(Simple_Net, self).__init__()
        self.fc1 = nn.Linear(6, 7)
        self.fc2 = nn.Linear(7, 1)
        #self.relu = nn.Sigmoid()

    def forward(self, x):
        x = self.fc1(x)
        x = self.fc2(x)
        return x

# Create an instance of the neural network
net = Simple_Net()

# Define the loss function and optimizer
criterion = nn.MSELoss()
optimizer = optim.Adam(net.parameters(), lr=0.001)

# Load the data and preprocess


# Train the network
for epoch in range(600):
    running_loss = 0.0
    for inp, tar in dataset:
        inp = [float(i) for i in inp]
        tar = float(tar)
        input_tensor = torch.tensor(inp)
        # to fix dimensionality conflict add it to a list
        tar_tensor = torch.tensor([tar])
        optimizer.zero_grad()
        outputs = net(input_tensor)
        #print(f'{input_tensor.shape},{tar_tensor.shape}, {outputs.shape}')
        loss = criterion(outputs, tar_tensor)
        loss.backward()
        optimizer.step()

        running_loss += loss.item()

    print('[Epoch %d] loss: %.3f' % (epoch + 1, running_loss / len(dataset)))


with torch.no_grad():
    for inp, tar in dataset:
        inp = [float(i) for i in inp]
        tar = float(tar)
        input_tensor = torch.tensor(inp)
        # to fix dimensionality conflict add it to a list
        tar_tensor = torch.tensor([tar])
        outputs = net(input_tensor)
        print(f'For {inp} we expect {tar} and received {outputs.data}')