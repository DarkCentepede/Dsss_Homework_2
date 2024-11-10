from setuptools import setup, find_packages

setup(
    name="math_quiz_package",  # Package name
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "math-quiz=math_quiz.math_quiz:math_quiz",  # command name = package.module:function
        ]
    },
    author="Ramsundar Yellamelli",
    author_email="ramsundaryellamelli@gmail.com",
    description="A simple math quiz game.",
    long_description=open("README.md").read(),  # Optional: add a README.md
    long_description_content_type="text/markdown",
    url="https://github.com/DarkCentepede/Dsss_Homework_2.git",  # Optional: GitHub URL
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: apache license",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)