import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

def plot_epicenter(self, coor='utm'):
    """
    plotting earthquake distributions (epicenters)

    :param catalog (dataframe): seismic catalog containing earthquake locations (x,y,z) and magnitudes (m)
    :param coor (str): coordinate system, it is only used for labelling x and y axes.
    options are 'lon/lat' or 'utm'.
    :return: none
    """

    x = self.x
    y = self.y
    z = self.z
    m = self.magnitude

    fig = plt.figure()
    ax = fig.add_subplot(111)
    norm = cm.colors.Normalize(vmin=min(z), vmax=max(z))
    cmap = cm.Oranges

    ax.scatter(x, y, c=z, cmap=cmap, edgecolors='k', s=m**3.5, alpha=0.8)
    fig.colorbar(cm.ScalarMappable(cmap=cmap, norm=norm), ax=ax, label='Depth')
    ax.set_title('Earthquake Distributions')
    if coor == 'lon/lat':
        ax.set_xlabel('Longitude')
        ax.set_ylabel('Latitude')
    elif coor == 'utm':
        ax.set_xlabel('Easting')
        ax.set_ylabel('Northing')



def model_grid_xy(self, grid_size):
    x1 = np.arange(min(self.x), max(self.x), grid_size[0])
    x2 = np.arange(min(self.x) + grid_size[0], max(self.x) + grid_size[0], grid_size[0])

    n_x = len(x1)
    n_y = len(np.arange(min(self.y), max(self.y), grid_size[1]))

    model_grid = np.zeros((8, n_x * n_y))
    model_grid[0, :] = np.tile(x1, n_y)
    model_grid[1, :] = np.tile(x2, n_y)
    model_grid[2, :] = np.tile(x2, n_y)
    model_grid[3, :] = np.tile(x1, n_y)

    minyp = min(self.y)
    for i in range(n_y):
        model_grid[4, i * n_x:(i + 1) * n_x] = minyp
        model_grid[6, i * n_x:(i + 1) * n_x] = minyp + grid_size[1]
        minyp = minyp + grid_size[1]
    model_grid[5, :] = model_grid[4, :]
    model_grid[7, :] = model_grid[6, :]

    x_grid = np.array(
        [min(self.x), min(self.x), max(self.x), max(self.x), min(self.x)])
    y_grid = np.array(
        [min(self.y), max(self.y), max(self.y), min(self.y), min(self.y)])

    return model_grid