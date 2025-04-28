'''
Test reading KeePass XML export.
'''

import os
from src.keepass_xml_parser import KeePassXmlParser
import xml.etree.ElementTree as ET


class TestKeePassXmlParser:
    '''
    Test KeePass XML Parser.
    '''
    def setup_class(self):
        '''
        Setup class for KeePass XML Parser tests.
        '''
        self.kp = KeePassXmlParser()
        self.home_dir = os.path.expanduser("~")
        self.file_path = os.path.join(self.home_dir, 'desktop', 'kp.xml')

    def test_read_file(self):
        '''
        Test reading KeePass XML file.
        '''
        contents = self.kp.read_file(self.file_path)

        assert contents is not None, 'File contents should not be None'
        assert isinstance(contents, str), 'File contents should be a string'
        assert len(contents) > 0, 'File contents should not be empty'
        assert '<KeePassFile>' in contents, 'File contents should contain <KeePassFile>'
        assert '</KeePassFile>' in contents, 'File contents should contain </KeePassFile>'
        assert '<Group>' in contents, 'File contents should contain <Group>'
        assert '</Group>' in contents, 'File contents should contain </Group>'
        assert '<Entry>' in contents, 'File contents should contain <Entry>'
        assert '</Entry>' in contents, 'File contents should contain </Entry>'
        # assert '<String>' in contents, 'File contents should contain <String>'
        # assert '</String>' in contents, 'File contents should contain </String>'
        # assert '<Title>' in contents, 'File contents should contain <Title>'
        # assert '</Title>' in contents, 'File contents should contain </Title>'
        # assert '<UserName>' in contents, 'File contents should contain <UserName>'
        # assert '</UserName>' in contents, 'File contents should contain </UserName>'
        # assert '<Password>' in contents, 'File contents should contain <Password>'
        # assert '</Password>' in contents, 'File contents should contain </Password>'

    def test_read_first_item(self):
        '''
        Test reading first item from KeePass XML file.
        '''
        root = self.kp.read_xml_file(self.file_path)

        assert root is not None, 'File contents should not be None'
        assert isinstance(root, ET.Element), 'Parsed XML should be an Element'
        assert len(root) > 0, 'Parsed XML should not be empty'

        # print(ET.tostring(xml, encoding='unicode'))
        # item = xml.find('Entry')
        entry = root.find('.//Entry')
        if entry is not None:
            print('Entry:', entry.tag, entry.attrib, entry.text)

        assert entry is not None, 'Entry should not be None'
        assert entry.tag == 'Entry', 'Entry tag should be <Entry>'
        assert len(entry) > 0, 'Entry should not be empty'
        # assert 'UUID' in entry.attrib, 'Entry should have UUID attribute'
        assert False
