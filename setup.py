"""A setuptools based setup module.

See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

from setuptools import setup, find_packages
import pathlib


def read_file(file_name: str) -> str:
    here = pathlib.Path(__file__).parent.resolve()
    return (here / file_name).read_text(encoding='utf-8')
    # with open(os.path.join(os.path.dirname(__file__), file_name)) as input_file:
    #     data = input_file.read()
    # return data


setup(
    name='pythontemplate',
    version='0.0.1',
    description='A sample Python project',  # Optional
    long_description=read_file('README.md'),  # Optional
    long_description_content_type='text/markdown',  # Optional (see note above)
    url='https://github.com/colms/python-template',  # Optional
    author='A. Random Developer',  # Optional
    author_email='author@example.com',  # Optional
    package_dir={'': 'src'},  # Optional
    packages=find_packages(where='src'),  # Required
    python_requires='>=3.9, <4',
    install_requires=read_file('requirements.txt'),  # Optional
    extras_require={  # Optional
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
    package_data={"": ["*.json", "*.yaml"]},  # Optional
    include_package_data=True,  # Optional
    entry_points={  # Optional
        'console_scripts': [
            'pythontemplate=pythontemplate.example:main',
        ],
    },
)
