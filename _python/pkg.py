# A package is a set of py files plus __init__.py file 

# in the __init__.py you should import all the necessary stuff from the package
# that you want to import when executing a file that uses this package 
# use both relative import .something to tell it it's in the same module

# if you run the __init__.py directly you'll have ImportError exception, to resolve
# use try catch and in the catch use absolute imports 


# if you don't want to use from mypackg.subpkg import something 
# you should import something in the __init__ of the subpkg 
# you should import it also in the mypackg ('veut dire surmonter les imports')

# when you import a package in python, the __init__ will be executed

from mymath import square

# directly mymath.square because in __init__.py is imported from the submodule

# if it was not imported we would have to do mymath.adv.square
print(square(5))





from mymath.adv import StaticClass
from mymath import add 



print(StaticClass.NUM_CLASSES)



from mymath.adv import square
print(add(1,2))



from transformers import AutoTokenizer

model_name = 'bert-base-cased'
tokenizer = AutoTokenizer.from_pretrained(model_name)
sentences = ['hello my name is hamza',"I am testing again the tokenize"]





tokens = tokenizer.tokenize(sentences)
token_ids =tokenizer.convert_tokens_to_ids(tokens)
print(tokens)
print('token ids: ', token_ids)
