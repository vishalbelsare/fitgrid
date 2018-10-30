import pandas as pd
import re
import sys

from .context import fitgrid
from fitgrid import tools


def test_duplicate_index_printer():

    df = pd.DataFrame(
        {'a': [1, 2, 3, 4, 5], 'b': [1, 1, 2, 3, 2], 'c': [0, 1, 2, 3, 4]}
    )

    single_level_df = df.set_index('b')

    table = tools.get_index_duplicates_table(single_level_df, 'b')

    assert re.search(r'1\s+0, 1\n', table) is not None
    assert re.search(r'2\s+2, 4\n', table) is not None


def test_blas_getter():

    assert sys.platform.startswith('linux')

    import numpy

    blas = tools.get_blas_library(numpy)

    blas.set_n_threads(4)
    assert blas.get_n_threads() == 4

    blas.set_n_threads(2)
    assert blas.get_n_threads() == 2
