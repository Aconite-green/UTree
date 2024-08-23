import os
import yaml

class YmlLoader:
    def __init__(self, can_directory, uds_directory, error_handler):
        self.can_directory = os.path.abspath(can_directory)
        self.uds_directory = os.path.abspath(uds_directory)
        self.can_data = {}
        self.uds_data = {}
        self.error_handler = error_handler

    # Load YML
    # ///////////////////////////////////////////////////////////////
    def load_yml_files(self):
        try:
            self.can_data = self._load_yml_from_directory(self.can_directory)
            self.uds_data = self._load_yml_from_directory(self.uds_directory)
        except Exception as e:
            self.error_handler.handle_error(f"Error loading YML files: {str(e)}")
    
    def _load_yml_from_directory(self, directory):
        data = {}
        try:
            if not os.path.exists(directory):
                raise FileNotFoundError(f"Directory not found: {directory}")
            
            yml_files = [f for f in os.listdir(directory) if f.endswith('.yml')]
            if not yml_files:
                self.error_handler.handle_error(f"No YML files found in directory: {directory}")

            for filename in yml_files:
                try:
                    with open(os.path.join(directory, filename), 'r') as file:
                        data[filename] = yaml.safe_load(file)
                except yaml.YAMLError as e:
                    self.error_handler.handle_error(f"Error parsing YML file '{filename}': {str(e)}")
                except Exception as e:
                    self.error_handler.handle_error(f"Unexpected error with file '{filename}': {str(e)}")
        except Exception as e:
            self.error_handler.handle_error(f"Error reading directory '{directory}': {str(e)}")

        return data
    
    # CAN YAML
    # ///////////////////////////////////////////////////////////////   
    def get_selected_can_yml(self, filename):

        if not filename.endswith('.yml'):
            filename += '.yml'
        try:
            if filename in self.can_data.keys():
                return self.can_data[filename]
            else:
                raise KeyError(f"Filename '{filename}' not found in CAN data.")
        except KeyError as e:
            self.error_handler.handle_error(str(e))
            return None
        except Exception as e:
            self.error_handler.handle_error(f"Error retrieving CAN YML data: {str(e)}")
            return None
        
    def get_can_file_names(self):
        try:
            return [os.path.splitext(filename)[0] for filename in self.can_data.keys()]
        except Exception as e:
            self.error_handler.handle_error(f"Error getting CAN file names: {str(e)}")
            return []

    # UDS YAML
    # ///////////////////////////////////////////////////////////////
    def get_can_data(self):
        try:
            return self.can_data
        except Exception as e:
            self.error_handler.handle_error(f"Error retrieving CAN data: {str(e)}")
            return {}

    def get_uds_data(self):
        try:
            return self.uds_data
        except Exception as e:
            self.error_handler.handle_error(f"Error retrieving UDS data: {str(e)}")
            return {}

    def get_selected_uds_yml(self, filename):
        try:
            if filename in self.uds_data:
                return self.uds_data[filename]
            else:
                raise KeyError(f"Filename '{filename}' not found in UDS data.")
        except KeyError as e:
            self.error_handler.handle_error(str(e))
            return None
        except Exception as e:
            self.error_handler.handle_error(f"Error retrieving UDS YML data: {str(e)}")
            return None

    def get_uds_file_names(self):
        try:
            return [os.path.splitext(filename)[0] for filename in self.uds_data.keys()]
        except Exception as e:
            self.error_handler.handle_error(f"Error getting UDS file names: {str(e)}")
            return []
