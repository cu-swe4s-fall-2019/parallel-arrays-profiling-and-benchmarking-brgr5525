"""Various methods for data visualization

    * boxplot - creates a boxplot from data and saves to file
    * histogram - creates a histogram from data and saves to file
    * combo - creates a boxplot and histogram from data, saves to file
"""
import sys
import os.path
from os import path
#import math_lib

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
    except TypeError:
        raise TypeError('No file name given.')

    if exist:
        raise SystemExit('File already exists.')

    width = 10
    height = 3

    fig = plt.figure(figsize=(width, height), dpi=300)

    ax = fig.add_subplot(1, 1, 1)

    ax.boxplot(L)

    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.xticks(tick_labels)

    try:
        plt.savefig(out_file_name, bbox_inches='tight')
    except ValueError:
        raise ValueError('Out file type unsupported.')

    return path.exists(out_file_name)


def histogram(L, out_file_name):
    """Create histogram from given data and save to designated file

    Parameters
    __________
    L : array of ints and floats
        Array containing data whose histogram is desired.
    out_file_name : str
        Name of file where figured is to be saved.

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
    except TypeError:
        raise TypeError('No file name given.')

    if exist:
        raise SystemExit('File already exists.')

    width = 3
    height = 3

    fig = plt.figure(figsize=(width, height), dpi=300)

    ax = fig.add_subplot(1, 1, 1)

    ax.hist(L)

    mean = math_lib.list_mean(L)
    stdev = math_lib.list_stdev(L)

    if mean is not None:
        mean = round(mean, 5)
    if stdev is not None:
        stdev = round(stdev, 7)

    title = str('Mean: ' + str(mean) + ' Stdev: ' + str(stdev))
    ax.set_title(title)

    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')

    try:
        plt.savefig(out_file_name, bbox_inches='tight')
    except ValueError:
        raise ValueError('Out file type unsupported.')

    return path.exists(out_file_name)


def combo(L, out_file_name):
    """Create boxplot and histogram from data and save to designated file

    Parameters
    __________
    L : array of ints and floats
        Array containing data whose boxplot and histogram is desired.
    out_file_name : str
        Name of file where figured is to be saved.

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
    except TypeError:
        raise TypeError('No file name given.')

    if exist:
        raise SystemExit('File already exists.')

    fig, axs = plt.subplots(1, 2)

    # Create the box subplot
    axs[0].boxplot(L)

    mean = math_lib.list_mean(L)
    stdev = math_lib.list_stdev(L)

    if mean is not None:
        mean = round(mean, 5)
    if stdev is not None:
        stdev = round(stdev, 7)

    title = str('Mean: ' + str(mean) + ' Stdev: ' + str(stdev))
    axs[0].set_title(title)

    axs[0].set_xlabel('Value')
    axs[0].set_ylabel('Distribution')

    # Create the histogram subplot
    axs[1].hist(L)

    axs[1].set_title(title)

    axs[1].set_xlabel('Value')
    axs[1].set_ylabel('Frequency')

    fig.subplots_adjust(left=0.08, right=0.98, bottom=0.05, top=0.9,
                        hspace=0.4, wspace=0.4)

    try:
        plt.savefig(out_file_name, bbox_inches='tight')
    except ValueError:
        raise ValueError('Out file type unsupported.')

    return path.exists(out_file_name)
