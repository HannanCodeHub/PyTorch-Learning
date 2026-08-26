import torch

#requires_grad = True/False
w = torch.tensor(2.0 , requires_grad = True)
x = torch.tensor(4.0)

y_pred =  w * x
actual_pred = torch.tensor(10)

loss = (y_pred - actual_pred) ** 2 
loss.backward()
print("y_pred:", y_pred.item())
print("actual_pred:", actual_pred.item())
print("loss:", loss.item())

#gradient desc:

#fixed input:
x = torch.tensor(3.0)

#learnable number:
w = torch.tensor(4.0, requires_grad=True)

#correct answer
y_true = torch.tensor(10.0)


#learning rate:
lr = 0.1

#pred:
y_pred =  w * x 
loss = (y_pred - y_true) ** 2 

loss.backward() #zaruri hai warna add up hujayega loss.

print("Before Updating")
print("w:", w.item())
print("loss:", loss.item())
print("grad:", w.grad.item())

with torch.no_grad():
    w -= lr * w.grad

w.grad.zero_()

print("After Update:")
print("w:", w.item())

#training loop:
x = torch.tensor([1. ,2. , 3. , 4. ])
y_true = torch.tensor([2. , 4. ,6. , 8.])

w = torch.tensor(0.0 , requires_grad= True)

lr = 0.1

epochs = 10

for epoch in range(epochs):

    #step1 : prediction
    y_pred = w * x

    #step2 : loss
    loss = ((y_pred - y_true) ** 2 ).mean()

    loss.backward() #garbar pta lagao

    with torch.no_grad():
        w-= lr * w.grad


    print(f"Epoch {epoch+1}: w = {w.item():.4f}, loss = {loss.item():.4f}")