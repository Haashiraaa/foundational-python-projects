# Foundational Python Projects

A collection of beginner-friendly Python command-line applications demonstrating fundamental programming concepts, clean code architecture, and practical problem-solving skills.

## Overview

This repository contains educational Python projects designed to showcase core programming principles including input validation, error handling, modular design, and user-friendly interfaces. Each project is self-contained, well-documented, and built with industry-standard practices in mind.

## Projects

### 1. Number Analyzer
An interactive mathematical operations tool that performs various checks and calculations on numbers.

**Features:**
- Even/Odd number detection
- Prime number validation
- Square root calculation with customizable precision

**Tech Stack:** Python 3.10+, custom utility package

[→ View Number Analyzer README](projects/number-analyzer/README.md)

---

### 2. Temperature Converter
A robust temperature conversion utility supporting all major temperature scales.

**Features:**
- Bidirectional conversions between Kelvin, Celsius, and Fahrenheit
- Real-time input validation
- Rich console output with colored formatting

**Tech Stack:** Python 3.10+, Rich library, custom utility package

[→ View Temperature Converter README](projects/temperature-converter/README.md)

---

## Prerequisites

### Required Dependency: haashi_pkg

Both projects depend on **haashi_pkg**, a custom utility package that provides:
- Screen management utilities (clearing lines, clearing screen)
- Logging configuration
- Common helper functions

**Installation:**

```bash
# Clone the haashi_pkg repository
git clone https://github.com/Haashiraaa/my-packages.git
cd haashiraaa_pkg

# Install the package
pip install -e .
```

For more details about haashi_pkg capabilities, see the [haashi_pkg repository](https://github.com/Haashiraaa/my-packages).

### Additional Dependencies

Install project-specific dependencies:

```bash
# For Temperature Converter
pip install rich
```

## Getting Started

### 1. Install haashi_pkg (Required)
Follow the installation instructions in the Prerequisites section above.

### 2. Clone This Repository
```bash
git clone https://github.com/Haashiraaa/foundational-python-projects.git
cd foundational-python-projects
```

### 3. Navigate to a Project
```bash
cd projects/number-analyzer
# or
cd projects/temperature-converter
```

### 4. Run the Application
```bash
python main_launcher.py
```

## Repository Structure

```
foundational-python-projects/
├── README.md                      # This file
└── projects/
    ├── number-analyzer/
    │   ├── README.md
    │   ├── main_launcher.py
    │   └── classes/
    │       ├── logic.py
    │       └── validator.py
    └── temperature-converter/
        ├── README.md
        ├── main_launcher.py
        ├── guide.py
        └── classes/
            ├── logic.py
            └── validator.py
```

## Design Philosophy

These projects emphasize:

- **Clean Architecture**: Separation of concerns with dedicated logic, validation, and UI layers
- **Type Safety**: Comprehensive type hints for better code documentation and IDE support
- **Error Handling**: Robust input validation with user-friendly error messages
- **User Experience**: Intuitive interfaces with helpful prompts and clear feedback
- **Modularity**: Reusable components and well-defined class responsibilities
- **Best Practices**: Following Python conventions and modern programming patterns

## Learning Objectives

These projects are ideal for:

- Understanding object-oriented programming in Python
- Learning input validation and error handling patterns
- Practicing modular code organization
- Exploring user interface design for CLI applications
- Building maintainable and testable code

## Technology Stack

- **Python 3.10+**: Modern Python features including pattern matching and enhanced type hints
- **Rich**: Terminal formatting and colored output (Temperature Converter)
- **haashi_pkg**: Custom utilities for screen management and logging
- **Type Hints**: Full type annotation for code clarity
- **Dataclasses**: Structured data representation (Temperature Converter)

## Contributing

Contributions are welcome! Whether it's bug fixes, new features, or additional projects, feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-project`)
3. Commit your changes (`git commit -m 'Add new project'`)
4. Push to the branch (`git push origin feature/new-project`)
5. Open a Pull Request

### Contribution Guidelines

- Maintain consistent code style with existing projects
- Include comprehensive docstrings and type hints
- Add README documentation for new projects
- Ensure error handling is robust and user-friendly
- Test thoroughly before submitting

## Future Projects

Planned additions to this repository:

- **Calculator**: Basic arithmetic operations with expression parsing
- **To-Do List Manager**: Task management with file persistence
- **Password Generator**: Secure password creation with customizable rules
- **Expense Tracker**: Personal finance logging and reporting
- **Unit Converter**: Multi-unit conversion tool (length, weight, volume)

## License

This project is licensed under the MIT License.
See the [LICENSE](LICENSE) file for details.

## Author

**Haashiraaa**

- GitHub: [@Haashiraaa](https://github.com/Haashiraaa)

## Acknowledgments

- Built with Python's standard library and select third-party packages
- Inspired by common beginner programming challenges
- Uses haashi_pkg for shared utilities across projects

---

**Note:** These projects are educational in nature and designed to demonstrate fundamental programming concepts. They serve as practical examples for learning Python development and software engineering principles.
