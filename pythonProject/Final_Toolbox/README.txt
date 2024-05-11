This toolbox takes in  a folder of 32-bit signed bathymetric tile rasters and allows the user to name the output as its
inputs. Then, it mosaics the tiles to a single raster image file, finds slope for the raster, and outputs a reclassified
raster. The reclassification runs as follows: A slope grade of 0 to 22.5 is given a value of 1, 22.5 to 45 is given a
value of 2, and values from 45 to 90 receive a 0. The purpose of the tool is to classify bathymetric slopes that may
produce more dangerous tsunami run-ups. Shallow slopes are known to build tsunami run-ups, moderate slopes build run-up
more severely, and very steep slope dampen runup. Higher values in this reclassification correspond with more risk.