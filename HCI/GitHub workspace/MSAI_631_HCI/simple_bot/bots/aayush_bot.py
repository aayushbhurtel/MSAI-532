# bots/aayush_bot.py

from botbuilder.core import ActivityHandler, TurnContext, MessageFactory
from botbuilder.schema import ChannelAccount
import random

class AayushBot(ActivityHandler):
    async def on_members_added_activity(
        self, members_added: [ChannelAccount], turn_context: TurnContext
    ):
        # welcome message
        for member in members_added:
            if member.id != turn_context.activity.recipient.id:
                await turn_context.send_activity(
                    "👋 Hello, I'm **AayushBot**! Type 'help' to see what I can do."
                )

    async def on_message_activity(self, turn_context: TurnContext):
        # handle user input
        user_input = turn_context.activity.text.strip().lower()

        if user_input in ["hi", "hello", "hey"]:
            await turn_context.send_activity("Hello there! How can I help you today? 😊")

        elif "help" in user_input or "what can you do" in user_input:
            capabilities = (
                "Here’s what I can do:\n"
                "- Greet you \n"
                "- Tell 'time' \n"
                "- Tell you a 'fun fact' \n"
            )
            await turn_context.send_activity(capabilities)

        elif "fun fact" in user_input:
            facts = [
                "Python was named after the comedy group *Monty Python*, not the snake!",
                "The first chatbot, ELIZA, was created in 1966 at MIT.",
                "The Microsoft Bot Framework can connect your bot to over 15 channels, including Teams and Slack.",
            ]
            await turn_context.send_activity(random.choice(facts))

        elif "time" in user_input:
            from datetime import datetime
            now = datetime.now().strftime("%I:%M %p")
            await turn_context.send_activity(f"The current time is {now} ⏰")

        elif "bye" in user_input:
            await turn_context.send_activity("Goodbye! It was nice chatting with you 👋")

        else:
            await turn_context.send_activity(
                "🤔 Sorry, I didn’t quite get that. Type 'help' to see what I understand."
            )
