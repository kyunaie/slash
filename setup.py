from setuptools import setup
setup(
    name = 'slash',
    version = '0.1.0',
    packages = ['slash'],
    entry_points = {
        'console_scripts': [
            'slash = slash.__main__:main'
        ]
    })