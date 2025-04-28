'''
    Parser for KeePass XML file export.
'''
import xml.etree.ElementTree as ET

class KeePassXmlParser:
    '''
    Parser for KeePass XML file export.
    '''
    def echo(self):
        '''
        demo
        '''
        print('hello')

    def read_file(self, file_path):
        '''
        Read KeePass XML file.
        '''
        with open(file_path, 'r', encoding='utf-8') as file:
            data = file.read()
        return data

    def read_xml_file(self, file_path):
        '''
        Read KeePass XML file and parse it.
        '''
        tree = ET.parse(file_path)
        root = tree.getroot()
        return root
