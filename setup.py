"""A setuptools based setup module for motleydatetime.
See Also:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
https://github.com/pypa/sampleproject/blob/master/setup.py
"""
from setuptools import setup
from os import path
import subprocess
# Get the long description from the README file
here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
vers_result = subprocess.run(['python','src/motleytestpython/version.py'], stdout=subprocess.PIPE)
vers = vers_result.stdout.decode('utf-8').strip(' \t\r\n')
print('vers=' + vers)

setup(
    name='motleytestpython',
    version=vers,
    packages=['motleytestpython'],
    package_dir={'': 'src'},
    url='https://github.com/ericmotleybytes/motleytestpython',
    license='MIT',
    author='Eric Christiansen',
    author_email='eric@motleybytes.com',
    description='Simple and quick sanity check that Python is working correctly.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
    ],
    keywords='date time datetime timezone',
    python_requires='>=3.6, <4',
    install_requires=[
        'pytz>=2020.1',
        'tzlocal>=2.1'
    ],
    project_urls={
        'Documentation' : 'https://ericmotleybytes.github.io/motleytestpython/',
        'PyPI Page'     : 'https://pypi.org/project/motleytestpython/',
        'Bug Reports'   : 'https://github.com/ericmotleybytes/motleytestpython/issues',
        'Source'        : 'https://github.com/ericmotleybytes/motleytestpython'
    }
)
