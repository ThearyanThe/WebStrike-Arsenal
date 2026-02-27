from setuptools import setup, find_packages

setup(
    name="webstrike-arsenal",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
        "colorama",
        "beautifulsoup4",
    ],
    entry_points={
        "console_scripts": [
            "webstrike=webstrike:main",
        ],
    },
    author="Your Name",
    description="Advanced exploit toolkit for web application security testing",
    license="MIT",
)
