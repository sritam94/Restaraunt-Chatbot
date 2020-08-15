from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals
from rasa_core_sdk.events import AllSlotsReset
from rasa_core_sdk.events import Restarted
from rasa_core_sdk.events import FollowupAction
from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import zomatopy
import json
import smtplib 

email_response=""
app_response = ""

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'

	def filterRestaurantsOnBudget(self, budget, restaurants):
		global email_response
		global app_response
		rangeMin = 0
		rangeMax = 999999
		# print("################ budget: ",budget)
		try:
			price = int(budget)
			if price == 1:
				rangeMax = 300
			elif price == 2:
				rangeMin = 300
				rangeMax = 700
			elif price == 3:
				rangeMax = 700
			elif price <= 300:
				rangeMax = 300
			elif price <= 700 and price >= 300:
				rangeMin = 300
				rangeMax = 700
			else:
				rangeMin = 700
		except Exception as e:
			print("Setting default budget as exception: ",e)
			# default budget 
			rangeMin = 300
			rangeMax = 700

		#sort function right
		# print("before sort!!",len(restaurants))
		restaurants = sorted(restaurants,key=lambda x: float(x['restaurant']['user_rating']['aggregate_rating']), reverse=True)
		res_email = []
		res_app = []
		cnt = 1
		# print("reached here!!",len(restaurants))
		# print(restaurants[0])
		for restaurant in restaurants:
			avg_c_2 = restaurant['restaurant']['average_cost_for_two']
			if avg_c_2 <= rangeMax and avg_c_2 >= rangeMin:
				if(cnt == 1 ):
					res_app.append("\n Showing you top rated restaurants: \n")
				res_email.append( str(cnt)+ ". " + restaurant['restaurant']['name'] + " in " + restaurant['restaurant']['location']['address'] + " with average budget of " + str(restaurant['restaurant']['average_cost_for_two'])  + " has been rated " + restaurant['restaurant']['user_rating']['aggregate_rating'] + "/5 ." )
				res_app.append( str(cnt)+ ". "+ restaurant['restaurant']['name'] + " in " + restaurant['restaurant']['location']['address'] + " has been rated " + restaurant['restaurant']['user_rating']['aggregate_rating'] + "/5 ." )
				cnt=cnt+1
		email_response = "\n".join(res_email[0:min(10,len(res_email))])	
		app_response = "\n".join(res_app[0:min(6,len(res_app))])
		
		if(len(res_app)==0):
			app_response += "Oops! no restaurant found for this query. Search results = 0"
		if(len(res_app)<5):
			app_response += "\n \nFor more results please search in higher budget range...\n \n"
		if(len(email_response)<10):
			email_response += "\n \nFor more results please search in higher budget range...\n \n"
		return app_response

		
	def run(self, dispatcher, tracker, domain):
		config={ "user_key":"f4924dc9ad672ee8c4f8c84743301af5"}
		zomato = zomatopy.initialize_app(config)

		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine').lower()
		budget = tracker.get_slot('budget')
		#print("################ vals: ",loc,cuisine,budget)
		location_detail=zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		cuisines_dict={'american':1,'mexican':73,'italian':55,'thai':95,'chinese':25,'north indian':50,'cafe':30,'bakery':5,'biryani':7,'south indian':85}
		results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 100000)
		# print(lat,lon,cuisine)
		res = json.loads(results)
		response=""
		if res['results_found'] == 0:
			response = "no results"
		else:
			# print("results found: ",res['results_found']
			response = self.filterRestaurantsOnBudget(budget, res['restaurants'])
		dispatcher.utter_message("\n"+response)
		return [SlotSet('location',loc)]



tierOneTwoCities = ["Ahmedabad","Bangalore","Chennai","Delhi","Hyderabad","Kolkata","Mumbai","Pune","Agra","Ajmer","Aligarh","Allahabad","Amravati"
,"Amritsar","Asansol","Aurangabad","Bareilly","Belgaum","Bhavnagar","Bhiwandi","Bhopal","Bhubaneswar","Bikaner","Bokaro Steel City",
"Chandigarh","Coimbatore","Cuttack","Dehradun","Dhanbad","Durg-Bhilai Nagar","Durgapur","Erode","Faridabad","Firozabad","Ghaziabad",
"Gorakhpur","Gulbarga","Guntur","Gurgaon","Guwahati","Gwalior","Hubli-Dharwad","Indore","Jabalpur","Jaipur","Jalandhar","Jammu",
"Jamnagar","Jamshedpur","Jhansi","Jodhpur","Kannur","Kanpur","Kakinada","Kochi","Kottayam","Kolhapur","Kollam","Kota","Kozhikode","Kurnool","Lucknow","Ludhiana",
"Madurai","Malappuram","Mathura","Goa","Mangalore","Meerut","Moradabad","Mysore","Nagpur","Nanded","Nashik","Nellore","Noida","Palakkad",
"Patna","Pondicherry","Raipur","Rajkot","Rajahmundry","Ranchi","Rourkela","Salem","Sangli","Siliguri","Solapur","Srinagar","Sultanpur","Surat",
"Thiruvananthapuram","Thrissur","Tiruchirappalli","Tirunelveli","Tiruppur","Ujjain","Vijayapura","Vadodara","Varanasi",
"Vasai-Virar City","Vijayawada","Visakhapatnam","Warangal"]

allowed_cities = [ city.lower() for city in tierOneTwoCities ]

class ActionValidateLocation(Action):
	def name(self):
		return 'action_check_location'

	def run(self, dispatcher, tracker, domain):
		config={ "user_key":"f4924dc9ad672ee8c4f8c84743301af5"}
		zomato = zomatopy.initialize_app(config)
	
		loc = tracker.get_slot('location')
		city = str(loc)
		if city.lower() in allowed_cities:
			return [SlotSet('location_match',"one")]
		else:
			zomato = zomatopy.initialize_app(config)
			# return [SlotSet('location_match',"zero")]
			try:
				results = zomato.get_city_ID(city)
				return [SlotSet('location_match',"one")]
			except:
				# dispatcher.utter_template(, tracker)
				return [SlotSet('location_match',"zero"),FollowupAction("utter_sorry_dont_operate")]


# Email list of 10 restaurants
class ActionSendEmail(Action):
	def name(self):
		return 'action_send_email'

	def run(self, dispatcher, tracker, domain):
		email = tracker.get_slot('email')
		global email_response
		global app_response
		s = smtplib.SMTP('smtp.gmail.com', 587) 
		s.starttls() 
		s.login("foodiesahitya@gmail.com", "test1234@1")
		message = "The details of all the restaurants you inquried: \n \n"
		message += email_response
		message = 'Subject: {}\n\n{}'.format("Foodie says Hi !!", message)
		try:
			s.sendmail("foodiesahitya@gmail.com", str(email), message)
			s.quit()
		except:
			dispatcher.utter_message(email)
		email_response = ""
		app_response = ""
		return [AllSlotsReset()]

