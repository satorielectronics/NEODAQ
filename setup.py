from setuptools import setup

setup(
    name='neodaq',
    version='1.0',
    description='Neopets Stocks Aggregator',
    author='satorielectronics',
    install_requires=[
        'selenium',
        'beautifulsoup4',
        'requests',
        'numpy',
        'pandas',
        'fake_useragent',
        'colorama',
        'matplotlib'
    ],
)
