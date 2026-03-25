"""
NumPy Examples - Array Operations and Mathematical Functions
"""

import numpy as np


def basic_array_operations():
    """Demonstrate basic NumPy array creation and operations."""
    print("=== Basic Array Operations ===")
    
    # Create arrays
    arr1 = np.array([1, 2, 3, 4, 5])
    arr2 = np.array([10, 20, 30, 40, 50])
    
    print(f"Array 1: {arr1}")
    print(f"Array 2: {arr2}")
    
    # Basic operations
    print(f"Addition: {arr1 + arr2}")
    print(f"Subtraction: {arr2 - arr1}")
    print(f"Multiplication: {arr1 * arr2}")
    print(f"Division: {arr2 / arr1}")
    print()


def array_attributes():
    """Demonstrate NumPy array attributes."""
    print("=== Array Attributes ===")
    
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    
    print(f"Array:\n{arr}")
    print(f"Shape: {arr.shape}")
    print(f"Dimensions: {arr.ndim}")
    print(f"Size: {arr.size}")
    print(f"Data type: {arr.dtype}")
    print()


def array_creation_methods():
    """Demonstrate various array creation methods."""
    print("=== Array Creation Methods ===")
    
    # Zeros
    zeros = np.zeros((3, 3))
    print(f"Zeros:\n{zeros}\n")
    
    # Ones
    ones = np.ones((2, 4))
    print(f"Ones:\n{ones}\n")
    
    # Identity matrix
    identity = np.eye(3)
    print(f"Identity:\n{identity}\n")
    
    # Range
    range_arr = np.arange(0, 10, 2)
    print(f"Range (0 to 10, step 2): {range_arr}\n")
    
    # Linspace
    linspace = np.linspace(0, 1, 5)
    print(f"Linspace (5 values between 0 and 1): {linspace}\n")
    
    # Random
    random = np.random.rand(3, 3)
    print(f"Random 3x3:\n{random}\n")


def mathematical_functions():
    """Demonstrate NumPy mathematical functions."""
    print("=== Mathematical Functions ===")
    
    arr = np.array([1, 4, 9, 16, 25])
    
    print(f"Original array: {arr}")
    print(f"Square root: {np.sqrt(arr)}")
    print(f"Exponential: {np.exp([1, 2, 3])}")
    print(f"Logarithm: {np.log([1, np.e, np.e**2])}")
    print()


def statistical_operations():
    """Demonstrate statistical operations."""
    print("=== Statistical Operations ===")
    
    arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    
    print(f"Array:\n{arr}")
    print(f"Mean: {np.mean(arr)}")
    print(f"Median: {np.median(arr)}")
    print(f"Standard deviation: {np.std(arr)}")
    print(f"Variance: {np.var(arr)}")
    print(f"Min: {np.min(arr)}")
    print(f"Max: {np.max(arr)}")
    print(f"Sum: {np.sum(arr)}")
    print()


def array_indexing_slicing():
    """Demonstrate array indexing and slicing."""
    print("=== Array Indexing and Slicing ===")
    
    arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    
    print(f"Original array:\n{arr}")
    print(f"Element at [1, 2]: {arr[1, 2]}")
    print(f"First row: {arr[0, :]}")
    print(f"Second column: {arr[:, 1]}")
    print(f"Sub-array:\n{arr[0:2, 1:3]}")
    print()


def array_reshaping():
    """Demonstrate array reshaping operations."""
    print("=== Array Reshaping ===")
    
    arr = np.arange(12)
    print(f"Original array: {arr}")
    
    reshaped = arr.reshape(3, 4)
    print(f"Reshaped to 3x4:\n{reshaped}")
    
    flattened = reshaped.flatten()
    print(f"Flattened: {flattened}")
    
    transposed = reshaped.T
    print(f"Transposed:\n{transposed}")
    print()


def linear_algebra():
    """Demonstrate linear algebra operations."""
    print("=== Linear Algebra Operations ===")
    
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[5, 6], [7, 8]])
    
    print(f"Matrix A:\n{a}")
    print(f"Matrix B:\n{b}")
    
    # Matrix multiplication
    product = np.dot(a, b)
    print(f"Matrix multiplication (A·B):\n{product}")
    
    # Determinant
    det = np.linalg.det(a)
    print(f"Determinant of A: {det}")
    
    # Inverse
    inv = np.linalg.inv(a)
    print(f"Inverse of A:\n{inv}")
    print()


if __name__ == "__main__":
    print("=" * 60)
    print("NumPy Examples")
    print("=" * 60)
    print()
    
    basic_array_operations()
    array_attributes()
    array_creation_methods()
    mathematical_functions()
    statistical_operations()
    array_indexing_slicing()
    array_reshaping()
    linear_algebra()
    
    print("=" * 60)
    print("All NumPy examples completed successfully!")
    print("=" * 60)
