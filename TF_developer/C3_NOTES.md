# WEEK 1 

- tokenizer 
- wordindex 
- tokenizer.vocabsize 
It makes upper case and lower case the same 
It removes poncutation and grammar 
```py

from tensorflow.keras.preprocessing.text import Tokenizer

sentences = [
    'I love my dog', 
    'I love my cat', 
    'You love my dog'
]



tokenizer = Tokenizer(num_words=100)
# num_words parameter specifies the maximum number of words to keep, based on word frequency. 
# Only the most common num_words-1 words will be kept. Rare words will be discarded.
tokenizer.fit_on_texts(sentences) 
word_index = tokenizer.word_index
```

### text to sequence 
in images we have fixed size 
we will do same things with tensorflow 



```py
tokenizer.texts_to_sequence(sentences)
```

out of vocabulary token 
just add the parameter `oov_token = "<OOV>"` in the `Tokenizer()` object

> :memo: **NOTE**    
> With texts you'll face a similar requirement before you can train with texts, we needed to have some level of uniformity of size, so `padding` is your friend there.

### padding the sequences 

```py
from tensorflow.keras.preprocessing.sequence import pad_sequences
sequences = tokenizer.texts_to_sequences(sentences)
padded = pad_sequences(sequences)

# here the matrix width will be same size of the longest sequence in sequences
```
> :warning: **WARNING**  
> the `text_to_sequence` function when given an array of sentences or directly just sentences, it doesn't give same output
> shall pass an array of sentences, if one pass one sentence

or  directly in 
```py 
padded = pad_sequences(sequences, padding='post', maxlen=5)
# here we fined the matrix width , post means after the sentencs

# truncating means from the end , will truncate from the end    
# for example if sentece is 7 words and maxlen = 5, truncating = post, means we will loose the two last words
padded = pad_sequences(sequences, padding='post', truncating='post',  maxlen=5)
```

> :bulb: **Remember** 
> the embedding is just in the netwrork, to learn
> the network has to learn the embedding matrix
> for us, we only preprocess words and sequuences and array of sequences, using padding, tokenizers etf

<br> 

---  
<center> <h1 style='color:green;'> WEEK2 </h1> </center>  

Dataset
https://ai.stanford.edu/~amaas/data/sentiment/



vocab_size : vocabulary size of the words
the sequence must be fixed value (length of the sequence) 
    hence : embed and truncate



creating the embedding in tensorflow
```py

model = tf.keras.Sequential([

    # Embedding layer 
    tf.keras.layers.Embedding(vocab_size, embedding_dim, input_length=max_length),

    #   embedding_dim : is the embedding_size of how a word is 

    # in terms of input and outputs : we input a sequence of tokens of (seq_lenth) and it outputs a (seq_lenth, embedding_dim)
    # the seq_length is equals to mex_legth, that we have defined before


    # vocab size is important : because the network will learn the embedding of each wor in the vocabulary 
        # hence the embedding matrix
        # the embedding matrix is of shape (vocab_size, embedding_dim)
        # so number of parameters to learn is the dot product of this shape[0]*shape[1]
    
    # Yes, that's correct. The embedding layer takes a sequence of word indices 
    # (representing a sentence or input sequence) and outputs an embedding matrix,
    # where each word index in the input sequence is mapped to its corresponding dense vector representation (embedding).

    tf.keras.layers.Flatten(), 
    tf.keras.layers.Dense(6, activation = 'relu'), 
    tf.keras.layers.Dense(1, activation='sigmoid')
    
])
```

## subwrod text encoders 
encoder 

```py
    encoder = tfds.deprecated.text.SubwordTextEncoder(
    vocab_list= ['something happened here']
)
```

we can code and decode 
```py
ids = encoder.encode ("something here")
text = encoder.decode([1,2,3,4])    
```

## dictionary comprehension 
same thing as list comprehension, you just need to sey what is the key:value for your conditional loop 

```py
 vocab = {token: idx for idx, (token, _) in enumerate(token_counts.items())}
```

tokenizer_subwords.subwords
and the tokenizer_subwords is an encoder (just be careful )


input_length in embedding is not really specified


In this lab, you saw how subword text encoding can be a robust technique to avoid out-of-vocabulary tokens. It can decode uncommon words it hasn't seen before even with a relatively small vocab size. Consequently, it results in longer token sequences when compared to full word tokenization. Next week, you will look at other architectures that you can use when building your classifier. These will be recurrent neural networks and convolutional neural networks.


### subword text encoding
when the number of words exceeds the number of vocab_sizer parameter, then it will make some subwords stuff you feel me, that's why with small examples we didn't get subwords as desired fhemtni kho 



### some key notes
- remove stopwords 
- Vocabulary (all words we will train on )
- Tokenizing 
- Sequence length 
- Embedding 
- Sub word encoding 
- embedding matrix vs embedding vector (embedding dimension)
- the train data is the `padded` sequences  

### tokenized labels
:warning: remember to subtract 1 (e => e-1) in the tokenized label of arrays (since it starts from one and in the neural network, values should start from 0)

### spcategorical cross entropy vs sparse categorical cross entropy
in a classification task, le'ts say the last layer you have 5 neurones that corresponds to five classes
in `categorical cross entorpy` you will neet to have your labels one hot encoded
in `sparse categorical cross entropy` you can just use integers directly  

### visualizing 3D vectors
```py
# Reverse word index
reverse_word_index = dict([(value, key) for (key, value) in word_index.items()])

# Save the embedding layer
e = model.layers[0]

# Save the weights of the embedding layer
weights = e.get_weights()[0]
print(f"Weights of embedding layer have shape: {weights.shape}")

###### -------------------------------------- preferable to split cell here

# Generate files for embedding visualization
out_v = io.open('vecs.tsv', 'w', encoding='utf-8')
out_m = io.open('meta.tsv', 'w', encoding='utf-8')
for word_num in range(1, NUM_WORDS):
    word = reverse_word_index[word_num]
    embeddings = weights[word_num]
    out_m.write(word + "\n")
    out_v.write('\t'.join([str(x) for x in embeddings]) + "\n")
out_v.close()
out_m.close()

```



<br>

---

# WEEK 3 

$ `traindata.shuffle(BUFF_SIZE)` method : shuffles the data randomly to avoid biases, il prend [BUFF_SIZE] element à la fois, exemple array de 20 elements il prend 5 a la fois et les melangent

$ `traindata.padded_batch(BUFF_SIZE)` method: 
* batches the data to baches of size BATCH_SIZE
* pads the sequences within each batch to the length of the longest sequence in that batch.
 



$ ` tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(lstm_dim))` layer   

$ **About the lstm layer**  
1. **Capturing Dependencies:** As the LSTM layer processes the sequence, it captures dependencies between tokens at different timesteps. This allows the LSTM to consider the context of each token within the sentence, including information from preceding tokens.

2. **Final Output:** The final output of the LSTM layer, after processing the entire sequence, is a single vector representation of the entire sequence. This vector encapsulates information about the entire sentence, taking into account the dependencies and context of each token within the sequence.

$ second version of LSTM layer 

here's this code : 

```py
import tensorflow as tf
from tensorflow.keras.layers import Embedding, LSTM, Dense
from tensorflow.keras.models import Model

# Define the vocabulary size and embedding dimension
vocab_size = 10000
embedding_dim = 64

# Define the LSTM units
lstm_units = 64

# Define the input sequence length and target sequence length
input_seq_length = 20
target_seq_length = 20

# Define the encoder
encoder_inputs = tf.keras.Input(shape=(input_seq_length,))
encoder_embedding = Embedding(vocab_size, embedding_dim)(encoder_inputs)
encoder_lstm = LSTM(lstm_units, return_state=True)
encoder_outputs, state_h, state_c = encoder_lstm(encoder_embedding)
encoder_states = [state_h, state_c]

# Define the decoder
decoder_inputs = tf.keras.Input(shape=(target_seq_length,))
decoder_embedding = Embedding(vocab_size, embedding_dim)(decoder_inputs)
decoder_lstm = LSTM(lstm_units, return_sequences=True, return_state=True)
decoder_outputs, _, _ = decoder_lstm(decoder_embedding, initial_state=encoder_states)
decoder_dense = Dense(vocab_size, activation='softmax')
decoder_outputs = decoder_dense(decoder_outputs)

# Define the model
model = Model([encoder_inputs, decoder_inputs], decoder_outputs)

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Print the model summary
model.summary()
```

`encoder_outputs, state_h, state_c = LSTM(lstm_units,return_sequences=True, return_state=True)`
* That `return sequences` return the hidden state output for each input time step.
* That `return state` returns the hidden state output and cell state for the last input time step.
* That return sequences and return state can be used at the same time.

so the state_h is also included in encoder_outputs since encoder outputs contain the output of all hideen states of each timestep. and the state_h is the output of the last hidden state or am I wrong 

* decoder_LSTM(...initial_state = encoder_states)



$ in the lab we trained without labels because in the loading of the dataset 
When as_supervised=True, train_data and test_data are loaded as tuple datasets (input, label) where input represents the input data (in this case, the movie reviews) and label represents the corresponding sentiment labels (positive or negative).

heres the train code 
```py
NUM_EPOCHS = 10

history = model.fit(
    train_dataset, # here we have both sequences , labels
    epochs=NUM_EPOCHS, 
    validation_data=test_dataset)

```


$ we can define layers, and pass them an input  
1. LSTM that returns a single output 
```py
# Define LSTM that returns a single output
lstm = tf.keras.layers.LSTM(lstm_dim)
result = lstm(random_input)
```

2. LSTM that returns a sequence 
```py

# Define LSTM that returns a sequence
lstm_rs = tf.keras.layers.LSTM(lstm_dim, return_sequences=True)
result = lstm_rs(random_input)
print(f'shape of lstm output(return_sequences=True): {result.shape}')
```

$ shapes with (none, none, value), tensorflow haas like predefines shapes for tensors, and when are not specified they're just to none, the first none for example corresponds to the batch size 

$ The LSTM layer expects a 3D tensor (batch_size, timesteps, units),

$ **using convolutions**   
1. Inspecting 
```py
# Pass array to convolution layer and inspect output shape
conv1d = tf.keras.layers.Conv1D(filters=filters, kernel_size=kernel_size, activation='relu')
result = conv1d(random_input)
print(f'shape of conv1d output: {result.shape}')

# Pass array to max pooling layer and inspect output shape
gmp = tf.keras.layers.GlobalMaxPooling1D()
result = gmp(result)
print(f'shape of global max pooling output: {result.shape}')
```

2. in the model 
```py
# Build the model
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(tokenizer.vocab_size, embedding_dim),
    tf.keras.layers.Conv1D(filters=filters, kernel_size=kernel_size, activation='relu'),
    tf.keras.layers.GlobalMaxPooling1D(),
    tf.keras.layers.Dense(dense_dim, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])
``` 


$ stacking two LSTMs
ensure that return sequences = True

### Conclusion
in some architectures GRU gave better perfomance comparedn to LSTM 
also you can see that we can use convolutions(1d) and combine all these architectures, but it's really important to know which layer w need to use 




sentences = 'something happened today okay?'
sequences : 

