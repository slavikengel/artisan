from setuptools import setup, find_packages


package_name = "artisan"


with open("requirements.txt", "r", encoding="utf-8") as f:
    requires = f.readlines()


setup(
    name="artisan",
    version="0.0.1",
    long_description_content_type="text/markdown",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=requires,
    entry_points={"console_scripts": ["artisan = artisan.cli.main:cli"]},
)
