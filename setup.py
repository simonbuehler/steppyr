from setuptools import setup, find_packages

setup(
    name="steppyr",
    version="0.2",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
    ],
    author="Simon Buehler",
    author_email="simon@00010111.de",
    description="Ein Schrittmotor-Bibliothek in Python",
    url="https://github.com/simonbuehler/steppyr",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
