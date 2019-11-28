import os
import hashlib
import mimetypes
from chardet.universaldetector import UniversalDetector

temp_file = 'temp/listfile.txt'

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def write_list(root) :

    open(temp_file, 'w').close() # clear temp files

    for path, subdirs, files in os.walk(root):
        for name in files:
            fl = os.path.join(path, name)
            with open(temp_file, 'a') as f:
                f.writelines(fl + '\n')
            # print(os.path.join(path, name))

def delete_line(this_line) :
    with open(temp_file, "r") as f:
        lines = f.readlines()
    # print(len(lines))
    with open(temp_file, "w") as f:
        for line in lines:
            if line.strip("\n") != this_line:
                f.write(line)

def get_detail_line(root, filepath) :
    md5check = md5(filepath)
    filetype = mimetypes.guess_type(filepath)[0]
    purepath = '/' + filepath[len(root):]
    filesize = os.path.getsize(filepath)
    # encoding detection
    detector = UniversalDetector()
    for line in open(filepath, 'rb'):
        detector.feed(line)
        if detector.done: break
    detector.close()
    encoding = detector.result['encoding']
    return [str(md5check),str(filesize),str(filetype),str(encoding),str(purepath)]