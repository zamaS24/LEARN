from torch.utils.data import Dataset, DataLoader
import numpy as np 
import torch 


class WineDataset(Dataset):

    def __init__(self, transform=None):
        # Initialize data, download, etc.
        # read with numpy or pandas
        xy = np.loadtxt('./data/wine.csv', delimiter=',', dtype=np.float32, skiprows=1)
        self.n_samples = xy.shape[0]

        # this one is for the 9th notebook 
        # here the first column is the class label, the rest are the features
        # self.x_data = torch.from_numpy(xy[:, 1:]) # size [n_samples, n_features]
        # self.y_data = torch.from_numpy(xy[:, [0]]) # size [n_samples, 1]



        #this one is for the 10TH NOTEBOOK 
        self.x_data = xy[:, 1:]
        self.y_data = xy[:, [0]]
        self.transform = transform


    # support indexing such that dataset[i] can be used to get i-th sample
    def __getitem__(self, index):
        sample =  self.x_data[index], self.y_data[index]

        if self.transform:
            sample = self.transform(sample)

        return sample 
    

    # we can call len(dataset) to return the size
    def __len__(self):
        return self.n_samples
    

# this one is for the 10th I guess
class ToTensor(): 

    def __call__(self, sample): 
        inputs, targets = sample

        return torch.from_numpy(inputs), torch.from_numpy(targets)  
    


def main(): pass


if __name__ =='__main__': 
    main()


