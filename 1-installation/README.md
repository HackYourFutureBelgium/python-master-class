# Installing Python

Python is a versatile and widely-used programming language. To start writing Python code, you need to install Python on your system. This guide will walk you through the installation process on Windows, Mac, and Ubuntu.

## Windows

### 1. Download Python Installer

1. Visit the official Python website at [python.org](https://www.python.org/downloads/windows/).

2. Click on the "Downloads" tab and select the latest version of Python (e.g., Python 3.10.1) for Windows.

3. Scroll down to the "Files" section and choose the installer that matches your system. Most users should choose the "Windows installer (64-bit)".

### 2. Run the Installer

1. After downloading the installer, run the executable file (e.g., `python-3.10.1-amd64.exe`).

2. Check the box that says "Add Python x.x to PATH" during installation. This ensures that Python is added to your system's PATH environment variable, making it accessible from the command line.

3. Click "Install Now" and follow the installation wizard's instructions.

### 3. Verify Installation

1. Open a Command Prompt by searching for "cmd" in the Start menu.

2. Type `python --version` and press Enter. You should see the installed Python version.

## Mac

### 1. Install Homebrew (if not already installed)

1. Open Terminal.

2. Install Homebrew by running the following command:

   ```shell
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

3. Follow the on-screen instructions to complete the installation.

### 2. Install Python

1. Once Homebrew is installed, you can install Python by running the following command:

   ```shell
   brew install python
   ```

2. After the installation is complete, you can verify the Python version by running `python3 --version` in the Terminal.

## Ubuntu

### 1. Update Package Lists

Open a terminal window and update the package lists for your system:

```shell
sudo apt update
```

### 2. Install Python

1. You can install Python 3 with the following command:

   ```shell
   sudo apt install python3
   ```

2. To check the installed Python version, run:

   ```shell
   python3 --version
   ```

### 3. Install pip (Python Package Manager)

1. Install pip for Python 3 with:

   ```shell
   sudo apt install python3-pip
   ```

2. Verify the installation by running:

   ```shell
   pip3 --version
   ```
