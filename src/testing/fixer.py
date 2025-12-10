from src.utils import call_llm
from src.testing.prompts import FIXER_PROMPT
from src.generation.file_utils import save_code_to_file
import os


def run_fix_loop(file_path: str, error_message: str, provider: str = "openai"
                 , model: str  = "gpt-4o-mini") -> tuple[str | None, str]:
    """
    Auto Fix Loop: Read Codes -> Submit Errors -> Get new codes -> save
    The first return is the path to the fixed file.
    The second return is the result message.
    """
    print(f"[Member 3] 正在嘗試修復代碼... (Error: {error_message[:50]}...)")

    # Read the broken codes
    if not os.path.exists(file_path):
        return None, "找不到原始代碼檔案"

    with open(file_path, "r", encoding="utf-8") as f:
        broken_code = f.read()

    # Insert the codes to the prompt
    full_prompt: str = FIXER_PROMPT.format(code=broken_code, error=error_message)

    # Call LLM for fixing
    response: str = call_llm("You are a Code Fixer.", full_prompt, provider=provider, model=model)

    # Save the fixed files (truncate)
    output_dir: str = os.path.dirname(file_path)
    new_path: str | None = save_code_to_file(response, output_dir=output_dir)

    if new_path:
        return new_path, "修復完成，已更新代碼。"
    else:
        return None, "AI 無法生成有效的 Python 代碼區塊。"