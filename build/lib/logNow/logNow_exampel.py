"""Full Doku on: https://github.com/NapoII/logNow
-----------------------------------------------
logNow" is a Python package created to simplify logging for developers working on Python applications. The package provides a simple logging function that allows developers to output log messages to a file with timestamps, instead of using the standard "print" statement.

With "logNow", developers can easily create custom log messages and output them to a log file, allowing them to monitor the behavior of their applications and quickly identify any errors or issues that arise. The package provides several useful features, including support for multiple log levels, the ability to configure log formatting, and the option to output logs to the console in addition to the log file.

In addition to its core functionality, "logNow" is designed to be easy to use and configure. The package is well-documented, and the code is written in a modular and extensible manner, making it easy for developers to customize and extend its functionality to suit their needs."""


# To use logNow, you only need to import and write log("a str")

import logNow
from logNow import log

log("hello world")
log("hello red world", "R")
log("hello green world", "G")
log("hello blue world", "B")
