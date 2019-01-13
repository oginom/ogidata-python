#!/usr/bin/env python3
#coding:utf-8

import json
import sys
sys.path.append('..')
from OgiData import OgiDataManager

if __name__ == '__main__':

  if len(sys.argv) != 4:
    print("for example:")
    print(sys.argv[0] + " img0.jpg cider,coke,CocaCola Coke_Normal")
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
  #    'type_detail':{
  #      'img_width':512,
  #      'img_height':512
  #    }
  #  },
  #  {
  #    'name':'Tags',
  #    'type':'TAGS',
  #  },
  #  {
  #    'name':'Description',
  #    'type':'STRING',
  #  },
  #])
  #m.createTable(title, cols)

  ###### insert data ######
  imgID = m.uploadImage(sys.argv[1])
  data = json.dumps({
    'Image' : imgID,
    'Tags' : sys.argv[2],
    'Description' : sys.argv[3]
  })
  print(data)
  if not m.insertData(title, data):
    m.removeImage(imgID)

