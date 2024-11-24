# Tinc
Talk is not cheap


# Simple Example

```shell
(py311) (base) xx@zhuyudeMacBook-Air Tinc % python main.py

please input your api key for TheB.AI: xxxxxx
Enter your design prompt (type 'exit' to quit): numpy矩阵乘法
Code has been written to ./output/example_directory/generated_code.py
Require permission to execute. Grant permission? (yes/no): yes
Executing code: ./output/example_directory/generated_code.py
Code has been written to ./output/example_directory/test_generated_code.py
Require permission to execute. Grant permission? (yes/no): yes
Executing code: ./output/example_directory/test_generated_code.py

```

## result
code and test code will be generated in `output` folder

```python
# generated_code.py
import numpy as np

def matrix_multiplication(matrix1, matrix2):
    result = np.dot(matrix1, matrix2)
    return result

# 测试代码
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])
result = matrix_multiplication(matrix1, matrix2)
print(result)
```

```python
# test_generated_code.py
import numpy as np
from generated_code import matrix_multiplication

def test_matrix_multiplication():
    matrix1 = np.array([[1, 2], [3, 4]])
    matrix2 = np.array([[5, 6], [7, 8]])
    expected_result = np.array([[19, 22], [43, 50]])
    assert np.array_equal(matrix_multiplication(matrix1, matrix2), expected_result)

    matrix3 = np.array([[1, 2, 3], [4, 5, 6]])
    matrix4 = np.array([[7, 8], [9, 10], [11, 12]])
    expected_result2 = np.array([[58, 64], [139, 154]])
    assert np.array_equal(matrix_multiplication(matrix3, matrix4), expected_result2)

    matrix5 = np.array([[1, 2], [3, 4], [5, 6]])
    matrix6 = np.array([[7, 8, 9], [10, 11, 12]])
    expected_result3 = np.array([[27, 30, 33], [61, 68, 75], [95, 106, 117]])
    assert np.array_equal(matrix_multiplication(matrix5, matrix6), expected_result3)

if __name__ == "__main__":
    test_matrix_multiplication()
```

# Check log
Check log from `project.log`

```shell
2024-11-24 20:12:17 - INFO - INTERACTION: User prompt: numpy矩阵乘法
2024-11-24 20:12:19 - INFO - INTERACTION: Generated Code: import numpy as np

def matrix_multiplication(matrix1, matrix2):
    result = np.dot(matrix1, matrix2)
    return result

# 测试代码
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])
result = matrix_multiplication(matrix1, matrix2)
print(result)
2024-11-24 20:12:26 - INFO - EXECUTION: Execution result: Execution completed.
Output:
[[19 22]
 [43 50]]

2024-11-24 20:12:29 - INFO - INTERACTION: Generated Test Code: import numpy as np
from generated_code import matrix_multiplication

def test_matrix_multiplication():
    matrix1 = np.array([[1, 2], [3, 4]])
    matrix2 = np.array([[5, 6], [7, 8]])
    expected_result = np.array([[19, 22], [43, 50]])
    assert np.array_equal(matrix_multiplication(matrix1, matrix2), expected_result)

    matrix3 = np.array([[1, 2, 3], [4, 5, 6]])
    matrix4 = np.array([[7, 8], [9, 10], [11, 12]])
    expected_result2 = np.array([[58, 64], [139, 154]])
    assert np.array_equal(matrix_multiplication(matrix3, matrix4), expected_result2)

    matrix5 = np.array([[1, 2], [3, 4], [5, 6]])
    matrix6 = np.array([[7, 8, 9], [10, 11, 12]])
    expected_result3 = np.array([[27, 30, 33], [61, 68, 75], [95, 106, 117]])
    assert np.array_equal(matrix_multiplication(matrix5, matrix6), expected_result3)

if __name__ == "__main__":
    test_matrix_multiplication()
2024-11-24 20:12:40 - INFO - EXECUTION: Test execution result: Execution completed.
Output:
[[19 22]
 [43 50]]


```
