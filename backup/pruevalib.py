# -*- coding: utf-8 -*-
import libcerebrov3
a = libcerebrov3.fichero('/home/i2p/python2remonte/basesdedatos/')
libcerebrov3.ouput('Articulo : ')
b = libcerebrov3.input()
c = a.check(b)
if c == 0:
    a.crea(b)
a.mues()
