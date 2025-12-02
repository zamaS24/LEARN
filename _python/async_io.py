"""
asyncio is native python : it is introduced at a certain time, to handle what we call 
couroutines and we can await coroutines


running on an event loop, meaning on the main thread and tasks are run concurrently.
But this doesn't mean we can't do parallelism, we can do it, for example using asyncio.to_thread().

asyncio.slepp(<time in seconds>)
asyncio.gather(<coroutine 1>, <coroutine 2>, ..., )
    coroutine is just an async function

calling a couroutine without the await , will just return an awaitable object
    An object is awaitable if it implements either:
        The __await__ method (for low-level custom awaitables).
        Or is a coroutine (defined by async def).

How event loop works ?
    while(certain_condition[coroutines are not all terminated]): 
        run_task1

        
        # this requires OS level calls 
        for event in events 

            # event can be for example (end of I/O operation)
            if event is triggered : 
                add the process to the ready queue

                
if you wanna make your own function awaitable you need to do: 
    -> await asyncio.thread(my_awaitable_function)

"""


"""
    await() : here the event loop, schedules the  coroutine to be run later 
    when we have the await() keyword before the function, it doesn't mean that it's enough to halt the process in this point, and move to the next coroutine
    there has to be a certain instruction inside this function that we actually can halt in it. so don't expect by just writing the await() the event loop will automatically schedules it later and move to the next one 

    for cpu tasks, we can use asyncio.to_thread() and it should be awaited, here for example it is an instruction that actually halts it, until the process is done


    
typically the asyncio.sleep() function is defined as follow : 
    async def sleep(seconds):
        # Internally, asyncio.sleep does this:
        loop = asyncio.get_event_loop()  # Get the current event loop
        future = loop.create_future()  # Create a future object

        # This line schedules the task to run after the 'seconds' delay
        loop.call_later(seconds, future.set_result, None)  # Callback to set result

        # We await the future, but it doesn't block the event loop.
        await future  # This doesn't block; it yields control to the event loop
    
    
Implementing stuff on top of asyncio: 
    this involves interacting with the event loop and understanding futures, so that we can make awaitable async functions like in this example: 

    import asyncio

    async def someAsyncFetchData():
        loop = asyncio.get_running_loop()
        future = loop.create_future()

        # Simulate data fetching
        loop.call_later(2, future.set_result, "Fetched Data")
        data = await future  # Pauses here until future is resolved
        return data

    async def main():
        data = await someAsyncFetchData()
        print(data)  # Outputs: "Fetched Data"

    asyncio.run(main())
   
    

# the whole magic happens in the event loop
# the await asyncio.sleep() : this yields back control to the event loop to schedule next task
#   
    
"""


import asyncio
from time import sleep

# threading ensures parallelism, while this asyncio can ensure concurrency in a single thread, event loop. 

# The await keyword in Python is used within an async function to pause the execution of the coroutine until the awaited task is completed.

# This can be seen as a certain job in the main thread
async def say_hello():
    print("Hello")
    await asyncio.sleep(1)  # Simulate an I/O-bound operation
    print("World")


# this can be seen as another job in the main thread too
async def say_bye(): 
    print("Bye")
    for i in range(50000): 
        print('something')
    await asyncio.sleep(1)  # Simulate an I/O-bound operation
    print("Mr")




# async def main():
#     # the thread is composed with these two tasks. 
#     await asyncio.gather(say_hello(), say_bye())



async def nested():
    return 42

async def main():
    # Nothing happens if we just call "nested()".
    # A coroutine object is created but not awaited,
    # so it *won't run at all*.
    # nested()

    # Let's do it differently now and await it:
    print(await nested())  # will print "42".


# Start the event loop
asyncio.run(main())









# OS : can handle stuff, and can handle the multithreading stuff, and uses context switch basically, with Queue tracking. 
# event loop: just a loop and launching some processes 
# CS:IP and making conext switch, only the CPU that does that, but it gives you a way to do this, through an API. 
# OS kernel developer is the GOD tier programmer
# can't have multiple access through everything in life right 
# Buy him a gaming chair too 



# 

# Why can't I be confident enough about this thing in the future man? 
# I really don't know anything about this topic, but let's say that this is the real value of it 






# what the OS can provide is really something very very very very very BIG. s
# the OPEN source stuff, the IPC, and all of these functionalities that are in the lower basis something very very simple if you actually see that 







