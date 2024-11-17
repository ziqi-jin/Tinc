'''
@copyright ziqi-jin
'''

import os

class ExecutionInterface:
    def __init__(self, base_directory):
        self.base_directory = base_directory

    def request_permission(self):
        return input("Require permission to execute. Grant permission? (yes/no): ").lower() == 'yes'

    def execute_code(self, code, directory, filename='generated_code.py'):
        target_directory = os.path.join(self.base_directory, directory)
        
        if not os.path.exists(target_directory):
            os.makedirs(target_directory)

        file_path = os.path.join(target_directory, filename)
        with open(file_path, 'w') as file:
            file.write(code)
        
        if self.request_permission():
            print(f"Executing code in {target_directory}")
            try:
                exec(open(file_path).read())
                return "Execution completed."
            except Exception as e:
                return f"Execution failed: {str(e)}"
        else:
            return "Execution denied by user."
