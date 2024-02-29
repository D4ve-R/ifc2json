# IFCJSON_python - ifc2json.py
# Convert IFC SPF file to ifcJSON
# https://github.com/IFCJSON-Team

# MIT License

# Copyright (c) 2020 Jan Brouwer <jan@brewsky.nl>

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from time import perf_counter
import os
import argparse
from ifc2json.convert import ifc2json, json2ifc

def main():
    t1_start = perf_counter()
    parser = argparse.ArgumentParser(
        description='Convert IFC SPF file to ifcJSON')
    parser.add_argument('-i', type=str, help='input ifc file path')
    parser.add_argument('-o', type=str, help='output json file path')
    parser.add_argument(
        '-v', type=str, help='ifcJSON version, options: "4"(default), "5a"')
    parser.add_argument('-c', '--compact', action='store_true',
                        help='Pretty print is turned off and references are created without informative "type" property')
    parser.add_argument('-n', '--no_inverse', action='store_true',
                        help='Inverse relationships will be explicitly added to entities for version 4, default is True')
    parser.add_argument('-e', '--empty_properties', action='store_true',
                        help='Include empty properties, default is False')
    parser.add_argument('-w', '--no_ownerhistory', action='store_true',
                        help='Remove IfcOwnerHistory for version 4, default is False. WARNING: THIS BREAKS THE IFC SCHEMA!')
    parser.add_argument('-g', '--geometry', type=str,
                        help='Set geometry output type: "none", "tessellate", "unchanged"(default) WARNING: SETTING TO NONE MIGHT BREAK THE IFC SCHEMA!')
    # parser.add_argument('NO_GEOMETRY', action='store_true')
    args = parser.parse_args()
    input_path = args.i
    
    if os.path.isfile(input_path):
        if input_path.endswith('.ifc'):
            ifc2json(input_path, args.o, args.v, args.compact, args.no_inverse, args.empty_properties, args.no_ownerhistory, args.geometry)
        else:
            json2ifc(input_path, args.o)

    else:
        print(str(input_path) + ' is not a valid file')
    
    t1_stop = perf_counter()
    print("Conversion took ", t1_stop-t1_start, " seconds")

if __name__ == '__main__':
    main()
