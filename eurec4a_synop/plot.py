import warnings
import datetime as dt
import cartopy.crs as ccrs
import matplotlib.pyplot as plt


def add_synop(ax, date, image_path="../cropped/"):
    if isinstance(date, dt.datetime):
        warnings.warn(
            "You provided a `datetime` to `add_synop`, but because synoptic"
            " charts are only available at 00:00UTC the nearest time to midnight"
            " will be used"
        )
        date = _nearest_midnight(date)
    fn = Path(image_path) / f"{date:%Y%m%d000000}.png"
    im = plt.imread(fn)

    ax.imshow(im, extent=[-100, -10, 0, 35], transform=ccrs.PlateCarree())


def _nearest_midnight(t):
    current = dt.datetime.now()
    current_td = dt.timedelta(
        hours=current.hour,
        minutes=current.minute,
        seconds=current.second,
        microseconds=current.microsecond,
    )

    to_midnight = dt.timedelta(hours=round(current_td.total_seconds() / (60 * 60 * 24)))
    return dt.datetime.combine(current, dt.time(0)) + to_midnight
