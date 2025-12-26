from setuptools import setup, find_packages

setup(
    name="data-collection-analyzer",
    version="2.3.0",
    author="Applied Science Research Institute",
    author_email="research@appresearch.org",
    description="Comprehensive analysis tool for examining data collection practices",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "requests>=2.25.0",
    ],
)


