import matplotlib.pyplot as plt
import numpy as np
from .config import DEFAULT_CONFIG, GOLDEN
from .utils import set_config, set_config_double

CM_TO_INCHES = 1/2.54

def grid_plot(nrows:int, ncols:int, config:dict=None):
    # Merge user config with default config
    config = {**DEFAULT_CONFIG, **(config or {})}
    # Apply style globally
    plt.style.use(config["style"])

    # Compute axes width
    ax_width = config["figwidth"] - config["Margin"][0] - config["Margin"][1]
    ax_width -= (ncols-1)*config['Gap'][0]
    ax_width /= ncols

    if config['aspect'] == 'Golden':
        ax_height = ax_width*GOLDEN
    elif config['aspect'] == 'Square':
        ax_height = ax_width
    elif config['aspect'] == 'Equal':
        dx = config['xlim'][1]-config['xlim'][0]
        dy = config['ylim'][1]-config['ylim'][0]
        ax_height = ax_width*dy/dx
    elif isinstance(config['aspect'],(int,float)):
        ax_height = ax_width*config['aspect']

    fig_height = ax_height*nrows + (nrows-1)*config['Gap'][1] + config["Margin"][2] + config["Margin"][3]

    # Create the figure and subplots
    fig, axs = plt.subplots(nrows, ncols, figsize=(config["figwidth"]*CM_TO_INCHES, fig_height*CM_TO_INCHES))
    axs = axs.reshape((nrows,ncols))

    # Set configuration
    axs = set_config(axs, config)

    # Set the position of the axes
    for i in range(nrows):
        for j in range(ncols):
            position_x = (config["Margin"][0] + j*ax_width + j*config['Gap'][0])/(config["figwidth"])
            position_y = (config["Margin"][2] + (nrows-1-i)*(ax_height + config['Gap'][1]))/(fig_height)
            axs[i,j].set_position([position_x,position_y,ax_width/(config["figwidth"]),ax_height/(fig_height)])

    # Flatten the array of axes for easier indexing
    # axs = axs.flatten() if isinstance(axs, (list, np.ndarray)) else [axs]

    return fig, axs

def grid_plot_double(nrows:int, ncols:int, config:dict=None, pair = 'Horizontal'):
    # Merge user config with default config
    config = {**DEFAULT_CONFIG, **(config or {})}
    # Apply style globally
    plt.style.use(config["style"])

    # Compute axes width
    ax_width = config["figwidth"] - config["Margin"][0] - config["Margin"][1]
    ax_width -= (ncols-1)*config['Gap'][0]
    ax_width /= ncols

    if config['aspect'] == 'Golden':
        ax_height = ax_width*GOLDEN
    elif config['aspect'] == 'Square':
        ax_height = ax_width
    elif config['aspect'] == 'Equal':
        dx = config['xlim'][1]-config['xlim'][0]
        dy = config['ylim'][1]-config['ylim'][0]
        ax_height = ax_width*dy/dx
    elif isinstance(config['aspect'],(int,float)):
        ax_height = ax_width*config['aspect']

    fig_height = ax_height*nrows + (nrows-1)*config['Gap'][1] + config["Margin"][2] + config["Margin"][3]

    # Create the figure and subplots
    fig, axs = plt.subplots(nrows*2, ncols, figsize=(config["figwidth"]*CM_TO_INCHES, fig_height*CM_TO_INCHES))
    axs = axs.reshape((nrows,ncols,2))

    # Set configuration
    axs = set_config_double(axs, config, pair)

    # Set the position of the axes
    for i in range(nrows):
        for j in range(ncols):
            position_x = (config["Margin"][0] + j*ax_width + j*config['Gap'][0])/(config["figwidth"])
            position_y = (config["Margin"][2] + (nrows-1-i)*(ax_height + config['Gap'][1]))/(fig_height)
            if pair == 'Horizontal':
                axs[i,j,0].set_position([position_x,position_y,0.5*ax_width/(config["figwidth"]),ax_height/(fig_height)])
                axs[i,j,1].set_position([position_x+0.5*ax_width/(config["figwidth"]),position_y,0.5*ax_width/(config["figwidth"]),ax_height/(fig_height)])
            elif pair == 'Vertical':
                axs[i,j,0].set_position([position_x,position_y,ax_width/(config["figwidth"]),0.5*ax_height/(fig_height)])
                axs[i,j,1].set_position([position_x,position_y+0.5*ax_height/(fig_height),ax_width/(config["figwidth"]),0.5*ax_height/(fig_height)])

    # Flatten the array of axes for easier indexing
    # axs = axs.flatten() if isinstance(axs, (list, np.ndarray)) else [axs]

    return fig, axs