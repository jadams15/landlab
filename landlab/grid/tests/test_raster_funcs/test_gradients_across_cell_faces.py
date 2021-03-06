import numpy as np
from numpy.testing import assert_array_equal
from nose import with_setup
from nose.tools import assert_equal
try:
    from nose.tools import assert_is
except ImportError:
    from landlab.testing.tools import assert_is

from landlab.grid import raster_funcs as rfuncs


def setup_unit_grid():
    from landlab import RasterModelGrid
    globals().update({
        'rmg': RasterModelGrid(4, 5),
        'values_at_nodes':  np.arange(20.),
    })


def setup_grid():
    from landlab import RasterModelGrid
    globals().update({
        'rmg': RasterModelGrid(4, 5, 2.),
        'values_at_nodes':  np.arange(20.),
    })


@with_setup(setup_unit_grid)
def test_scalar_arg():
    grads = rfuncs.calculate_gradient_across_cell_faces(
        rmg, values_at_nodes, 0)
    assert_array_equal(grads, np.array([[1., 5., -1., -5.]]))


@with_setup(setup_unit_grid)
def test_iterable():
    grads = rmg.calculate_gradient_across_cell_faces(values_at_nodes, [0, 4])
    assert_array_equal(grads, np.array([[1., 5., -1., -5.],
                                        [1., 5., -1., -5.]]))


@with_setup(setup_unit_grid)
def test_with_no_cell_id_arg():
    values = np.array([0, 1,  3, 6, 10,
                       0, 1,  3, 6, 10,
                       0, 1,  3, 5, 10,
                       0, 1, -3, 6, 10], dtype=float)
    grads = rmg.calculate_gradient_across_cell_faces(values)

    assert_array_equal(grads, np.array([
        [2., 0., -1., 0.], [3.,  0., -2., 0.], [4., -1., -3., 0.],
        [2., 0., -1., 0.], [2., -6., -2., 0.], [5.,  1., -2., 1.]]))


@with_setup(setup_unit_grid)
def test_with_out_keyword():
    out = np.empty((1, 4))
    rtn = rmg.calculate_gradient_across_cell_faces(values_at_nodes, 5, out=out)
    assert_is(rtn, out)
    assert_array_equal(out, np.array([[1., 5., -1., -5.]]))
