import unittest
from coverage import Coverage
import sys
from typing import Dict, Tuple

def run_tests_with_coverage(test_class, source_module) -> Tuple[int, float, float]:
    """Run tests for a class and return test count, coverage, and error rate."""
    # Count actual test methods in the class
    test_count = len([method for method in dir(test_class) 
                     if method.startswith('test_')])
    
    # Set up coverage
    cov = Coverage()
    cov.start()
    
    # Run tests
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    result = unittest.TextTestRunner(stream=None).run(suite)
    
    # Stop coverage
    cov.stop()
    
    # Calculate metrics
    errors_and_failures = len(result.failures) + len(result.errors)
    error_rate = (errors_and_failures / test_count * 100) if test_count > 0 else 0
    
    # Get coverage
    total_stmts = 0
    covered_stmts = 0
    for filename in cov.get_data().measured_files():
        if source_module in filename:
            analysis = cov.analysis(filename)
            total_stmts = len(analysis[1])
            covered_stmts = len(analysis[2])
            break
    
    coverage = (covered_stmts / total_stmts * 100) if total_stmts > 0 else 0
    return test_count, coverage, error_rate

def print_table(title: str, results: Dict[str, Tuple[int, float, float]]):
    """Print results in a formatted table."""
    # Print header
    print(f"\n{title}")
    print("-" * 60)
    print(f"{'Prompt ID':<20} {'Test Cases':<12} {'Coverage (%)':<14} {'Error Rate (%)'}")
    print("-" * 60)
    
    # Print results
    total_tests = 0
    total_coverage = 0
    total_error_rate = 0
    count = 0
    
    for name, (tests, coverage, error_rate) in sorted(results.items()):
        print(f"{name:<20} {tests:<12d} {coverage:<14.1f} {error_rate:.1f}")
        total_tests += tests
        total_coverage += coverage
        total_error_rate += error_rate
        count += 1
    
    # Print average
    if count > 0:
        print("-" * 60)
        print(f"{'Average':<20} {total_tests/count:<12.1f} {total_coverage/count:<14.1f} {total_error_rate/count:.1f}")

def get_test_results(test_module_name: str, source_module_name: str) -> Dict[str, Tuple[int, float, float]]:
    """Get test results for a specific test module."""
    # Import test module
    test_module = __import__(test_module_name)
    
    # Get all test classes
    test_classes = {
        name: cls for name, cls in test_module.__dict__.items()
        if isinstance(cls, type) 
        and issubclass(cls, unittest.TestCase) 
        and cls != unittest.TestCase
    }
    
    # Run tests and collect results
    results = {}
    for name, test_class in test_classes.items():
        # Remove 'Test' from the name
        name = name.replace('Test', '')
        # Get test statistics
        test_count, coverage, error_rate = run_tests_with_coverage(test_class, source_module_name)
        results[name] = (test_count, coverage, error_rate)
    
    return results

def main():
    # Test GPT implementation
    gpt_results = get_test_results('newTestsGPT', 'newPromptsGPT.py')
    print_table("GPT CODE AND TEST SUMMARY", gpt_results)
    
    print("\n" + "="*60 + "\n")  # Separator between tables
    
    # Test DeepSeek implementation
    deepseek_results = get_test_results('newTestsDeepSeek', 'newPromptsDeepSeek.py')
    print_table("DEEPSEEK CODE AND TEST SUMMARY", deepseek_results)

if __name__ == '__main__':
    main() 