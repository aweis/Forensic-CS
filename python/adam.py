import os
import sys
from datetime import *


#The root directory of the filesystem
base_dir = "filesystem"

def mount(path):
  #check if it is mac os
  if sys.platform == "darwin":
    os.system( "hdid -nomount "+ path +" > macos.txt")
    fileHandler = open("macos.txt", "rt")
    text = fileHandler.read().rstrip('\n')
    os.system( "rm macos.txt")
    print text
    os.system( "sudo mount -t msdos " + text + " ./tmp_fs")
  else:
    os.system( "sudo mount " + path + " ./tmp_fs -o loop" )

#The array used to accumulate datetime objects
date_times = []

def getmount(path):
  path = os.path.realpath(os.path.abspath(path))
  while path != os.path.sep:
    if os.path.ismount(path):
      return path
    path = os.path.abspath(os.path.join(path, os.pardir))
  return path

def truncatefilesystem(path):
  path = os.path.realpath(os.path.abspath(path))
  builder = ""
  while path != os.path.sep:
    if os.path.ismount(path):
      return builder
    builder = os.path.sep + path.split(os.path.sep)[-1] + builder
    path = os.path.abspath(os.path.join(path, os.pardir))
  return builder

def processDirectory ( f, dirname, filenames ):
  current_abspath = f(dirname) 
  dir_datetime = datetime.fromtimestamp(int(os.path.getmtime(current_abspath)))
  dir_size = os.path.getsize(current_abspath)
  dir_name = dirname
  dir_path = truncatefilesystem(current_abspath)
  date_times.append((dir_datetime, dir_name, dir_size, dir_path))
  print "In directory:" + dirname + " Last Modified: " + str(dir_datetime)
  
  for filename in filenames:
    file_path = current_abspath + "/" + filename
    file_datetime = datetime.fromtimestamp(int(os.path.getmtime(file_path)))
    file_size = os.path.getsize(file_path)
    file_name = filename
    date_times.append((file_datetime, file_name, file_size, truncatefilesystem(file_path))) 
    print " " * 4 + "In file: " + filename + " Last Modified: " + str(file_datetime)

#print "Is this a mount point? " + str(os.path.ismount(base_dir))

#print "The last modified time of the root dir: " + str(int(os.path.getctime(base_dir)))

def run(path_to_image):
  mount(path_to_image) 
  base_dir = "./tmp_fs"
  print base_dir
  if not os.path.exists(base_dir):
    os.makedirs(base_dir)
  os.path.walk(base_dir, processDirectory, lambda path: os.path.realpath(os.path.abspath(path)) )
  os.system( "sudo umount ./tmp_fs" )
  return date_times

#print run("~/disk.img")
