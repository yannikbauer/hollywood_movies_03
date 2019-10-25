#!/usr/bin/env python

"""
utils.py:
Utility functions for Hollywood movie generation.
"""

__author__      = "Yannik Bauer"
__copyright__   = "2019, Yannik Bauer"
__license__     = "MIT License"

# Import libs
import numpy as np
import imageio
import matplotlib.pyplot as plt


def load_tiffs_into_array(fname, fps, scene_dur):
    """
    Loads tiff image stack from file and puts it into numpy array.
    INPUTS:
    - fname: str: file name
    - fps: scalar: frames per second
    - scene_dur: scalar: scene duration (s)
    OUTPUTS:
    - tiff_array: np.array: tiff image array [frame, height, width]
    - tiff_meta: dict: tiff meta data (n_frames, width, height, n_scenes, fp_scene)
    """

    # Load file
    decoder = imageio.get_reader(fname, 'TIFF')
    meta = eval(decoder.get_meta_data()['description'])

    # Get parameters
    n_frames = meta['shape'][0]
    width, height = meta['shape'][2], meta['shape'][1]
    n_scenes = int(n_frames / (fps * scene_dur)) # number of scenes
    fp_scene = int(n_frames / n_scenes) # frames per scene

    print('n_frames =', n_frames)
    print('width =', width)
    print('height =', height)
    print('number of scenes =', n_scenes)
    print('frames per scene =', fp_scene)

    # Put tiff stack into array
    print('\nPutting tiff stack into array:')
    tiff_array = np.zeros((n_frames, height, width), dtype=np.uint8)

    for i in range(n_frames):
        tiff_array[i,:,:] = decoder.get_data(i)

        # Show progress    
        if (i+1)%fp_scene == 0:
            print('.', end='')
            if (i+1)%(fp_scene*36) == 0: # line break every 36 scenes (= 1 training part later)
                print('\n', end='')
    
    # Store meta data
    tiff_meta = {"n_frames": n_frames,
                 "width": width,
                 "height": height,
                 "n_scenes": n_scenes,
                 "fp_scene": fp_scene,
                }
    
    return tiff_array, tiff_meta

def histogram_equalization(array):
    """Histogram equalization distributes the intensities uniformly on the histogram.
    This allows for areas of lower local contrast to gain a higher contrast. Histogram 
    equalization accomplishes this by effectively spreading out the most frequent intensity values.
    See: https://en.wikipedia.org/wiki/Histogram_equalization
    INPUT: array = numpy array of image frames [frame, height, width]
    OUTPUT: hist_eq = numpy array of corrected image frames [frame, height, width]
    """
    
    assert array.dtype == np.uint8
    n = array.size
    assert n < 2**32
    n_frames, height, width = array.shape
    
    array.reshape((n_frames,-1))
    rnd = np.random.uniform(0, 1, size=array.shape).astype(np.float32)
    array = (array + rnd)
    del rnd
    idx = np.argsort(array.flatten()).astype(np.uint32)
    ranks = np.zeros(array.size, dtype=np.uint32)
    ranks[idx] = np.arange(n, dtype=np.uint32)
    del idx
    ranks = ranks.reshape(array.shape)
    hist_eq = np.fix(ranks / n * 256).astype(np.uint8).reshape((n_frames, height, width))
    return hist_eq

def build_checkerboard(w, h):
    re = np.r_[ int(w/2)*[0,255] ] # even-numbered rows
    ro = np.r_[ int(w/2)*[255,0] ] # odd-numbered rows
    return np.row_stack(int(h/2)*(re, ro)).astype(np.uint8)

def make_test_image(w, h):

    checkerboard = build_checkerboard(w, h)
    print(checkerboard)
    print(checkerboard.shape)
    print(checkerboard.dtype)

    # Show image
    plt.imshow(checkerboard, vmin=0, vmax=1, cmap='gray')

    # Make into image sequence
    checkerboard_stack = np.repeat(checkerboard[np.newaxis,:,:], fps*scene_dur, axis=0).astype(np.uint8)
    print(checkerboard_stack.shape)
    print(checkerboard_stack.dtype)

    # Save img as PNG
    fname = '../data/processed/test_image_{}x{}'.format(shape[0], shape[1])
    imageio.imwrite(fname+'.png', checkerboard, 'PNG')

    # Save img sequence as TIFF
    imageio.mimwrite(fname+'.tiff', checkerboard_stack, 'TIFF')

    # Now convert this tiff stack to .avi using 03_make_rnd_avi_seq; or use FIJI