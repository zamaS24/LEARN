- kafka: distributed event streaming platform



- brokers : are kafka servers
- producers and consummers (communication over TCP) 
- kafka connector 
- kafka stores event in ordered logs (partitions): 
```
[Event0][Event1][Event2][Event3]...
```
this is an immutable stream that consummers can replay anytime 
this is streaming and not **queueing** cuz : 
    - one consumer can read events as soon as they come 
    - another can read the same events later 
    - anoterh can re-read from the beginning  


RECORD: 
    - Headers
    - Key, value 

TOPICS  
    - TOPICS : are to organize events 
    - consummers subscribe to a topic  


SCALING :
    - lot of messages, lot of producers 
    -  **PARTITIONING**:    



Internals 
    - partition offsets :  
    - 

Brokers: 
    - distributed deployment of kafka 
    - provide fault tolerance and horizontal scale 

Replication : 
    - fault tolerance for topic data 
    - each partition is replicated across brokers 
    - Leader, accepts writers, reads can fall back to followers      
    - 



