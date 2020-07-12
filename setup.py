from setuptools import setup, find_packages

setup(
    name='python-template',
    version='0.1',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    entry_points='''
        [console_scripts]
        run=src.main:run
    ''',
)
