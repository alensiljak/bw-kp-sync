'''
    Main entry point.
'''

from src.keepass_xml_parser import KeePassXmlParser
from src import kpcli


def main():
    '''
    entry point
    '''
    # 1. export KeePass database.
    kpcli.export()
    # 2. export BitWarden database.

    # 3. compare.
    kp = KeePassXmlParser()
    kp.echo()

    print("Hello from bw-kp-sync!")


if __name__ == "__main__":
    main()
