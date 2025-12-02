### 1. Create an environement: 

```cmd
conda create -n env_name python=3.7
```


### 2. activate the environement:
```cmd
conda activate env_name
```
you will see this image
![Alt text](image.png)


Once the virtual environment is activated, any packages you install with pip will be installed within that environment. For example:
``` 
pip install package_name
```

### 3. deactivate environement: 
```cmd
conda deactivate env_name
```

### 4. install a certain library 
```bash
conda install -c anaconda numpy
```
In an Anaconda environment, it is generally recommended to use conda install for installing packages whenever possible, especially for packages that are available in the Conda repository. This helps maintain consistency and manage package dependencies effectively. Use pip when you need to install packages that are not available through Conda or are specific to Python packages not covered by Conda.