

# 0.0 NOTES for docker 

Docker solves, it works on my machine problem :) 
We run an example with js in this tutorial 

The people who developed Docker needed deep OS knowledge because they weren't inventing isolation from scratch—they were hacking existing OS features like namespaces, cgroups, and chroot to create lightweight, efficient containers.


The namespace concept in operating systems, which is essential for technologies like Docker, was introduced into Linux in 2002. Specifically, Linux namespaces were first added as a part of the Linux 2.4.19 kernel and expanded over the years



### 0.1 vocabulary 
- `Dockerfile`  used to build a docker image 
- `Image`  is a template for running docker containers  
- `Container`  it's just a running process  

images can be uploaded to the cluod both public or private  

## 1 Philosophy of things 
1. Namespaces (Process Isolation) 🏠
Docker uses Linux namespaces to provide process isolation. Each container gets its own set of namespaces, which isolates different system resources. Here are the key namespaces:

- PID Namespace: Each container has its own process tree. A process inside a container sees only the processes within that container, even though they share the host’s kernel.
- Mount Namespace: Each container has its own filesystem, separate from the host.
- UTS Namespace: Containers can have their own hostname and domain name, independent of the host.
- IPC Namespace: Controls shared memory and interprocess communication inside the container.
- Network Namespace: Each container can have its own network interfaces, IP addresses, and routing rules.
- User Namespace: Containers can map user and group IDs to be different from the host, adding security.




we can pull the image down to create a container which is just a running process of that image 


### 2 Installation and tooling 
Docker destkop installs everything to command line and having a GUI app where we can inspest our running containers 




## 3 Docker file 




## 4 Build an Image 



## 5 Run A container 


## 6 Debugging 


## 7 Docker compose 



## Extra : other comamnds 

- `--name=<name>` gives us the ability to pick our name for the container 


Having all of that process working out together and stuff like that right 

How is that even possible, how did they write that ? 
    -> First we need to know if it's like in OS level 
    -> Since you create isolation and like required envs only for that 
    -> It needs to be added as a feature to the OS itself 
