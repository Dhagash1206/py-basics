import torch
import torch.nn as nn
import torch.optim as optim

a = torch.tensor([1,2,3])
b = torch.tensor([4,5,6])
c = a + b

m = torch.tensor([[1,2],[3,4]])
d = m * 2

x = torch.rand(3,3)
y = torch.ones(3,3)
z = x + y

model = nn.Linear(3,1)
inp = torch.tensor([[1.0,2.0,3.0]])
out = model(inp)

loss_fn = nn.MSELoss()
target = torch.tensor([[1.0]])
loss = loss_fn(out,target)

opt = optim.SGD(model.parameters(),lr=0.01)
opt.zero_grad()
loss.backward()
opt.step()

print(c)
print(d)
print(z)
print(out)
print(loss)