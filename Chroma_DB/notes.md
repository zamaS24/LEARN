# notes for advanced rag technique

**WORKFLOW**
![Alt text](RAG_workflow.png)

**pre production**
* knowledge base : documents
* chunking the documents
* choosing of embedding model
* creatig a vector store using the embedding model 

**in production**
* user query 
* embedded user query 
* finding closest document (top k similar documetns)

* response = llm(user query + context) 


**METHODS SUMMARY**

```py
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import PyPDFLoader

# this one looks better than the PyPDFLoader
from langchain_community.document_loaders import PyMuPDFLoader

# chunk_size here is the number of characters per chunk
from langchain.text_splitter import RecursiveCharacterTextSplitter

# for the embedding model 
from langchain_community.embeddings import HuggingFaceEmbeddings

# chunk_size parameter is number of tokens per chunk
from langchain.text_splitter import RecursiveCharacterTextSplitter.from_huggingface_tokenizer

# for the FAISS algrithm, I guess
from langchain.vectorstores import FAISS

how to calculate speed of an object.






# pac-map projector
import pacmap 

documet = Docuemnt(pagecontent, metadata)

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,  # the maximum number of characters in a chunk: we selected this value arbitrarily
    chunk_overlap=100,  # the number of characters to overlap between chunks
    add_start_index=True,  # If `True`, includes chunk's start index in metadata
    strip_whitespace=True,  # If `True`, strips whitespace from the start and end of every document
    separators=MARKDOWN_SEPARATORS,
)


# split and take in consideration tokens sizer and models
text_splitter = RecursiveCharacterTextSplitter.from_huggingface_tokenizer(
        AutoTokenizer.from_pretrained(tokenizer_name),
        chunk_size=chunk_size,
        chunk_overlap=int(chunk_size / 10),
        add_start_index=True,
        strip_whitespace=True,
        separators=MARKDOWN_SEPARATORS,
    )

(return documents) : text_splitter.split_documents([docs])


embedding_model = HuggingFaceEmbeddings(
    model_name=EMBEDDING_MODEL_NAME,
    multi_process=True,
    model_kwargs={"device": "cuda"},
    encode_kwargs={"normalize_embeddings": True},  # set True for cosine similarity
)


KNOWLEDGE_VECTOR_DATABASE = FAISS.from_documents(  
    docs_processed, embedding_model,   
    distance_strategy=DistanceStrategy.COSINE  
)

embedding_projector = pacmap.PaCMAP(
    n_components=2, n_neighbors=None, MN_ratio=0.5, FP_ratio=2.0, random_state=1
)

.... you gotta watch the rest on how to make the visualization 

```



**LIBRARIES**
```py
pip install dotenv
pip install -q torch transformers transformers accelerate bitsandbytes langchain sentence-transformers faiss-gpu openpyxl pacmap
```


```py

ds = datasets.load_dataset(
    "m-ric/huggingface_doc", 
    split="train"
)
```


**Loading langchain documents** 
* loop over the dataset and create list of Documents
* raw_knowledge_base = list of langchain Documents

```py 
from langchain.docstore.document import Document as LangchainDocument

# loop over the dataset 
RAW_KNOWLEDGE_BASE = [
    LangchainDocument(
        page_content=doc["text"], 
        metadata={"source": doc["source"]}
    )
    for doc in tqdm(ds)
    # tqdm is to provide a progress bar in the ds
]

```


# 1 building the retriever
## 1 Split the documents into chunks 

But we gotta know the chunk size : 
* Recursive chunking :
using separator for example :   
    ["\n\n", "\n", ".", ""],  
    * The method will first break down the document wherever there is a double line break "\n\n".
    * Resulting documents will be split again on simple line breaks "\n", then on sentence ends ".".
    * And finally, if some chunks are still too big, they will be split whenever they overflow the maximum size.



```py 



from langchain.text_splitter import RecursiveCharacterTextSplitter

# We use a hierarchical list of separators specifically tailored for splitting Markdown documents
# This list is taken from LangChain's MarkdownTextSplitter class.
MARKDOWN_SEPARATORS = [
    "\n#{1,6} ",
    "```\n",
    "\n\\*\\*\\*+\n",
    "\n---+\n",
    "\n___+\n",
    "\n\n",
    "\n",
    " ",
    "",

    # 

]

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,  # the maximum number of characters in a chunk: we selected this value arbitrarily
    chunk_overlap=100,  # the number of characters to overlap between chunks
    add_start_index=True,  # If `True`, includes chunk's start index in metadata
    strip_whitespace=True,  # If `True`, strips whitespace from the start and end of every document
    separators=MARKDOWN_SEPARATORS,
)

docs_processed = []
for doc in RAW_KNOWLEDGE_BASE:
    docs_processed += text_splitter.split_documents([doc])
```

> :warning: **WARNING**  
> now remember that the embedding model with have the 
> `max_seq_length`, meaning that you should have chunks of sizes that should not exceed this lenth, otherwise we will just loose the size 



