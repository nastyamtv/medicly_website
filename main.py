# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

    import os
    api_key = "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"  # Використовуй свій OpenAI API ключ
    os.environ["OPENAI_API_KEY"] = api_key
    import openai
    import json
    from openai import OpenAI


    user_message = "Hello"

    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": user_message,
            }
        ],
        model="gpt-4o",
    )
    print(response)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
