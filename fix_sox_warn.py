# -*- coding: utf-8 -*-
# @Time    : 1/28/20 11:40 PM
# @Author  : Yuan Gong
# @Affiliation  : University of Notre Dame
# @Email   : yuangongfdu@gmail.com 
# @File    : fix_sox_warn.py

# this code fix the sox warning of "wave header missing extended part of fmt chunk"
"""
This warning doesn't affect the use of the dataset, you can safely ignore it. It can be solved by either of the following method:

1) Download the new version of the dataset, we've already fixed that.
2) Use this code to fix the problem, you just need to change the path in line 27 and 28.


The problem of "wave header missing extended part of fmt chunk" is due to a bug of MATLAB 2018 - the software used to process and generate the wave files.
According to the definition of WAVE file header, for all formats other than PCM, the Format chunk must have an extended portion. The extension can be of zero length, but the size field (with value 0) must be present.
A lot of ReMASC recordings use IEEE_FLOAT format instead of PCM format to provide higher precision but the Matlab audiowrite function doesn't automatically add the zero fmtext code to the wave header, which leads to this warning.

Reference:
https://github.com/Distrotech/sox/blob/0242e319c894156bf53cd9446c65f7c9d129008b/src/wav.c
http://www-mmsp.ece.mcgill.ca/Documents/AudioFormats/WAVE/WAVE.html
"""

import os

original_path = '/home/ndmobilecomp/remasc/core/data'
target_path = '/home/ndmobilecomp/remasc/core_fix/data'

if not os.path.exists(target_path):
    os.makedirs(target_path)

audio_list = os.listdir(original_path)
for i in range(len(audio_list)):
    file_name = audio_list[i]
    os.system('sox {} {}'.format(os.path.join(original_path, file_name), os.path.join(target_path, file_name)))
