import os, os.path
import sys

def search(path, str):
    for x in os.listdir(path):
       fp = os.path.join(path, x)
       if os.path.isfile(fp):
          with open(fp, 'r') as fc:
             for line in fc.readlines():
               if str in line:
                 print fp
                 break
       elif os.path.isdir(fp):
          search(fp, str)

if len(sys.argv) == 1:
   print 'useage: search str'
elif len(sys.argv) == 2:
   str = sys.argv[1]
   search('.', str)
elif len(sys.argv) == 3:
    str = sys.argv[2]
    search(sys.argv[1], str)
else:
   print 'too many parameters'