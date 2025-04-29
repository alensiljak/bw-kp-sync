'''
    Encapsulates operations on BitWarden CLI.

    Flow:
    bw login [--apikey]
    bw unlock
    bw sync
    bw export --format json --output $EXPORT_JSON --session $SESSION_KEY
'''

def export():
    '''
    C:\Users\<user>\AppData\Local\Programs\Bitwarden\bw.exe
    bw export

    '''