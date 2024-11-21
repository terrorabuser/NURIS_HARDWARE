from  generate import gen
from send_to_flammap import clicker
from asc_to_csv import *
import time





def main():
    for i in range (0,7):
        avg_wind_spd, avg_wind_dir = gen()
        clicker(avg_wind_spd, avg_wind_dir)
        time.sleep(2)
        all()
        time.sleep(2)
        i+= 1 
    

if __name__ == "__main__":
    main()
    
    