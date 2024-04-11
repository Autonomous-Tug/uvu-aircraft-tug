import sys
import pyzed.sl as sl
import time

#Set configuration parameters
init_params = sl.InitParameters()
init_params.camera_resolution = sl.RESOLUTION.HD720 # Use HD720 video mode (default fps: 60)
init_params.coordinate_system = sl.COORDINATE_SYSTEM.RIGHT_HANDED_Y_UP # Use a right-handed Y-up coordinate system
init_params.coordinate_units = sl.UNIT.METER # Set units in meters
init_params.depth_maximum_distance = 10.0


mapping_parameters = sl.SpatialMappingParameters()
mapping_parameters.resolution_meter = mapping_parameters.get_resolution_preset(sl.MAPPING_RESOLUTION.LOW) # Or use preset
mapping_parameters.range_meter = mapping_parameters.get_range_preset(sl.MAPPING_RANGE.MEDIUM) # Preset MEDIUM is set to 5m
mapping_parameters.map_type = sl.SPATIAL_MAP_TYPE.MESH # uncomment below if wanting to use point cloud data. 
# mapping_parameters.map_type = sl.SPATIAL_MAP_TYPE.FUSED_POINT_CLOUD 
zed = sl.Camera()
status = zed.open(init_params)
if status != sl.ERROR_CODE.SUCCESS:
    print("Camera Open : "+repr(status)+". Exit program.")
    exit()
print("Hello My Zeddy bear!!")