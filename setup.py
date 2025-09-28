import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Kidney-Disease-Classification-MLflow"
AUTHOR = "Turgut Nasrullayev","Baljinder Singh"
AUTHOR_USERNAME = "tempoo04"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "turgut.nasrullayev@gmail.com","rajadps98@gmail.com"

setuptools.setup(
    name = REPO_NAME,
    version = __version__,
    author = AUTHOR,
    author_email = AUTHOR_EMAIL,
    description = "Python package for CNN app",
    long_description = long_description,
    long_description_content = "text/markdown",
    url = f"https://github.com/{AUTHOR_USERNAME}/{REPO_NAME}",
    project_urls = {"Bug Tracker": "https://github.com/{AUTHOR_USERNAME}/{REPO_NAME}/issues"},
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src"),
)