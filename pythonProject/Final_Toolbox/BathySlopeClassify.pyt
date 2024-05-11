import arcpy


class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "BathySlopeTool"
        self.alias = "Bathymetric Slope Tool"

        # List of tool classes associated with this toolbox
        self.tools = [BSTool]


class BSTool(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "BathymetricSlopeClassifier"
        self.description = "This tool takes in bathymetric raster tiles, mosaics them to a single raster, creates a slope raster, and reclassifies ranges of slope."
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        params = []
        input_folder = arcpy.Parameter(name="input_folder",
                                     displayName="Input tiles",
                                     datatype="DEFolder",
                                     parameterType="Required",  # Required|Optional|Derived
                                     direction="Input",  # Input|Output
                                     )
        input_folder.value = 'C:\Peck_NRS528_PythonGIS\pythonProject\Final_Toolbox\exampleData'  # This is a default value that can be over-ridden in the toolbox
        params.append(input_folder)

        output = arcpy.Parameter(name="bathyGradeClasses.img",
                                 displayName="bathyGradeClasses.img",
                                 datatype="GPRasterLayer",
                                 parameterType="Required",  # Required|Optional|Derived
                                 direction="Output",  # Input|Output
                                 )
        output.value = r"C:\Peck_NRS528_PythonGIS\pythonProject\Final_Toolbox\exampleData\mosaicBathy.img"  # This is a default value that can be over-ridden in the toolbox
        params.append(output)
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        input_folder = parameters[0].valueAsText
        output = parameters[1].valueAsText

        arcpy.env.workspace = input_folder
        workspace = arcpy.env.workspace
        arcpy.env.overwriteOutput = True

        inBathy = []
        rasters = arcpy.ListRasters("*", "TIF")
        for raster in rasters:
            print(raster)
            inBathy.append(raster)
        print(inBathy)

        # Process: Mosaic To New Raster (Mosaic To New Raster) (management)
        mosaic = arcpy.management.MosaicToNewRaster(inBathy, workspace, 'mosaicBathy.img', '', '32_BIT_SIGNED', '', 1,
         'LAST', '')
        mosaic = arcpy.Raster(mosaic)
        print(mosaic)

        # Process: Slope (Slope) (3d)
        slope = arcpy.ddd.Slope('mosaicBathy.img', 'slope.img', 'DEGREE', 1, 'PLANAR', 'METER', 'GPU_THEN_CPU')
        slope = arcpy.Raster(slope)
        print(slope)

        # Process: Reclassify (Reclassify) (3d)
        remap = arcpy.sa.RemapRange([[0, 22.5, 1], [22.5, 45, 2], [45, 90, 0]])
        reclassify = arcpy.sa.Reclassify('slope.img', 'VALUE', remap, 'NODATA')
        reclassify = arcpy.Raster(reclassify)
        reclassify.save(output)
        print(reclassify)

        return

# This code block allows you to run your code in a test-mode within PyCharm, i.e. you do not have to open the tool in
# ArcMap. This works best for a "single tool" within the Toolbox.
def main():
    tool = BSTool()
    tool.execute(tool.getParameterInfo(), None)

if __name__ == '__main__':
    main()