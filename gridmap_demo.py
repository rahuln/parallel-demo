""" gridmap_demo.py

    Usage: gridmap_demo.py [--N=<N>] [--njobs=<njobs>] [--sge]

    Options:
      --help            Show this screen
      --N=<N>           Number of random values to generate [default: 100000000]
      --njobs=<njobs>   Number of jobs to use [default: 4]
      --sge             Whether or not to use SGE
"""

from __future__ import division, print_function

import numpy as np
from gridmap import Job, process_jobs
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
    sge = args['--sge']

    print('generating random values...')
    X = np.random.randn(N)

    print('running jobs...')
    step = int(np.ceil(N / njobs))
    jobs = [ Job(worker, [X[i:i+step]], queue='all.q') for i in xrange(0, N, step) ]
    output = process_jobs(jobs, local=(not sge),
        max_processes=njobs, temp_dir='./logging')

    sums, counts = zip(*output)
    print('mean(X):', np.sum(sums) / np.sum(counts))

