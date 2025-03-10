
# Keylogger & Keylogging Detector

## Overview

This project consists of two tools:

- **Keylogger** - A simple keylogger implemented using pynput that records keystrokes and logs them to a file.
- **Keylogging Detector** - A tool that scans running processes for specific keywords associated with keyloggers, allowing users to detect potential threats. The detector can also be used to identify other malicious processes by modifying the keyword list.

## Features

### Keylogger

- Runs in the terminal and records all keystrokes.
- Uses pynput for non-intrusive key logging.
- Logs output to a file for later analysis.

### Keylogging Detector

- Scans active processes for suspicious keywords.
- Allows users to customize the keyword list to detect different threats.
- Provides insight into potentially malicious activity running on the system.

## Requirements

Make sure you have Python installed, then install the necessary dependencies:

```bash
pip install pynput psutil
```

## Usage

### Running the Keylogger

```bash
python keylogger.py
```

This will start the keylogger in the terminal, and it will begin recording keystrokes to a log file.

### Running the Keylogging Detector

```bash
python detector.py
```

This will scan the running processes and output a list of processes matching the suspicious keywords.

## Customization

- Modify keywords in `detector.py` to expand detection capabilities for different types of malware.
- Adjust logging mechanisms in `keylogger.py` for different storage formats.

## Security Notice

This project is for educational and security research purposes only.

Running a keylogger without consent is illegal and unethical.

Use the detector to enhance security and detect unauthorized keylogging activity on your system.

## License

This project is open-source and available under the MIT License.
