#coding:utf-8

import os
def get_curdir():
    return os.getcwd()

#__name__是python内置专有变量
if __name__=="__main__":
    
    print(get_curdir()) #测试代码