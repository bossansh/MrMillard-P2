import random
import openai

openai.api_key = "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"
def generate_story():
    # Define the prompt that the API will use to generate the response
    prompt = f"Who is Adolf HItler>?"
    
    # Define the parameters for the API request
    model_engine = "GPT-3"  # Choose the GPT-3 model engine
    temperature = random.uniform(0.5, 1)  # Choose a random temperature between 0.5 and 1
    max_tokens = 1024  # Set the maximum number of tokens to generate
    
    # Send a request to the GPT-3 API to generate the response
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens
    )
    
    # Parse the response and extract the generated information
    story = response.choices[0].text
    
    # Return the generated response
    return story

generate_story()
