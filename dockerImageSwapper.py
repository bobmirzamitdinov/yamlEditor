import os
import yaml

def swap_docker_image(root_folder, old_value, new_value):
    for folder, subfolders, files in os.walk(root_folder):
        for file in files:
            if file.endswith(".yaml") or file.endswith(".yml"):
                file_path = os.path.join(folder, file)
                with open(file_path, 'r') as f:
                    data = yaml.safe_load(f)
                if 'spec' in data and 'containers' in data['spec']:
                    for container in data['spec']['containers']:
                        if 'image' in container and container['image'] == old_value:
                            container['image'] = new_value
                            with open(file_path, 'w') as f:
                                yaml.dump(data, f)
                            print(f"New image at {file_path}: {new_value}")

# Example usage
root_folder = "main"
old_value = "oldImage"
new_value = "newdImage"

swap_docker_image(root_folder, old_value, new_value)