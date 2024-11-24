'''
@copyright ziqi-jin
'''

import os
import subprocess

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
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(code)
        
        print(f"Code has been written to {file_path}")
        
        allow_execution = True
        # 在这里，你可以实现更复杂的权限检查逻辑
        # 例如，根据代码内容决定是否需要权限
        allow_execution = self.request_permission()

        if allow_execution:
            print(f"Executing code: {file_path}")
            try:
                result = subprocess.run(['python', file_path], capture_output=True, text=True, check=True)
                return f"Execution completed.\nOutput:\n{result.stdout}"
            except subprocess.CalledProcessError as e:
                return f"Execution failed.\nError:\n{e.stderr}"
        else:
            return "Execution denied by user."
