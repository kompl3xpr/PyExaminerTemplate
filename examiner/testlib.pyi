from typing import Any, Tuple, Callable, List, Self

class BColors:
    """
    Terminal color codes class for formatting output.
    终端颜色代码类，用于格式化输出。
    """
    BOLD: str
    BLUE: str
    YELLOW: str
    GREEN: str
    RED: str
    ENDC: str  # Ends formatting
    HEADER: str  # Used for titles or highlights


class Args:
    """
    Class to encapsulate and handle positional arguments.
    用于封装和处理位置参数的类。
    """
    def __init__(self, *args):
        """
        Initialize with any number of arguments.
        使用任意数量的参数初始化。

        :param args: Positional arguments (位置参数)
        """

    def get(self):
        """
        Retrieve stored arguments as a tuple.
        以元组形式获取存储的参数。

        :return: Tuple of arguments (参数元组)
        """


class TestResult:
    """
    Base class for test results.
    测试结果基类。
    """
    def get_handled(self, suite: 'TestSuite', case: 'TestCase'):
        """
        Handle the test result and display related information.
        处理测试结果并显示相关信息。

        :param suite: The test suite containing this result (包含此结果的测试套件)
        :param case: The specific test case related to this result (与此结果相关的具体测试案例)
        """

    def failed(self) -> bool:
        """
        Determine if the test result indicates a failure.
        判断测试结果是否表明测试失败。

        :return: True if failed, otherwise False (如果失败返回 True，否则返回 False)
        """


class TestResults:
    class UnexpectedResult(TestResult):
        """
        Represents a test case where the actual result was unexpected.
        表示实际结果与预期不符的测试案例。
        """
        def __init__(self, actual_result: Any):
            """
            Initialize with the unexpected actual result.
            使用不符合预期的实际结果初始化。

            :param actual_result: The result obtained (获取的结果)
            """

        def get_handled(self, suite: 'TestSuite', case: 'TestCase'):
            """
            Display details about the mismatch.
            显示结果不匹配的详细信息。
            """

    class ThrowException(TestResult):
        """
        Represents a test case where an exception was thrown.
        表示在测试案例中抛出异常。
        """
        def __init__(self, exception: Exception):
            """
            Initialize with the exception thrown.
            使用抛出的异常初始化。

            :param exception: The exception that occurred (发生的异常)
            """

        def get_handled(self, suite: 'TestSuite', case: 'TestCase'):
            """
            Display exception details.
            显示异常的详细信息。
            """

    class Pass(TestResult):
        """
        Represents a passing test case.
        表示通过的测试案例。
        """
        def failed(self) -> bool:
            """
            Always return False, as this result indicates success.
            始终返回 False，因为此结果表示成功。
            """


class TestCase:
    """
    A single test case consisting of input and expected output.
    单个测试案例，包括输入和预期输出。
    """
    def __init__(self, input_data, expected_output: Any):
        """
        Initialize with test input and expected output.
        使用测试输入和预期输出初始化。

        :param input_data: Input data for the test (测试的输入数据)
        :param expected_output: Expected result (预期结果)
        """

    def test(self, solution: Callable) -> TestResult:
        """
        Run the test case with a given solution and return the result.
        使用给定的解决方案运行测试案例并返回结果。

        :param solution: Function to test (要测试的函数)
        :return: Test result instance (测试结果实例)
        """


class TestSuite:
    """
    A suite of test cases for a single solution.
    用于单个解决方案的一组测试案例。
    """
    def __init__(self, solution: Callable):
        """
        Initialize with a solution function.
        使用解决方案函数初始化。

        :param solution: The solution function to test (要测试的解决方案函数)
        """

    def __call__(self, input_data, expected_output: Any) -> Self:
        """
        Add a test case to the suite.
        将测试案例添加到套件中。

        :param input_data: Input for the test case (测试案例的输入)
        :param expected_output: Expected output for the test case (测试案例的预期输出)
        :return: Self instance (返回当前实例)
        """

    def run(self) -> bool:
        """
        Run all test cases in the suite and report results.
        运行套件中的所有测试案例并报告结果。

        :return: True if all tests pass, otherwise False (如果所有测试通过返回 True，否则返回 False)
        """


class TestFramework:
    """
    Framework to manage and run multiple test suites.
    用于管理和运行多个测试套件的框架。
    """
    def __init__(self):
        """
        Initialize the test framework.
        初始化测试框架。
        """

    def add(self, test_suite: TestSuite):
        """
        Add a test suite to the framework.
        向框架添加测试套件。

        :param test_suite: Test suite to add (要添加的测试套件)
        """

    def run_all(self):
        """
        Run all test suites and summarize the results.
        运行所有测试套件并汇总结果。
        """
