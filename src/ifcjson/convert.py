import json
import ifcjson

def json2ifc(jsonFilePath, ifcFilePath):
    ifc_json = ifcjson.JSON2IFC(jsonFilePath)
    ifc_model = ifc_json.ifcModel()
    ifc_model.write(ifcFilePath)
    return ifc_model

def ifc2json(
        ifcFilePath,
        jsonFilePath,
        version=None,
        compact=False,
        no_inverse=False,
        empty_properties=False,
        no_ownerhistory=False,
        geometry="unchanged",
        indent=2,
    ):
    if compact: indent = None

    if not geometry or geometry == "none":
        GEOMETRY = False
    elif geometry == "tessellate":
        GEOMETRY = "tessellate"
    else:
        GEOMETRY = True

    if not version or version == "4":
        jsonData = ifcjson.IFC2JSON4(ifcFilePath,
                                     compact,
                                     NO_INVERSE=no_inverse,
                                     EMPTY_PROPERTIES=empty_properties,
                                     NO_OWNERHISTORY=no_ownerhistory,
                                     GEOMETRY=GEOMETRY
                                     ).spf2Json()
        with open(jsonFilePath, 'w') as outfile:
            json.dump(jsonData, outfile, indent=indent)
    elif version == "5a":
        jsonData = ifcjson.IFC2JSON5a(ifcFilePath,
                                      compact,
                                      EMPTY_PROPERTIES=empty_properties
                                      ).spf2Json()
        with open(jsonFilePath, 'w') as outfile:
            json.dump(jsonData, outfile, indent=indent)
    else:
        print(f"Version {version} is not supported")
