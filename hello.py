# -*- coding: utf-8 -*-

' a test module '


__author__ = 'Michael Liao'

import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print '哈喽, world!'

    elif len(args) == 2:
        print '哈喽, %s!' % args[1]

    else:
        print 'Too many arguments!'

if __name__ == '__main__':
    test()