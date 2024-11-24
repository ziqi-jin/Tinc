'''
@copyright ziqi-jin
'''

from interfaces.model_interface import TheBAIModelRequest
from interfaces.execution_interface import ExecutionInterface
from log.logger import Logger
from code_generator import CodeGenerator
from test_case_generator import TestCaseGenerator

def main():
    base_directory = './output'
    api_key = input("please input your api key for TheB.AI: ")
    model_interface = TheBAIModelRequest(api_key=api_key)
    logger = Logger()
    execution_interface = ExecutionInterface(base_directory)
    code_generator = CodeGenerator(model_interface)
    test_case_generator = TestCaseGenerator(model_interface)

    while True:
        prompt = input("Enter your design prompt (type 'exit' to quit): ")
        if prompt.lower() == 'exit':
            break
        
        logger.log_interaction(f"User prompt: {prompt}")

        # 生成代码
        generated_code = code_generator.generate_code(prompt)
        logger.log_interaction(f"Generated Code: {generated_code}")
        
        # 执行代码
        execution_result = execution_interface.execute_code(generated_code, 'example_directory', 'generated_code.py')
        logger.log_execution(f"Execution result: {execution_result}")

        # 生成测试用例
        test_prompt = f"Generate test cases for: {prompt}"
        test_code = test_case_generator.generate_test_cases(test_prompt)
        logger.log_interaction(f"Generated Test Code: {test_code}")

        # 执行测试用例
        test_result = execution_interface.execute_code(test_code, 'example_directory', 'test_generated_code.py')
        logger.log_execution(f"Test execution result: {test_result}")
if __name__ == "__main__":
    main()

