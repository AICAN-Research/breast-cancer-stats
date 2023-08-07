import setuptools


with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


setuptools.setup(
    name="who-extract",
    version="0.0.1",
    author="André Pedersen",
    author_email="andrped94@gmail.com",
    license="MIT",
    description="Project for extraction of World Health Organization (WHO) data and visualization.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/andreped/breast-cancer-stats",
    include_package_data=True,
    packages=setuptools.find_packages(),
    install_requires=[
        "numpy",
        "pandas",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires=">=3.8",
)
