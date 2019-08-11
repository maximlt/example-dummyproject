import pathlib
from setuptools import setup
import codecs
import re

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

AUTOMATION_REQUIRE = ["tox>=3.12.1"]
LINTERS_REQUIRE = ["flake8>=3.7.8"]
FORMATTER_REQUIRE = ["black>=19.3b0"]
NOTEBOOK_REQUIRE = ["jupyterlab>=1.0.4"]
TEST_REQUIRE = ["pytest>=5.0.1", "pytest-cov>=2.7.1"]
TEST_NOTEBOOKS_REQUIRE = ["pytest>=5.0.1", "nbval>=0.1"]
PUBLISH_REQUIRE = ["twine>=1.13.0"]
DOCS_REQUIRE = ["sphinx>=2.1.2", "sphinx-rtd-theme>=0.4.3"]
DEV_REQUIRE = list(
    set(
        AUTOMATION_REQUIRE
        + LINTERS_REQUIRE
        + FORMATTER_REQUIRE
        + NOTEBOOK_REQUIRE
        + TEST_REQUIRE
        + TEST_NOTEBOOKS_REQUIRE
        + DOCS_REQUIRE
        + PUBLISH_REQUIRE
    )
)


def read(*parts):
    # with codecs.open(os.path.join(HERE, *parts), "r") as fp:
    with codecs.open(HERE.joinpath(*parts), "r") as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


# This call to setup() does all the work
setup(
    name="projectxyxyxy",
    # First method from https://packaging.python.org/guides/single-sourcing-package-version/
    version=find_version("project", "__init__.py"),
    description="Project description",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/maximlt/project",
    author="Maxime Liquet",
    author_email="maximeliquet@free.fr",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    python_requires=">=3.6",
    packages=["project"],
    include_package_data=True,
    install_requires=["Click>=7.0"],
    entry_points="""
        [console_scripts]
        calc=project:cli
    """,
    extras_require={
        "dev": DEV_REQUIRE,
        "test": TEST_REQUIRE,
        "test_notebooks": TEST_NOTEBOOKS_REQUIRE,
        "formatter": FORMATTER_REQUIRE,
        "linters": LINTERS_REQUIRE,
        "docs": DOCS_REQUIRE,
    },
    project_urls={"Documentation": "https://xyxyxy.readthedocs.io/en/latest/"},
)
