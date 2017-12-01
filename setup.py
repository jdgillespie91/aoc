from setuptools import setup, find_packages

setup(
    name='aoc',
    version='1.0.0',
    packages=find_packages(exclude=['test']),
    description='My solutions to Advent of Code 2017',
    author='Jake Gillespie',
    author_email='jdgillepsie91@gmail.com',
    zip_safe=True,
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=['click'],
    entry_points={'console_scripts': ['aoc=aoc.main:main']},
)
