def call_llm(model_name: str, prompt: str) -> str:
    """
    Routes prompt to the selected LLM.
    Currently mocked — easy to replace with real APIs later.
    """

    if model_name == "GPT-4":
        return f"[GPT-4 Answer]\n{prompt}"

    elif model_name == "Claude":
        return f"[Claude Answer]\n{prompt}"

    elif model_name == "Gemini":
        return f"[Gemini Answer]\n{prompt}"

    else:
        return f"[Default Model]\n{prompt}"
