# ESRI's ArcPy geoprocessing python package

For ArcGIS users. Some useful ArcPy scripts for batch applying symbology, definition query and map export.
Especially useful for creating animated maps or videos, when bulk modification and export of large numbers of layers is required.

The script arcpy_batch_map_export.py contains three code blocks:

## 1) apply_symbology=True:

For a given MXD file (in layout mode), and a given .LYR file holding template symbology, the script applies the symbology to all layers in the MXD and saves.

## 2) set_definition_query=True:

Sets an individual definition query for each layer, to only display features with certain attributes.
The queries can be defined in a dictionary, or could be set based on the layer name or similar.

## 3) batch_export=True:

Loops oer the layers, sets each layer to "visible" and exports the map to a .PNG file.

# Example animations created with this script:

## HISDAC-US: Historical settlement data compilation for the United States (https://www.youtube.com/channel/UCYChFz-8stVzTVyqazXbqOQ/)

## "Animating 200 years of urban spatial development in 35 U.S. cities" (https://av.tib.eu/media/48115)

## https://twitter.com/JohannesHUhl1/status/1274000048653660160
