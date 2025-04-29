# bw-kp-sync
BitWarden - KeePass sync

# Purpose
The intention for this application is to assist in synchronizing BitWarden and
KeePass databases.

# Analysis
Both applications are GUI applications. They also offer CLI versions with relatively limited functionality and incompatible formats.

## Problems
Passwords using unusual and high-ASCII characters are difficult to transfer via stdin/out.

# Design
An optimal solution seems to be the one that gets an output from both applications that is officially supported.
For KeePassXC, this is (likely) XML.
For BitWarden, it is JSON.

These exported files can then be parsed and compared.

# Technology
Python.
Python seems good at manipulating data and reading different data sources. It is easily 
maintainable and seems a perfect fit for a very small project.

# Process

Export BitWarden JSON using CLI.

Export KeePass XML, manually from GUI.
```sh
keepassxc-cli export --format|-f xml -k|--key-file <keyfile> <database.kdbx> > backup.xml
```

Compare the  files.
