from setuptools import setup, find_packages

setup(
    name="Topsis-Vijayshree-102316131",
    version="1.0.1",
    author="Vijayshree",
    description="TOPSIS implementation using Python",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=["pandas", "numpy"],
    entry_points={
        "console_scripts": [
            "topsis=topsis_vijayshree_102316131.topsis:main"
        ]
    },
)
