# API Project

This project is an API developed in Python, designed to provide price predictions for cars using a machine learning model (XGBoost) trained on a dataset provided by Kaggle user (sidharth178/car-prices-dataset). The API loads a pre-trained model, processes input data, and returns prediction results. The project includes both a wrapped version deployed at the following url : <https://api-project-d7ao.onrender.com/predict>

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Overview

The purpose of **API Project** is to provide a simple and modular interface to leverage an XGBoost model in an API application in the context of my EDHEC 2025 Business Data Management Final Evaluation. This project allows you to:

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
To access the deployed prediction algorithm via its Render API provider :
```bash
https://api-project-d7ao.onrender.com/predict
```
## Data Structure

Here is the allowed format for a request to the Render url :
```bash
{
  "prod_year": 0, int
  "mileage": 0, float
  "cylinders": 0, int
  "airbags": 0, int
  "fuel_cng": false, boolean
  "fuel_diesel": false, boolean
  "fuel_hybrid": false, boolean
  "fuel_hydrogen": false, boolean
  "fuel_lpg": true, boolean
  "fuel_petrol": false, boolean
  "fuel_plugin_hybrid": false, boolean
}
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
