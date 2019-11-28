# MD5-Checksum-Directory-Generator
Generate listing md5 checksum for all files in a directory. The result will be add new file in your targer directory 

`ListDocuments.md5` (this file will be added) 

And its contain list of your file detail in target directory (including all subdirectory file). The detail that produced by this tool is like in the following order :

`| md5 checksum | filesize | filetype | encoding | filepath |`

# How to run this tool

This tool based on python3.
First you need to install library needed

` pip3 install -r requirements.txt`

Then run the program :

` python3 app.py [path]`

example :

` python3 app.py /Users/yogi/Documents/Python/source/ `
