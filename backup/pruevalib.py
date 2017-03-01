# -*- coding: utf-8 -*-
import libcerebrov2
a = libcerebrov2.fichero('/home/i2p/python2remonte/basesdedatos/')
libcerebrov2.ouput('Articulo : ')
b = libcerebrov2.input()
c = a.check(b)
if c == 0:
    a.crea(b)
a.mues()