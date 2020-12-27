import os
from setuptools import setup

setup(
    name='algorithmia-environments',
    version='0.1.0',
    description='Algorithmia Runnable Environments CLI for running Algorithmia Algorithms and their runtime environments locally.',
    license='MIT',
    url='https://github.com/algorithmiaio/runnable-environments',
    author='Algorithmia',
    author_email='support@algorithmia.com',
    entry_points={
        'console_scripts': ['algo env = src.main:entrypoint']
    },
    install_requires=[
        'requests',
        'six',
        'docker',
        'argparse'
    ],
    include_package_data=True,
)
