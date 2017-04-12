Demo to show parallelization using `joblib` and `gridmap`.

#### Setting up the environment

To install all necessary dependencies, run:
`/path/to/miniconda/bin/conda-env create -f environment.yml`

To activate the environment, run:
`source /path/to/miniconda/bin/activate demo`

#### Running jobs in parallel locally

Use the `tmux` command to start a new session. You can split a horizontal pane using `Ctrl-B %`, a vertical pane using `Ctrl-B "`, and switch between panes using `Ctrl-B o`. Create a separate pane and run `htop` to observe running processes. Switching to the original pane, run:

`python gridmap_demo.py`

To use `gridmap` for parallelization, or 

`python joblib_demo.py`

To use `joblib`. When you start the demo, you should see additional CPUs being used in `htop`. The demos work by generating a random sequence of values and splitting the values across jobs, each of which computes the sum and count of the values assigned to it. These numbers are then aggregated to compute the mean of the values. You can edit the number of jobs and number of random value generated using the command-line arguments `--njobs=<njobs>` and `--N=<N>`, respectively.

#### Running jobs in parallel using SGE

For `gridmap_demo.py`, you can also use the command-line argument `--sge` to run jobs in parallel using Sun Grid Engine (SGE). This distributes jobs across multiple machines (if available) using a scheduler, rather than running processes just on the machine you're SSH'ed into. To observe jobs being queued, running, and finishing, open a separate pane in `tmux` and run

`watch -n 1 qstat`

To delete a job if it hangs, run

`qdel <jobid>`

Where the `<jobid>` for each job is printed by `qstat`.