from router.router import route_prompt
from experts.prompts import MODEL_CONFIG
from experts.llm_expert import call_expert
from tools.crypto_tool import get_bitcoin_price


def process_request(user_input: str):

    # Step 1: Route query
    category = route_prompt(user_input)
    print("🔀 Routed to:", category)

    # Step 2: Tool Expert
    if category == "crypto_tool":
        price = get_bitcoin_price()
        return f"💰 Current Bitcoin Price: {price}"

    # Step 3: Select expert prompt
    system_prompt = MODEL_CONFIG.get(category, MODEL_CONFIG["general"])["system_prompt"]

    # Step 4: Call LLM expert
    return call_expert(system_prompt, user_input)


if __name__ == "__main__":

    print("🤖 Smart Customer Support Router Started")
    print("Type 'exit' to quit")

    while True:
        user_query = input("\nYou: ")

        if user_query.lower() == "exit":
            break

        response = process_request(user_query)
        print("\nAI:", response)