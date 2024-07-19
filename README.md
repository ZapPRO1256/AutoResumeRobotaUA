# ResumeParserRobotaUA

A parser for constantly updating resumes to be constantly on top of the search

## Contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)

## Introduction

The project implements logging into the account on the robota.ua website, switching to the user's resume page and constantly updating the resume to raise it to the top of the search engine

## Requirements

- Python 3.8+
- Downloaded Chrome browser
- Installed packages:
 - `selenium 4.23.0`

## Installation

1. Cloning the repository

 ```bash
 git clone https://github.com/ZapPRO1256/ResumeParserRobotaUA.git
 ```

2. Go to the project directory

 ```bash
 cd ResumeParserRobotaUA
 ```

3. Creation of a virtual environment and activation

 ```bash
 python -m venv .venv
 source .venv/bin/activate # for Windows: .venv\Scripts\activate
 ```

4. Installation of dependencies

 ```bash
 pip install -r requirements.txt
 ```

## Configuration

Enter your login, password and time in the data.txt file

## Usage

Run the parser:

```bash
python main.py

