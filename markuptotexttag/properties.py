#    This module is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

__author__ = "Wesley Hansen"
__date__ = "07/06/2012 11:29:17 PM"

import gtk
import pango

class MarkupProps(object):
	'''
	Stores properties that contain indices and appropriate values for that property.
	Includes an iterator that generates GtkTextTags with the start and end indices to 
	apply them to
	'''
	def __init__(self):	
		'''
		properties = (	{	
							'properties': {'foreground': 'green', 'background': 'red'}
							'start': 0,
							'end': 3
						},
						{
							'properties': {'font': 'Lucida Sans 10'},
							'start': 1,
							'end':2,
							
						},
					)
		'''
		self.properties = []#Sequence containing all the properties, and values, organized by like start and end indices
		self.text = ""#The raw text without any markup

	def add( self, label, value, start, end ):
		'''
		Add a property to MarkupProps. If the start and end indices are already in
		a property dictionary, then add the property:value entry into
		that property, otherwise create a new one
		'''
		for prop in self.properties:
			if prop['start'] == start and prop['end'] == end:
				prop['properties'].update({label:value})
                                break
		else:
			new_prop = 	{
							'properties': {label:value},
							'start': start,
							'end':end,
						}
			self.properties.append( new_prop )
						 

	def __iter__(self):
		'''
		Yields (TextTag, start, end)
		'''
		for prop in self.properties:
			tag = gtk.TextTag()
			tag.set_properties( **prop['properties'] )
			yield (tag, prop['start'], prop['end'])


		
