from qgis.core import *
import processing
from processing.core.Processing import Processing
Processing.initialize()
project = QgsProject.instance();

src_csv = "./data/dst/REG_PEOPLE_DENSITY_18_LEVEL.csv"
shp_csv = "./data/gwangjin_area/광진구_집계구_2016_면적0.shp"

csvLayer = QgsVectorLayer(src_csv)
shpLayer = QgsVectorLayer(shp_csv)

project.addMapLayer(csvLayer)
project.addMapLayer(shpLayer)
csvField = 'TOT_REG_CD'
shpField = 'TOT_REG_CD'

joinObject = QgsVectorLayerJoinInfo()

joinObject.setJoinFieldName(csvField)
joinObject.setTargetFieldName(shpField)
joinObject.setJoinLayerId(csvLayer.id())
joinObject.setUsingMemoryCache(True)
joinObject.setJoinLayer(csvLayer)
shpLayer.addJoin(joinObject)


res = processing.run("native:refactorfields", {'INPUT':'C:/Users/nijey/Desktop/2022-1/Capstone/cloud_zone/data/join/join.shp','FIELDS_MAPPING':[{'expression': '"TOT_REG_CD"','length': 20,'name': 'TOT_REG_CD','precision': 0,'type': 10},{'expression': '"ADM_NM"','length': 20,'name': 'ADM_NM','precision': 0,'type': 10},{'expression': '"ADM_CD"','length': 7,'name': 'ADM_CD','precision': 0,'type': 10},{'expression': '"area"','length': 10,'name': 'area','precision': 3,'type': 6},{'expression': '"REG_PEOPLE"','length': 10,'name': 'REG_PEOPLE','precision': 0,'type': 2}],'OUTPUT':'./data/res.shp'})




print(type(res))

project.write("./data/dst/shp_csv_join.qgs")
