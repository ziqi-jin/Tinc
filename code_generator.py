'''
@copyright ziqi-jin
'''


class CodeGenerator:
    def __init__(self, model_interface):
        self.model_interface = model_interface

    def generate_code(self, prompt):
        code = self.model_interface.make_request(prompt)
        self.model_interface.add_message_to_history(code, role="assistant")
        return code
