# extractor

A command-line tool that extracts API endpoints from React Native Android applications by decompiling the APK and scanning the JavaScript bundle.

## How it works

1. Decompiles the APK using `apktool`
2. Detects whether the app was built with React Native by inspecting `AndroidManifest.xml` and looking for `assets/index.android.bundle`
3. Beautifies the JavaScript bundle with `jsbeautifier`
4. Extracts URLs and API endpoints using regex pattern matching


## Requirements

### System dependencies

- Python 3.x
- [apktool](https://apktool.org/) — must be installed and available on `PATH`

### Python dependencies

| Package | Version |
|---|---|
| jsbeautifier | 1.14.7 |
| editorconfig | 0.12.3 |
| six | 1.16.0 |


## Installation

```bash
git clone https://github.com/h4pp1n3ss/extractor.git
cd extractor
pipenv install -r requirements.txt
```


## Usage

```bash
python extractor.py --apk <APK_FILE>
```

### Example

```bash
python extractor.py --apk com.example.app.apk
```

The tool will:
- Decompile the APK into `com.example.app_out/`
- Detect React Native usage
- Extract and print all discovered endpoints


## Project structure

```
extractor/
├── extractor.py                  # Entry point / CLI argument parsing
└── react_extractor/
    ├── main.py                   # Orchestration logic
    ├── commands.py               # apktool decompilation, bundle extraction, endpoint extraction
    ├── utils.py                  # Helpers: tool checks, file checks, React Native detection
    └── exceptions.py             # Custom exceptions
```


## Exceptions

| Exception | Raised when |
|---|---|
| `ExecutionFailedException` | `apktool` returns an error during decompilation |
| `BinaryNotFoundException` | A required binary is not found on the system |
| `FileNotFoundException` | An expected file is missing |


## Author

- **h4pp1n3ss**
- Version: 0.1
