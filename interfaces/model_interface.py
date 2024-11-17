'''
@copyright ziqi-jin
'''

class ModelInterface:
    def __init__(self):
        pass

    def get_decision(self, prompt):
        # 简单的示例返回
        return """def add_numbers(a, b):
    return a + b
print(add_numbers(3, 4))"""
