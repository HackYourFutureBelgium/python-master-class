# Installing Python on Windows, macOS, and Ubuntu

This comprehensive guide will walk you through the steps to install Python on three major operating systems: Windows, macOS, and Ubuntu. Follow the instructions below for your specific platform.

## Windows

### Step 1: Download Python Installer

1. Visit the [official Python website](https://www.python.org/downloads/) and click on the "Downloads" tab.

2. Scroll down to the "Looking for a specific release?" section and select the version of Python you want.

3. Choose the appropriate installer based on your Windows version (32-bit or 64-bit). Most modern systems are 64-bit.

### Step 2: Run the Installer

1. Double-click on the downloaded installer file (e.g., `python-3.x.x.exe`).

2. Check the box that says "Add Python x.x to PATH" during installation. This makes it easier to run Python from the command line.

3. Click "Install Now" to start the installation.

### Step 3: Verify Installation

1. Open a command prompt by pressing `Win + R`, typing `cmd`, and pressing Enter.

2. Type `python --version` or `python -V` and press Enter. You should see the installed Python version.

## macOS

### Step 1: Install Homebrew (if not installed)

1. Open a terminal window.

2. Run the following command to install Homebrew:
    ```bash
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```

### Step 2: Install Python

1. In the terminal, run the following command to install Python:

    ```bash
    brew install python
    ```

2. Homebrew will download and install Python on your system.

### Step 3: Verify Installation

1. Type `python3 --version` in the terminal and press Enter. You should see the installed Python version.

## Ubuntu

### Step 1: Update Package Lists

1. Open a terminal.

2. Run the following commands to update the package lists:
    ```bash
    sudo apt update
    sudo apt upgrade
    ```

### Step 2: Install Python

1. Run the following command to install Python:

    ```bash
    sudo apt install python3
    ```

2. Enter your password when prompted.

### Step 3: Verify Installation

1. Type `python3 --version` in the terminal and press Enter. You should see the installed Python version.
