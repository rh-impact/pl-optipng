from os import path
from setuptools import setup

with open(path.join(path.dirname(path.abspath(__file__)), 'README.rst')) as f:
    readme = f.read()

setup(
    name             = 'optipng',
    version          = '0.0.1',
    description      = 'A plugin to recompresses Portable Network Graphics (PNG) image files to a smaller size. This program also converts external formats (BMP, GIF, PNM and TIFF) to optimized PNG, and performs PNG integrity checks and corrections.',
    long_description = readme,
    author           = 'rh-impact',
    author_email     = 'porridge@redhat.com',
    url              = 'https://github.com/rh-impact/pl-optipng',
    packages         = ['optipng'],
    install_requires = ['chrisapp'],
    test_suite       = 'nose.collector',
    tests_require    = ['nose'],
    license          = 'MIT',
    zip_safe         = False,
    python_requires  = '>=3.6',
    entry_points     = {
        'console_scripts': [
            'optipng = optipng.__main__:main'
            ]
        }
)
