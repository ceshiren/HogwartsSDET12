import os

import yaml

from requests_wework.core.exception import FileNotFound


class Content:
    def __init__(self, path):
        if not os.path.isfile(path):
            raise FileNotFound(f"{path} not file")
        file_suffix = os.path.splitext(path)[1].lower()
        if file_suffix in [".yaml", ".yml"]:
            self.path = path
            with open(path) as f:
                self._data = yaml.safe_load(f)
            self._filepath, self._tmpfilename = os.path.split(path)

    def get_data(self):
        return self._data
