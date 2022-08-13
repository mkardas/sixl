from setuptools import setup
from pathlib import Path

setup(
    name = "sixl",
    version = "0.1",
    author = "Marcin Kardas",
    description = "IPython inline plots and images through Sixel.",
    license = "MIT",
    keywords = "sixel ipython",
    url = "https://github.com/mkardas/sixl",
    packages=['sixl'],
    long_description=Path('README.md').read_text(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Software Development :: Libraries",
        "Topic :: System :: Softwaredd Distribution",
        "License :: OSI Approved :: MIT License",
    ],
)
