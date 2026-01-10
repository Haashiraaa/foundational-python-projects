# Temperature Converter

A Python-based interactive command-line application for converting temperatures between Kelvin, Celsius, and Fahrenheit with a user-friendly interface and robust validation.

## Overview

Temperature Converter is a streamlined utility that enables seamless conversion between the three primary temperature scales used in science and everyday life. Built with clean architecture principles, the application features comprehensive error handling, colored console output, and an intuitive workflow that guides users through each conversion step.

## Features

### Supported Conversions

The application supports all six bidirectional conversion paths:

- **Kelvin ↔ Celsius**
- **Kelvin ↔ Fahrenheit**
- **Celsius ↔ Fahrenheit**

### Key Capabilities

- **Multi-unit Support**: Convert between K (Kelvin), °C (Celsius), and °F (Fahrenheit)
- **High Precision**: Handles both integer and floating-point temperature values
- **Real-time Validation**: Instant feedback on invalid inputs
- **Interactive Guide**: Optional user guide on startup
- **Colored Output**: Rich console formatting for better readability
- **Quick Exit**: Type `q` at any prompt to exit immediately

## Technical Architecture

### Core Components

- **`main_launcher.py`**: Application entry point and main loop
- **`logic.py`**: Conversion algorithms and formulas
- **`validator.py`**: Input validation, routing, and user interaction
- **`guide.py`**: User documentation display

### Class Structure

#### ConverterLogic Class
Contains all temperature conversion methods using standard formulas:
- `kelvin_to_celsius()`: K → °C conversion
- `kelvin_to_fahrenheit()`: K → °F conversion
- `celsius_to_kelvin()`: °C → K conversion
- `celsius_to_fahrenheit()`: °C → °F conversion
- `fahrenheit_to_kelvin()`: °F → K conversion
- `fahrenheit_to_celsius()`: °F → °C conversion

Uses `KELVIN_OFFSET` constant (273.15) for accurate conversions.

#### Validate Class
Manages the complete user interaction flow:
- `check_exit()`: Monitors for quit command
- `get_unit()`: Prompts for source temperature unit
- `get_value()`: Prompts for temperature value
- `get_converted_unit()`: Prompts for target unit
- `parse_returns()`: Validates all inputs and returns structured result
- `validate_conversions()`: Orchestrates full conversion workflow

#### Routes Class
Maps unit pairs to their corresponding conversion functions using a dictionary-based routing system for efficient lookup.

#### ValidationResult Dataclass
Generic wrapper for validation outcomes containing:
- `ok`: Boolean success/failure status
- `message`: Optional error message
- `data`: Optional result data

## Dependencies

- **Python 3.7+** (uses dataclasses and type hints)
- **rich**: Enhanced console output with colors and formatting
- **haashi_pkg.utility.utils**: Custom utility package for screen management
- **typing**: Type annotations for better code clarity
- **logging**: Application logging support

## Installation

```bash
# Install required dependencies
pip install rich

# Clone the repository
git clone https://github.com/Haashiraaa/foundational-python-projects.git
cd foundational-python-projects/temperature_converter
```

## Usage

### Running the Application

```bash
python main_launcher.py
```

### Workflow

1. **Optional Guide**: Choose whether to view the usage guide on startup
2. **Enter Source Unit**: Type `k`, `c`, or `f`
3. **Enter Value**: Provide the temperature value (numeric)
4. **Enter Target Unit**: Type the unit you want to convert to
5. **View Result**: Conversion result is displayed with proper unit symbol

### Example Conversion

```
Welcome to the Temperature Converter!

Would you like to see the guide? (y/n): n

Welcome to the Temperature Converter!

Unit: c
Value: 100
Converted Unit: f

Result = 212.0°F
```

### Unit Abbreviations

- `k` → Kelvin (K)
- `c` → Celsius (°C)
- `f` → Fahrenheit (°F)

### Exit Options

- Type `q` at any input prompt to exit immediately
- Use `Ctrl+C` for keyboard interrupt exit

## Error Handling

The application includes comprehensive error handling:

- **Invalid Unit**: Alerts when an unrecognized unit is entered
- **Invalid Value**: Catches non-numeric temperature inputs
- **Unsupported Conversion**: Validates that the conversion path exists
- **Type Safety**: Uses type hints and generic types for robust validation
- **Graceful Exit**: Handles keyboard interrupts cleanly

All error messages are displayed in bright red for visibility and automatically clear after a brief timeout.

## Design Patterns

- **Separation of Concerns**: Logic, validation, and UI are cleanly separated
- **Strategy Pattern**: Routes class implements function mapping strategy
- **Result Pattern**: ValidationResult wraps outcomes with success/failure status
- **Constants Management**: Centralized error messages in Constants class
- **Type Safety**: Extensive use of type hints and generics
- **Dataclasses**: Structured data with ValidationResult

## Conversion Formulas

### Celsius ↔ Fahrenheit
- °F = (°C × 9/5) + 32
- °C = (°F - 32) × 5/9

### Celsius ↔ Kelvin
- K = °C + 273.15
- °C = K - 273.15

### Fahrenheit ↔ Kelvin
- K = (°F - 32) × 5/9 + 273.15
- °F = (K - 273.15) × 9/5 + 32

## Future Enhancements

Potential features for expansion:
- Add Rankine temperature scale
- Batch conversion mode (convert multiple values at once)
- File input/output for bulk conversions
- Conversion history tracking
- Configuration file for default units
- GUI version using Tkinter or PyQt


## Author

Haashiraaa

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page or submit a pull request.
