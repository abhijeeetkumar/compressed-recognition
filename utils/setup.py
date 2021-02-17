from distutils.core import setup, Extension
import numpy as np

utils_module = Extension('cva',
		sources = ['main.c'],
		include_dirs=[np.get_include(), '/home/mdl/amk7371/ffmpeg_lib/include/'],
		extra_compile_args=['-DNDEBUG', '-O3', '-std=c99'],
		extra_link_args=['-L/home/mdl/amk7371/ffmpeg_lib/lib/']
)

setup ( name = 'cva',
	version = '0.1',
	description = 'Utils for compressed video analytics (cva).',
	ext_modules = [ utils_module ]
)
