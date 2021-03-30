rm -rf build #TODO: remove hardcoding of py3.8.3 
python3 setup.py build_ext --inplace
python3 setup.py install --user
