import arcpy


class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "TsunamiRunupTool"
        self.alias = "Bathymetric Tsunami Runup Tool"

        # List of tool classes associated with this toolbox
        self.tools = [SlopeFactor, DepthFactor, Combine]

class SlopeFactor(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "SlopeFactor_1st"
        self.description = "This tool takes in bathymetric raster tiles, mosaics them to a single raster, creates a slope raster, and reclassifies ranges of slope."
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        params = []
        input_folder = arcpy.Parameter(name="input_folder",
                                     displayName="Bathymetric Tile Folder",
                                     datatype="DEFolder",
                                     parameterType="Required",  # Required|Optional|Derived
                                     direction="Input",  # Input|Output
                                     )
        input_folder.value = 'exampleData'  # This is a default value that can be over-ridden in the toolbox
        params.append(input_folder)

        output = arcpy.Parameter(name="bathyGradeClasses",
                                 displayName="Reclassed Bathymetric Raster",
                                 datatype="GPRasterLayer",
                                 parameterType="Required",  # Required|Optional|Derived
                                 direction="Output",  # Input|Output
                                 )
        output.value = 'SlopeFactor.img'  # This is a default value that can be over-ridden in the toolbox
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
            arcpy.AddMessage('Adding raster tile: ' + str(raster))
            inBathy.append(raster)
        arcpy.AddMessage('Added all raster tiles: ' + str(inBathy))

        # Process: Mosaic To New Raster (Mosaic To New Raster) (management)
        mosaic = arcpy.management.MosaicToNewRaster(inBathy, workspace, 'mosaicBathy.img', '', '32_BIT_SIGNED', '', 1,
         'LAST', '')
        mosaic = arcpy.Raster(mosaic)
        arcpy.AddMessage('Created mosaic raster: ' + str(mosaic))

        # Process: Slope (Slope) (3d)
        slope = arcpy.ddd.Slope('mosaicBathy.img', 'slope.img', 'DEGREE', 1, 'PLANAR', 'METER', 'GPU_THEN_CPU')
        slope = arcpy.Raster(slope)
        arcpy.AddMessage('Created slope raster: ' + str(slope))

        # Process: Reclassify (Reclassify) (3d)
        remap = arcpy.sa.RemapRange([[0, 22.5, 1], [22.5, 45, 2], [45, 90, 0]])
        reclassify = arcpy.sa.Reclassify('slope.img', 'VALUE', remap, 'NODATA')
        reclassify = arcpy.Raster(reclassify)
        reclassify.save(output)
        arcpy.AddMessage('Created tsunami runnup risk zones by slope: ' + str(reclassify))

        arcpy.AddMessage('Complete')

        return

class DepthFactor(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "DepthFactor_2nd"
        self.description = "This tool takes in bathymetric raster tiles, mosaics them to a single raster, and tests for depth."
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        params = []
        input_folder = arcpy.Parameter(name="input_folder",
                                     displayName="Bathymetric Tile Folder",
                                     datatype="DEFolder",
                                     parameterType="Required",  # Required|Optional|Derived
                                     direction="Input",  # Input|Output
                                     )
        input_folder.value = 'exampleData'  # This is a default value that can be over-ridden in the toolbox
        params.append(input_folder)

        output = arcpy.Parameter(name="bathyDepth",
                                 displayName=" Bathymetric Depth Raster",
                                 datatype="GPRasterLayer",
                                 parameterType="Required",  # Required|Optional|Derived
                                 direction="Output",  # Input|Output
                                 )
        output.value = 'DepthFactor.img'  # This is a default value that can be over-ridden in the toolbox
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
            arcpy.AddMessage('Adding raster tile: ' + str(raster))
            inBathy.append(raster)
        arcpy.AddMessage('Added all raster tiles: ' + str(inBathy))

        # Process: Mosaic To New Raster (Mosaic To New Raster) (management)
        mosaic = arcpy.management.MosaicToNewRaster(inBathy, workspace, 'mosaicBathy.img', '', '32_BIT_SIGNED', '', 1,
         'LAST', '')
        mosaic = arcpy.Raster(mosaic)
        arcpy.AddMessage('Created mosaic raster: ' + str(mosaic))

        # Process: Test (Spatial Analyst)
        depthTest = arcpy.sa.Test('mosaicBathy.img', "Value >= -100")
        depthTest = arcpy.Raster(depthTest)
        depthTest.save(output)

        arcpy.AddMessage('Created tsunami runup risk zones by depth: ' + str(output))

        arcpy.AddMessage('Complete')

        return

class Combine(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "CombineFactors_Last"
        self.description = "This tool takes in the slope and depth factors and adds them together."
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        params = []
        input_SlopeFactor = arcpy.Parameter(name="input_SlopeFactor",
                                     displayName="Input Slope Factor Raster Layer",
                                     datatype="GPRasterLayer",
                                     parameterType="Required",  # Required|Optional|Derived
                                     direction="Input",  # Input|Output
                                     )
        input_SlopeFactor.value = 'SlopeFactor.img'  # This is a default value that can be over-ridden in the toolbox
        params.append(input_SlopeFactor)

        input_DepthFactor = arcpy.Parameter(name="input_DepthFactor",
                                            displayName="Input Depth Factor Raster Layer",
                                            datatype="GPRasterLayer",
                                            parameterType="Required",  # Required|Optional|Derived
                                            direction="Input",  # Input|Output
                                            )
        input_DepthFactor.value = 'DepthFactor.img'  # This is a default value that can be over-ridden in the toolbox
        params.append(input_DepthFactor)

        output = arcpy.Parameter(name="TsunamiRunupRisk",
                                 displayName="Tsunami Runup Risk Raster",
                                 datatype="GPRasterLayer",
                                 parameterType="Required",  # Required|Optional|Derived
                                 direction="Output",  # Input|Output
                                 )
        output.value = 'TsunamiRunupRisk.img'  # This is a default value that can be over-ridden in the toolbox
        params.append(output)

        input_folder = arcpy.Parameter(name="input_folder",
                                     displayName="Bathymetric Tile Folder",
                                     datatype="DEFolder",
                                     parameterType="Required",  # Required|Optional|Derived
                                     direction="Input",  # Input|Output
                                     )
        input_folder.value = 'exampleData'  # This is a default value that can be over-ridden in the toolbox
        params.append(input_folder)

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
        input_SlopeFactor = parameters[0].valueAsText
        input_DepthFactor = parameters[1].valueAsText
        output = parameters[2].valueAsText
        input_folder = parameters[3].valueAsText

        arcpy.env.workspace = input_folder
        workspace = arcpy.env.workspace
        arcpy.env.overwriteOutput = True

        combineFactors = arcpy.sa.Plus(input_SlopeFactor, input_DepthFactor)
        combineFactors = arcpy.Raster(combineFactors)
        combineFactors.save(output)

        arcpy.AddMessage('Created the combined factors layer: ' + str(output))

        return