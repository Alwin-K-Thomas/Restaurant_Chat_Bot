
## interactive_story_1
* goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* goodbye

## interactive_story_1
* affirm
    - utter_goodbye
    - action_restart

## interactive_story_4
* greet
    - utter_greet
* goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* not
    - utter_goodbye
    - action_restart

## interactive_story_1
* goodbye
    - action_restart

## interactive_story_2
* goodbye
    - action_restart

## interactive_story_1
* restaurant_search{"location": "bengaluru"}
    - slot{"location": "bengaluru"}
    - action_location_valid
    - slot{"location_validity": "valid"}
    - utter_ask_cuisine
* location{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price
* price{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "bengaluru"}
    - utter_email_prompt
* not
    - utter_goodbye
    - action_restart

## interactive_story_1
* restaurant_search{"location": "bengaluru"}
    - slot{"location": "bengaluru"}
    - utter_ask_cuisine
    - action_location_valid
    - slot{"location_validity": "valid"}
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* price{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"got_all": "yes"}
    - utter_email_prompt
* affirm
    - utter_request_email
* email{"email": "upgradchatbot6@gmail.com"}
    - slot{"email": "upgradchatbot6@gmail.com"}
    - action_send_email
    - utter_goodbye
    - action_restart

## interactive_story_1
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_location_valid
    - slot{"location_validity": "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_price
* price{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"got_all": "yes"}
    - utter_email_prompt
* not
    - utter_goodbye
    - action_restart

## interactive_story_1
* restaurant_search{"cuisine": "chinese", "location": "bengaluru"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "bengaluru"}
    - action_location_valid
    - slot{"location_validity": "valid"}
    - utter_ask_price
* price{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"got_all": "yes"}
    - utter_email_prompt
* affirm
    - utter_request_email
* email{"email": "upgradchatbot6@gmail.com"}
    - slot{"email": "upgradchatbot6@gmail.com"}
    - action_send_email
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"price": "low", "location": "bengaluru"}
    - slot{"location": "bengaluru"}
    - action_location_valid
    - slot{"location_validity": "valid"}
    - slot{"price": "low"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_search_restaurants
    - utter_email_prompt
* affirm
    - action_send_email
    - utter_goodbye
    - action_restart

## interactive_story_1
* restaurant_search{"price": "low", "cuisine": "north indian", "location": "new delhi"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "new delhi"}
    - action_location_valid
    - slot{"location_validity": "valid"}
    - slot{"price": "low"}
    - action_search_restaurants
    - utter_email_prompt
* not{"not": "no"}
    - utter_goodbye
    - action_restart

## interactive_story_1
* restaurant_search{"price": "low", "location": "bengaluru"}
    - slot{"location": "bengaluru"}
    - action_location_valid
    - slot{"location_validity": "valid"}
    - slot{"price": "low"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_search_restaurants
    - utter_email_prompt
* affirm
    - utter_request_email
* email{"email": "srinivas.soma@gmail.com"}
    - slot{"email": "srinivas.soma@gmail.com"}
    - action_send_email
    - utter_goodbye
    - action_restart

## interactive_story_1
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_location_valid
    - slot{"location_validity": "valid"}
    - utter_ask_cuisine
* cuisine{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_price
* price{"price": "low"}
    - slot{"price": "low"}
    - action_search_restaurants
    - utter_email_prompt
* not
    - utter_goodbye
    - action_restart

## interactive_story_1
* restaurant_search{"cuisine": "italian", "location": "dharmavaram"}
    - slot{"cuisine": "italian"}
    - slot{"location": "dharmavaram"}
    - action_location_valid
    - slot{"location_validity": "valid"}
    - utter_ask_price
* price{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - reset_slots
    - utter_goodbye
    - action_restart

## interactive_story_1
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_location_valid
    - slot{"location_validity": "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* price{"price": "low"}
    - slot{"price": "low"}
    - action_search_restaurants
* goodbye
    - utter_email_prompt
* affirm
    - utter_request_email
* email{"email": "srinivas.soma@gmail.com"}
    - slot{"email": "srinivas.soma@gmail.com"}
    - action_send_email
    - utter_goodbye
    - action_restart

## interactive_story_1
* restaurant_search{"price": "low", "cuisine": "italian", "location": "Delhi"}
    - slot{"cuisine": "italian"}
    - slot{"location": "Delhi"}
    - slot{"price": "low"}
    - action_location_valid
    - slot{"location_validity": "valid"}
    - action_search_restaurants
* goodbye
    - utter_email_prompt
* email{"email": "vickyviper@protonmail.com"}
    - slot{"email": "vickyviper@protonmail.com"}
    - action_send_email
    - utter_goodbye
    - action_restart

## interactive_story_1
* restaurant_search{"price": "high", "location": "Delhi"}
    - slot{"location": "Delhi"}
    - slot{"price": "high"}
    - action_location_valid
    - slot{"location_validity": "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_search_restaurants
    - utter_email_prompt
* not
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "bengaluru"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "bengaluru"}
    - action_location_valid
    - slot{"location_validity": "valid"}
    - utter_ask_price
* goodbye{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
* restaurant_search
    - utter_email_prompt
* affirm
    - utter_request_email
* email{"email": "upgradchatbot6@gmail.com"}
    - slot{"email": "upgradchatbot6@gmail.com"}
    - action_send_email
    - utter_goodbye
    - action_restart

## interactive_story_1
* restaurant_search{"price": "high", "location": "dharmavaram"}
    - slot{"location": "dharmavaram"}
    - slot{"price": "high"}
    - action_location_valid
    - slot{"location_validity": "valid"}
    - utter_ask_cuisine
* cuisine{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_search_restaurants
    - reset_slots
    - utter_goodbye
    - action_restart

## interactive_story_1
* restaurant_search{"price": "low", "cuisine": "italian", "location": "bengaluru"}
    - slot{"cuisine": "italian"}
    - slot{"location": "bengaluru"}
    - slot{"price": "low"}
    - action_location_valid
    - slot{"location_validity": "valid"}
    - action_search_restaurants
    - utter_email_prompt
* not
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_price
* goodbye{"price": "mid"}
    - slot{"price": "mid"}
    - utter_ask_location
* location{"location": "bengaluru"}
    - slot{"location": "bengaluru"}
    - action_location_valid
    - slot{"location_validity": "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_search_restaurants
    - utter_email_prompt
* affirm
    - utter_request_email
* email{"email": "alwinkthomas@gmail.com"}
    - slot{"email": "alwinkthomas@gmail.com"}
    - action_send_email
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "jaipur"}
    - slot{"location": "jaipur"}
    - action_location_valid
    - slot{"location_validity": "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_price
* price{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
* not

## interactive_story_2
* restaurant_search{"price": "high", "cuisine": "indian", "location": "jaipur"}
    - slot{"cuisine": "indian"}
    - slot{"location": "jaipur"}
    - slot{"price": "high"}
    - action_location_valid
    - slot{"location_validity": "valid"}
    - action_search_restaurants
    - utter_email_prompt
* not
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet

## interactive_story_2
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* goodbye{"price": "mid"}
    - slot{"price": "mid"}
    - utter_ask_location
* location{"location": "jalandhar"}
    - slot{"location": "jalandhar"}
    - action_location_valid
    - slot{"location_validity": "valid"}
    - action_search_restaurants
    - utter_email_prompt
* email{"email": "srinivas.soma@gmail.com"}
    - slot{"email": "srinivas.soma@gmail.com"}
    - action_send_email
    - utter_goodbye
    - action_restart

## interactive_story_1
* restaurant_search{"price": "low", "cuisine": "italian", "location": "warangal"}
    - slot{"cuisine": "italian"}
    - slot{"location": "warangal"}
    - slot{"price": "low"}
    - action_location_valid
    - slot{"location_validity": "valid"}
    - action_search_restaurants
    - utter_email_prompt
* affirm
    - utter_request_email
* email{"email": "upgradchatbot6@gmail.com"}
    - slot{"email": "upgradchatbot6@gmail.com"}
    - action_send_email
    - utter_goodbye
    - action_restart

## interactive_story_1
* restaurant_search{"price": "low", "cuisine": "american"}
    - slot{"cuisine": "american"}
    - slot{"price": "low"}
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_location_valid
    - slot{"location_validity": "valid"}
    - action_search_restaurants
    - utter_email_prompt
* not
    - utter_goodbye
    - action_restart

## interactive_story_1
* restaurant_search{"cuisine": "italian", "location": "dharmavaram"}
    - slot{"cuisine": "italian"}
    - slot{"location": "dharmavaram"}
    - action_location_valid
    - slot{"location_validity": "valid"}
    - utter_ask_price
* goodbye{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - reset_slots
    - utter_email_prompt
* email{"email": "admin@cpanel.com"}
    - slot{"email": "admin@cpanel.com"}
    - action_send_email
    - reset_slots
    - utter_goodbye
    - action_restart

## interactive_story_1
* restaurant_search{"price": "high", "cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - slot{"price": "high"}
    - utter_ask_location
* location{"location": "jodhpur"}
    - slot{"location": "jodhpur"}
    - action_location_valid
    - slot{"location_validity": "valid"}
    - action_search_restaurants
    - slot{"location": "jodhpur"}
    - slot{"price": "high"}
    - slot{"cuisine": "italian"}
    - utter_email_prompt
* affirm
    - utter_request_email
* email{"email": "emantav@gmail.com"}
    - slot{"email": "emantav@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_goodbye
    - action_restart

## interactive_story_1
* restaurant_search{"cuisine": "italian", "location": "bengaluru"}
    - slot{"cuisine": "italian"}
    - slot{"location": "bengaluru"}
    - action_location_valid
    - slot{"location_validity": "valid"}
    - utter_ask_price
* price{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - utter_email_prompt
* affirm
    - utter_request_email
* email{"email": "upgradchatbot6@gmail.com"}
    - slot{"email": "upgradchatbot6@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_goodbye
    - action_restart

## interactive_story_1
* restaurant_search{"cuisine": "italian", "location": "dharmavram"}
    - slot{"cuisine": "italian"}
    - slot{"location": "dharmavram"}
    - action_location_valid
    - slot{"location_validity": "valid"}
    - utter_ask_price
* price{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location_validity": "invalid"}

## interactive_story_2
* restaurant_search{"cuisine": "italian", "location": "dharmavram"}
    - slot{"cuisine": "italian"}
    - slot{"location": "dharmavram"}
    - action_location_valid
    - slot{"location_validity" : "invalid"}
    - utter_location_invalid
    - utter_ask_location_retry
* affirm
    - utter_ask_location
    - reset_slots
    - utter_ask_price
* price{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location_validity": "invalid"}

## interactive_story_3
* restaurant_search{"cuisine": "italian", "location": "dharmavaram"}
    - slot{"cuisine": "italian"}
    - slot{"location": "dharmavaram"}
    - action_location_valid
    - slot{"location_validity": "valid"}
    - utter_ask_price
* goodbye{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - reset_slots
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"price": "low", "location": "anantapur"}
    - slot{"location": "anantapur"}
    - action_location_valid
    - slot{"location_validity": "valid"}
    - slot{"price": "low"}
    - utter_ask_cuisine
* cuisine{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_search_restaurants
    - reset_slots
    - utter_goodbye
    - action_restart

## interactive_story_1
* restaurant_search{"location": "bengaluru"}
    - slot{"location": "bengaluru"}
    - action_location_valid
    - slot{"location_validity": "valid"}
    - utter_ask_cuisine
* cuisine{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_price
* price{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - utter_email_prompt
* not
    - utter_goodbye
    - action_restart

## interactive_story_1
* restaurant_search{"location": "bengaluru"}
    - slot{"location": "bengaluru"}
    - action_location_valid
    - slot{"location_validity": "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* goodbye{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - utter_email_prompt
* affirm
    - utter_request_email
* email{"email": "upgradchatbot6@gmail.com"}
    - slot{"email": "upgradchatbot6@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_goodbye
    - action_restart

## interactive_story_1
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* price{"price": "high"}
    - slot{"price": "high"}
    - utter_ask_location
* location{"location": "bengaluru"}
    - slot{"location": "bengaluru"}
    - action_location_valid
    - slot{"location_validity": "valid"}
    - action_search_restaurants
    - utter_email_prompt
* email{"email": "gajulajadageesh7@gmail.com"}
    - slot{"email": "gajulajadageesh7@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_goodbye
    - action_restart

## interactive_story_1
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_price
* goodbye{"price": "mid"}
    - slot{"price": "mid"}
    - utter_ask_location
* location{"location": "bengaluru"}
    - slot{"location": "bengaluru"}
    - action_location_valid
    - slot{"location_validity": "valid"}
    - action_search_restaurants
    - utter_email_prompt
* not
    - action_restart

## interactive_story_1
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_price
* price{"price": "high"}
    - slot{"price": "high"}
    - utter_ask_location
* location{"location": "dharmavaram"}
    - slot{"location": "dharmavaram"}
    - action_location_valid
    - slot{"location_validity": "valid"}
    - action_search_restaurants
    - reset_slots
    - utter_goodbye
    - action_restart

## interactive_story_1
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - utter_ask_location
* location{"location": "culcutta"}
    - slot{"location": "culcutta"}
    - action_location_valid
    - slot{"location_validity": "valid"}
    - utter_ask_cuisine
* cuisine{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_search_restaurants
    - reset_slots
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - utter_ask_price
* goodbye{"price": "mid"}
    - slot{"price": "mid"}

## interactive_story_2
* greet
    - utter_greet
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - utter_ask_location
* location{"location": "jaipur"}
    - slot{"location": "jaipur"}
    - action_location_valid
    - slot{"location_validity": "valid"}
    - utter_ask_cuisine
* location{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_search_restaurants
    - utter_email_prompt
* not{"not": "never"}
    - utter_goodbye
    - action_restart

## interactive_story_1
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - utter_ask_location
* location{"location": "jodhpur"}
    - slot{"location": "jodhpur"}
    - action_location_valid
    - slot{"location_validity": "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_search_restaurants
    - utter_email_prompt
* affirm
    - utter_request_email
* email{"email": "upgradchatbot6@gmail.com"}
    - slot{"email": "upgradchatbot6@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_goodbye
    - action_restart

## interactive_story_1
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - utter_ask_location
* location{"location": "varanasi"}
    - slot{"location": "varanasi"}
    - action_location_valid
    - slot{"location_validity": "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_search_restaurants
    - utter_email_prompt
* not
    - utter_goodbye
    - action_restart

## interactive_story_1
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - utter_ask_location
* location{"location": "jhansi"}
    - slot{"location": "jhansi"}
    - action_location_valid
    - slot{"location_validity": "valid"}
    - utter_ask_cuisine
* cuisine{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_search_restaurants
    - utter_email_prompt
* not
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"price": "low", "cuisine": "mexican", "location": "jodhpur"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "jodhpur"}
    - slot{"price": "low"}
    - action_location_valid
    - slot{"location_validity": "valid"}
    - action_search_restaurants
    - utter_email_prompt
* not
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"price": "high", "cuisine": "italian", "location": "mumbai"}
    - slot{"cuisine": "italian"}
    - slot{"location": "mumbai"}
    - slot{"price": "high"}
    - action_location_valid
    - slot{"location_validity": "valid"}
    - action_search_restaurants
    - utter_email_prompt
* affirm
    - utter_request_email
* email{"email": "upgradchatbot6@gmail.com"}
    - slot{"email": "upgradchatbot6@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "malaysia"}
    - slot{"location": "malaysia"}
    - action_location_valid
    - slot{"location_validity": "invalid"}
    - utter_location_invalid
    - utter_ask_location_retry
* location{"location": "bengaluru"}
    - slot{"location": "bengaluru"}
    - action_location_valid
    - slot{"location_validity": "valid"}
    - utter_ask_cuisine
* cuisine{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_price
* price{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - utter_email_prompt
* not
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "Italian", "location": "Varansi"}
    - slot{"cuisine": "Italian"}
    - slot{"location": "Varansi"}
    - action_location_valid
    - slot{"location_validity": "invalid"}
    - utter_location_invalid
    - utter_ask_location_retry
* location{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_location_valid
    - slot{"location_validity": "valid"}
    - utter_ask_price
* price{"price": "low"}
    - slot{"price": "low"}
    - action_search_restaurants
    - utter_email_prompt
* affirm
    - utter_request_email
* email{"email": "alwin.alwiland@gmail.com"}
    - slot{"email": "alwin.alwiland@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "ashramam"}
    - slot{"location": "ashramam"}
    - action_location_valid
    - slot{"location_validity": "invalid"}
    - utter_location_invalid
    - utter_ask_location_retry
* affirm
    - utter_ask_location
* location{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_location_valid
    - slot{"location_validity": "valid"}
    - utter_ask_cuisine
* cuisine{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_price
* price{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - utter_email_prompt
* not
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Delhi", "price": "high"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Delhi"}
    - slot{"price": "high"}
    - action_location_valid
    - slot{"location_validity": "valid"}
    - action_search_restaurants
    - utter_email_prompt
* not
    - utter_goodbye
    - action_restart

* greet
    - utter_greet
* restaurant_search{"location": "bengaluru"}
    - slot{"location": "bengaluru"}
    - action_location_valid
    - slot{"location_validity": "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_price
* price{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - utter_email_prompt
* affirm
    - utter_request_email
* email{"email": "alwin.alwiland@gmail.com"}
    - slot{"email": "alwin.alwiland@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_goodbye
    - action_restart
