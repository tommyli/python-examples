# Python Examples

Examples and snippets of Python code

## Getting Started

### Prerequisites

* Python 3 installed - [https://www.python.org/downloads/](https://www.python.org/downloads/)
* pip installed - [https://pip.pypa.io/en/stable/installing/](https://pip.pypa.io/en/stable/installing/)
* Conda installed - [https://www.anaconda.com/distribution/](https://www.anaconda.com/distribution/)
* Miniconda installed - [https://docs.conda.io/en/latest/miniconda.html](https://docs.conda.io/en/latest/miniconda.html)

You only need either pip or Miniconda.  Here's a good [blog post](http://deeplearning.lipingyang.org/2018/12/23/anaconda-vs-miniconda-vs-virtualenv/)
discussing the merits of each.  Miniconda is basically Conda without pre-installed Conda packages.


### Installing and Preparing Environment

Pick one of `pip+venv` of `miniconda` section below, I do not recommend mixing both together.

#### pip+venv

Create venv and install packages.

```bash
python -m venv .venv

source .venv/bin/activate

pip install --upgrade pip

pip install -r requirements.txt
```

More info: [https://docs.python.org/3/library/venv.html](https://docs.python.org/3/library/venv.html)

#### miniconda

Add [conda-forge](https://conda-forge.org/) channel

```bash
conda config --add channels conda-forge
conda config --set channel_priority strict
```

Create conda environment and install packages.

```bash
conda create --name python-examples --file requirements.txt
```

More info: [https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)

## Examples

Refer to individual .py script's docstring and --help for more information.
