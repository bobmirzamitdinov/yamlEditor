# YAML Editor

# Docker Image Swapper
This Python script allows you to update the image field in YAML files within a specified directory. It recursively searches through the folders, checks the content of .yaml files, and replaces the value for the image field from the old value to the new value

## Prerequisites

- Python 3.x
- PyYAML

## Installation

1. Clone the repository or download the script directly
2. Install the required Python packages using the following command:

pip install pyyaml

## Usage

1. Modify the `root_folder`, `old_value`, and `new_value` variables in the script according to your requirements
2. Run the script using the following command:

python dockerImageSwapper.py


## Script Details

The script employs the following functions:

- `swap_docker_image(root_folder, old_value, new_value)`: This function walks through the root folder, locates YAML files, and updates the image field from the old value to the new value
- The script prints the paths of the YAML files where the image field is updated, along with the old and new image values