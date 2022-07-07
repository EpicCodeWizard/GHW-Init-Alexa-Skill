from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_model.ui import SimpleCard
from ask_sdk_model import Response

sb = SkillBuilder()

@sb.request_handler(can_handle_func=is_request_type("LaunchRequest"))
def launch_request_handler(handler_input):
  speech_text = "Welcome to the GHW Bot!"
  return handler_input.response_builder.speak(speech_text).set_card(SimpleCard("GHW Bot", speech_text)).set_should_end_session(False).response

@sb.request_handler(can_handle_func=is_intent_name("GHWBotIntent"))
def ghw_bot_intent_handler(handler_input):
  speech_text = "Hello from the wonderful world of GHW!"
  return handler_input.response_builder.speak(speech_text).set_card(SimpleCard("GHW Bot", speech_text)).set_should_end_session(True).response

@sb.request_handler(can_handle_func=is_intent_name("AMAZON.HelpIntent"))
def help_intent_handler(handler_input):
  speech_text = "Why hello, say anything!"
  return handler_input.response_builder.speak(speech_text).set_card(SimpleCard("GHW Bot", speech_text)).response

@sb.request_handler(can_handle_func=lambda handler_input: is_intent_name("AMAZON.CancelIntent")(handler_input) or is_intent_name("AMAZON.StopIntent")(handler_input))
def cancel_and_stop_intent_handler(handler_input):
  speech_text = "Bye, have a nice hacker day!"
  return handler_input.response_builder.speak(speech_text).set_card(SimpleCard("GHW Bot", speech_text)).response

@sb.request_handler(can_handle_func=is_intent_name("AMAZON.FallbackIntent"))
def fallback_handler(handler_input):
  speech = ("Why hello, say anything!")
  reprompt = "You can even just say hello!"
  handler_input.response_builder.speak(speech).ask(reprompt)
  return handler_input.response_builder.response

@sb.request_handler(can_handle_func=is_request_type("SessionEndedRequest"))
def session_ended_request_handler(handler_input):
  return handler_input.response_builder.response

@sb.exception_handler(can_handle_func=lambda i, e: True)
def all_exception_handler(handler_input, exception):
  speech = "Sorry, there was some problem. Our admin are hard at work about that. While that time, why don't you say hello?"
  handler_input.response_builder.speak(speech).ask(speech)
  return handler_input.response_builder.response

handler = sb.lambda_handler()
