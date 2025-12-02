from util import say_hello



def debug_mode(func): 

    def wraper(sender, app_data, user_data): 
        print('app_data:', app_data)
        print('user_data:,', user_data)
        print('sender', sender)
        
        func(sender, app_data, user_data)
        
    return wraper


@debug_mode
def callback_fn(sender, app_data, user_data): 
    print('function called ')



callback_fn(1,2,3)