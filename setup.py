from setuptools import setup, find_packages

with open("README.md") as readme_file:
    readme = readme_file.read()

setup(
    name='logNow',
    version='0.21.4',    
    description=('logNow" is a Python package created to simplify logging for developers working on Python applications. The package provides a simple logging function that allows developers to output log messages to a file with timestamps, instead of using the standard "print" statement.'),
    long_description = readme,
    long_description_content_type="text/markdown",
    url='https://github.com/NapoII/logNow',
    author='Napo_II',
    author_email='Napo_the_II@protonmail.com',
    license='MIT License',
    packages=find_packages(),
    install_requires= [],

    classifiers=[
        'Development Status :: 4 - Beta',
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Financial and Insurance Industry",
        "Intended Audience :: Healthcare Industry",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Legal Industry",
        "Intended Audience :: Manufacturing",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Telecommunications Industry",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Topic :: Adaptive Technologies",
        "Topic :: Database",
        "Topic :: Documentation",
        "Topic :: Education :: Testing",
        "Topic :: Printing",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Bug Tracking",
        "Topic :: Software Development :: Debuggers",
        "Topic :: Software Development :: Documentation",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Localization",
        "Topic :: Software Development :: Testing",
        "Topic :: Software Development :: Testing :: Traffic Generation",
        "Topic :: System",
        "Topic :: System :: Console Fonts",
        "Topic :: System :: Logging",
        "Topic :: System :: Systems Administration",
        "Topic :: Utilities",
        ],)