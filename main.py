# -*- coding: utf-8 -*-
# @Author: ander
# @Date:   2020-07-16 15:21:52
# @Last Modified by:   ander
# @Last Modified time: 2020-07-20 18:14:27
import os
import glob
import random
import shutil


if not os.path.exists('output'):
	os.mkdir('output')
else:
	for file in glob.glob(os.path.join('output', '*.*')):
		os.remove(file)
files = glob.glob(os.path.join('input', '*.*'))
new_names = [i for i in range(len(files))]
random.shuffle(new_names)
for i, file in enumerate(files):
	dirname, basename = os.path.split(file)
	filename, ext = os.path.splitext(basename)
	shutil.copy(file, os.path.join('output', f'{new_names[i]:05}{ext}'))
