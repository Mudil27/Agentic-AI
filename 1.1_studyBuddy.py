import anthropic
import os

# --- 1. SETUP ---
API_KEY = "" 

client = anthropic.Anthropic(api_key=API_KEY)

def main():
    print("Welcome to the Study Buddy Bot!")
    print("Type 'exit' to quit.\n")

    while True:
        # --- 2. GET USER INPUT ---
        topic = input("Enter a topic you want explained: ")

        # --- 3. INPUT VALIDATION ---
        if not topic.strip():
            print("Error: Please enter a valid topic. You cannot leave it blank!\n")
            continue  # Skips the rest of the loop and asks again

        if topic.lower() == 'exit':
            print("Goodbye!")
            break

        print(f"\nAsking Claude about '{topic}'...")
        
        #--- 4. MAKE THE API REQUEST ---
        response = client.messages.create(
            model="claude-haiku-4-5-20251001", # We use Haiku because it's fast and cheap
            max_tokens=150, # Limits how long Claude's response can be
            
            messages=[
                {
                    "role": "user",
                    "content": f"Explain the topic '{topic}' in simple terms in under 100 words."
                }
            ]
        )
        
        # The API returns a complex object. We just want the text content.
        bot_reply = response.content[0].text
        print("\n--- Study Buddy ---")
        print(bot_reply)
        print("-------------------\n")

if __name__ == "__main__":
    main()
