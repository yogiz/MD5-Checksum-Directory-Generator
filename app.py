from listingDoc import write_list, delete_line, md5, get_detail_line
from datetime import datetime
import sys 
import os

if (len(sys.argv) > 1 ):

    root = str(sys.argv[1])
    if root[-1] != '/' : root = root + '/'

    now = datetime.now()
    timeversion = now.strftime("V%y%m%d%H%M%S")

    if (os.path.isdir(root)):
        write_list(root)
        fpaths = []
        with open('temp/listfile.txt', 'r') as f:
            for line in f :      
                fpaths.append(line.strip('\n'))

        with open(root + 'ListDocuments.md5', 'w') as f :
            f.writelines(timeversion + '\n')
            for path in fpaths :
                detail = get_detail_line(root, path)
                detail_join = ','.join(detail)
                f.write( detail_join + '\n')
                print('writing ... ' + detail_join)
                delete_line(path)
        print('Process done! please see result in '+ root + 'ListDocuments.md5')
    else :
        print("Path doesnt exist or incorrect!")

else :
    print(" please input correct argument , ex = python3 app.py /User/document/source/ ")




