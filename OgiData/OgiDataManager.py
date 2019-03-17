#!/usr/bin/env python3
#coding:utf-8

import requests
import json

from . import config

class OgiDataManager:

  def __init__(self, apiurl=None):
    if apiurl is None:
      self.apiurl = config.apiurl
    else:
      self.apiurl = apiurl
    self.printErrorMessage = True
    return

  def __isErrorResponse(self, response_j):
    if type(response_j) != dict:
      return False
    if 'ErrorMessage' in response_j:
      if self.printErrorMessage:
        print(response_j['ErrorMessage'])
      return True
    return False

  def createTable(self, title, cols):
    url = self.apiurl + 'createtable'
    params = {
      'title': title,
      'cols': cols
    }
    response = requests.post(url, params)
    ret = response.json()
    if self.__isErrorResponse(ret):
      return False
    return ret

  def dropTable(self, title):
    url = self.apiurl + 'droptable'
    params = {
      'title': title,
    }
    response = requests.post(url, params)
    ret = response.json()
    if self.__isErrorResponse(ret):
      return False
    return ret

  def insertData(self, title, data):
    url = self.apiurl + 'insertdata'
    params = {
      'title' : title,
      'data' : data
    }
    response = requests.post(url, params)
    ret = response.json()
    if self.__isErrorResponse(ret):
      return False
    return ret

  def updateData(self, title, data_id, data):
    url = self.apiurl + 'updatedata'
    params = {
      'title' : title,
      'data_id' : data_id,
      'data' : json.dumps(data)
    }
    response = requests.post(url, params)
    ret = response.json()
    if self.__isErrorResponse(ret):
      return False
    return ret

  def deleteData(self, title, data_id):
    url = self.apiurl + 'deletedata'
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
    url = self.apiurl + 'uploadimage'
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
    url = self.apiurl + 'removeimage'
    params = {
      'img_id' : img_id
    }
    response = requests.post(url, params)
    ret = response.json()
    if self.__isErrorResponse(ret):
      return False
    return ret

  def getImageInfo(self, img_id):
    url = self.apiurl + 'getimageinfo'
    params = {
      'img_id' : img_id
    }
    response = requests.get(url, params)
    ret = response.json()
    if self.__isErrorResponse(ret):
      return False
    return ret

  def getTables(self):
    url = self.apiurl + 'gettables'
    response = requests.get(url)
    ret = response.json()
    if self.__isErrorResponse(ret):
      return False
    return ret

  def getTableID(self, title):
    url = self.apiurl + 'gettableid'
    params = {
      'title' : title
    }
    response = requests.get(url, params=params)
    ret = response.json()
    if self.__isErrorResponse(ret):
      return False
    return ret

  def getTableInfo(self, title):
    url = self.apiurl + 'gettableinfo'
    params = {
      'title' : title
    }
    response = requests.get(url, params=params)
    ret = response.json()
    if self.__isErrorResponse(ret):
      return False
    return ret

  def getData(self, title, start_index=None, limit=None, asc=None):
    url = self.apiurl + 'getdata'
    params = {
      'title' : title
    }
    if start_index != None:
      params['start_index'] = start_index
    if limit != None:
      params['limit'] = limit
    if asc != None:
      if asc:
        params['asc'] = "YES"
      else:
        params['asc'] = "NO"
    response = requests.get(url, params=params)
    ret = response.json()
    if self.__isErrorResponse(ret):
      return False
    return ret

  def getChoice(self, title, columns=None, limit=None):
    url = self.apiurl + 'getchoice'
    params = {
      'title' : title
    }
    if columns != None:
      params['columns'] = json.dumps(columns)
    if limit != None:
      params['limit'] = limit
    response = requests.get(url, params=params)
    ret = response.json()
    if self.__isErrorResponse(ret):
      return False
    return ret


