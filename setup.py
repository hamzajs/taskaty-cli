from setuptools import setup

setup(
    name="Taskaty",
    version="0.1.0",
    description="A simple CLI Task manager in Python",
    author="Hamza Sulieman",
    packages=['taskaty'],
    install_requires=['tabulate'],
    entry_points={
        "console_scripts":[
            "taskaty=taskaty:main"
        ]
    },
)