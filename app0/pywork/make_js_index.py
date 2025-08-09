# coding=utf-8
""" make_js_index.py for vikramor_mw
    REvised so ipage 1-608,  epage = ipage + 26
"""
from __future__ import print_function
import sys, re, codecs
import json


class Pagerec(object):

 def __init__(self,ipage,epage):
  self.ipage = ipage
  self.epage = epage
  self.vpstr = '%03d' % epage
 def todict(self):
  e = {
   'ipage':self.ipage,
   'vp':self.vpstr
  }
  return e

def init_pagerecs(first,last,offset):
 """ filein is a tsv file, with first line as fieldnames
 """
 recs = []
 for ipage in range(first,last + 1):
  epage = ipage + offset
  pagerec = Pagerec(ipage,epage)
  recs.append(pagerec)
 return recs


def make_js(recs):
 outarr = []
 outarr.append('indexdata = [')
 arr = [] # array of Python dicts
 for rec in recs:
  d = rec.todict()  # a Python dictionary
  arr.append(d)
 return arr

def write_recs(fileout,data):
 with codecs.open(fileout,"w","utf-8") as f:
  f.write('indexdata = \n')
  jsonstring = json.dumps(data,indent=1)
  f.write( jsonstring +  '\n')
  f.write('; // end of indexdata\n')
  
 print('json data written to',fileout)


if __name__ == "__main__":
 fileout = sys.argv[1]
 pagerecs = []
 pagerecs = init_pagerecs(1,162,26)
 outrecs = make_js(pagerecs)
 write_recs(fileout,outrecs)

 
