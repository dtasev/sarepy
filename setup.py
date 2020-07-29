from setuptools import setup, find_packages

setup(
    name="sarepy",
    version="2020.7",
    packages=find_packages(exclude=["data"]),
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
    ],
    description="""Sarepy is the Python implementations
    of methods used for removing ring artifacts in tomography.
    These methods work in sinogram space where artifacts appear
    as straight lines or stripe artifacts. The codes are developed
    from the original implementations of methods published in
    Optics Epxress, Nghia T. Vo, Robert C. Atwood, and Michael Drakopoulos,
    "Superior techniques for eliminating ring artifacts in X-ray micro-tomography,"
    26, 28396-28412 (2018). https://doi.org/10.1364/OE.26.028396""",
)