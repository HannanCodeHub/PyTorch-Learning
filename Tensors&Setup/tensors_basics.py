import torch

x = torch.tensor([1,2,3]) #1d tensor
print(x)

y = torch.tensor([ #2d tensor
    [3,4],
    [5,6]
])
print(y)
print(y.shape) #rows and cols batayega.

o= torch.ones(3,2) #fill matrix with 1
print(o)

z = torch.zeros(2,3) #fill matrix with 0
print(z)

r = torch.rand(2,3) #fill matrix with random values
print(r)



i = torch.tensor([1,2,4])
print(i[1])

d_2 = torch.tensor([
    [2,3,4],  #[0,0 , 0,1 , 0,2]
    [5,6,7]   #[1,0 , 1,1 , 1,2]
])

print(d_2[1,2]) #7

#linear example:
x = torch.tensor([10. , 20. ,33. ])
y = torch.tensor([15. , 25. ,30.])

#wrong guesses :
w = torch.tensor(0.0)
b = torch.tensor(0.0)

y_pred = w * x + b

loss = ((y_pred - y) ** 2).mean()

print("Predicted Values:", y_pred) # 0 , 0 , 0
print("Actual Values:",y) # 15,25,30

print("loss:" , loss) 