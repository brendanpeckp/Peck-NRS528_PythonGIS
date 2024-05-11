This toolbox takes in  a folder of 32-bit signed bathymetric tile rasters and allows the user to name the output as its
inputs. Then, it mosaics the tiles to a single raster image file, finds slope for the raster, and outputs a reclassified
raster. The reclassification runs as follows: A slope grade of 0 to 22.5 is given a value of 1, 22.5 to 45 is given a
value of 2, and values from 45 to 90 receive a 0. The purpose of the tool is to classify bathymetric slopes that may
produce more dangerous tsunami run-ups. Shallow slopes are known to build tsunami run-ups, moderate slopes build run-up
more severely, and very steep slope dampen runup. Higher values in this reclassification correspond with more risk.

This tool has a folder named "exampleData" for first-time users to use. The data contained is 6 bathymetric tiles off
the coast of American Samoa. The tile data is from:
https://noaa-nos-coastal-lidar-pds.s3.amazonaws.com/dem/NCEI_third_Topobathy_AmSam_9461/index.html
I have also included a file named exampleDataNE for users to try.
You can use the following link to find data for other areas
https://coast.noaa.gov/dataviewer/#/lidar/search/

The .py file in this directory is just a place to test the script.