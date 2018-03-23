# -*- coding: utf-8 -*-

def write(text=' '):
    import datetime, os
    time = datetime.datetime.today()
    path = "./log/new/" + time.strftime("%Y//%m//%d")
    if not os.path.exists(path):
      os.makedirs(path)
    f = open(time.strftime("./log/new/%Y/%m/%d/%H:%M.log"), 'a')
    f.write(text)
    f.close()

def wprint(text=' '):
    import datetime
    time = datetime.datetime.today()
    write("[" + time.strftime("%H:%M.%S") + "] " + text + "と出力しました\n")
    print(text)

def wprintf(text=' '):
    import datetime, sys
    time = datetime.datetime.today()
    write("[" + time.strftime("%H:%M.%S") + "] " + text + "と出力しました\n")
    sys.stdout.write("\r" + text)
    sys.stdout.flush()
    
def archive():
    import shutil, os
    if not os.path.exists("./log/archive/old.zip"):
      shutil.make_archive('./log/archive/old', 'zip', root_dir='./log/', base_dir='./new/')
      write("ログファイルを圧縮しました")
    else:
      os.remove("./log/archive/old.zip")
      shutil.make_archive('./log/archive/old', 'zip', root_dir='./log/', base_dir='./new/')
      write("ログファイルを圧縮しました")