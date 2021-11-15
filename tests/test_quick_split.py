from toolbox.quick_split import ml_split
import numpy as np

def test_quick_split():
    X, y = np.arange(10).reshape((5, 2)), range(5)
    assert len(ml_split(X, y)) == 4
