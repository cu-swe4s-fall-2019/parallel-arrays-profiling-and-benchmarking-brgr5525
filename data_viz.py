"""Various methods for data visualization

    * boxplot - creates a boxplot from data and saves to file
    * histogram - creates a histogram from data and saves to file
    * combo - creates a boxplot and histogram from data, saves to file
"""
import sys
import os.path
from os import path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def boxplot(L, out_file_name, title, x_label, y_label, tick_labels):
    """Create boxplot from given data and save to designated file

    Parameters
    __________
    L : array of ints and floats
        Array containing data whose boxplot is desired.
    out_file_name : string
        Name of file where figured is to be saved.
    title : string
        Title of Boxplot
    x_label : string
        Label for x-axis
    y_label : string
        Label for y-axis
    tick_labels : list of strings
        Labels of xticks

    Returns
    _______
        Creates file containing figure with Mean and Stdev of data in title.

    Raises
    ______
    TypeError
        Occurs when no file name is given.
    SystemExit
        Occurs when given file already exists in directory.
    """
    try:
        exist = path.exists(out_file_name)
        print(exist)
    except TypeError:
        raise TypeError('No file name given.')

    if exist:
        raise SystemExit('File already exists.')

    width = 10
    height = 3

    fig = plt.figure(figsize=(width, height), dpi=300)

    ax = fig.add_subplot(1, 1, 1)

    ax.boxplot(L)

    ticks = list(range(len(tick_labels)))

    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_xticklabels(tick_labels)
    plt.xticks(rotation='vertical')

    try:
        plt.savefig(out_file_name, bbox_inches='tight')
    except ValueError:
        raise ValueError('Out file type unsupported.')

    return path.exists(out_file_name)
