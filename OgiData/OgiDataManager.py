#!/usr/bin/env python3
# coding:utf-8

import requests
import json

import config

class OgiDataManager:

  def __init__(self, apiurl=None):
    if apiurl is None:
      self.apiurl = config.apiurl
    else:
      self.apiurl = apiurl
    return

  def __isErrorResponse(self, response_j):
    if type(response_j) != dict:
      return False
    if 'ErrorMessage' in response_j:
      print(response_j['ErrorMessage'])
      return True
    return False

  def createTable(self, title, cols):
    url = self.apiurl + 'createtable.php'
    params = {
      'title': title,
      'cols': cols
    }
    response = requests.post(url, params)
    #print(response.json())
    print(response.text)

  def dropTable(self, title):
    url = self.apiurl + 'droptable.php'
    params = {
      'title': title,
    }
    response = requests.post(url, params)
    ret = response.json()
    if self.__isErrorResponse(ret):
      return False
    return ret

  def insertData(self, title, data):
    url = self.apiurl + 'insertdata.php'
    params = {
      'title' : title,
      'data' : data
    }
    response = requests.post(url, params)
    print(response.text)

  def deleteData(self, title, data_id):
    url = self.apiurl + 'deletedata.php'
    params = {
      'title' : title,
      'data_id' : data_id
    }
    response = requests.post(url, params)
    ret = response.json()
    if self.__isErrorResponse(ret):
      return False
    return ret

  def uploadImage(self, filename):
    url = self.apiurl + 'uploadimage.php'
    params = {
    }
    files = {
      'file' : open(filename, 'rb')
    }
    response = requests.post(url, params, files=files)
    ret = response.json()
    if self.__isErrorResponse(ret):
      return False
    return ret['img_id']

  def removeImage(self, img_id):
    url = self.apiurl + 'removeimage.php'
    params = {
      'img_id' : img_id
    }
    response = requests.post(url, params)
    ret = response.json()
    if self.__isErrorResponse(ret):
      return False
    return ret

  def getTables(self):
    url = self.apiurl + 'gettables.php'
    response = requests.get(url)
    ret = response.json()
    if self.__isErrorResponse(ret):
      return False
    return ret

  def getTableInfo(self, title):
    url = self.apiurl + 'gettableinfo.php'
    params = {
      'title' : title
    }
    response = requests.get(url, params=params)
    ret = response.json()
    if self.__isErrorResponse(ret):
      return False
    return ret

  def getData(self, title):
    url = self.apiurl + 'getdata.php'
    params = {
      'title' : title
    }
    response = requests.get(url, params=params)
    ret = response.json()
    if self.__isErrorResponse(ret):
      return False
    return ret


