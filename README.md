<!--
 * @Author: hibana2077 hibana2077@gmail.com
 * @Date: 2023-10-14 12:20:00
 * @LastEditors: hibana2077 hibana2077@gmail.com
 * @LastEditTime: 2024-01-04 01:11:28
 * @FilePath: \haya\README.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
# Hayabusa

![python](https://img.shields.io/badge/python-3.10.0-blue?logo=python)
![pandas](https://img.shields.io/badge/pandas-1.3.3-blue?logo=pandas)
![numpy](https://img.shields.io/badge/numpy-1.21.2-blue?logo=numpy)
![streamlit](https://img.shields.io/badge/streamlit-1.25.0-blue?logo=streamlit)

[![Open in Spaces](https://huggingface.co/datasets/huggingface/badges/resolve/main/open-in-hf-spaces-sm.svg)](https://huggingface.co/spaces/hibana2077/AutoML)

## Introduction

This is a `Lightweight` and `Fast` WEB UI AutoML framework for small dataset (Less than 200MB).

## Installation

### Install from GitHub

Download the source code from GitHub and install dependencies.

```bash
git clone https://github.com/hibana2077/hayabusa.git
cd hayabusa
pip install -r requirements.txt
```

```bash
cd src
streamlit run main.py
```

### Install from Docker

Install Docker.

```bash
curl -sSL https://get.docker.com | sh
```

Build the image.

```bash
git clone https://github.com/hibana2077/hayabusa.git
cd hayabusa
docker build -t hayabusa .
```

Run the container.

```bash
docker run -p 8501:80 hayabusa
```

## Usage

### Upload Data

Upload your data in `csv` format.

### Data Profiling

Click `Data Profiling` button to get the data profiling report.

### Data Preprocessing (TODO)

Choose the columns you want to preprocess.

### Modelling

Choose the columns you want to predict.

### Download

You can download the model and the data pipeline in `pkl` format.

## License

[MIT](./LICENSE)

## Reference

- [Nicholas Renotte](https://youtu.be/xTKoyfCQiiU?si=VOuwpjufxmsEVMhD)
- [Streamlit](https://docs.streamlit.io/en/stable/)