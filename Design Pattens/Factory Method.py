import json
import xml.etree.ElementTree as etree



"""This is a factory method"""
def connect_factory(filepath):
    class JSONConnector:

        def __init__(self, filepath):
            self.data = dict()
            with open(filepath, mode='r', encoding='utf-8') as fh:
                self.data = json.loads(s)

        @property
        def parse_data(self):
            return self.data

    class XMLConnector:

        def __init__(self, filepath):
            self.tree = etree.parse(filepath)

        @property
        def parse_data(self):
            return self.tree
    if filepath.endswith('json'):
        connector = JSONConnector
    elif filepath.endswith('xml'):
        connector = XMLConnector
    else:
        raise ValueError("Cannot connect to {}".format(filepath))
    return connector(filepath)

"""Packaging connect_factory()"""
def connect_to(filepath):
    factory = None
    try:
        factory = connect_factory(filepath)
    except ValueError as err:
        print(err)
    return factory

def main():
    a = JSONConnector("File")

if __name__ == "__main__":
    main()
