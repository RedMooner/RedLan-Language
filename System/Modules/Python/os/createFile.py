#! /usr/bin/env python
# -*- coding: utf-8 -*-
class Module:
   def main(self,args):  
      my_file = open("some.txt", "w")
      my_file.write(str(args[1]))
      my_file.close()
      return "file created " + args[0] + " " +  args[1]