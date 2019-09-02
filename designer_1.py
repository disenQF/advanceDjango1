#!/usr/bin/python3
# coding: utf-8
"""
设计模式之工厂
"""
class FuLei(object):
    def __int__(self,number1=None,number2=None):
        self.num1 = number1
        self.num2 = number2

    def getJisuan(self):
        pass

class Add(FuLei):
    def getJisuan(self):
        return self.num1 + self.num2

class Sub(FuLei):
    def getJisuan(self):
        return self.num1 - self.num2

class Gongchang(object):
    @staticmethod
    def yunsuanfu(ch):
        if ch == '+':
            return Add()
        elif ch == '-':
            return Sub()
        else:
            return 'Error'

if __name__ == '__main__':
    num1 = int(input('one'))
    ch = input('yunsuan')
    num2 = int(input('two'))
    # OF = Gongchang().yunsuanfu
    OF_OBJ = Gongchang.yunsuanfu(ch)
    OF_OBJ.num1 = num1
    OF_OBJ.num2 = num2
    print(OF_OBJ.getJisuan())
