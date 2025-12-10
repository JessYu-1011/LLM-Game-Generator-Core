import ast
import subprocess
import sys

def static_code_check(file_path: str) -> tuple[bool, str]:
    """
    Use Python ast module, inspecting the syntax errors.
    @:return (syntax validity, error message)
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            code = f.read()
        ast.parse(code)
        return True, "語法檢查通過 ✅"
    except SyntaxError as e:
        return False, f"語法錯誤 ❌: {e}"
    except Exception as e:
        return False, f"其他錯誤 ❌: {e}"

def launch_game(file_path: str) -> str:
    """
    Try to launch the generated game file.
    """
    try:
        if sys.platform == "win32":
            subprocess.Popen(["python", file_path], creationflags=subprocess.CREATE_NEW_CONSOLE)
        else:
            # Mac/Linux
            subprocess.Popen(["python3", file_path])
        return "遊戲視窗已啟動！"
    except Exception as e:
        return f"啟動失敗: {str(e)}"