# API Project

This project is an API developed in Python, designed to provide predictions using a machine learning model (XGBoost). The API loads a pre-trained model, processes input data, and returns prediction results. The project also includes specific processing functions organized in the `model_functions` folder and offers a streaming mode launch via `stream_launch.py`.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Overview

The purpose of **API Project** is to provide a simple and modular interface to leverage an XGBoost model in an API application. This project allows you to:

- Load and use a pre-trained model (`xgb_model.pkl`) for making predictions.
- Provide an entry point via `main.py` to start the API server.
- Offer a streaming launch mode using `stream_launch.py` (if applicable).
- Organize code into modules to facilitate extensions and maintenance.

## Features

- **Prediction**: Generate predictions based on user-provided data.
- **Modularity**: Processing and prediction functions are grouped in the `model_functions` folder.
- **Streaming Mode**: Dedicated script (`stream_launch.py`) for launching streaming processes.
- **Automation**: A Makefile is included to simplify the execution of various tasks.

## Installation

### Prerequisites

- Python 3.11 or higher
- Pip (Python package manager)

### Installation Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Melmouth/api_project.git

- Open a terminal in the same directory as main and run :
   ```bash 
   make install
