from qgis.core import *
from qgis.core import QgsVectorLayer
from PyQt5.QtWidgets import QDialog

GUIEnabled=True
app = QgsApplication([], GUIEnabled)


# dlg = QDialog()
# dlg.exec_()
#
# app.exit(app.exec_())

from qgis.PyQt.QtGui import (
    QColor,
)

# from qgis.PyQt.QtCore import Qt, QRectF
#
# from qgis.core import (
#     QgsVectorLayer,
#     QgsApplication,
#     QgsPoint,
#     QgsPointXY,
#     QgsProject,
#     QgsGeometry,
#     QgsMapRendererJob,
# )
#
# from qgis.gui import (
#     QgsMapCanvas,
#     QgsVertexMarker,
#     QgsMapCanvasItem,
#     QgsRubberBand,
# )
#
# from qgis import *
#
# GUIEnabled=True
# app = QgsApplication([], GUIEnabled)
#
# canvas = QgsMapCanvas()
#
#
# canvas.setCanvasColor(Qt.white)
# canvas.enableAntiAliasing(True)
#
#
# # get the path to the shapefile e.g. /home/project/data/ports.shp
# path_to_airports_layer = "C:\capstone\광진구_음식점_영업만_5181.shp"
#
# # The format is:
# # vlayer = QgsVectorLayer(data_source, layer_name, provider_name)
#
# vlayer = QgsVectorLayer(path_to_airports_layer, "Airports layer", "ogr")
# if not vlayer.isValid():
#     print("Layer failed to load!")
# else:
#     QgsProject.instance().addMapLayer(vlayer)
#
# canvas.show()

