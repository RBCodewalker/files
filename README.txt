Packages Used
=============
(PYTHON INSTALLATION IS REQUIRED)
1-> argparse
    Installation: "pip install argparse"
2-> requests
    Installation: "pip install requests"

Usage
=====

-> Python files are different for the coverages(Wind = "getwind.py", Temperature = "gettemp.py" and Icing = "geticing.py")

-> Select a file and each file requires input parameters(plev, lat, long) which are the pressure level, latitude and longitude ranges

-> Example requests:
        => "python3 gettemp.py --plev 5000,84310 --lat 60,70 --long 30,40 --fname final_temp.nc"
        => "python3 getwind.py --plev 5000,84310 --lat 60,70 --long 30,40 --fname final_wind.nc"
        => "python3 geticing.py --plev 22730,84310 --lat 60,70 --long 30,40 --fname final_icing.nc"
        (THE RESPECTIVE FILES ARE ALSO INCLUDED IN THE FOLDER)
