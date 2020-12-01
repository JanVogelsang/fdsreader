import setuptools

with open("README.md", "r") as rf:
    long_description = rf.read()

setuptools.setup(
    name="fdsreader", # Replace with your own username
    use_incremental=True,
    setup_requires=['incremental'],
    install_requires=['incremental'],
    author="FZJ IAS-7 (Prof. Dr. Lukas Arnold, Jan Vogelsang)",
    author_email="j.vogelsang@fz-juelich.de",
    description="Python reader for data generated by FDS.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JanVogelsang/fdsreader",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)