# NOTES for anything related to DL in general. Architectures, loss functions, intuition, etc...Mostly in theory 

<br>

###  jitter, gap, offset in achor boxes 
- **jitter**:  In the context of anchor boxes (like in object detection models — YOLO, Faster R-CNN, etc.), “jitter” generally means adding small random noise or perturbations to anchor box parameters during training. For better generalization.
- **gap** : how far neighboring patches, are sampled around a center patch 
- **offset** : how much a neighbooring patch's coordinates differ from the center patch 
    - (i,j) (dx,dy)
- **crop** : obvious, it's like cutting a rectangle from an image, and getting it as a new image.


### TP, FP, TN all what matters 
You know in binary classification, the roles of positive and negative are symmetric
That’s why in multiclass setups, we often compute TP, FP, FN per class using a “one-vs-all” approach — each class is treated as “positive” vs all others (“negative”) in turn.


### What is batch norm : 
We take the activations of the batch xi in the layer and we perform : 
- normalization through std and var x ~ x'
- scale and shift y = alpha.x' + b (learned params)

<br>

### supervised, semi-supervised, self-supervised 
- Supervised learning : samples and labels (very simple) 
- unsupervised : without labels at all: 
    - Auto Encoders (AE)
    - KNN, KMEANS,DBSCAN, PCA, TSNE, 

- self-supervised (Auto supervised): creates own labels from data. **(Learns by making predictions task from data)** predict masked word, predict missing part of image or rotaion.

- Semi supervised: small part of data are labeled and the other is unlabeled. We use the model to label the rest, and then iterate again.  

- **How to evaluate a self supervised learing method** : 
    - you train the network on a pretext task, and you willg get an encoded feature extractor.
    - you take the trained feature extractor 
    - add a linear layer and slightly fine tune it for example on class task (cat, bird, ... etc)
    
    - you can also zero shot eval your backbone

    - we can see the neighrest neighbors in latent space and display it.

- **Contrastive representation learning**: 
    - instance contrastive learning : SimCLR, COCO
    - 



### Good practices : 
- **overfitting small batch :** When debugging a model, it is often useful to make quick tests to see if there is any major issue with the architecture of the model itself. In particular, in order to make sure that the model can be properly trained, a mini-batch is passed inside the network to see if it can overfit on it. If it cannot, it means that the model is either too complex or not complex enough to even overfit on a small batch, let alone a normal-sized training set.  


- **Gradient checking:*Gradient checking is a method used during the implementation of the backward pass of a neural network. It compares the value of the analytical gradient to the numerical gradient at given points and plays the role of a sanity-check for correctness.*



### TO be learned 
- Weight decay 
- Standard scalar 
- Warmup 
- Scheduler 



