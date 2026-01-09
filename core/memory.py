def build_message_history(system_prompt, history, user_query):
    messages = [{"role": "system", "content": system_prompt}]
    messages.extend(history)
    messages.append({"role": "user", "content": user_query})
    return messages
