# pymylib

`pymylib` is a Python package that allows you to save functions to a global library using a simple decorator. You can then import these functions in other scripts and use them as needed.

### Installation

To make full use of this package (including GitHub sync), fork this repository and clone the fork. Then, navigate to the repository folder and run:

```bash
pip install -e ./
```

### Usage

In script 1:

```python
import pymylib

@pymylib.add()
def test():
    print("This is a test function")
```

In another folder and script:

```python
>> import pymylib
>> pymylib.test()
This is a test function
```

You can also add a function to a 'collection':

```python
@pymylib.add("plots")
def plot_im(impath):
    import matplotlib.pyplot as plt
    import matplotlib.image as mpimg
    img = mpimg.imread(image_path)
    plt.imshow(img)
    plt.show()
```

In another folder and script:

```python
>> pymylib.plots.plot_im("./myimage.png")
```

It's possible to **add 'subcollections'** and so on, like: **'plots.personal'**, and the function can be called as **pymylib.plots.personal.function()**

**Removing a function**:

```python
pymylib.remove_function(function_name, collection="")
```

**Removing a collection**:

This will remove all functions inside the collection.

```python
pymylib.remove_collection(collection_name)
```

#### Explanation:

All functions and collections that are saved are stored in the pymylib installation folder. If desired, functions can be organized further by specifying a module_name parameter in the pymylib.add() decorator. This will save the function in a separate file within the selected collection.

### Syncing to GitHub

You can add, commit, push, and pull from GitHub to save your code in the cloud. Make sure you have the git command line installed with your credentials saved (at least in Jupyter Notebook).

```python
import pymylib

pymylib.push_to_github(commit_message)
# or 
pymylib.pull_from_github()
```


### Contributing

We welcome contributions to improve pymylib. Please submit issues and pull requests on the GitHub repository.

## License

Apache License 2.0