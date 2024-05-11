### Description:
This tool box consists of three tools for tsunami runup risk analysis. The three tools together take in a folder of contiguous bathymetry raster tiles and will measure tsunami runup risk depending on slope, then depth, then will combine the two factors to produce an output. 

### Tool 1: "SlopeFactor_1st"
#### Description:
This script takes in a folder of bathymetry tiles in TIF format with z-values as meters. It also takes in a name for the output. As the script runs, it first mosaics the tiles to a new raster using *'arcpy.management.MosaicToNewRaster'*. Note that if the collection of input tiles do not create a perfect rectangle, the mosaic output will fill in the space with pixels equal to 0. Next, it uses *'arcpy.ddd.Slope'* to find the slope for every pixel in the mosaic raster. Then it uses *'arcpy.sa.Reclassify'* to bin slope values into three hazard levels. It gives a moderate hazard and a value of 1 to areas with a slope-grade between 0 and 22.5. It gives a high hazard and a value of 2 to areas with a slope-grade of 22.5 to 45. It gives low risk and a value of 0 to any abrupt slopes with a slope-grade greater than 45.
#### Dialog Instructions:
In **"Bathymetric Tile Folder"** select your folder that contains the your bathymetric raster tile data. The raster tiles must be in TIF format and have z-units in meters.
In **"Reclassed Bathymetric Raster"** type a path for your output reclassified raster. This can be any name you want but it should be a IMG format. This output will be the input for the third tool, being "CombineFactors_Last".

### Tool 2: "DepthFactor_2nd"
#### Description:
This script takes in the same folder as Tool 1 and an output raster-file name similar to Tool 1. As the script runs, it first mosaics the tiles with the same process as Tool 1. Then, it uses *'arcpy.sa.Test'* to make all depth values greater than -100 equal to 1 and all other values equal to 0. In simple terms; This script creates a raster where shallow seafloor and land are represented by values of 1.
#### Dialog Instructions:
In **"Bathymetric Tile Folder"** select your folder that contains the your bathymetric raster tile data. The raster tiles must be in TIF format and have z-units in meters.
In **"Reclassed Bathymetric Raster"** type a path for your output test raster. This can be any name you want but it should be a IMG format. This output will be the input for the third tool, being "CombineFactors_Last".

### Tool 3: "CombineFactor_Last"
#### Description: 
This script takes the output rasters from Tool 1 and Tool 2 and combines them to a final output risk layer. It also takes in a path name for the output raster layer. It uses *'arcpy.sa.Plus'* to combine the two factors into a risk layer. The final layer will have values from 0 to 3.
#### Dialog Instructions:
In **"Input Slope Factor Raster Layer"** select your output from Tool 1. In **"Input Depth Factor Raster Layer"** select your output from Tool 2. In **"Tsunami Runup Risk Raster"** write a path. In **"Bathymetric Tile Folder"** select the folder that you selected in Tool 1.

### Interpretation of Final Output:
The final output will be a raster with values ranging from 0 to 3. Low risk is indicated by 0 and high risk by 3. Pixels do not represent risk to tsunami impact at the pixels location. Instead, this out put should be used with a line drawn from tsunami source to landfall. Then, risk level for the coastline can be evaluated by the values of the output raster that was passed over by the line.
