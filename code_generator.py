'''
@copyright ziqi-jin
'''


class CodeGenerator:
    def __init__(self, model_interface):
        self.model_interface = model_interface

    def generate_code(self, prompt):
        return self.model_interface.get_decision(prompt)
