from rag.retriever import retrieve_context
from tools.weather import get_weather
from core.prompts import FAQ_PROMPT, RESEARCH_PROMPT
from core.memory import build_message_history
from core.llm import call_llm
from core.parser import parse_llm_output

def is_weather_query(query):
    return "weather" in query.lower()

def classify_query(query):
    if len(query) < 60:
        return "faq"
    return "research"

def chat_pipeline(query, history, model):
    # Tool routing
    if is_weather_query(query):
        city = query.split()[-1]
        weather = get_weather(city)
        return {
            "answer": f"It is {weather['temp']} and {weather['condition']} in {city}.",
            "source": "external"
        }

    # Retrieval
    retrieved = retrieve_context(query)

    # Dynamic prompt
    category = classify_query(query)
    system_prompt = FAQ_PROMPT if category == "faq" else RESEARCH_PROMPT

    final_query = f"""
Context:
{retrieved['text']}

Question:
{query}
"""

    messages = build_message_history(system_prompt, history, final_query)

    response = call_llm(messages, model)
    content = response.choices[0].message.content

    return parse_llm_output(content)
