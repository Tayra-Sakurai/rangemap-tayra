# SPDX-FileCopyrightText: 2026-present Tayra Sakurai <tayra_sakurai@icloud.com>
#
# SPDX-License-Identifier: AGPL-3.0-or-later
"""The mapping module."""
import folium
import requests
from typing import overload, Sequence

__all__ = [
    'DataMap',
    'load_data',
    'map_circle',
    'save_map',
]


def _load_name(name: str) -> tuple[float, float]:
    """Loads the place name.

    Parameters
    ----------
    name : str
        The place name.

    Returns
    -------
    latitude : float
        The latitude.
    longitude : float
        The longitude.

    Notes
    -----
    This function uses the Nominatim API.
    """
    endpoint = "https://nominatim.openstreetmap.org/search"
    jsoncontent = requests.get(
        endpoint,
        {
            'q': name,
            'format': 'jsonv2',
        },
        headers={
            'User-Agent': 'RangeMap-Tayra',
        }
    )
    print(jsoncontent.text)
    json = jsoncontent.json()
    return float(json[0]['lat']), float(json[0]['lon'])


class DataMap:
    """The data to be mapped.

    Parameters
    ----------
    name : str, optional
        The name of the place.
    latitude, longitude : float, optional
        The coordinate of the place.
    range : float
        The range to be mapped in km.
    """
    @overload
    def __init__(
        self,
        range: float,
        name: str
    ) -> None:
        pass

    @overload
    def __init__(
        self,
        range: float,
        name: None,
        latitude: float,
        longitude: float
    ) -> None:
        pass

    def __init__(
        self,
        range: float,
        name: str | None = None,
        latitude: float | None = None,
        longitude: float | None = None
    ) -> None:
        self.name = name
        self.range = range
        if (latitude is not None) and (longitude is not None):
            self.latitude = latitude
            self.longitude = longitude
        elif name is not None:
            self.latitude, self.longitude = _load_name(name)


def load_data(
    nameorcoord: str | Sequence[float],
    range: float
) -> DataMap:
    """Loads the data from the parameter.

    Parameters
    ----------
    nameorcoord : str or Sequence[float]
        The name of the place or coordinate.
    range : float
        The range. In kilometers.

    Returns
    -------
    data : DataMap
        The mapping data.
    """
    if isinstance(nameorcoord, str):
        return DataMap(range, nameorcoord)
    else:
        return DataMap(range, None, nameorcoord[0], nameorcoord[1])


def map_circle(data: DataMap) -> folium.Map:
    """Makes a map with a pin and a circle.

    Parameters
    ----------
    data : DataMap
        The data.

    Returns
    -------
    m : Map
        The map.

    Notes
    -----
    This function uses the folium API.

    Examples
    --------
    First and clear example:

    >>> from rangemap_tayra import load_data, map_circle
    >>> data = load_data('Pyongyang', 500.)
    >>> map_circle(data)
    Map[...]
    """
    m = folium.Map(
        location=(data.latitude, data.longitude),
        zoom_start=4
    )
    folium.Marker(
        (data.latitude, data.longitude,),
        data.name or 'A place',
        icon=folium.Icon(color='red')
    ).add_to(m)
    folium.Circle(
        location=(data.latitude, data.longitude,),
        radius=data.range * 1000,
        fill=True,
        color='red',
        fill_color='red',
        fill_opacity=0.15
    ).add_to(m)
    return m


def save_map(
    fpath: str,
    m: folium.Map
) -> None:
    """Saves the map data as html.

    Parameters
    ----------
    fpath : StrPath
        The path to the saving file.
    m : Map
        The map.
    """
    m.save(
        fpath
    )
