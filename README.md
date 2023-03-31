# `cvgui` Examples

The purpose of this repository is to showcase the Python library 
`cvgui` through various examples. Explainations of each example can be found below.
Examples are located in the `examples` folder.

The package source code is located on github [here](https://github.com/mitchellss/cvgui). 

Documentation for `cvgui` can be found [here](https://mitchellss.github.io/cvgui/#cvgui).

## How to use:

1. Ensure the version of python you are using is 3.9 or above by running:

> `python --version`

2. Create a virtual environment using the command:

> `python -m venv env`

3. Activate the virtual environment:

Windows
> `./env/Scripts/activate`

Linux
> `source env/bin/activate`

4. Install `cvgui`

> `pip install cvgui`

5. Run the example activity of your choosing (note: all examples require a webcam or camera plugged into the computer):

> `python examples/simple_example.py`

## Example Activities:

### `simple_example.py`

This is a simple example of how `cvgui` can be used to create a
body-interactive GUI. A single button appears in a random color that,
when "clicked" by one's hand, reappears at a random location and changing
to another random color.

### `multi_scene_example.py`

This example showcases how to use "scenes" in `cvgui` to create a
multi-stage GUI. A single red button appears on-screen that can only
be "clicked" by the user's left hand. Once clicked, a new scene begins
in which a single blue button appears that can only be clicked by the 
user's right hand. This second scene switches back to the first once
the blue button has been clicked.
