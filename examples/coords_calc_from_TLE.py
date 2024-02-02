import ephem
import datetime
## [...]

name = "ISS (ZARYA)"
line1 = "1 25544U 98067A   24033.14127905  .00013172  00000-0  24312-3 0  9990"
line2 = "2 25544  51.6421 269.5100 0002368 186.5110 324.3032 15.49436537437452"

tle_rec = ephem.readtle(name, line1, line2)
tle_rec.compute()

print(tle_rec.sublong, tle_rec.sublat)
