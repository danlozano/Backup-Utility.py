""" 
Daniel Lozano Valdes
"""

from time import strptime
import datetime
from os import path

from DirectoryCrawler import *

if __name__ == '__main__':


	print("Welcome to Dan's Magic File Utility V 1.0")


	while True:
		location = raw_input('What location would you like to backup? Example: /Users/danlozano/Desktop \n')
		if path.isdir(location):
			break
		else:
			print('Please enter a valid directory. \n') 
			

	print('What types of files would you like to backup? ')

	while True:
		text = raw_input('Text? (Y/N) \n')
		if text.lower() == 'y' or text.lower() == 'n':
			break
		else:
			print('Please enter Y or N ! \n')

	while True:
		audio = raw_input('Audio? (Y/N) \n')
		if audio.lower() == 'y' or audio.lower() == 'n':
			break
		else:
			print('Please enter Y or N ! \n')

	while True:
		image = raw_input('Image? (Y/N) \n')
		if image.lower() == 'y' or image.lower() == 'n':
			break
		else:
			print('Please enter Y or N ! \n')

	while True:
		video = raw_input('Video? (Y/N) \n')
		if video.lower() == 'y' or video.lower() == 'n':
			break
		else:
			print('Please enter Y or N ! \n')


	while True:
		while True:
			try:
				createdAfter = raw_input('Files created after: Format: 2012-12-31 \n')
				if createdAfter.lower() == 'y':
					createdAfter = '1950-01-01'
				createdAfterDate = datetime.date(*strptime(createdAfter, "%Y-%m-%d")[0:3])
				break
			except ValueError:
				print('Please enter a valid date. \n')

		while True:
			try:
				createdBefore = raw_input('Files created before: Format: 2012-12-31 \n')
				if createdBefore.lower() == 'y':
					createdBeforeDate = datetime.datetime.now().date()
					break
				createdBeforeDate = datetime.date(*strptime(createdBefore, "%Y-%m-%d")[0:3])
				break
			except ValueError:
				print('Please enter a valid date. \n')

		if createdAfterDate < createdBeforeDate:
			break
		else:
			print('Created after date must be EARLIER THAN created before date ! \n')

	while True:
		while True:
			try:
				modifiedAfter = raw_input('Files modified after: Format: 2012-12-31 \n')
				if modifiedAfter.lower() == 'y':
					modifiedAfter = '1950-01-01'
				modifiedAfterDate = datetime.date(*strptime(modifiedAfter, "%Y-%m-%d")[0:3])
				break
			except ValueError:
				print('Please enter a valid date. \n')

		while True:
			try:
				modifiedBefore = raw_input('Files modified before: Format: 2012-12-31 \n')
				if modifiedBefore.lower() == 'y':
					modifiedBeforeDate = datetime.datetime.now().date()
					break
				modifiedBeforeDate = datetime.date(*strptime(modifiedBefore, "%Y-%m-%d")[0:3])
				break
			except ValueError:
				print('Please enter a valid date. \n')

		if modifiedAfterDate <= modifiedBeforeDate:
			break
		else:
			print('Modifed after date must be EARLIER THAN modified before date ! \n')


	while True:
		while True:
			biggerThan = raw_input('Files bigger than: (Mb) \n')
			biggerThan = int(biggerThan)
			if biggerThan >= 0:
				break
			else:
				print('Please enter a valid number (0 - X) \n')

		while True:
			smallerThan = raw_input('Files smaller than: (Mb) \n')
			smallerThan = int(smallerThan)
			if smallerThan > 0:
				break
			else:
				print('Please enter a number bigger than 0. \n')

		if biggerThan < smallerThan:
			break
		else:
			print('Bigger than value must BE SMALLER than smaller than value. \n')

	while True:
		duplicates = raw_input('Would you like to backup duplicates? (Y/N) \n')
		if duplicates.lower() == 'y' or duplicates.lower() == 'n':
			break
		else:
			print('Please enter Y or N ! \n')


	types = []
	if text == 'y':
		types.append('text')
	if audio == 'y':
		types.append('audio')
	if image == 'y':
		types.append('image')
	if video == 'y':
		types.append('video')

	if duplicates.lower() == 'y':
		duplicates = False
	elif duplicates.lower() == 'n':
		duplicates = True


	crawler = DirectoryCrawler(location, types, createdAfterDate, createdBeforeDate, modifiedAfterDate, modifiedBeforeDate, smallerThan, biggerThan, duplicates)
	
