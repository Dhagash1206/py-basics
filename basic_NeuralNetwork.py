import torch
import torch.nn as nn
import torch.optim as optim

model = nn.Sequential(
    nn.Linear(2,4),
    nn.ReLU(),
    nn.Linear(4,1)
)

x = torch.tensor([[1.0,2.0],[2.0,3.0],[3.0,4.0]])
y = torch.tensor([[1.0],[2.0],[3.0]])

loss_fn = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

for i in range(100):
    pred = model(x)
    loss = loss_fn(pred, y)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()