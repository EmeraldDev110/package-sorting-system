def sort(width: float, height: float, length: float, mass: float) -> str:
    """
    Sort packages into different stacks based on their dimensions and mass.
    
    Args:
        width (float): Width of the package in centimeters
        height (float): Height of the package in centimeters
        length (float): Length of the package in centimeters
        mass (float): Mass of the package in kilograms
    
    Returns:
        str: Stack designation ('STANDARD', 'SPECIAL', or 'REJECTED')
    """
    # Calculate volume
    volume = width * height * length
    
    # Check if package is bulky
    is_bulky = (volume >= 1_000_000 or 
                width >= 150 or 
                height >= 150 or 
                length >= 150)
    
    # Check if package is heavy
    is_heavy = mass >= 20
    
    # Sort package based on conditions
    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"


# Test cases
def run_tests():
    """Run comprehensive tests for the sort function."""
    
    test_cases = [
        # Standard cases
        {
            'input': (100, 100, 50, 10),
            'expected': "STANDARD",
            'description': "Standard package"
        },
        # Bulky cases
        {
            'input': (100, 100, 100, 10),
            'expected': "SPECIAL",
            'description': "Bulky by volume"
        },
        {
            'input': (150, 50, 50, 10),
            'expected': "SPECIAL",
            'description': "Bulky by dimension"
        },
        # Heavy cases
        {
            'input': (100, 100, 50, 20),
            'expected': "SPECIAL",
            'description': "Heavy package"
        },
        # Rejected cases
        {
            'input': (150, 100, 100, 20),
            'expected': "REJECTED",
            'description': "Both bulky and heavy"
        },
        # Edge cases
        {
            'input': (149.9, 149.9, 149.9, 19.9),
            'expected': "STANDARD",
            'description': "Just under limits"
        },
        {
            'input': (150, 150, 150, 20),
            'expected': "REJECTED",
            'description': "At the limits"
        }
    ]
    
    passed = 0
    failed = 0
    
    print("Running tests...")
    print("-" * 50)
    
    for test in test_cases:
        result = sort(*test['input'])
        if result == test['expected']:
            passed += 1
            status = "✓ PASSED"
        else:
            failed += 1
            status = "✗ FAILED"
            
        print(f"{status} | {test['description']}")
        print(f"Input: {test['input']}")
        print(f"Expected: {test['expected']}, Got: {result}")
        print("-" * 50)
    
    print(f"\nTest Summary:")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")
    print(f"Total: {passed + failed}")
    
if __name__ == "__main__":
    run_tests()