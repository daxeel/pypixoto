#! /usr/bin/env python
#
# MODULE NAME  : pypixoto
# DESCRIPTION  : Python SDK for accessing data of Pixoto.com
# AUTHOR       : Daxeel Soni
# AUTHOR EMAIL : sayhi@daxeelsoni.in
# AUTHOR WEB   : www.daxeelsoni.in
#
# Copyright (c) 2015, Daxeel Soni
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the author nor the names of its contributors may
#       be used to endorse or promote products derived from this software
#       without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR AND CONTRIBUTORS``AS IS'' AND ANY
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE AUTHOR OR CONTRIBUTORS BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# IMPORT SECTION
from bs4 import BeautifulSoup
import urllib2
import json

version = 1.0

# MAIN CLASS
class Pixoto(object):
	"""docstring for Pixoto"""

	# Initializing Pixoto class with username
	def __init__(self, username):
		self.username = username
		self.url = "http://www.pixoto.com/" + self.username
		self.response = urllib2.urlopen(self.url)
		self.soup = BeautifulSoup(self.response, "html.parser")

	# Get Full name of user
	def full_name(self):
		return self.soup.find_all('span', {'class' : 'profile-name'})[0].strong.string

	# Get description
	def about(self):
		return self.soup.find_all('p', {'itemprop': 'description'})[0].string

	# Get location
	def location(self, loc_type):
		if loc_type == 'country':
			return self.soup.find_all('meta', {'itemprop': 'addressCountry'})[0]['content']
		elif loc_type == 'region':
			return self.soup.find_all('meta', {'itemprop': 'addressRegion'})[0]['content']
		elif loc_type == 'locality':
			return self.soup.find_all('meta', {'itemprop': 'addressLocality'})[0]['content']
		else:
			return 'Error. Invalid argument!'

	# Get number of awards
	def n_awards(self):
		return int(self.soup.find_all('ul', {'class': 'profile-stats'})[0].find_all('span')[0].string.replace(',', ''))

	# Get number of points
	def n_points(self):
		return int(self.soup.find_all('ul', {'class': 'profile-stats'})[0].find_all('span')[1].string.replace(',', ''))

	# Get number of images posted
	def n_images(self):
		return int(self.soup.find_all('ul', {'class': 'profile-stats'})[0].find_all('span')[2].string.replace(',', ''))

	# Get number of followers
	def n_followers(self):
		return int(self.soup.find_all('h3', {'class': 'sec-head-1 followers'})[0].span.string)

	# Get number of following users
	def n_following(self):
		return int(self.soup.find_all('h3', {'class': 'following'})[0].span.string)

	# Get information of images published by user
	def get_images(self, no_of_images, required_list):
		img_info_lst = ['title', 'description', 'category', 'subcategory', 'tags', 'date_published', 'date_taken', 'image_url', 'data_url', 'wins', 'losses', 'completed_duels', 'rating', 'cam_company', 'cam_model', 'focal_length', 'shutter_speed', 'aperture', 'iso_film', 'width', 'height']

		tot_images = self.n_images()
		if no_of_images > tot_images:
			return "Error! Passed more number of images than user actually published."
		else:
			def verify_list(required_list, img_info_lst):
				for i in required_list:
					if i not in img_info_lst:return False
				return True
			if verify_list(required_list, img_info_lst) == True:
				request = urllib2.urlopen("http://www.pixoto.com/" + self.username + "/recent?json=true&offset=0&limit=" + str(no_of_images))
				data = json.loads(request.read())['list']
				final = []
				for each in range(no_of_images):
					temp = {}
					for each_required in required_list:
						if each_required == 'title':temp['title'] = str(data[each]['title'])
						elif each_required == 'description':temp['description'] = str(data[each]['description'])
						elif each_required == 'category':temp['category'] = str(data[each]['category']['name'])
						elif each_required == 'subcategory':temp['subcategory'] = str(data[each]['subCategory']['name'])
						elif each_required == 'tags':temp['tags'] = str(data[each]['tags'])
						elif each_required == 'date_published':temp['date_published'] = str(data[each]['publishedDateFormatted'])
						elif each_required == 'date_taken':temp['date_taken'] = str(data[each]['shotDateFormatted'])
						elif each_required == 'image_url':temp['image_url'] = str(data[each]['url'])
						elif each_required == 'data_url':temp['data_url'] = "http://www.pixoto.com/" + str(data[each]['detailUrl'])
						elif each_required == 'wins':temp['wins'] = str(data[each]['wins'])
						elif each_required == 'losses':temp['losses'] = str(data[each]['losses'])
						elif each_required == 'completed_duels':temp['completed_duels'] = str(data[each]['completedDuels'])
						elif each_required == 'rating':temp['rating'] = str(data[each]['rating'])
						elif each_required == 'cam_company':temp['cam_company'] = str(data[each]['make'])
						elif each_required == 'cam_model':temp['cam_model'] = str(data[each]['camera'])
						elif each_required == 'focal_length':temp['focal_length'] = str(data[each]['focalLength'])
						elif each_required == 'shutter_speed':temp['shutter_speed'] = str(data[each]['shutterSpeed'])
						elif each_required == 'aperture':temp['aperture'] = str(data[each]['aperture'])
						elif each_required == 'iso_film':temp['iso_film'] = str(data[each]['isoFilm800'])
						elif each_required == 'width':temp['width'] = str(data[each]['width'])
						elif each_required == 'height':temp['height'] = str(data[each]['height'])
					final.append(temp)						
				return final
			else:
				return "error: Undefined information parametre passed"
