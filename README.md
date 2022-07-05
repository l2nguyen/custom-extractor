# custom-extractor
 
Test extract_<slot_name> method behaviour in Rasa 3

They only seem to run after slot has been filled in a form due to when FormValidationAction is now called.

To see behaviour after training a model, have the following conversation with the bot:
`go go test form`