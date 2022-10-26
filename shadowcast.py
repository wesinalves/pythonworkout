import astropy.units as u
from einsteinpy.rays import Shadow
from einsteinpy.plotting import ShadowPlotter
import matplotlib.pyplot as plt

mass = 1 * u.kg
fov = 30 * u.km

shadow = Shadow(mass= mass, fov=fov, n_rays=1000)
obj = ShadowPlotter(shadow=shadow, is_line_plot=True)
obj.plot()
obj.show()

obj = ShadowPlotter(shadow=shadow, is_line_plot=False)
obj.plot()
obj.show()
plt.show()