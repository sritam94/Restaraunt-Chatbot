## complete path 1
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "300"}
    - slot{"budget": "300"}
    - utter_searching
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_response
* affirm
    - utter_ask_email_address
* send_email{"email": "tsahitya105@gmail.com"}
    - slot{"email": "tsahitya105@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

## complete path 2
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "bhopal"}
    - slot{"location": "bhopal"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "300"}
    - slot{"budget": "300"}
    - utter_searching
    - action_search_restaurants
    - slot{"location": "bhopal"}
    - utter_ask_for_email_response
* affirm
    - utter_ask_email_address
* send_email{"email": "tsahitya105@gmail.com"}
    - slot{"email": "tsahitya105@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

## complete path 3
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "jaipur"}
    - slot{"location": "jaipur"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "500"}
    - slot{"budget": "500"}
    - utter_searching
    - action_search_restaurants
    - slot{"location": "jaipur"}
    - utter_ask_for_email_response
* affirm
    - utter_ask_email_address
* send_email{"email": "tsahitya105@gmail.com"}
    - slot{"email": "tsahitya105@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

## complete path 4
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_budget
* inform{"budget": "1000"}
    - slot{"budget": "1000"}
    - utter_searching
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_response
* affirm
    - utter_ask_email_address
* send_email{"email": "tsahitya105@gmail.com"}
    - slot{"email": "tsahitya105@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

## complete path 5
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_budget
* inform{"budget": "500"}
    - slot{"budget": "500"}
    - utter_searching
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_response
* affirm
    - utter_ask_email_address
* send_email{"email": "tsahitya105@gmail.com"}
    - slot{"email": "tsahitya105@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart


## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "bhopal", "budget": "300", "cuisine": "mexican"}
    - slot{"budget": "300"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "bhopal"}
    - action_search_restaurants
    - action_search_restaurants
    - action_search_restaurants
    - slot{"location": "bhopal"}
    - utter_ask_for_email_response
* affirm
    - utter_ask_email_address
* restaurant_search{"email": "tsahitya105@gmail.com"}
    - slot{"email": "tsahitya105@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_email_sent

## interactive_story_2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_budget
* restaurant_search
* restaurant_search{"budget": "500"}
    - slot{"budget": "500"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_response
* affirm
    - utter_ask_email_address
* restaurant_search{"email": "tsahitya105@gmail.com"}
    - slot{"email": "tsahitya105@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_email_sent


## interactive_story_3
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "jaipur"}
    - slot{"location": "jaipur"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_budget
* restaurant_search{"budget": "500"}
    - slot{"budget": "500"}
    - action_search_restaurants
    - slot{"location": "jaipur"}
    - utter_ask_for_email_response
* affirm
    - utter_ask_email_address
* restaurant_search{"email": "tsahitya105@gmail.com"}
    - slot{"email": "tsahitya105@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_email_sent

## interactive_story_4
* greet
    - utter_greet
* restaurant_search{"location": "chandigarh"}
    - slot{"location": "chandigarh"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "1000"}
    - slot{"budget": "1000"}
    - action_search_restaurants
    - slot{"location": "chandigarh"}
    - utter_ask_for_email_response
* affirm
    - utter_ask_email_address
* restaurant_search{"email": "tsahitya105@gmail.com"}
    - slot{"email": "tsahitya105@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_email_sent

## interactive_story_5
* greet
    - utter_greet
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "allahabad"}
    - slot{"location": "allahabad"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chines"}
    - slot{"cuisine": "chines"}
    - utter_ask_budget
* restaurant_search{"budget": "500"}
    - slot{"budget": "500"}
    - action_search_restaurants
    - slot{"location": "allahabad"}
    - utter_ask_for_email_response
* affirm
    - utter_ask_email_address
* restaurant_search{"email": "sritamsahoo94@gmail.com"}
    - slot{"email": "sritamsahoo94@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_email_sent

## interactive_story_6
* greet
    - utter_greet
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_budget
* restaurant_search{"budget": "1000"}
    - slot{"budget": "1000"}
    - action_search_restaurants
    - slot{"location": "chennai"}
    - utter_ask_for_email_response
* restaurant_search{"email": "tsahitya105@gmail.com"}
    - slot{"email": "tsahitya105@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_email_sent

## interactive_story_7
* greet
    - utter_greet
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_budget
* restaurant_search{"budget": "300"}
    - slot{"budget": "300"}
    - action_search_restaurants
    - slot{"location": "kolkata"}
    - utter_ask_for_email_response
* affirm
    - utter_ask_email_address
* restaurant_search{"email": "sritamsahoo94@gmail.com"}
    - slot{"email": "sritamsahoo94@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_email_sent

## interactive_story_8
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* restaurant_search{"budget": "700"}
    - slot{"budget": "700"}
    - action_search_restaurants
    - slot{"location": "chandigarh"}
    - utter_ask_for_email_response
* deny
    - utter_goodbye


## interactive_story_9
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "bhopal"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "bhopal"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* restaurant_search{"budget": "500"}
    - slot{"budget": "500"}
    - action_search_restaurants
    - slot{"location": "bhopal"}
    - utter_ask_for_email_response
* deny
    - utter_goodbye

## interactive_story_10
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "delhi"}
    - slot{"cuisine": "italian"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* restaurant_search{"budget": "200"}
    - slot{"budget": "200"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_email_response
* deny
    - utter_goodbye

## interactive_story_11
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mubaim"}
    - slot{"location": "mubaim"}
    - action_check_location
    - slot{"location_match": "zero"}
    - followup{"name": "utter_sorry_dont_operate"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_budget
* restaurant_search{"budget": "300"}
    - slot{"budget": "300"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - utter_ask_for_email_response
* deny
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "bhubaneswar"}
    - slot{"location": "bhubaneswar"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "500"}
    - slot{"budget": "500"}
    - action_search_restaurants
    - slot{"location": "bhubaneswar"}
    - utter_ask_for_email_response
* deny
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "indore"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "indore"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* restaurant_search{"budget": "500"}
    - slot{"budget": "500"}
    - action_search_restaurants
    - slot{"location": "indore"}
    - utter_ask_for_email_response
* restaurant_search{"email": "tsahitya105@gmail.com"}
    - slot{"email": "tsahitya105@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_email_sent

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "chennai", "budget": "500"}
    - slot{"budget": "500"}
    - slot{"location": "chennai"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_search_restaurants
    - slot{"location": "chennai"}
    - utter_ask_for_email_response
* deny
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "cuttack"}
    - slot{"location": "cuttack"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_budget
* restaurant_search{"budget": "1000"}
    - slot{"budget": "1000"}
    - action_search_restaurants
    - slot{"location": "cuttack"}

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "momboi"}
    - slot{"location": "momboi"}
    - action_check_location
    - slot{"location_match": "zero"}
    - followup{"name": "utter_sorry_dont_operate"}
    - utter_sorry_dont_operate
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_budget
* restaurant_search{"budget": "700"}
    - slot{"budget": "700"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - utter_ask_for_email_response
* affirm
    - utter_ask_email_address
* restaurant_search{"email": "sritamsahoo94@gmail.com"}
    - slot{"email": "sritamsahoo94@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_email_sent

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "bhopal"}
    - slot{"location": "bhopal"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_budget
* restaurant_search{"budget": "700"}
    - slot{"budget": "700"}
    - action_search_restaurants
    - slot{"location": "bhopal"}
    - utter_ask_for_email_response
* restaurant_search{"email": "tsahitya105@gmail.com"}
    - slot{"email": "tsahitya105@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_email_sent
