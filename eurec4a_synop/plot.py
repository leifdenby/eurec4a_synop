import warnings
import datetime
import cartopy.crs as ccrs
import matplotlib.pyplot as plt


def add_synop(ax, date, image_path="../cropped/"):
    if isinstance(date, datetime.datetime):
        warnings.warn(
            "You provided a `datetime` to `add_synop`, but because synoptic"
            " charts are only available at 00:00UTC the nearest time to midnight"
            " will be used"
        )
        date = 
    fn = Path(image_path) / f"{date:%Y%m%d000000}.png"
    im = plt.imread(fn)

    ax.imshow(im, extent=[-100, -10, 0, 35], transform=ccrs.PlateCarree())


def round_time(dt=None, roundTo=60):
   """Round a datetime object to any time lapse in seconds
   dt : datetime.datetime object, default now.
   roundTo : Closest number of seconds to round to, default 1 minute.

   Author: Thierry Husson 2012 - Use it as you want but don't blame me.
   source https://stackoverflow.com/a/10854034/271776
   """
   if dt == None : dt = datetime.datetime.now()
   seconds = (dt.replace(tzinfo=None) - dt.min).seconds
   rounding = (seconds+roundTo/2) // roundTo * roundTo
   return dt + datetime.timedelta(0,rounding-seconds,-dt.microsecond)
