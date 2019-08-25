import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="awspass",
    version="0.1.0b5",
    author="Michał Zaborowski",
    author_email="michal@zaborowski.info.pl",
    description="Access keys management for AWS",
    keywords="aws pass credentials access-key",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://texxas.io/tag/awspass/",
    python_requires='>=3.6', # f-strings are nice
    packages=['awspass'],
    include_package_data=True,
    scripts=['awspass/awspass'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Operating System :: POSIX :: Linux"
     ],
)
