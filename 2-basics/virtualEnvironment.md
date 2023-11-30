# Python Virtual Environments Guide

## Introduction

Virtual environments in Python provide a self-contained space to manage dependencies and isolate project environments.

## 1. Why Use Virtual Environments?

-   **Isolation**: Prevents conflicts between project dependencies.
-   **Dependency Management**: Enables specific package versions for each project.
-   **Cleaner Projects**: Ensures a clean project directory without clutter.

## 2. Creating Virtual Environments

### On macOS

#### Using `venv`

1. Open Terminal.
2. Navigate to your project directory.
3. Run the following commands:

    ```bash
    # Create virtual environment
    python3 -m venv venv

    # Activate virtual environment
    source venv/bin/activate
    ```

4. You'll see the virtual environment name in your terminal prompt, indicating activation.

### On Windows

#### Using `venv` with Command Prompt

1. Open Command Prompt.
2. Navigate to your project directory.
3. Run the following commands:

    ```bash
    # Create virtual environment
    python -m venv venv

    # Activate virtual environment
    .\venv\Scripts\activate
    ```

4. You'll see the virtual environment name in your command prompt, indicating activation.

## 3. Activating and Deactivating Virtual Environments

-   **Activating on macOS and Windows:**

    ```bash
    # macOS
    source venv/bin/activate

    # Windows
    .\venv\Scripts\activate
    ```

-   **Deactivating:**
    ```bash
    deactivate
    ```

## 4. Installing Packages in Virtual Environments

-   **Using `pip`:**
    ```bash
    pip install package_name
    ```

## 5. Example Usage

```bash
# Create virtual environment on macOS
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install packages
pip install requests

# Check installed packages
pip list

# Deactivate virtual environment
deactivate
```

## 6. Best Practices

-   **Include virtual environment folder (`venv`) in `.gitignore`.**
-   **Document dependencies using `requirements.txt` or `Pipfile`.**
