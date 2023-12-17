### Hexlet tests and linter status:
[![Actions Status](https://github.com/Agrarox666/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Agrarox666/python-project-52/actions)
[![CI](https://github.com/Agrarox666/python-project-52/actions/workflows/test.yml/badge.svg)](https://github.com/Agrarox666/python-project-52/actions/workflows/test.yml)
<a href="https://codeclimate.com/github/Agrarox666/python-project-52/maintainability"><img src="https://api.codeclimate.com/v1/badges/9e33a70c7d6da06aefdc/maintainability" /></a>
<a href="https://codeclimate.com/github/Agrarox666/python-project-52/test_coverage"><img src="https://api.codeclimate.com/v1/badges/9e33a70c7d6da06aefdc/test_coverage" /></a>

# Task Manager
### try it: https://task-manager-bwi4.onrender.com

## Contents
- **[Description](#description)**
- **[Requirements](#requirements)**
- **[Installation](#installation-and-running-commands)**
- **[Routes](#routes)**

## Description
#### Welcome to task manager repository. It is my 4th educational project for the [Hexlet](https://ru.hexlet.io/) learning platform. It provides simplified functionality for task scheduling systems. You can manage your tasks with statuses and labels, assign an executors and filter tasks by this parameters. There are 2 languages available in the project: english and russian (depends on your system language).

## Requirements
- **Python >=3.10**
- **Git**
- **Poetry**
- **Pip**

## Installation and running commands
1. To clone the repo to your machine execute this command from your comamnd line:
``` shell
git clone https://github.com/Agrarox666/python-project-52.git
```
2. To install execute the commands below:
```shell
pip install -r requirements.txt
Make install
```
3. To start the application
```shell
Make start
```
## Routes
1. `/login`, `/logout` - for authentication and authorization
2. `/users` - list of all users, CRUD
3. `/tasks` - list of tasks, filter for it and its CRUD
4. `/labels` - list of labels and its CRUD
5. `/statuses` - list of statuses and its CRUD

