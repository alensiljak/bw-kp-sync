'''
Test reading KeePass XML export.
'''

from src.keepass_xml_parser import KeePassXmlParser


class TestKeePassXmlParser:
    '''
    Test KeePass XML Parser.
    '''
    def __init__(self):
        self.kp = KeePassXmlParser()

    def test_read_file(self):
        '''
        Test reading KeePass XML file.
        '''
        contents = self.kp.read_file('c:/users/alen/desktop/kp.xml')

        assert contents is not None, 'File contents should not be None'
        assert isinstance(contents, str), 'File contents should be a string'
        assert len(contents) > 0, 'File contents should not be empty'
        assert '<KeePassFile>' in contents, 'File contents should contain <KeePassFile>'
        assert '</KeePassFile>' in contents, 'File contents should contain </KeePassFile>'
        assert '<Group>' in contents, 'File contents should contain <Group>'
