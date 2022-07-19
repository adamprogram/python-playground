import os
import json

class JsonParser:
    def __init__(self):
        self._input_path = None
        self._output_path = None

    @property
    def input_path(self):
        return self._input_path

    @property
    def output_path(self):
        return self._output_path

    @input_path.setter
    def input_path(self, path):
        self._input_path = path

    @output_path.setter
    def input_path(self, path):
        self._output_path = path

    def read_json(self):
        try:
            with open(self._input_path, 'r') as jfile:
                jdata = jfile.read()

            if not jdata:
                print("No data in file %s" % self._input_path)

        except FileNotFoundError:
            print("File %s not found" % self._input_path)

        except OSError as e:
            print("File %s can not be read" % self._input_path, e)

        return json.load(jdata)

    def get_main_item_from_json(self, jdata):
        return jdata["item"]

    def get_variable_from_json(self, jdata):
        return jdata["variable"]

    def get_items_from_json(self, item_data):
        items = []
        for item in item_data:
            items.append(item)

        return items

    def write_items_as_json(self, items):
        for item in items:
            item_name = item["name"]
            try:
                if not os.path.exists(self._output_path):
                    os.mkdir(self._output_path)

                with open(self._output_path + "%s.json" %item_name, 'w') as jfile:
                    json.dumps(item, jfile, indent=4)

            except OSError as e:
                print("File %s can not be written in folder %s" %(item_name, self._output_path), e)

    def write_variable_as_json(self, variable):
        try:
            if not os.path.exists(self._output_path):
                os.mkdir(self._output_path)

            with open(self._output_path + "variable.json", 'w') as jfile:
                json.dumps(variable, jfile, indent=4)

        except OSError as e:
            print("File variable.json can not be written in folder %s" %self._output_path, e)