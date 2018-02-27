#!/usr/bin/env python3
#coding:utf-8

from OgiData import OgiDataManager
import json
import sys

if __name__ == '__main__':

  m = OgiDataManager()

  print m.getTables()

