from skyfield.api import load

ts = load.timescale()
t = ts.utc(2024, 2, 2, 14, 30)
eph = load('de421.bsp')
earth, mars = eph['earth'], eph['mars']
position = earth.at(t).observe(mars)

# Producing coordinates.

print('Cartesian ICRS:')

x, y, z = position.xyz.au

print('  x = {:.3f} au'.format(x))
print('  y = {:.3f} au'.format(y))
print('  z = {:.3f} au'.format(z))
print()

print('Spherical ICRS:')

ra, dec, distance = position.radec()

print(' ', ra, 'right ascension')
print(' ', dec, 'declination')
print(' ', distance, 'distance')