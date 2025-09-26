from setuptools import setup, find_packages

setup(
    name="ninjazippy",
    version="0.1",
    packages=find_packages(),
    install_requires=["py7zr"],
    entry_points={
        "console_scripts": [
            "ninjazippy = ninjazippy.cli:main"
        ],
    },
)
