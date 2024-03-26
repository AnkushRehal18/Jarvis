# # import openai

# # openai.api_key = "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"

# # def answers_with_gpt(input_text):
# #     try:
# #         response = openai.Completion.create(
# #             engine="whisper-1",
# #             prompt=input_text,
# #             max_tokens=100
# #         )
# #         return response['choices'][0]['text'].strip()
# #     except Exception as e:
# #         print(e)

# # # Example usage
# # user_input = "tell me what is the capital of India"p
# # response = answers_with_gpt(user_input)
# # print("Response:", response)

# # import os
# # import subprocess

# # inputt = input("enter the app to close").lower()
# # app_to_close = ["whatsapp","telegram","chrome","Ashpalt9","microsoft word","microsoft excel"
# #                     ,"microsoft powerpoint","calculator","hillclimbracing.exe",'notepad',"vs code"
# #                     ,"this pc"]
# # try:
# #     if inputt in app_to_close:
# #         result =  subprocess.run(["taskkill","/f" ,"/im", inputt] , capture_output = True ,text=True)

# #         if result.returncode == 0:
# #             print("app closed")
# #         else:
# #             print("not closed")
# #     else:
# #         print("not in the list")
# # except Exception as e:
# #      print(e)


# import os
# import subprocess

# inputt = input("Enter the app to close:")+".exe"
# inputt2 = [inputt ,".exe"]

# app_to_close = ["whatsapp", "telegram.exe", "chrome", "ashpalt9", "microsoft word",
#                 "microsoft excel", "microsoft powerpoint", "calculator",
#                 "hillclimbracing.exe", 'notepad', "vs code", "this pc"]

# try:
#     if inputt in app_to_close:
#         result = subprocess.run(["taskkill", "/f", "/im", inputt], capture_output=True, text=True)

#         if result.returncode == 0:
#             print(f"{inputt.capitalize()} closed")
#         else:
#             print(f"Failed to close {inputt.capitalize()}. Error: {result.stderr.strip()}")
#     else:
#         print(f"{inputt.capitalize()} is not in the list of applications to close.")
# except subprocess.CalledProcessError as e:
#     print(f"Error: {e}")
# except Exception as e:
#     print(f"An unexpected error occurred: {e}")


from AppOpener import open

open("notepad")