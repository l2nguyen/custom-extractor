from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, UserUttered, EventType
import random


class ValidateTestForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_test_form"
    
    async def extract_question1(
        self, 
        dispatcher: CollectingDispatcher, 
        tracker: Tracker, 
        domain: Dict
    ) -> Dict[Text, Any]:
        
        print("extract question1")

        text_of_last_user_message = tracker.latest_message.get("text")
        return {"question1": text_of_last_user_message}

    def validate_question1(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        print("validating question1")
        print("question1 value: {}".format(value))

        return {"question1": value}

    def validate_question2(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        print("validating question2")
        print("question2 value: {}".format(value))

        return {"question2": value}
