from setuptools import setup

with open("README.md", encoding="utf8") as f:
    long_description = f.read()

setup(
    name="mywsgi",
    version="0.0.0",
    author="Matt Robenolt",
    author_email="matt@ydekproductions.com",
    url="https://github.com/mattrobenolt/mywsgi",
    description="Opinionated uWSGI setup",
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=["mywsgi"],
    zip_safe=False,
    license="MIT",
    include_package_data=True,
    entry_points={"console_scripts": ["mywsgi = mywsgi:cli"]},
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development",
    ],
)