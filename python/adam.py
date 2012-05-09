
import os
from datetime import *


base_dir = "filesystem"

date_times = []


def processDirectory ( f, dirname, filenames ):
  current_abspath = f(dirname) 
  dir_datetime = datetime.fromtimestamp(int(os.path.getmtime(current_abspath)))
  date_times.append(dir_datetime)
  print "In directory:" + dirname + " Last Modified: " + str(dir_datetime)
  for filename in filenames:
    file_datetime = datetime.fromtimestamp(int(os.path.getmtime(current_abspath + "/" + filename)))
    date_times.append(file_datetime) 
    print " " * 4 + "In file: " + filename + " Last Modified: " + str(file_datetime)
    


#print "Is this a mount point? " + str(os.path.ismount(base_dir))

#print "The last modified time of the root dir: " + str(int(os.path.getctime(base_dir)))

def run():
  os.path.walk( base_dir, processDirectory, os.path.abspath )
  return date_times

print run()
