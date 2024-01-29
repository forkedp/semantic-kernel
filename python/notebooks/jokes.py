
import semantic_kernel as sk

kernel = sk.Kernel()


from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion

deployment, api_key, endpoint = sk.azure_openai_settings_from_dot_env()

kernel.add_chat_service("chat_completion", AzureChatCompletion(deployment_name=deployment, endpoint=endpoint, api_key=api_key))


skill = kernel.import_semantic_skill_from_directory("./samples/skills", "FunSkill")
# joke_function = skill["Joke"]

# print(joke_function("time travel to dinosaur age"))


# for s in skill:
#     print(s)


excuses_function = skill["Excuses"]

print(excuses_function("I am late because"))


# skill = kernel.import_semantic_skill_from_directory("./samples/skills", "FunSkill")
# joke_function = skill["Joke"]

# print(joke_function("quantum physics"))





