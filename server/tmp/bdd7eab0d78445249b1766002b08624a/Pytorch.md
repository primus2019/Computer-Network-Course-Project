# Pytorch

### torch.nn.Conv2d

Parameters: 

- in_channel (int) - Number of channels in the input image
- out_channels (int) - Number of channels produced by the convolution
- kernel_size (int or tuple) - Size of the convolving kernel

Optional:

- stride (int or tuple) - Stride of the convolution. Default: 1
- padding (int or tuple) - Zero-padding added to both sides of the input. Default: 0
- dilation (int or tuple) - Number of blocked connections from input channels to output channels. Default: 1
- bias (bool) - If True, adds a learnable bias to the output. Default: True



Input: $ (N, C_{in}, H_{in}, W_{in}) $

Output: $ (N, C_{in}, H_{in}, W_{in}) where$

$ H_{out} = \frac{H_{in} + 2 \times padding[0] - dilation[0] \times (kernel\_size[0] - 1) - 1}{stride[0]} + 1 $

$ W_{out} = \frac{W_{in} + 2 \times padding[1] - dilation[1] \times (kernel\_size[1] - 1) - 1}{stride[1]} + 1 $