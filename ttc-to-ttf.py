#!/usr/bin/env python3

from fontTools.ttLib.ttCollection import TTCollection
import os
import sys

filename = sys.argv[1]
ttc = TTCollection(filename)
print(sys.argv[1])
basename = os.path.basename(filename)
for i, font in enumerate(ttc):
    font.save(f"raw/ttf/{font['name'].getBestFullName()}.ttf")