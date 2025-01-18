import gradio as gr
from character_chatbot import CharacterChatBot
import os
from dotenv import load_dotenv
load_dotenv()


def chat_with_character_chatbot(message, history):
    character_chatbot = CharacterChatBot(
        "AbdullahTarek/Naruto_Llama-3-8B",
        huggingface_token=os.getenv('huggingface_token')
    )
    output = character_chatbot.chat(message, history)
    return output['content'].strip()

def main():
    # Character Chatbot Section
    with gr.Blocks() as iface:
        with gr.Row():
            with gr.Column():
                gr.HTML("<h1>Character Chatbot</h1>")
                gr.ChatInterface(chat_with_character_chatbot)

    iface.launch(share=True)

if __name__ == '__main__':
    main()
