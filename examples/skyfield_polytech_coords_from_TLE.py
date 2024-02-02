from skyfield.api import *

ts = load.timescale()
t = ts.now()

#eph = skyfield.api.load('de421.bsp')
stations_url = 'http://celestrak.org/NORAD/elements/gp.php?INTDES=2023-091'
satellites = load.tle_file(stations_url)
print('Loaded', len(satellites), 'satellites')
by_name = {sat.name: sat for sat in satellites}
satellite = by_name['POLYTECH-UNIVERSE 3 (R*)']
print(satellite)
position = satellite.at(t)
print(f'POLYTECH-UNIVERSE 3 (R*): {position.position.km}')


lat, lon = wgs84.latlon_of(position)
height = wgs84.height_of(position)

print('Latitude:', lat.degrees)
print('Longitude:', lon.degrees)
print('Height:', height.km)

print(f'\nVelocity: {position.speed().km_per_s}')