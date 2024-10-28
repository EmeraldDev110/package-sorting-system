# Package Sorting System

## Overview

This Python package implements an automated sorting system for a robotic automation factory. The system categorizes packages into different stacks based on their dimensions and mass, following specific business rules for handling packages of various sizes and weights.

## Features

- Sorts packages into three categories: STANDARD, SPECIAL, and REJECTED
- Handles both metric measurements for dimensions (cm) and mass (kg)
- Includes comprehensive test suite
- Provides clear documentation and type hints

## Installation

1. Clone this repository:

```bash
git clone [your-repository-url]
cd package-sorter
```

2. No additional dependencies required - uses Python standard library only.

## Usage

### Basic Usage

```python
from package_sorter import sort

# Example usage
result = sort(width=100, height=50, length=80, mass=15)
print(result)  # Output: "STANDARD"
```

### Function Parameters

- `width` (float): Width of the package in centimeters
- `height` (float): Height of the package in centimeters
- `length` (float): Length of the package in centimeters
- `mass` (float): Mass of the package in kilograms

### Return Values

The function returns one of three strings:

- `"STANDARD"`: Normal packages that can be handled automatically
- `"SPECIAL"`: Packages that are either bulky or heavy
- `"REJECTED"`: Packages that are both bulky and heavy

## Business Rules

### Package Classifications

1. **Bulky Package**:

   - Volume ≥ 1,000,000 cm³ (1m³) OR
   - Any dimension ≥ 150 cm

2. **Heavy Package**:
   - Mass ≥ 20 kg

### Sorting Rules

- **STANDARD**: Neither bulky nor heavy
- **SPECIAL**: Either bulky or heavy (but not both)
- **REJECTED**: Both bulky and heavy

## Testing

The package includes a comprehensive test suite. To run the tests:

```bash
python package_sorter.py
```

### Test Cases Include:

- Standard packages
- Bulky packages (by volume and dimension)
- Heavy packages
- Rejected packages
- Edge cases

## Examples

```python
# Standard package
sort(100, 100, 50, 10)  # Returns: "STANDARD"

# Bulky package (by volume)
sort(100, 100, 100, 10)  # Returns: "SPECIAL"

# Heavy package
sort(100, 100, 50, 20)  # Returns: "SPECIAL"

# Rejected package (both bulky and heavy)
sort(150, 100, 100, 20)  # Returns: "REJECTED"
```

## Technical Details

- Python version: 3.6+
- No external dependencies
- Type hints included for better IDE support
- Comprehensive docstrings

## Error Handling

The current implementation assumes valid numeric inputs. For production use, consider adding input validation for:

- Negative values
- Zero values
- Non-numeric inputs
- None/null values

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

[Your Name]

## Version

1.0.0
