# NinjaZipPy

NinjaZipPy is a simple Python utility to **zip and unzip `.7z` archives**.  
It was created as part of the **Gridplex Digital – Agentic AI Internship Qualifying Assignment**.

---

## ✨ Features
- Compress files or folders into `.7z` format.  
- Extract `.7z` archives into a folder.  
- Easy to use via **command line interface (CLI)**.  
- Lightweight implementation using [`py7zr`](https://pypi.org/project/py7zr/).

---

## 🚀 Installation

Clone this repository and install locally:

```bash
git clone https://github.com/<your-username>/NinjaZipPy.git
cd NinjaZipPy
pip install .
```
---

## 🔧 **Usage**
1. Zip a folder
ninjazippy zip myfolder archive.7z


This compresses myfolder into archive.7z.

2. Unzip an archive
ninjazippy unzip archive.7z extracted_folder


This extracts the contents of archive.7z into extracted_folder/.

---

## 📂 **Project Structure**
NinjaZipPy/

│── ninjazippy/

│   │── __init__.py

│   │── cli.py

│   │── core.py

│

│── setup.py

│── pyproject.toml

│── README.md


---

## 🛠️ **Requirements**

Python 3.8+

py7zr

## 📜 **License**

MIT License
