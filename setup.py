import setuptools


with open("README.md","r",encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.2.0"
REPO_NAME = "link_lens"
SRC_REPO = "link_lens"
AUTHOR_USER_NAME = "MvMukesh"
AUTHOR_EMAIL = "mukeshmanral777@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Python Package link_lens bridges missing link between your digital content and your NoteBook",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={"Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"},
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src"))