from openai import AzureOpenAI
import os
import dotenv

# import dotenv
dotenv.load_dotenv()

# test dotenv
def dotenv_test():
    test = {'azure_endpoint': os.environ['AZURE_OPENAI_ENDPOINT'],
            'model_version': os.environ['AZURE_OPENAI_API_VERSION'],
            'model_deployment': os.environ['AZURE_OPENAI_DEPLOYMENT']}
    for key, value in test.items():
        print(key, value)


dotenv_test()

# configure Azure OpenAI service client 
client = AzureOpenAI(
  azure_endpoint = os.environ['AZURE_OPENAI_ENDPOINT'], 
  api_key=os.environ['AZURE_OPENAI_API_KEY'],  
  api_version = os.environ['AZURE_OPENAI_API_VERSION']
  )

deployment=os.environ['AZURE_OPENAI_DEPLOYMENT']

# Prompt for recipies
def prompt_recipies(n='1'):
  no_recipes = n
  ingredients = input("Provide ingredients (ex. salmon olives): ")

# create prompt
  prompt = f"Provide for {no_recipes} dishes with the following ingredients: {ingredients} a brief tasting note and list the recipe."
  messages = [{"role": "user", "content": prompt}]

  completion = client.chat.completions.create(model=deployment, messages=messages, max_tokens=600, temperature = 0.1)

# print response
  print(f'Response: {completion.choices[0].message.content}')


prompt_recipies()