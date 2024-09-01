from setuptools import setup, find_packages

setup(
    name="motion_magnification",
    packages=find_packages(),
    install_requires=[
    ],
    entry_points={
        "console_scripts": [
            "motion_magnification=motion_magnification:main",
        ],
    },
)
