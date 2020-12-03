import numpy as np

def model_grid_xy(easting_boundary_i, easting_boundary_f, grid_size_x, northing_boundary_i, northing_boundary_f, grid_size_y):
    x1 = np.arange(easting_boundary_i, easting_boundary_f, grid_size_x)
    x2 = np.arange(easting_boundary_i + grid_size_x, easting_boundary_f + grid_size_x, grid_size_x)

    n_x = len(x1)
    n_y = len(np.arange(northing_boundary_i, northing_boundary_f, grid_size_y))

    model_grid = np.zeros((8, n_x * n_y))
    model_grid[0, :] = np.tile(x1, n_y)
    model_grid[1, :] = np.tile(x2, n_y)
    model_grid[2, :] = np.tile(x2, n_y)
    model_grid[3, :] = np.tile(x1, n_y)

    minyp = northing_boundary_i
    for i in range(n_y):
        model_grid[4, i * n_x:(i + 1) * n_x] = minyp
        model_grid[6, i * n_x:(i + 1) * n_x] = minyp + grid_size_y
        minyp = minyp + grid_size_y
    model_grid[5, :] = model_grid[4, :]
    model_grid[7, :] = model_grid[6, :]

    x_grid = np.array(
        [easting_boundary_i, easting_boundary_i, easting_boundary_f, easting_boundary_f, easting_boundary_i])
    y_grid = np.array(
        [northing_boundary_i, northing_boundary_f, northing_boundary_f, northing_boundary_i, northing_boundary_i])

    return model_grid


def model_grid_xz(easting_boundary_i, easting_boundary_f, grid_size_x, depth_boundary_i, depth_boundary_f, grid_size_z):
    x1 = np.arange(easting_boundary_i, easting_boundary_f, grid_size_x)
    x2 = np.arange(easting_boundary_i + grid_size_x, easting_boundary_f + grid_size_x, grid_size_x)
    x4 = x1
    x3 = x2

    n_x = len(x1)
    n_z = len(np.arange(depth_boundary_i, depth_boundary_f, grid_size_z))

    model_grid = np.zeros((8, n_x * n_z))
    model_grid[0, :] = np.tile(x1, n_z)
    model_grid[1, :] = np.tile(x2, n_z)
    model_grid[2, :] = np.tile(x2, n_z)
    model_grid[3, :] = np.tile(x1, n_z)

    minzp = depth_boundary_i
    for i in range(n_z):
        model_grid[4, i * n_x:(i + 1) * n_x] = minzp
        model_grid[6, i * n_x:(i + 1) * n_x] = minzp + grid_size_z
        minzp = minzp + grid_size_z
    model_grid[5, :] = model_grid[4, :]
    model_grid[7, :] = model_grid[6, :]

    x_grid = np.array(
        [(easting_boundary_i), (easting_boundary_i), (easting_boundary_f), (easting_boundary_f), (easting_boundary_i)])
    z_grid = np.array(
        [(depth_boundary_i), (depth_boundary_f), (depth_boundary_f), (depth_boundary_i), (depth_boundary_i)])

    return model_grid


def model_grid_yz(northing_boundary_i, northing_boundary_f, grid_size_y, depth_boundary_i, depth_boundary_f, grid_size_z):
    y1 = np.arange(northing_boundary_i, northing_boundary_f, grid_size_y)
    y2 = np.arange(northing_boundary_i + grid_size_y, northing_boundary_f + grid_size_y, grid_size_y)
    y4 = y1
    y3 = y2

    n_y = len(y1)
    n_z = len(np.arange(depth_boundary_i, depth_boundary_f, grid_size_z))

    model_grid = np.zeros((8, n_y * n_z))
    model_grid[0, :] = np.tile(y1, n_z)
    model_grid[1, :] = np.tile(y2, n_z)
    model_grid[2, :] = np.tile(y2, n_z)
    model_grid[3, :] = np.tile(y1, n_z)

    minzp = depth_boundary_i
    for i in range(n_z):
        model_grid[4, i * n_y:(i + 1) * n_y] = minzp
        model_grid[6, i * n_y:(i + 1) * n_y] = minzp + grid_size_z
        minzp = minzp + grid_size_z
    model_grid[5, :] = model_grid[4, :]
    model_grid[7, :] = model_grid[6, :]

    y_grid = np.array([(northing_boundary_i), (northing_boundary_i), (northing_boundary_f), (northing_boundary_f),
                       (northing_boundary_i)])
    z_grid = np.array(
        [(depth_boundary_i), (depth_boundary_f), (depth_boundary_f), (depth_boundary_i), (depth_boundary_i)])

    return model_grid
