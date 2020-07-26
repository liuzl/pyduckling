import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyduckling",
    version="0.0.1",
    author="Zhanliang Liu",
    author_email="liang@zliu.org",
    description="Python wrapper for facebook Duckling",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/liuzl/pyduckling",
    packages=setuptools.find_packages(),
    py_modules=['duckling'],
    install_requires=[
        "requests",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
