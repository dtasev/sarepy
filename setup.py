from setuptools import setup, find_packages

setup(
    name="sarepy",
    version="2020.7",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python",
        "Natural Language :: English",
        "Intended Audience :: Science/Research",
        "Operating System :: POSIX :: Linux",
    ],
    install_requires=[
        "numpy",
        "scipy",
        "scikit-image",
        "pyfftw",
    ]
)