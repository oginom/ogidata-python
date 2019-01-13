#!/usr/bin/env python3
#coding:utf-8

import sys
sys.path.append('..')
from OgiData import OgiDataManager

if __name__ == '__main__':

  m = OgiDataManager()

  print(m.getTables())

