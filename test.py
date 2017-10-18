from sys import argv
import subprocess
import time

if __name__ == "__main__":
    subp = subprocess.Popen("aria2c -d E:/ http://dl147.80s.im:920/1710/猩qj起3：终jz战/猩qj起3：终jz战.mp4 >> ./.test.log", shell=True, stdout=subprocess.PIPE);
    print("56");
    while True:
        time.sleep(0.5);
        print(subp.communicate());

    