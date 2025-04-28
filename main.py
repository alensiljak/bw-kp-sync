'''
    Main entry point.
'''

from src.keepass_xml_parser import KeePassXmlParser


def main():
    '''
    entry point
    '''
    kp = KeePassXmlParser()
    kp.echo()

    print("Hello from bw-kp-sync!")


if __name__ == "__main__":
    main()
