import arcpy


class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Python Toolbox"
        self.alias = ""

        # List of tool classes associated with this toolbox
        self.tools = [HelloWorld]


class HelloWorld(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "HelloWorld Tool"
        self.description = ""
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        params = []
        input_string = arcpy.Parameter(name="input_string",
                                       displayName="Add your name here",
                                       parameterType="Required",
                                       direction="Input",
                                       )
        params.append(input_string)
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
        input_string = parameters[0].valueAsText
        arcpy.AddMessage("Your name is: " + str(input_string))
        return