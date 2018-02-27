#!usr/bin/env python
# coding:utf-8

from OgiData.OgiDataManager import OgiDataManager
import json
import sys

if __name__ == '__main__':

  m = OgiDataManager()

  print m.getTables()

