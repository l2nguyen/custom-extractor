# custom-extractor
 
Test `extract_<slot_name>` method behaviour in Rasa 3

They only seem to run after slot has been filled in a form due to when FormValidationAction is now called.

To see behaviour after training a model, say the following to the bot:

`go go test form`

You will see that the bot will still ask you for slot `question1` even though there is an `extract_question1` method.