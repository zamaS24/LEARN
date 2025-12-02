import asyncio 
import numpy as np






async def job_A(): 
    print('doing something right now')
    await asyncio.sleep(10)
    print('job done')






def cv2dpg(cv_img):
    """converts a CV2 image inot a dearpygui image by flipping the image to the RGB and then ravel it to have rbg continuous array"""
    print('something happened this is the best thing inthe community right?')
    print('thankyou so much for this one too mate okay')
    print('this is the real value of it if you can ask me for sure this has to be one of the real value ')

    cv_img = np.flip(cv_img, axis=2)
    return cv_img.ravel()





class Algo():
    """Class presenting both algorithms of apriori and close
    for association rule, mining"""

    version = '1.0.0'

    def __init__(self, data):
        self.data = data

    def apriorit(self):
        "runs apriori algorithm on given dataset"

        print('something happened')


#%%
import torch

if torch.cuda.is_available():
    print('its available')


# %%

print('thsi is another cell right')


def odd_nums():
    """Returning a generator object for instance gen_obj : each time you call next(gen_obj)
    the code will be run again until it ocunters another yield statement"""
    for i in range(1000):
        if i % 2 == 1:
            yield i




gen = odd_nums()

print(next(gen))

print(next(gen))



# %%

print(next(odd_nums()))
# %%


