# -*- coding: utf-8 -*-
#
# Copyright © Spyder Project Contributors
# Licensed under the terms of the MIT License
# (see spyder_notebook/__init__.py for details)


"""
Spyder-notebook
===============

Jupyter notebook integration with Spyder.
"""

# Third party imports
from setuptools import find_packages, setup
from spyder_notebook import __version__

REQUIREMENTS = ['spyder', 'jupyter', 'notebook']

setup(
        name='spyder-notebook',
        version=__version__,
        keywords=["github changelog milestone"],
        url='https://github.com/spyder-ide/spyder-notebook',
        license='MIT',
        author='Spyder Development Team',
        description='Jupyter notebook integration with Spyder',
        long_description="This is a initial implementation of "
                         "the notebook running inside Spyder "
                         "as a plugin.",
        packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
        install_requires=REQUIREMENTS,
        classifiers=[
                     'Development Status :: 4 - Beta',
                     'Intended Audience :: Developers',
                     'License :: OSI Approved :: MIT License',
                     'Operating System :: OS Independent',
                     'Programming Language :: Python 2.7',
                     'Programming Language :: Python 3'
                     ])
