class TestCaseGenerator:
    def __init__(self, model_interface):
        self.model_interface = model_interface

    def generate_test_cases(self, code):
        prompt = f"为下面代码生成可以执行单元测试用例:\n   ## 待测试代码 \n {code} \n 注意：代测试代码文件存放在 generated_code.py 中，请尝试使用相对引用方式导入目标代码"
        test_code = self.model_interface.make_request(prompt)
        return test_code

