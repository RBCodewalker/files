# UNIDATA IDV FOR VOLUMETRIC VISUALIZATION OF MULTIDIMENSIONAL RASTER DATA VISUALIZATION

The Volumetric Visualization of multidimensional datacubes requires a raster data friendly environment which was found in the Unidata IDV API that contains a range of Java classes for compatibility. The Unidata IDV software framework uses this API along with the netCDF-Java package for dealing with such 3D netCDF data. The framework, along with the VisAD package, was used for an interactive UI. With a few adjustments to the existing tool, the available datasets were successfully visualized.

## Prerequisites

- The IDV is built on Java 3D, so Java Development Kit (JDK) version 8 or later has to be installed on your system.
  - In Ubuntu or Debian systems, you can simply install it via the terminal: `sudo apt-get install openjdk-8-jdk`
  - For other systems, you can download the JDK from the official Oracle website: [Oracle JDK Downloads](https://www.oracle.com/java/technologies/downloads/)

- System Requirements:
  - Operating System: Windows, macOS, or Linux
  - Memory: At least 4 GB RAM (8 GB or more recommended)
  - Disk Space: At least 500 MB of free disk space
  - Graphics Hardware: Systems with graphics cards that support OpenGL. Although any graphics hardware can run the tool, using a better one improves render times.

## Usage of IDV

### Run the Tool
- Launch the shell script "runIDV.sh" in the 'IDV' folder
  - OR
- Navigate to the 'IDV' folder and open a terminal there. From the command line, run `./runIDV`

### Add Data Source
- Use WCS client UI from [https://weather.cube4envsec.org/rasdaman/ows](https://weather.cube4envsec.org/rasdaman/ows) and enter the required parameters (Coverage Name, Pressure level (plev), Latitude (Lat), and Longitude (Lon)) to get the required file.
  - Alternatively,
- Python files with the same feature are available in the 'getfiles' folder, which use the 'argparse' and 'requests' packages and can be installed by `pip install <package_name>`. To use them:
  - Navigate to the 'getfiles' folder and open a terminal there.
  - Usage:
    - Python files are different for the coverages (Wind = "getwind.py", Temperature = "gettemp.py," and Icing = "geticing.py").
    - Select a file, and each file requires input parameters (plev, lat, long), which are the pressure level, latitude, and longitude ranges.
    - Example requests:
      - `python3 gettemp.py --plev 5000,84310 --lat 60,70 --long 30,40 --fname final_temp.nc`
      - `python3 getwind.py --plev 5000,84310 --lat 60,70 --long 30,40 --fname final_wind.nc`
      - `python3 geticing.py --plev 22730,84310 --lat 60,70 --long 30,40 --fname final_icing.nc`
      (THE RESPECTIVE FILES ARE ALSO INCLUDED IN THE FOLDER)

- Now you can add the files in the IDV pipeline.
  - From the options on the top bar in the tool, go to "Data > Choose Data > From the File System" and navigate to the netCDF files' location.
  - Select the files you want to add.
- The files can now be seen under the Data option in the top bar.
- Select a file and choose the parameter (temperature/icing) to visualize. (Files available in the 'getfiles' folder can be used)
  - For example, to visualize temperature as an isosurface, choose "3D Grid > Temperature."
- You can now also select the pressure levels you want to use and other relevant adjustments like display region and data sampling.
  (Please refer to IDV documentation: [IDV Workshop](https://docs.unidata.ucar.edu/idv/current/workshop/index.html))
- Finally, click on "Create Display" at the bottom of the screen to visualize.

### Visualization/Customization
- You can now customize the visualization, like changing the legend, color range, smoothing, etc.
- To add a base map, press the globe button on the top menu bar.
- For borders on the map, add a shapefile available in the provided folder named "world-administrative-boundaries.shp."
- You can repeat the process for other data files to show visualizations collectively.

### Interaction
- You can rotate the display with right-click and mouse movement simultaneously.
- Scroll in and out for zooming in and out.
- The options on the left side of the screen can be used as well to view a specific side of the display region.

(PLEASE REFER TO IDV DOCUMENTATION FOR AN EXTENSIVE USER GUIDE. THIS GUIDE ONLY SERVES AS FAR AS MY KNOWLEDGE AND SPECIFIC IMPLEMENTATION OF THE FRAMEWORK. [IDV Workshop](https://docs.unidata.ucar.edu/idv/current/workshop/index.html))

## Folder Tree

├── auxdata.jar
├── Example bundles
│   ├── final_bundle2.xidv
│   └── final_bundle.xidv
├── external.jar
├── getfiles
│   ├── geticing.py
│   ├── gettemp.py
│   ├── getwind.py
│   ├── icing.nc
│   ├── README_for_files.txt
│   ├── temp_all.nc
│   ├── temp.nc
│   ├── wind_69680.nc
│   ├── wind_72430.nc
│   ├── wind_75260.nc
│   ├── wind_78190.nc
│   ├── wind_81200.nc
│   └── wind_84310.nc
├── idv.gif
├── idv.jar
├── jython.jar
├── local-visad.jar
├── ncIdv.jar
├── README.txt
├── runIDV
├── runIDV.ico
├── uninstall
├── visad.jar
└── world-administrative-boundaries.shp
