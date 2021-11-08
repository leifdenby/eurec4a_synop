import eurec4a_synop

import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import datetime


def test_version():
    assert eurec4a_synop.__version__ == "0.1.0"
