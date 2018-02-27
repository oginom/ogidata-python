#!/usr/bin/env python
#coding:utf-8

from OgiData import OgiDataManager
import json
import sys

if __name__ == '__main__':

  if len(sys.argv) != 2:
    print "for example:"
    print "python test_getdata.py CapDB"
    sys.exit()

  m = OgiDataManager()

  print m.getData(sys.argv[1])

