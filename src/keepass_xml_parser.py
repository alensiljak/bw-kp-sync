'''
    Parser for KeePass XML file export.
'''

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
        with open(file_path, 'r') as file:
            data = file.read()
        return data
