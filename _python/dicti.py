# %%
myDict = {
    # version 
    "version": 1.0,

    # data train 
    "train_data": [
        'happened here ', 
        'something will happen', 
        'yesterday was element wise', 
        'cant you just do it in peace'
    ], 

    # train labels
    "train_labels": [
        1,
        0,
        0,
        1
    ]
}


train_data  = myDict['train_data']
train_labels = myDict['train_labels']

train_data
# %%
# get keys 

x = myDict.keys()


