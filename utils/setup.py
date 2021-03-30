from distutils.core import setup, Extension
import numpy as np

utils_module = Extension('cva',
		sources = ['main.c'],
		include_dirs=[np.get_include(), '/home/mdl/amk7371/video_analytics/FFmpeg_x64/include/'],
		extra_compile_args=['-DNDEBUG', '-O3', '-std=c99'],
		extra_link_args=['-L/home/mdl/amk7371/video_analytics/FFmpeg_x64/include/', '-lavutil', '-lavcodec', '-lavformat', '-lswresample', '-lswscale']
)

setup ( name = 'cva',
	version = '0.1',
	description = 'Utils for compressed video analytics (cva).',
	ext_modules = [ utils_module ]
)
