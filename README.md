# getindianname
[![PyPI version shields.io](https://img.shields.io/pypi/v/getindianname.svg?logo=pypi)](https://pypi.python.org/pypi/getindianname/)
[![PyPI license](https://img.shields.io/pypi/l/getindianname.svg)](https://pypi.python.org/pypi/getindianname)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://github.com/TechUX/getindianname/pulls)
[![GitHub issues](https://img.shields.io/github/issues/techux/getindianname.svg)](https://github.com/techux/getindianname/issues/)
[![Awesome Badges](https://img.shields.io/badge/Pypi-Install-brightgreen?logo=pypi)](https://pypi.org/project/getindianname/)
[![Run on Collab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1P84zjhjrGmV0rsRrnvTeeSbjQRtt1slQ?usp=sharing) <br>
[![Owner : Devesh Singh](https://img.shields.io/badge/Owner%20-Devesh%20Singh-blue.svg?style=flat-square)](https://instagram.com/devesh92744)
[![Available on Pypi](https://img.shields.io/badge/Available%20on%20-Pypi-brightgreen.svg?style=flat-square)](https://pypi.org/project/getindianname/)
[![Last Update](https://img.shields.io/badge/dynamic/xml?color=blue&label=Last%20Update&query=update&url=https%3A%2F%2Fraw.githubusercontent.com%2FTechUX%2Fgetindianname%2Fmain%2Fassets%2Flastupdate.xml&style=flat-square&?cacheSeconds=5)](https://github.com/TechUX/getindianname#changelogs) <br><br>
**Package Updated on :** ![Update On](https://img.shields.io/badge/dynamic/xml?color=Ffffff&label=%20&query=update&url=https%3A%2F%2Fraw.githubusercontent.com%2FTechUX%2Fgetindianname%2Fmain%2Fassets%2Flastupdate.xml) <br>[See Changelogs](#changelogs---)<br>

[![Total Downloads](https://pepy.tech/badge/getindianname)](https://pepy.tech/project/getindianname)
[![Downloads](https://pepy.tech/badge/getindianname/week)](https://pepy.tech/project/getindianname)
[![Downloads](https://pepy.tech/badge/getindianname/month)](https://pepy.tech/project/getindianname)
[![getindianname](https://snyk.io/advisor/python/getindianname/badge.svg)](https://snyk.io/advisor/python/getindianname)

This package have ability to generate 50K+ Indian Names [Hindi Names] for various uses. [See Project Ideas](#project-ideas)<br>
Generate Indian Names Randomly from various region of India. We add new names daily.

## What's New ? [See Changelogs](#changelogs---)
- Enable console/command line utility
- Added more names

# Table Of Content
- [Installation](#installation)
- [Statistics](#statistics)
- [Usages](#usage)
  - [Sample Example](#sample-example)
- [Features](#features)
- [Project Ideas](#project-ideas)
- [Changelogs](#changelogs---)
- [Contribution](#contributing)

## Installation
This package is available on pypi.<br>[Check Here](https://pypi.org/project/getindianname)

``` console
 pip install getindianname 
```
[![Run on Collab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1P84zjhjrGmV0rsRrnvTeeSbjQRtt1slQ?usp=sharing)
## Statistics
**Downloads** from *[pypi.org](https://pypi.org/project/getindianname)*

[![Total Downloads](https://pepy.tech/badge/getindianname)](https://pepy.tech/project/getindianname)
[![Downloads](https://pepy.tech/badge/getindianname/week)](https://pepy.tech/project/getindianname)
[![Downloads](https://pepy.tech/badge/getindianname/month)](https://pepy.tech/project/getindianname)
[![getindianname](https://snyk.io/advisor/python/getindianname/badge.svg)](https://snyk.io/advisor/python/getindianname)

## Usage
You will need to *_import getindianname_* on python program or python shell before use.
``` python
from getindianname import *
```
For **Command Line Utility** *CLI* or to print names directly from terminal/command prompt, use :
``` console
$ name
or
$ indianname
```
Use with flags to gain more control :
``` console
$ name male     // generate male name
$ name female   // generate female name
$ name random   // generate random name
```

### Sample Example
[![Run on Collab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1P84zjhjrGmV0rsRrnvTeeSbjQRtt1slQ?usp=sharing)
``` Python
>>> import getindianname as name

#random name
>>> print(name.randname())
Sanket Seth

#Female Name
>>> print(name.female())
Nitya Divedi

#Male Name
>>> print(name.male())
Abhijeet Pandey

```
For *_command line operation_* type this
```console
$ indianname
```


You can generate Names :
- Randomly name
using function ```randname()```

- Male name
using function ``` male() ```

- Female name
 using function ``` female()```

## Features
- Command Line Utility
- Update on latest version automatically
- Update names automatically
- 10+ Names added daily
- Create 70000+ Names
- Create male and female names separately
- Create Random Names
- Add Your own Names

## Project Ideas
- Fake Indian Name Generator
- Fake e-mail address generator
- Dumb Data Generator
- Generate Data for testing Form Filing
- Use it for Bulk Form filling spam checking
- And Much more like that

## Changelogs   <a href="https://pypi.org/rss/project/getindianname/releases.xml"><img src="https://www.svgrepo.com/show/25140/rss.svg" width="20px"></a>
- This Version : v1.0.5 _[01 March 2023]_
  - Command Line operations added
  - Added more names
  - Bugs fixed and performance improvements
 
- Version : v1.0.4 _[19 May 2021]_
  - Automatic Update from pypi.org added
  - Automatic Updates of Name Added
  - Bugs fixed and performance improvements

- Version : 1.0.3
   - Release on : December 20 , 2020
   - Full Documentation
   - Large list of Names
   - Bugs Fixed
- Version 1.0.2
   - Release on : December 19 , 2020
   - Few Names
   - Lack of Documentation
   - Performance improvement 
- Version 1.0.1
  - Release on : December 19 , 2020
  - First Release
  - No Documentation 

## [Contributing](https://github.com/devesh7272/getindianname/blob/main/CONTRIBUTING.md#contributing-to-getindianname)
See [Contributing.md](https://github.com/devesh7272/getindianname/blob/main/CONTRIBUTING.md#contributing-to-getindianname)

To add your own name you should follow these steps
- Fork this repo [From GitHub](https://github.com/devesh7272/getindianname)
- Edit malename and femalename file and add the male female names and titles separately
- Commit change and pull request

You also send names on my email 
connect.world12345@gmail.com

Thank you

## License
[![Awesome Badges](https://img.shields.io/badge/Made%20by-Devesh%20Singh-blue.svg)](https://www.facebook.com/devesh790)

Made with ❤ in India 🇮🇳

This Repository is Licensed Under MIT License.

See [LICENSE](https://github.com/devesh7272/getindianname/blob/main/LICENSE) for more
