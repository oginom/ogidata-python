#!usr/bin/env python
# coding:utf-8

from OgiData.OgiDataManager import OgiDataManager
import json
import sys

if __name__ == '__main__':

  if len(sys.argv) != 3:
    print "for example:"
    print "python memozny.py USAGI 208.49"
    sys.exit()

  ###### insert data ######
  m = OgiDataManager()
  title = 'MyZNY'
  data = json.dumps({
    'Wallet' : sys.argv[1],
    'Price' : sys.argv[2]
  })
  m.insertData(title, data)

  ###### create table ######
  #cols = json.dumps([
  #  {
  #    'name':'Price',
  #    'type':'DOUBLE',
  #    'unit':'YEN'
  #  },
  #  {
  #    'name':'Wallet',
  #    'type':'STRING',
  #  },
  #])
  #m.createTable(title, cols)

