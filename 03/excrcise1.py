import torch
from torch import nn

if __name__ == "__main__":
    # problem1
    my_tensor = torch.one((32, 3, 128, 128))
    print("===problem1===")
    print(my_tensor.shape)

    # problem2
    my_conv = nn.Conv2d(in_channels=3, out_channels=16, kernel_size=3)
    out1 = my_conv(my_tensor)
    print("===problem2===")
    print(out1.shape)

    # problem3
    print("===problem3===")
    conv2 = nn.Conv2d(in_channels=3, out_channels=256, kernel_size=3, stride=2, padding=1)
    out2 = conv2(my_tensor)
    print(f"out2 : {out2.shape}")

    # problem4
    print("===problem4===")
    conv3 = nn.Conv2d(in_channels=3, out_channels=16, kernel_size=5, stride=3, padding=2)
    out3 = conv3(my_tensor)
    print(f"out3 : ({out3.shape})")