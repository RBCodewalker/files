import argparse
import requests

parser = argparse.ArgumentParser(description="Get wind data from cube4envsec.org/rasdaman.")
parser.add_argument("--plev", type=str, help="Pressure level range in Pascal (e.g., '5000,84310') available=(5000 7170 7520 7900 8280 8700 9120 9570 10040 10530 11050 11600 12170 12770 13400 14060 14750 15470 16240 17040 17870 18750 19680 20650 21660 22730 23840 25000 26200 27450 28740 30090 31490 32930 34430 35990 37600 39270 41000 42790 44650 46560 48550 50600 52720 54920 57180 59520 61940 64440 67020 69680 72430 75260 78190 81200 84310)")
parser.add_argument("--lat", type=str, help="Latitude range in degrees north (e.g., '60,70') available=(29.46875 to 70.53125)")
parser.add_argument("--long", type=str, help="Longitude range in degrees east (e.g., '30,40') available=( -23.53125 to 62.53125)")
parser.add_argument("--fname", type=str, default="wind_data_all.nc", help="Output filename")
args = parser.parse_args()

base_url = "https://weather.cube4envsec.org/rasdaman/ows?"
service_param = "SERVICE=WCS"
version_param = "VERSION=2.0.1"
request_param = "REQUEST=GetCoverage"
coverage_id_param = "COVERAGEID=wind_plev_new"
ansi_subset = "SUBSET=ansi(\"2022-11-30T00:00:00.000Z\")"
plev_subset = f"SUBSET=plev({args.plev})" if args.plev else ""
lat_subset = f"SUBSET=Lat({args.lat})" if args.lat else ""
long_subset = f"SUBSET=Long({args.long})" if args.long else ""
format_param = "FORMAT=application/netcdf"

url = f"{base_url}&{service_param}&{version_param}&{request_param}&{coverage_id_param}&{ansi_subset}&{plev_subset}&{lat_subset}&{long_subset}&{format_param}"

username = "asubedi"
password = "Z@4k+fPnA"
auth = (username, password)

headers = {
    "Accept": "application/netcdf"
}

response = requests.get(url, headers=headers, auth=auth)

with open(args.fname, "wb") as file:
    file.write(response.content)
