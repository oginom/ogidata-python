#!/usr/bin/env python3
#coding:utf-8

from OgiData import OgiDataManager
import json
import sys

if __name__ == '__main__':

  if len(sys.argv) != 3:
    print("for example:")
    print("python test_img.py img0.jpg Coke_Normal")
    sys.exit()

  #m.uploadImage("img1.jpg")
  #m.removeImage(2);

  m = OgiDataManager()
  title = 'CapDB'

  ###### create table ######
  #cols = json.dumps([
  #  {
  #    'name':'Image',
  #    'type':'IMG',
  #  },
  #  {
  #    'name':'Description',
  #    'type':'STRING',
  #  },
  #])
  #m.createTable(title, cols)

  ###### insert data ######
  data = json.dumps({
    'Image' : m.uploadImage(sys.argv[1]),
    'Description' : sys.argv[2]
  })
  m.insertData(title, data)
