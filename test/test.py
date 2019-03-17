#!/usr/bin/env python3
#coding:utf-8

import sys
import json
sys.path.append('..')
from OgiData import OgiDataManager

from datetime import datetime

TEST_DB_TITLE = 'TEST_DB_{0:%y%m%d%H%M%S}'.format(datetime.now())

def check_error(res):
  if res is False:
    print(res)
    print('FAILED.')
    return True
  return False

def print_red(s):
  print('\033[31m' + str(s) + '\033[0m')
def print_green(s):
  print('\033[32m' + str(s) + '\033[0m')
def print_error():
  print_red('ERROR.')
  return -1
def print_success():
  print_green('SUCCESS.')

def test_createtable(m, title=TEST_DB_TITLE):
  print('=== CREATE TABLE ===')
  cols = json.dumps([
    {
      'name':'AAA',
      'type':'DOUBLE',
      'unit':'YEN'
    },
    {
      'name':'BBB',
      'type':'STRING',
    },
    {
      'name':'CCC',
      'type':'TIMESTAMP',
    },
    {
      'name':'あああ亜違雨',
      'type':'INT',
    },
  ])
  res = m.createTable(title, cols)
  print(res)
  if check_error(res):
    return print_error()
  else:
    print_success()

def test_gettables(m):
  print('=== GET TABLES ===')
  res = m.getTables()
  print(res)
  if check_error(res):
    return print_error()
  else:
    print_success()

def test_gettableid(m, title=TEST_DB_TITLE):
  print('=== GET TABLE ID ===')
  res = m.getTableID(title)
  print(res)
  if check_error(res):
    return print_error()
  else:
    print_success()

def test_gettableinfo(m, title=TEST_DB_TITLE):
  print('=== GET TABLE INFO ===')
  res = m.getTableInfo(title)
  print(res)
  if check_error(res):
    return print_error()
  else:
    print_success()

def test_insertdata(m, title=TEST_DB_TITLE):
  print('=== INSERT DATA ===')
  t = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
  data = json.dumps({
    'AAA':123.45,'BBB':'ABC','CCC':t,'あああ亜違雨':12345
  })
  res = m.insertData(title, data)
  print(res)
  if check_error(res):
    return print_error()
  else:
    print_success()

def test_droptable(m, title=TEST_DB_TITLE):
  print('=== DROP TABLE ===')
  res = m.dropTable(title)
  print(res)
  if check_error(res):
    print_error()
    print('* TEST DB may be still existing. *')
    return -1
  else:
    print_success()

def test_getdata(m, title=TEST_DB_TITLE):
  print('=== GET DATA ===')
  res = m.getData(title, asc=False, limit=None, start_index=None)
  print(res)
  if check_error(res):
    return print_error()
  else:
    print_success()

def test_updatedata(m, title=TEST_DB_TITLE):
  print('=== UPDATE DATA ===')
  data_id = 3
  data = {'AAA':99999}
  res = m.updateData(title, data_id, data)
  print(res)
  if check_error(res):
    return print_error()
  else:
    print_success()

def test_deletedata(m, title=TEST_DB_TITLE):
  print('=== DELETE DATA ===')
  data_id = 3
  res = m.deleteData(title, data_id)
  print(res)
  if check_error(res):
    return print_error()
  else:
    print_success()

def test_uploadimage(m):
  print('=== UPLOAD IMAGE ===')
  img_filename = 'img0.jpg'
  #img_filename = 'sss.png'
  res = m.uploadImage(img_filename)
  print(res)
  if check_error(res):
    return print_error()
  else:
    print_success()
    return res

def test_removeimage(m, img_id=13):
  print('=== REMOVE IMAGE ===')
  res = m.removeImage(img_id)
  print(res)
  if check_error(res):
    return print_error()
  else:
    print_success()

def test_getimageinfo(m, img_id=14):
  print('=== GET IMAGEINFO ===')
  res = m.getImageInfo(img_id)
  print(res)
  if check_error(res):
    return print_error()
  else:
    print_success()

def test_all():
  if len(sys.argv) != 1:
    print('no option is provided.', file=sys.stderr)
    sys.exit()

  title = TEST_DB_TITLE


  try:

    print('=== GET TABLE INFO')

    res = m.getTableInfo(title)
    print(res)
    if check_error(res):
      raise Error
    else:
      print_success()

    print('=== INSERT DATA')

    data = json.dumps({
      'AAA':123.45,'BBB':'ABC','CCC':'2018-01-23 04:56:07','DDD':12345
    })
    res = m.insertData(title, data)
    print(res)
    if check_error(res):
      raise Error
    else:
      print_success()

    data = json.dumps({
      'AAA':'123.4a','BBB':'ABC','CCC':'2018-01-23 04:56:07','DDD':12345
    })
    res = m.insertData(title, data)
    print(res)
    if res != False:
      raise Error
    else:
      print_success()

    data = json.dumps({
      'AAA':123.45,'BBB':'ABC','CCC':'2018-01-23 04:56:78','DDD':12345
    })
    res = m.insertData(title, data)
    print(res)
    if res != False:
      #raise Error
      print_error()
    else:
      print_success()

    data = json.dumps({
      'AAA':123.45,'BBB':'ABC','CCC':'2018-01-23 04:56:07','DDD':123.45
    })
    res = m.insertData(title, data)
    print(res)
    if res != False:
      raise Error
    else:
      print_success()

    print('=== GET DATA')

    res = m.getData(title)
    print(res)
    if check_error(res):
      raise Error
    else:
      print_success()

    print('=== DELETE DATA')

    res = m.deleteData(title, 1)
    print(res)
    if check_error(res):
      raise Error
    res = m.getData(title)
    print(res)
    if check_error(res):
      raise Error
    else:
      print_success()

    print('=== GET TABLES')

    res = m.getTables()
    print(res)
    if check_error(res):
      raise Error
    else:
      print_success()

    print('=== GET TABLEINFO')

    res = m.getTableInfo(title)
    print(res)
    if check_error(res):
      raise Error
    else:
      print_success()

  except:
    print_error()
    print('=== DROP TABLE')
    res = m.dropTable(title)
    if check_error(res):
      print('* TEST DB may be existing. *')
    return -1

  print('=== DROP TABLE')

  res = m.dropTable(title)
  print(res)
  if check_error(res):
    print_error()
    print('* TEST DB may be existing. *')
    return -1
  else:
    print_success()

  return 0

if __name__ == '__main__':
  print(sys.argv[1:])
  m = OgiDataManager(apiurl='http://localhost:8000/ogidata/api/')
  #m.printErrorMessage = False

  #test_createtable(m)
  #test_gettables(m)
  #test_gettableid(m)
  #test_gettableinfo(m, title='TEST_DB_181110221255')
  #test_insertdata(m)
  #test_droptable(m)

  #test_insertdata(m, title='TEST_DB_181110221255')
  #test_updatedata(m, title='TEST_DB_181110221255')
  #test_getdata(m, title='TEST_DB_181110221255')

  #test_getdata(m, title='TEST_DB_181110221255')
  #test_deletedata(m, title='TEST_DB_181110221255')
  #test_getdata(m, title='TEST_DB_181110221255')

  #test_uploadimage(m)
  #test_removeimage(m)
  test_getimageinfo(m)

  sys.exit(0)

  if test_all() == 0:
    print('FINISHED SUCCESSFULLY.')

