from setuptools import setup, find_packages

setup(
    name="slither-ethernaut",
    description="Some slither detectors designed to compliment OpenZepplin's Ethernaut CTF",
    url="https://github.com/citrusdeer/slither-ethernaut",
    author="Citrus Deer",
    version="0.0",
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=["slither-analyzer>=0.9.3"],
    entry_points={
        "slither_analyzer.plugin": "slither slither-ethernaut=slither_ethernaut:make_plugin",
    },
)
