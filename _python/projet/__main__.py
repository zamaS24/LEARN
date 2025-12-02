"""Module for testing some various CV with dearpygui stuff"""


import sys 


print(sys.version)




def debug_mode(func):
    def wraper(sender, app_data, user_data):

        # you are free to add whatever you want

        print('debug mode')
        print('sender', sender)
        print('app_data:', app_data)
        print('user_data:,', user_data)

        # calling this is necessary I guess
        func(sender, app_data, user_data)

        # You can still do whatever you want here maybe
        print('function called successfuly! ')
        
    return wraper


@debug_mode
def callback_fn(sender, app_data, user_data):
    print('function called ')





callback_fn(1,2,3)