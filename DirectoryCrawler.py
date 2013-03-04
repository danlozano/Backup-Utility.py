from datetime import date
import os

from FileContainer import *


class DirectoryCrawler(object):

	def __init__(self, location, types, createdAfterDate, createdBeforeDate, modifiedAfterDate, modifiedBeforeDate, smallerThan, biggerThan, duplicates):
		self.location = location
		
		self.types = types
		
		self.createdAfterDate = createdAfterDate
		self.createdBeforeDate = createdBeforeDate
		self.modifiedAfterDate = modifiedAfterDate
		self.modifiedBeforeDate = modifiedBeforeDate

		self.smallerThan = smallerThan
		self.biggerThan = biggerThan

		self.duplicates = duplicates

		self.fileList = []

		self.__lookForFiles__()
		self.__saveToFile__()


	def __lookForFiles__(self):

		for (dirName, subsHere, filesHere) in os.walk(self.location):
			
			#print('[' + dirName + ']')
			breakLoop = False

			for fname in filesHere:
				breakLoop = False
				if fname.startswith('.'):
					continue

				fullPath = os.path.join(dirName, fname)
				fileSize = os.path.getsize(fullPath) / (1024.0 * 1024.0)
				fileType = os.path.splitext(fname)[1].lower()
				dateCreated = date.fromtimestamp(os.path.getctime(fullPath))
				dateModified = date.fromtimestamp(os.path.getmtime(fullPath))

				if self.duplicates:
					for possibleDuplicate in self.fileList:
						if fname == possibleDuplicate.fileName and fileSize == possibleDuplicate.fileSize:
							breakLoop = True
				
				if breakLoop:
					continue

				f = FileContainer(fname, fullPath, fileType, fileSize, dateCreated, dateModified)

				if f.type() not in self.types:
					continue
				elif not f.createdAfter(self.createdAfterDate):
					continue
				elif not f.createdBefore(self.createdBeforeDate):
					continue
				elif not f.modifiedAfter(self.modifiedAfterDate):
					continue
				elif not f.modifiedBefore(self.modifiedBeforeDate):
					continue
				elif not f.biggerThan(self.biggerThan):
					continue
				elif not f.smallerThan(self.smallerThan):
					continue

				self.fileList.append(f)


	def __saveToFile__(self):
		print('Saving to file. \n')
		f = open('BackupResults.txt','w')
		f.write('File Name | File Location')
		f.write('\n')
		for fileEntry in self.fileList:
			f.write(str(fileEntry))
			f.write('\n')
		f.close()

