import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name="fiddup",
    version="3.0.0",
    description="Utility to find similar files based on filename or hash.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/jarviscodes/fiddup",
    author="Jarvis Codes",
    author_email="jarvis@jayradz.com",
    license="MIT",
    classifiers=["Programming Language :: Python :: 3"],
    packages=["fiddup"],
    include_package_data=True,
    install_requires=["click", "colorama", "alive-progress", "terminaltables"],
    entry_points={"console_scripts": ["fiddup=fiddup.__main__:main"]},
)
