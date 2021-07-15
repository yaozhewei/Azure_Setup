import torch

X = torch.randn(1, 1)
W = torch.nn.Linear(1, 1, bias=False)
W.weight.data = W.weight.data * 0 + 1

print('X: ', X)
print('W: ', W.weight)

Y = (W(X)).square() / 2.

print('Y: ', Y)

loss = Y.sum()

loss.backward()

print('W grad: ', W.weight.grad)

# W = W.detach() + ...

W.weight.grad = None

print('W grad: ', W.weight.grad)


print('---' * 30)

Double_W = W.weight.data * 2
Original_W = W.weight.data

# W.weight.data
W.weight.data = Original_W - Original_W.detach() + Double_W.detach()

#W = W
#W.grad = W_fake.grad
#FC(W_fake, x, bias)

print('X: ', X)
print('W: ', W.weight)

Y = (W(X)).square() / 2.

print('Y: ', Y)

loss = Y.sum()

loss.backward()

print('W grad: ', W.weight.grad)
