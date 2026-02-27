"""
Run All Examples - Execute all library examples in sequence
"""

import sys


def run_numpy_examples():
    """Run NumPy examples."""
    print("\n" + "=" * 70)
    print("RUNNING NUMPY EXAMPLES")
    print("=" * 70 + "\n")
    
    try:
        import numpy_examples
        print("\n✓ NumPy examples completed successfully!\n")
        return True
    except Exception as e:
        print(f"\n✗ Error running NumPy examples: {e}\n")
        return False


def run_pandas_examples():
    """Run Pandas examples."""
    print("\n" + "=" * 70)
    print("RUNNING PANDAS EXAMPLES")
    print("=" * 70 + "\n")
    
    try:
        import pandas_examples
        print("\n✓ Pandas examples completed successfully!\n")
        return True
    except Exception as e:
        print(f"\n✗ Error running Pandas examples: {e}\n")
        return False


def run_matplotlib_examples():
    """Run Matplotlib examples."""
    print("\n" + "=" * 70)
    print("RUNNING MATPLOTLIB EXAMPLES")
    print("=" * 70 + "\n")
    
    try:
        import matplotlib_examples
        print("\n✓ Matplotlib examples completed successfully!\n")
        return True
    except Exception as e:
        print(f"\n✗ Error running Matplotlib examples: {e}\n")
        return False


def run_seaborn_examples():
    """Run Seaborn examples."""
    print("\n" + "=" * 70)
    print("RUNNING SEABORN EXAMPLES")
    print("=" * 70 + "\n")
    
    try:
        import seaborn_examples
        print("\n✓ Seaborn examples completed successfully!\n")
        return True
    except Exception as e:
        print(f"\n✗ Error running Seaborn examples: {e}\n")
        return False


def main():
    """Main function to run all examples."""
    print("\n" + "=" * 70)
    print("RUNNING ALL DATA SCIENCE LIBRARY EXAMPLES")
    print("=" * 70)
    
    results = {
        'NumPy': run_numpy_examples(),
        'Pandas': run_pandas_examples(),
        'Matplotlib': run_matplotlib_examples(),
        'Seaborn': run_seaborn_examples()
    }
    
    # Print summary
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    
    for library, success in results.items():
        status = "✓ SUCCESS" if success else "✗ FAILED"
        print(f"{library:15s}: {status}")
    
    print("=" * 70)
    
    # Exit with appropriate code
    all_success = all(results.values())
    if all_success:
        print("\n🎉 All examples completed successfully!")
        print("Check the current directory for generated plots.\n")
        sys.exit(0)
    else:
        print("\n⚠ Some examples failed. Please check the error messages above.\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
