import subprocess
import sys

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