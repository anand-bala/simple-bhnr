"""
Plot the results of your training.

Many ideas borrowed from https://www.bastibl.net/publication-quality-plots/
"""

import os
import pathlib

import pandas as pd
import numpy as np

import matplotlib as mpl
import matplotlib.pyplot as plt

import logging

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

# mpl.use('pdf')

plt.style.use('seaborn-whitegrid')

plt.rc('font', family='serif', serif='Times')
plt.rc('text', usetex=True)
plt.rc('xtick', labelsize=8)
plt.rc('ytick', labelsize=8)
plt.rc('axes', labelsize=8)

WIDTH = 3.487
HEIGHT = WIDTH / 1.618


def parse_args():
    import argparse
    parser = argparse.ArgumentParser(
        description='Plot results generated by running a safe_rl algorithm',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument('--logdir', help='Path to directory with the logs (if file, will plot single plot)', metavar='LOG_DIRECTORY', nargs='+')
    parser.add_argument('--title', help='Title of plot', default='Training data')
    parser.add_argument('--output', help='Where to store the figure')
    parser.add_argument('--pdf-output', help='Set the output to be a PDF', action='store_true')

    data_g = parser.add_argument_group('Data Processing')
    data_g.add_argument('--smooth-span', help='Smooth span of the Exponential-Mean smoothing window', default=50,
                        type=int)

    plot_g = parser.add_argument_group('Plot options')
    plot_g.add_argument('--name', help='Names of the plots for each log directory', metavar='PLOT_NAME', nargs='+')
    plot_g.add_argument('--col', help='Names of the columns for each plot', metavar='COLS', nargs='*')
    plot_g.add_argument('--plot-cols', help='Specify name of columns to plot for each subplot', metavar='COLS',
                        nargs='*')
    plot_g.add_argument('--subplot-shape', help='Shape of subplots', metavar=('NROWS', 'NCOLS'), nargs=2, type=int)
    plot_g.add_argument('--width', help='Width of 1 subplot', default=WIDTH, type=float)
    plot_g.add_argument('--height', help='Height of 1 subplot', default=HEIGHT, type=float)
    plot_g.add_argument('--sharex', help='Set if subplots share X-axis', action='store_true')
    plot_g.add_argument('--sharey', help='Set if subplots share Y-axis', action='store_true')
    plot_g.add_argument('--subplots-adjust', help='Set margins for figure', metavar=('left', 'bottom', 'right', 'top'),
                        nargs=4, type=float)

    plot_g.add_argument('--confidence-interval', help='Set confidence interval for error margin (percent value)',
                        type=float, default=95)

    plot_g.add_argument('--legend-position', help='Position of legend', nargs='*', default=('upper', 'center'))
    plot_g.add_argument('--legend-ncols', help='Number of columns in legend', default=2, type=int)

    return parser.parse_args()


def load_data(data, cols, smooth_span):
    d = pathlib.Path(data)
    pattern = '*.monitor.csv'
    assert d.exists(), 'Data directory/file does not exist'
    assert d.



if __name__ == '__main__':
    args = parse_args()
