from setuptools import setup,find_packages
import pyCommon

setup(
    name = pyCommon.__application__,
    version = pyCommon.__version__,
    packages = find_packages(),
    package_data = {
        'pyCommon':['']
    },
    author_email = "thisisaspider@gmail.com",
    description = "基础框架",
    url = None,
    entry_points = {
        'console_scripts':[
            'startapp = pyCommon.main:main'
        ]
    },
    install_requires = [
    ],
    long_description = open("README.md","r", encoding='utf-8').read(),
    long_description_content_type = "text/markdown",
    python_requires = ">=3.6"
    # test_suite = 'pyCommon.test'
)