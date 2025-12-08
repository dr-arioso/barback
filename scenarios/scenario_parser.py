
import yaml
import glob
import os

class ScenarioLoader:
    def __init__(self, schema_path=None):
        self.schema = None
        if schema_path:
            with open(schema_path, 'r') as f:
                self.schema = yaml.safe_load(f)

    def load_scenario(self, path):
        with open(path, 'r') as f:
            data = yaml.safe_load(f)
        return data

    def load_all(self, directory):
        scenarios = []
        for file in glob.glob(os.path.join(directory, "*.yaml")):
            scenarios.append(self.load_scenario(file))
        return scenarios
