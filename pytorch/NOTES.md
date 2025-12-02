doc cheatsheet : https://pytorch.org/tutorials/beginner/ptcheat.html

## 0. Major Notes 

* `torch.max(x:Tensor, dim:int)`
if you have multiple array (batch size), so you need for each element know which max is, 
you gotta set dim=1, otherwise it will only return the max of all elements without dim parameter


* note that in Loss calculation when dealing with batch-size, we need to multiply with number of samples in the batch, and then at the end we devide by the total amount of the data 


* becasue loss = 1/n * (something) in the batch this n is the batch size, but in the actual loss of an epoch the n is the total amounts of samples in the whole data, so that's why when we are dealing with batches we need to multiply back with n_batch `loss*inputs.size(0)`



- `torch.toTensor()` changes (height, width, channels) np arrays of pil images to (channels, height, width). This transformation is performed to align with the expected input format for PyTorch models.


## 1. Tensor creation and basics 

`torch.from_numpy(np_array)` numpy to torch 
- `torch.view(new_shape) `
    behaves same as np.reshape()
    
- `torch.empty(shape)` -> tensor of shape 
    careful this methods retuns some stuff that are not 
    created at the first place 
- `torch.permute(new_pos, new_pos, new_pos) : the old axis in the new axis, new_pos = 0 meaning the axis 0 should be in this new_pos
- `torch.zeros(shape)` -> Tensor 
- `torch.ones(shape)` - > Tensor
- `torch.tensor(array|np_array, dtype:torch.float32...etc)` -> Tensor


## 2. Autograd package  
    - torch.tensor(..., `requires_grad = True`)  
    - W.grad : to get the gradients  
    - W.grad.zero_() : resets the gradients to zero   
    - torch.softmax(tensor, dim): dim is the axis you want to   apply to   

INFOS : 
y = x +2, and x has required_grad => y will have grad_function

SUPER INFO :  

        a tensor has 
        .data
        .grad (the actual dl/dw)
        .grad_fn
        .is_leaf
        .requires_grad


## 3.  optimizers
        torch.optim.Optimizer : the base class for all optimizers
        torch.optim.SGD() 


## 4. Learning rate scheduler 
scheduler = optim.X(optimizer,...) 

`optimizer.step() `: for updating the weights with the used optimizer  
`optimizer.zero_grad()` : to empty the gradients, to prepate them for the next iteration, can be used in the begging or the end. 

## 5. loss functions 
torch.nn : contains all of loss functions 
nn.MSELoss()


## 6. Activation functions
`torch.nn.X` : LeakyReLU, HardTanH, 

## 7. Training 

    forward pass 
    compute loss (computation graph created)
    compute dl/dW (loss.backward())
    update parameters 
    gradients.zero()

## CUDA 
-` torch.cuda_is_avialable()` -> Bool 
        checks if cuda is available 
model.to(device)
device = 'cuda' if torch.cuda.is_available() else 'cpu'


## Datasets & DataLoaders
for managing big/small datsets and more 
combined with dataloader to specify how to load the batches 


    Dataset(torch.utils.data.Dataset)
        def __init__(self, transform=None):


        def __getiem(idx): 
        
        def __len__(idx): 

        #optional for managing how batches should be loaded 
        def __getitems(): 

<br>




## NeuralNetwork 
torch.nn.Module is the base class for all neural nets 

```py
class NeuralNet(nn.Module):

    def __init__(self, *args, **kwargs):
        super(NeuralNet, self).__init__()

    def forward(X): 


        return output

```  
<br>  

> :bulb: **INFO**  
> When you think about input shape and output shape of the layers in the init, make in your head as if the input is not batched
> in the forward the input is always batched (bs, *input_shape)      

<br>


- `model.train() ` : sets model for training phase
- `model.eval()` : sets model for evaluation phase 

- `model.fc.in_features` : shape of input features (not sure )
- `freeze layers `: setting requires_grad = False 


**Freeze specific layers (e.g., conv1 and conv2)**
```py
for param in model.conv1.parameters():
    param.requires_grad = False
```

**freezer all layers** 
```py 
for param in model.params() 
    param.requires_grad = False
```


##  ImageFolder (torchvision.datasets.ImageFolder)
- `datasets.ImageFolder (path, transformations) ` in  ` torchvision.datasets `
A generic data loader where the images are arranged in this way by default 
Image folder is to have your file structure like this :   

        root/  
        root/train/  
                /class1
                /classe2 
                /..etc  

and you call it to for the validation folder 
root/val/
          /class1
          /classe2 
           /..etc

- `DataLoader(dataset:ImageFolder, batchsize:int, shuffle:bool, numworkers:int)` in   `torch.utils.data`  
we make this iterable and use it later 


- `model.state_dict()` : for loading and saving models 
- `optimizer.state_dict()` : same thing 
- `model.load_state_dict()` : to load the params on the model 

```py
for param_tensor in net.state_dict():
    # do something 
```

## Saving and loading 



Methods : 
    - torch.save(model, PATH) ->            # for saving the whole mode 
    - torch.load(PATH) ->       
        will load the whole model, with it's architecture parameters ...etc            
    - model.eval() -> 
    - model.load_state_dict(args) -> 
    - torch.save(model.state_dict(), PATH)

    # model must be created again with parameters 
    model = Model(*args, **kargs)
    model.load_state_dict(torch.load(PATH))
    model.eval()


```
tensor basics and creation : 
    torch.tensor(array, dtype=torch.float32)
    torch.randn(max, [min, max], dtype=torch.float32)
    torch.max(tensor, dim)
    torch.view(new_shape) : the order is still the same 
    torch.permute(*new_positions)

```




## Array manipulations 
Adding a dimension for image to bs 
```py
img.unsqueeze(0)
# this will make it [1, C, W, H]
```
```py
t.norm(dim=-1, keep_dim=True) # makes it nromalized, a vector of norm = 1 

```




## Layers 




## Extra notes : 
when we do    
```python
    model(images, targets)
```
PyTorch returns 

- An optimizer, takes the parameters to be optimzed.
model.parameters() return a generator of Parameters, which are tensors



- the collate function collate_fn in the batch, controls how the dataloader returns the batch.
def collate_fn(batch):
batch is like [dataset[i] for i in batch_indices]


- the tuple(zip(*batch)) in the Object detection is very brilliant : 
    transforms this : [(img1, target1), (img2, target2)]
    into this : ((img1, img2), (target1, target2))


- PyTorch’s DataLoader uses default_collate if you don’t provide one.
default_collate will:
    Stack tensors along a new batch dimension when all samples have the same shape.
    Convert lists of numbers to tensors.
    Recursively handle tuples/dicts of tensors.

zip works with any iterable.


- nn.Sequential() when used, we don't need to use the forward. it stackes the layer automatically, knowing the flow of the input. 


- never forget in foward we thinkg as X in batch size
- in inference also we give x in batch_size 
- in definition of layers not in batch size


- You don’t need a Softmax layer in your MLP when you’re using
nn.CrossEntropyLoss — it already includes it internally.