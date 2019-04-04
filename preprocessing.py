# -*- coding: utf-8 -*- 
import os, subprocess, sys

def getFiles(path):
    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if '.mp3' in file:
                files.append(os.path.join(r, file))
    return files

def fixTags(files,author,book):
    part = 0
    total = len(files)
    for file in sorted(files):
        part += 1
        subprocess.call([
          'kid3-cli',
          '-c', 'remove "2"',
          '-c', 'tag "2"',
          '-c', 'set title "Part '+str(part)+' of '+str(total)+'"',
          '-c', 'set artist "'+author+'"',
          '-c', 'set album "'+book+'"',
          '-c', 'set song ""',
          '-c', 'set track "'+str(part)+'"',
          '-c', 'set comment ""',
          '-c', 'set year ""',
          '-c', 'set genre "183"',
          '-c', 'set band ""',
          '-c', 'set composer ""',
          '-c', 'set copyright ""',
          '-c', 'set url ""',
          '-c', 'set publisher ""',
          '-c', 'syncto 1',
          file])

authorname = ''
bookname = ''
if sys.argv[1] == 'test':
    if '.py' in subprocess.check_output(['kid3-cli','-c', 'ls']):
        print 'preprocessing.py sucessfully installed'
    else:
        print 'kid3-cli seems to be missing'
else:
    booktype = sys.argv[1]
    bookfolder = sys.argv[2]
    if len(sys.argv) == 5:
        authorname = sys.argv[3]
        bookname = sys.argv[4]
    fixTags(getFiles(bookfolder),authorname,bookname)
