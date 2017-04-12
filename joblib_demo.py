""" joblib_demo.py

    Usage: joblib_demo.py [--N=<N>] [--njobs=<njobs>]

    Options:
      --help            Show this screen
      --N=<N>           Number of random values to generate [default: 100000000]
      --njobs=<njobs>   Number of jobs to use [default: 4]
"""

from __future__ import division, print_function

import numpy as np
from joblib import Parallel, delayed
import time

def worker(x):
    sum, count = 0, 0
    for i in xrange(len(x)):
        sum += x[i]
        count += 1
    time.sleep(10 * np.random.rand())
    print('job finished, sum = %.2f, count = %d' % (sum, count))
    return sum, count

if __name__ == '__main__':

    from docopt import docopt
    args = docopt(__doc__)

    N = int(args['--N'])
    njobs = int(args['--njobs'])

    print('generating random values...')
    X = np.random.randn(N) + 5

    print('running jobs...')
    step = int(np.ceil(N / njobs))
    output = Parallel(n_jobs=njobs)(
                 delayed(worker)(X[i:i+step])
             for i in xrange(0, N, step))

    sums, counts = zip(*output)
    print('mean(X):', np.sum(sums) / np.sum(counts))

