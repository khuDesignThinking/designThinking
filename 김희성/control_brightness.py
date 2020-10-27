"""
2020/10/27
HeeSung Kim
This module control brightness of window

!!CAUTION!!
before start, go termial and load
pip install wmi
"""

import wmi
brightness = 100
wmi.WMI(namespace='wmi').WmiMonitorBrightnessMethods()[0].WmiSetBrightness(brightness, 0)
