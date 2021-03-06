from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import zomatopy
import json
import smtplib 
import pprint, json
import zomatopy
import requests

from rasa_sdk.events import AllSlotsReset
from rasa_sdk.events import Restarted
from rasa_sdk import Action
from rasa_sdk.events import SlotSet



cities = [
	'ahmedabad','bengaluru',' bangalore', 'chennai','madras', 'delhi','new delhi',
	'hyderabad', 'kolkata', 'culcatta' ,'mumbai','bombay', 'pune', 'agra', 'ajmer',
	'aligarh', 'amravati','amaravati', 'amritsar', 'asansol', 'aurangabad', 'bareilly',
	'belgaum', 'bhavnagar', 'bhiwandi', 'bhopal', 'bhubaneswar', 'bikaner', 'bilaspur', 
	'bokaro', 'chandigarh', 'coimbatore', 'cuttack', 'dehradun', 'dhanbad', 'bhilai',
	'durgapur', 'erode', 'faridabad', 'firozabad', 'ghaziabad', 'gorakhpur', 'gulbarga',
	'guntur', 'gwalior', 'gurgaon', 'guwahati', 'hamirpur', 'hubli–dharwad', 'indore',
	'jabalpur', 'jaipur', 'jalandhar', 'jammu', 'jamnagar', 'jamshedpur', 'jhansi',
	'jodhpur', 'kakinada', 'kannur', 'kanpur', 'kochi', 'kolhapur', 'kollam', 'kozhikode',
	'kurnool', 'ludhiana', 'lucknow', 'madurai', 'malappuram', 'mathura', 'goa', 'mangalore',
	'meerut', 'moradabad', 'mysore', 'nagpur', 'nanded', 'nashik', 'nellore', 'noida',
	'patna', 'pondicherry', 'purulia prayagraj', 'raipur', 'rajkot', 'rajahmundry', 'ranchi', 
	'rourkela', 'salem', 'sangli', 'shimla', 'siliguri', 'solapur', 'srinagar', 'surat', 
	'thiruvananthapuram', 'thrissur', 'tiruchirappalli', 'tiruppur', 'ujjain', 'bijapur',
	'vadodara', 'varanasi', 'vasai-virar', 'vijayawada','vijaywada', 'visakhapatnam',
	'vellore', 'warangal'
]


class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'

	def fetch(self, loc='banglore', cuisine='north indian', price='high'):
		#adjust the price range
		price_min = 0
		price_max = 99999
		if price == 'low':
			price_max = 300
		elif price == 'mid':
			price_min = 300
			price_max = 700
		elif price == 'high':
			price_min = 700
		else:
			price_min = 300
			price_max = 9999
		
		# provide API key and initialise a 'zomato app' object
		config={ "user_key": "<zomato_key>"}
		zomato = zomatopy.initialize_app(config)
		cuisines_dict={
			'bakery':5, 'chinese':25, 'cafe':30,
			'italian':55, 'biryani':7, 'north indian':50,
			'south indian':85,'north':50,'south':85, 'indian':80,
			'american': 1, 'mexican': 73
		}

		# get_location gets the lat-long coordinates of 'loc'
		loc_detail=zomato.get_location(loc, 1)
		loc_detail=json.loads(loc_detail)
		if loc_detail['status'] == 'success':
			data =  zomato.restaurant_search(
				query='',
				latitude=loc_detail['location_suggestions'][0]['latitude'],
				longitude=loc_detail['location_suggestions'][0]['longitude'],
				cuisines=str(cuisines_dict.get(cuisine)),
				limit=100
			)
			data = json.loads(data)
			results = ""
			if data['results_found'] > 0:
				added=0
				for i in sorted(data['restaurants'], key=lambda x: x['restaurant']['user_rating']['aggregate_rating'], reverse=True):
					if i['restaurant']['average_cost_for_two'] > price_min and i['restaurant']['average_cost_for_two'] < price_max and added < 5:
						results = results + "\n\nname: "+str(i['restaurant']['name'])+"\naddress :"+str(i['restaurant']['location']['address'])+"\nrating :"+str(i['restaurant']['user_rating']['aggregate_rating'])
						added = added +1
				if len(results) == 0:
					SlotSet('results_found',False)
					return "no results found"
			return "here are the results \n\n "+ results

		else:
			return 0

	def run(self, dispatcher, tracker, domain):
		loc = tracker.get_slot('location')
		if loc == None:
			return dispatcher.utter_message('Location got is None')
		if loc.lower() not in cities:
			dispatcher.utter_message("We don't operate in your location")
			return [SlotSet("location_validity", "invalid")]

		cuisine = tracker.get_slot('cuisine')
		price = tracker.get_slot('price')
		res=''
		if cuisine == None or price == None:
				dispatcher.utter_message(
					"I didn't get all details, deafault results will be shown"
				)
				cuisine = 'north'
				price = 'mid'
		
		else:
			res = self.fetch(loc,cuisine,price)
			dispatcher.utter_message(res+"\n\n\n")


class ActionSendEmail(Action):
	def name(self):
		return 'action_send_email'

	def fetch(self,loc='delhi',cuisine='north indian',price='high'):
		#adjust the price range
		price_min = 0
		price_max = 99999
		if price == 'low':
			price_max = 300
		elif price == 'mid':
			price_min = 300
			price_max = 700
		elif price == 'high':
			price_min = 700
		else:
			price_min = 300
			price_max = 9999
		
		# provide API key and initialise a 'zomato app' object
		config={ "user_key": "<zomato_key""}
		zomato = zomatopy.initialize_app(config)
		cuisines_dict={
			'bakery':5, 'chinese':25, 'cafe':30,
			'italian':55, 'biryani':7, 'north indian':50,
			'south indian':85,'north':50,'south':85, 'indian':80,
			'american': 1, 'mexican': 73
		}

		# get_location gets the lat-long coordinates of 'loc'
		loc_detail=zomato.get_location(loc, 1)
		loc_detail=json.loads(loc_detail)
		if loc_detail['status'] == 'success':
			lat = loc_detail['location_suggestions'][0]['latitude']
			lon = loc_detail['location_suggestions'][0]['longitude']
			data =  zomato.restaurant_search(
				query='',
				latitude=lat,
				longitude=lon,
				cuisines=str(cuisines_dict.get(cuisine)),
				limit=200
			)
			data = json.loads(data)
			results = ""
			if data['results_found'] > 0:
				added=0
				for i in sorted(data['restaurants'], key=lambda x: x['restaurant']['user_rating']['aggregate_rating'], reverse=True):
					if i['restaurant']['average_cost_for_two'] > price_min and i['restaurant']['average_cost_for_two'] < price_max and added < 10:
						results = results + "\n\nname: "+str(i['restaurant']['name'])+"\naddress :"+str(i['restaurant']['location']['address'])+"\n cost for 2 people: "+str(i['restaurant']['average_cost_for_two'])+"\nrating :"+str(i['restaurant']['user_rating']['aggregate_rating'])
						added = added +1
					if len(results) == 0:
						return "can't get anything with your preferances"

				return "here are the results \n\n "+ results
			else:
				return "can't retrive data properly"

		else:
			return "results not found..!!"


	def run(self, dispatcher, tracker, domain):
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		price = tracker.get_slot('price')
		res = self.fetch(loc,cuisine,price)
		email = tracker.get_slot('email')
		if email == None:
			email = '@gmail.com'
		s = smtplib.SMTP('smtp.gmail.com', 587) 
		s.starttls() 
		try:
			s.login("@gmail.com", "")
		except:
			dispatcher.utter_message('bad credentials, your preferences deleted')
			return [AllSlotsReset()]
		message = "The details of all the restaurants you inquried \n \n"
		message = message + res
		try:
			s.sendmail("@gmail.com", str(email), message)
			s.quit()
			dispatcher.utter_message(
				"Email sent please check your inbox. your preferances will be deleted "
			)
			return [AllSlotsReset()]
		except:
			dispatcher.utter_message("Can't send the email. deleted your preferances")
			return [AllSlotsReset()]

class ActionValidateLocation(Action):

    def name(self):
        return "action_location_valid"

    def run(self, dispatcher, tracker, domain):
        location = tracker.get_slot("location")
        location_validity = "valid"
        if not location:
            location_validity = "invalid"
        else:
            if location.lower() not in cities:
                location_validity = "invalid"
            else:
                location_validity = "valid"

        return [SlotSet("location_validity", location_validity)]
