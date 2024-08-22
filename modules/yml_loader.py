import os
import yaml

class YmlLoader:
    def __init__(self, can_directory, uds_directory):
        self.can_directory = os.path.abspath(can_directory)
        self.uds_directory = os.path.abspath(uds_directory)
        self.can_data = {}
        self.uds_data = {}

    # Load YML
    # ///////////////////////////////////////////////////////////////
    def load_yml_files(self):
        self.can_data = self._load_yml_from_directory(self.can_directory)
        self.uds_data = self._load_yml_from_directory(self.uds_directory)
    
    def _load_yml_from_directory(self, directory):
        yml_files = [f for f in os.listdir(directory) if f.endswith('.yml')]
        data = {}
        for filename in yml_files:
            with open(os.path.join(directory, filename), 'r') as file:
                data[filename] = yaml.safe_load(file)
        return data
    

    # UTILS
    # ///////////////////////////////////////////////////////////////
    def get_can_data(self):
        return self.can_data

    def get_uds_data(self):
        return self.uds_data

    def get_selected_can_yml(self, filename):
        return self.can_data.get(filename, None)

    def get_selected_uds_yml(self, filename):
        return self.uds_data.get(filename, None)

    def get_can_file_names(self):
        """Return a list of CAN YML file names without extensions."""
        return [os.path.splitext(filename)[0] for filename in self.can_data.keys()]

    def get_uds_file_names(self):
        """Return a list of UDS YML file names without extensions."""
        return [os.path.splitext(filename)[0] for filename in self.uds_data.keys()]

# Example usage:
# loader = YmlLoader('./config_can', './config_project_uds')
# loader.load_yml_files()
# print(loader.get_can_data())
# print(loader.get_uds_data())
