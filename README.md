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
- Offer a streamlit interface launch mode using `stream_launch.py` (for offline use).
- Organize code into modules to facilitate extensions and maintenance.

## Features

- **Prediction**: Generate predictions based on user-provided data.
- **Modularity**: Processing and prediction functions are grouped in the `model_functions` folder.
- **Streamlit Mode**: Dedicated script (`stream_launch.py`) for launching streamlit interface.
- **Automation**: A Makefile is included to simplify the execution of various tasks.

## Installation

### Prerequisites

- Python 3.11 or higher
- Pip (Python package manager)

### Installation Steps

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Melmouth/api_project.git
    ```

2. **Open a terminal in the same directory as main and run:**
    ```bash 
    make install
    ```

## Usage

To start the API on a local server, run:
```bash
make run
```
To start the API on a local server and use streamlit for vizualization of a request

```bash
make local
```


## Project Structure

- `main.py`: Entry point for the API server.
- `stream_launch.py`: Script for launching the streamlit mode.
- `model_functions/`: Folder containing processing and prediction functions.
- `xgb_model.pkl`: Pre-trained XGBoost model.
- `Makefile`: Automation of tasks.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request.

## License

This project is licensed under the MIT License.
