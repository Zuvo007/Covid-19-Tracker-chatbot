#source code for the custom actions 

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
class InformAction(Action):

     def name(self) -> Text:
         return "action_inform"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         dispatcher.utter_message(text="Seems like you are feeling bored or something!")
         dispatcher.utter_message(text="wanna go somewhere?")

         return []


class InformLocation(Action):

     

     def name(self) -> Text:
         return "action_location"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         entities=tracker.latest_message['entities']
         
         message= None
         for e in entities:
             if e['entity']=='location':
                 name=e['value']
                 
             if name== "Gujrat":
                 message="Gir national park will be the best trip for you once the lockdown is over"
             if name== "Kolkata":
                 message= "I think you should visit Indian Museum once the lockdown is over"
             if name== "Delhi":
                 message= "You should visit Red Fort once the lockdown is over"
             if name=="chennai":
                 message= "you should visit Marina Beach once the lockdown is over"
          
             
         dispatcher.utter_message(text=message)
       

         return []






class InformAction(Action):

     def name(self) -> Text:
         return "action_update"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         dispatcher.utter_message(text="Yeah sure! enter a state to know about COVID-19 status")
         

         return []









class ActionAffectedState(Action):

     def name(self) -> Text:
         return "action_condition"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         responses=requests.get("https://api.covid19india.org/data.json").json()
         entities=tracker.latest_message['entities']
         state=None
         for e in entities:
             if e['entity']=='state':
                 state=e['value']


         message="Wrong state name please give the correct one"
         for data in responses["statewise"]:
             if data['state']==state.title():
                  print(data)
                  message="Active :"+data["active"]+"    "+ "Confirmed :"+data["confirmed"]+"    "+"Deaths :" +data["deaths"]+"    "+"Last updated time :" +data["lastupdatedtime"]
                    
                       
         print(message)
         dispatcher.utter_message(text=message)

         return []























