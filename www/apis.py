# -*- coding: utf-8 -*-
__author__ = 'wangbb13'

'''
JSON API definition
'''
import json, logging, inspect, functools

class APIError(Exception):
    '''
    the base APIError which contains error(required), data(opt) and msg(opt)
    '''
    def __init__(self, error, data='', message=''):
        super(APIError, self).__init__(message)
        self.error = error
        self.data = data
        self.message = message

class APIValueError(APIError):
    '''
    Indicate the input value has error or invalid. The data specifies the error field of input form.
    '''
    def __init__(self, field, message=''):
        super(APIValueError, self).__init__('value:invalid', field, message)

class APIResourceNotFoundError(APIError):
    '''
    Indicate the resource not found. The data specifies the resource name.
    '''
    def __init__(self, field, message=''):
        super(APIResourceNotFoundError, self).__init__('value: not found', field, message)

class APIPermisssionError(APIError):
    '''
    Indicate the api has no permission.
    '''
    def __init__(self, message=''):
        super(APIPermisssionError, self).__init__('permission: forbidden', 'permission', message)
