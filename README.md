# IFC2JSON
Python converter from IFC SPF to JSON

**Original code taken from https://github.com/buildingSMART/ifcJSON** 

# Getting Started

## Requirements
- ifcopenshell (using conda or in folder ./ifcopenshell)
- pandas

## Install
```bash
pip install ifcjson
```

## Usage
Run converter:
```bash
# ifc to json
python -m ifcjson -i model.ifc -o model.json --compact
# or json to ifc
python -m ifcjson -i model.json -o model.ifc
```
```
usage: ifc2json.py [-h] [-i I] [-o O] [-v V] [-c] [-n] [-e] [-w] [-g GEOMETRY]

Convert IFC SPF file to ifcJSON

optional arguments:
  -h, --help            show this help message and exit
  -i I                  input file path
  -o O                  output file path
  -v V                  ifcJSON version, options: "4"(default), "5a"
  -c, --compact         Pretty print is turned off and references are created without informative "type" property
  -n, --no_inverse      Inverse relationships will be explicitly added to entities for version 4, default is True
  -e, --empty_properties
                        Include empty properties, default is False
  -w, --no_ownerhistory
                        Remove IfcOwnerHistory for version 4, default is False. WARNING: THIS BREAKS THE IFC SCHEMA!
  -g GEOMETRY, --geometry GEOMETRY
                        Set geometry output type: "none", "tessellate", "unchanged"(default) WARNING: SETTING TO NONE MIGHT BREAK THE IFC
                        SCHEMA!
```