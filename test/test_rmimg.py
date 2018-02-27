#!usr/bin/env python
# coding:utf-8

from OgiData.OgiDataManager import OgiDataManager
import json
import sys

if __name__ == '__main__':

  if len(sys.argv) != 2:
    print "for example:"
    print "python test_rmimg.py 6"
    sys.exit()

  m = OgiDataManager()

  #m.uploadImage("img1.jpg")
  print m.removeImage(sys.argv[1])

