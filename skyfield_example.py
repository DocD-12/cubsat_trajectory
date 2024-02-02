from skyfield.api import *

ts = load.timescale()

t = ts.now()
t = ts.utc(2024, 2, 2, 11, 48)
#eph = skyfield.api.load('de421.bsp')
stations_url = 'http://celestrak.org/NORAD/elements/stations.txt'
satellites = load.tle_file(stations_url)
print('Loaded', len(satellites), 'satellites')
by_name = {sat.name: sat for sat in satellites}
satellite = by_name['ISS (ZARYA)']
print(satellite)
position = satellite.at(t)
print(f'ISS (ZARYA): {position.position.km}')


lat, lon = wgs84.latlon_of(position)
height = wgs84.height_of(position)

print('Latitude:', lat)
print('Longitude:', lon)
print('Height:', height.km)
