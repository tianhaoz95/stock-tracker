import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="stock_tracker",
    version="0.0.1",
    author="Tianhao Zhou",
    author_email="jacksonzhou666@gmail.com",
    description="A utility to help track stock investment.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tianhaoz95/stock-tracker",
    packages=['stock_tracker'],
    entry_points = {
        'console_scripts': ['stock_tracker=stock_tracker.cli:main'],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)