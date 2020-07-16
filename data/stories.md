## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy
* affirm
  - utter_iamabot
* report
  - action_update
* states_name
  - action_condition
* greet
  - utter_did_that_help

*affirm
  - utter_goodbye


## sad path 1
* greet
  - utter_greet
* mood_great
  - utter_happy
* affirm
  - utter_iamabot

* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy
* deny
  -utter_goodbye



## information path

* greet
  - utter_greet

* information
  - action_inform

* places
  - action_location

* report
  - action_update

* states_name
  - action_condition

* goodbye
  - utter_goodbye




  



## planning for a visit 

* places
  - action_location
* greet
  - utter_did_that_help
* affirm
  - utter_goodbye 




## yo path
* chill
  - utter_yo

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## Ask for COVID-19
* report
  - action_update

## All India States
* states_name
  - action_condition

## Update path

* states_name
  - action_condition

* greet
  - utter_did_that_help

*affirm
  - utter_goodbye
