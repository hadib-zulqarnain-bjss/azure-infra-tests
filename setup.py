from distutils.core import setup
import setuptools

packages = setuptools.find_packages("src")
print(packages)

setup(
    name="azure-infra-tests",
    version="0.0.1",
    author="Simon Dale",
    author_email="simon.dale@bjss.com",
    description="Azure Infrastructure Tests",
    packages=packages,
    package_dir={"": "src"},
    classifiers=["Programming Language :: Python :: 3"],
    python_requires="==3.7.6",
)
