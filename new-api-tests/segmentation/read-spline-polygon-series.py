'''Test reading in an SV contour group .ctgr file for spline polygons.
'''
from pathlib import Path
import sv
import sys
import vtk
sys.path.insert(1, '../graphics/')
import graphics as gr

## Read an SV segmentation group file. 
#
home = str(Path.home())
file_name = "../data/DemoProject/Segmentations/spline-poly.ctgr"
print("Read SV ctgr file: {0:s}".format(file_name))
seg_series = sv.segmentation.Series(file_name)
num_times = seg_series.get_num_times()
print("Number of times: {0:d}".format(num_times))

## Create renderer and graphics window.
win_width = 500
win_height = 500
renderer, renderer_window = gr.init_graphics(win_width, win_height)

## Show contours.
for time in range(num_times):
    num_segs = seg_series.get_num_segmentations(time)
    for sid in range(num_segs):
        print('\n---------- segmentation {0:d} ---------- '.format(sid))
        seg = seg_series.get_segmentation(sid, time)
        ctype = seg.get_type()
        print('Segmentation type: {0:s}'.format(ctype))
        try:
            control_points = seg.get_control_points()
        except:
            print("**** Exception getting control points")
            control_points = []
        print("Number of control points: {0:d}".format(len(control_points)))

        gr.create_segmentation_geometry(renderer, seg)

# Display window.
gr.display(renderer_window)
