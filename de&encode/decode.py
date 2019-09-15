import os,stat

class decode:
    def __init__(self, numb = 98):
        self._num = numb

    def exchange(self,file_name):
        f1 = 0
        f3 = 0
        try:
            #os.chmod('./videos_folder/' + file_name,stat.S_IWRITE)
            f1 = open('./videos_folder/' + file_name, mode = 'rb+')
            f3 = open('./decode_folder/' + file_name, mode = 'rb')
        except PermissionError:
            print('for ' + file_name + ', Permission denied, we can not deal with this file and skip it.')
        except:
            print('while opening file ' + file_name + ', we come across some issues, and skip it')
        else:
            b = f3.read(self._num)
            f1.seek(0)
            f1.write(b)
        finally:
            if f1:
                f1.close()
            if f3:
                f3.close()

def main():
    code = decode(numb = 98)
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

    print('Decoding task is done!'+'\n'+'And the unprocessed files have been list above!(if the unprocessed files list is the same as the one shown up when you decode them, you do not have to worry).')

if __name__ == "__main__":
    main()

