from setuptools import setup, find_packages

setup(
    name="tangods_thorlabssc10",
    version="0.0.1",
    description="Tango device server written in PyTango for a Thorlabs SC10 shutter controller",
    author="Daniel Schick",
    author_email="dschick@mbi-berlin.de",
    python_requires=">=3.6",
    entry_points={"console_scripts": ["ThorlabsSC10 = tangods_thorlabssc10:main"]},
    license="MIT",
    packages=["tangods_thorlabssc10"],
    install_requires=[
        "pytango",
        "instrumentkit" # which version? library is updating so far...
    ],
    url="https://github.com/MBI-Div-b/pytango-ThorlabsSC10",
    keywords=[
        "tango device",
        "tango",
        "pytango",
    ],
)
