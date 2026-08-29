import torch
import torch.nn as nn

image = torch.randn(1, 1, 28, 28)

conv = nn.Conv2d(
    in_channels=1,
    out_channels=8,
    kernel_size=3,
    stride=1,
    padding=0
)

output = conv(image)

print("Input Image:", image.shape)
print("Output Image:", output.shape)

#Pooling:
x = torch.randn(1,8, 28,28)

pool = nn.MaxPool2d(kernel_size=2)

y = pool(x)

print("before pooling:", x.shape)
print("after pooling:", y.shape)