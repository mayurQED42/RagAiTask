from litellm import completion

def call_llm(messages, model, stream=False):
    response = completion(
        model=model,
        messages=messages,
        stream=stream,
    )
    return response
