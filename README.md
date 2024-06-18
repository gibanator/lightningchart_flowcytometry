## LightningChart Python
For this task we may use [LightningChart](https://lightningchart.com/python-charts/) library. It provides a wide range of tools for creating graphs that can be useful for flow cytometry white cell analysis in Python. \
In this project, we will use:
- XY Charts ([Link to docs](https://lightningchart.com/python-charts/docs/charts/chart-xy/)) \
*in combination with*
- Point Series ([Link to docs](https://lightningchart.com/python-charts/docs/charts/chart-xy/#point-series))

LightningChart uses GPUs for faster rendering, so it is possible to 'feed' it a huge sample of data (which will be the case in this project).
## Setting Up Python Environment
For white blood cell flow cytometry visualizing in Python, first we need to set up our Python environment. 
### Installation of Python on Mac
I recommend using [Homebrew package manager](https://brew.sh/) as it is popular and has a lot of packages.\
Moreover, it is arguably more convenient than installing Python using .dmg.

#### 1. First step is installing Homebrew itself
> You can skip this step if it is already installed on your Mac

Enter Terminal app and copy/paste this string
```sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
:exclamation: **Important note:** 
  Installation of Homebrew can be not fast, usually from 5 to 15 minutes.

#### 2. Installation of Python
```sh
brew install python
```
This command will install the latest stable version of python.


<details>
  <summary><b>If you don't want to use Homebrew</b></summary>
  You can access the <a href = 'https://www.python.org/downloads/macos/'>official Python website</a>, select the      latest stable version downloader for MacOS (it is named macOS 64-bit universal2 installer) and follow the installation instructions.
</details>

You can check the version using `python3 –version` in Terminal.
> If it displays `Unknown command` error, it is most likely due to PATH variables. Refer to  
[this guide](https://www.mygreatlearning.com/blog/add-python-to-path/) to fix.

---
### Installation of Python on Windows
I recommend using cli tool [Winget](https://learn.microsoft.com/en-us/windows/package-manager/winget/). 

#### Install Python package
Open cmd or PowerShell as Administrator and type in:
```powershell
winget install Python.Python.3
```

<details>
  <summary><b>If you don't want to use Winget</b></summary>
  You can access the <a href = 'https://www.python.org/downloads/macos/'>official Python website</a>, select the      latest stable version downloader for Windows <br> (it is named Windows installer (64-bit)) and follow the installation instructions.
</details>

You can verify installation of python and pip by typing `python --version` and `pip --version` respectively. 
> If it displays `'command' is not recognized` error, it is most likely due to PATH variables. Refer to [this guide](https://www.mygreatlearning.com/blog/add-python-to-path/) to fix.

---

### Installation of IDE
For IDE (integrated development environment) I recommend using [PyCharm](https://www.jetbrains.com/pycharm/download/?section=mac) as it is clean and powerful. However, full version is paid so you can also use [VSCode](https://code.visualstudio.com/).

(*Optional*) You may want to set up `venv` (Python virtual environment) so you can install packages there and not clutter the Python installation.
Environment creating instructions:
- PyCharm - https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html#python_create_virtual_env
- VSCode - https://code.visualstudio.com/docs/python/environments

Then, using the terminal (IDEs have integrated terminals) install needed packages:
```sh
pip install pandas lightningchart
```
---
### Libraries Used
#### Pandas
In this project, we will mainly use the dataframe, two-dimensional data structure provided by Pandas. It can be easily created from CSV or Excel file.

#### LightningChart
Lightningchart is the main library used in the project for creating white blood cell flow chart in Python. It provides a highly customizable graph building tools, including simple XY charts, 3D charts, Bar charts, Spider charts, Map charts. However, this time we will use only XY chart (and Point Series).

## Loading and Processing Data
You can find a lot of medical data, including Flow Cytometry for analyzing in Python, at PhysioNet website (https://www.immport.org/shared/) \
Here, you can search for flow cytometry data by using respective keywords, e.g. "flow cytometry white cells"

:exclamation: **Important note:** Unfortunately, the dataset used was created manually from multiple files, thus you may have a trouble finding data for different cells in a single file on ImmPort.

##### The data was combined out of files under study accessions STDY2310, STDY2370, SDY1630.

For performing flow cytometry white blood cell analysis we need the SSC(FSC); Y-axis is SSC, X-axis is FSC.
Along with these two metrics, KDE (kernel density estimation) data is provided for each point. It is needed to color the chart based on the concentration of points on it.

Thus, the csv looks like this:

| # | FSC           | SSC            | KDE                   |
|---|---------------|----------------|-----------------------|
| 0 | 79326.953125  | 54160.35546875 | 3.339982707067524e-10 |
| 1 | 84336.5703125 | 60048.74609375 | 2.626928410663256e-10 |
| 2 |               |                |                       |
