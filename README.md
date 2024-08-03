# Python .DS_Store parser
This repository contains a parser for Apple's `.DS_Store` file format.

<!-- BADGIE TIME -->
<!-- END BADGIE TIME -->

## Installation
Ensure Python 3 is installed on your computer, and use pip to
install this project with the command listed below:

```
pip install git+https://github.com/CoolCat467/ds-store-reader.git
```

## Usage
After installing, now you can use the program by running `ds_store_reader <filename> [--debug]`.

For example:
```console
$ ds_store_reader samples/DS_Store.ctf
Count:  6
favicon.ico
flag
static
templates
vulnerable.py
vulnerable.wsgi
```

## Useful resources

Original Author's blogpost that tries to explain the structure and format in detail:  https://0day.work/parsing-the-ds_store-file-format/
Original Author found the following links to be quite helpful while developing the parser:

- https://wiki.mozilla.org/DS_Store_File_Format
- http://search.cpan.org/~wiml/Mac-Finder-DSStore/DSStoreFormat.pod
- https://digi.ninja/projects/fdb.php

## License

MIT - See LICENSE file
