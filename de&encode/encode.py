import os,stat

class encode:
    def __init__(self, numb = 98):
        self._num = numb

    def exchange(self,file_name):
        f1 = 0
        f2 = 0
        f3 = 0
        try:
            os.chmod('./videos_folder/' + file_name, stat.S_IWRITE)
            f1 = open(r'./videos_folder/' + file_name, mode = 'rb+')
            f2 = open(r'./sample.mp4',mode = 'rb+')
            #f3 = open(r'./decode_folder/' + file_name, mode = 'wb')
        except PermissionError:
            print('for ' + file_name + ', Permission denied, we can not deal with this file and skip it.')
        except:
            print('while opening file ' + file_name + ', we come across some issues, and skip it')
        else:
            a = f1.read(self._num)
            b = f2.read(self._num)
            if a != b:
                f3 = open(r'./decode_folder/' + file_name, mode='wb')
                f3.write(a)
                f1.seek(0)
                f1.write(b)
        finally:
            if f1:
                f1.close()
            if f2:
                f2.close()
            if f3:
                f3.close()

def main():
    code = encode(numb = 98)
    filelis = os.walk('./videos_folder')
    for ro, di, files in filelis:
        for file in files:
            _filename = file
            if _filename =='encode.py':
                continue
            elif _filename == 'sample.mp4':
                continue
            else:
                code.exchange(_filename)
    print('Encoding task is done!'+'\n'+ 'And the unprocessed files have been list above! If you wanna restore the files, please run \'decode.py\' file')

if __name__ == "__main__":
    main()
