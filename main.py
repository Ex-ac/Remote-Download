import os
import time
from aria2c import Aria2

if __name__ == "__main__":
    Aria2.start();
    Aria2.addUri(["https://www.python.org/ftp/python/3.6.3/Python-3.6.3.tgz"]);