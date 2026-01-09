import json

def parse_llm_output(raw_text):
    try:
        start = raw_text.index("{")
        end = raw_text.rindex("}") + 1
        return json.loads(raw_text[start:end])
    except Exception:
        return {
            "answer": raw_text.strip(),
            "source": "unknown"
        }
