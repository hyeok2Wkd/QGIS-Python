import sys
import os
import qgis

from qgis.core import *
from qgis.gui import *

path_to_layer = "C:/Users/SAMSUNG/OneDrive/바탕 화면/캡스톤5.9~/test/data/광진구/광진구_SIG.shp"

vlayer = QgsVectorLayer(path_to_layer)

if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    print("")
    print("로드 성공")


print("")
print("개발환경 구축 성공")