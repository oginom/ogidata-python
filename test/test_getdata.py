#!/usr/bin/env python3
#coding:utf-8

import sys
sys.path.append('..')
from OgiData import OgiDataManager

if __name__ == '__main__':

  if len(sys.argv) != 2:
    print('usage:')
    print(sys.argv[0] + ' [DBname]')
    sys.exit()

  m = OgiDataManager()

  print(m.getData(sys.argv[1],start_index=0,limit=100,asc=False))

