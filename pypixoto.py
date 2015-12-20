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
