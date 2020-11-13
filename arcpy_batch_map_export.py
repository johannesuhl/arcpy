# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 04:32:25 2020

@author: Johannes H. Uhl, Department of Geography, University of Colorado Boulder.
"""

import arcpy,os,sys
import numpy as np
from arcpy.mapping import *
arcpy.env.overwriteOutput=1

### run in shell: C:\Python27\ArcGIS10.8\python.exe arcpy_batch_map_export.py

#####################################################################
inmxd = 'test_mxd.mxd' ### MXD needs to be in layout mode
template_symbology_lyr = 'template.lyr' ### path to layer file with template symbology
plot_dir = './plots' ### plot directory
apply_symbology=False
set_definition_query=False
batch_export=True
#####################################################################

mxd = arcpy.mapping.MapDocument(inmxd)  
    
if apply_symbology: #####################################################################

    for df in arcpy.mapping.ListDataFrames(mxd, ''):
        mxd.activeView = df    
        for lyr in arcpy.mapping.ListLayers(mxd, '', df):
            arcpy.ApplySymbologyFromLayer_management(lyr, template_symbology_lyr) 
            print 'applied symbology %s %s' %(df.name,lyr)        
        arcpy.RefreshActiveView()
        arcpy.RefreshTOC()
        
    mxd.save()

if set_definition_query: #####################################################################
       
    query_dict={'layer1':'library',
                'layer2':'fast_food',
                'layer3':'pharmacy'
                }
    
    for df in arcpy.mapping.ListDataFrames(mxd, ''):
        for lyr in arcpy.mapping.ListLayers(mxd, '', df):
            lyr.definitionQuery = """amenity = '%s'""" %query_dict[lyr.name] ### gdb feature class
            #lyr.definitionQuery = """"amenity" = '%s'""" %query_dict[lyr.name] ### shapefile
            print 'set definition query %s %s' %(df.name,lyr)        
        
        arcpy.RefreshActiveView()
        arcpy.RefreshTOC()                
                
    mxd.save()


if batch_export: #####################################################################   
    
    for df in arcpy.mapping.ListDataFrames(mxd, ''):
        #Turn off all lyrs in list
        for lyr in arcpy.mapping.ListLayers(mxd, '', df):
            lyr.visible = False
        
        for lyr in arcpy.mapping.ListLayers(mxd, '', df):             
            lyr.visible = True
            arcpy.RefreshActiveView()
            outfilename = plot_dir+os.sep+'%s.png' %lyr.name
            arcpy.mapping.ExportToPNG(mxd, outfilename, df_export_width=4700, df_export_height=3311)
            print('exported %s' %lyr.name)
            lyr.visible = False