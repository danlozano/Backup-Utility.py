import time

class FileContainer(object):

	textTypes = ['.txt','.doc','.docx','.rtf','.pages']
	imageTypes = ['.png','.jpg','.tiff','.gif']
	audioTypes = ['.mp3','.wav','.aiff']
	videoTypes = ['.mov', '.avi','.mp4']

	def __init__(self, fileName, location, fileType, fileSize, dateCreated, dateModified):
		self.fileName = fileName
		self.location = location
		self.fileType = fileType
		self.fileSize = fileSize
		self.dateCreated = dateCreated
		self.dateModified = dateModified

	def __str__(self):
		return self.fileName + ' | ' + self.location

	def createdAfter(self, date):
		if self.dateCreated > date:
			return True
		else:
			return False

	def createdBefore(self, date):
		if self.dateCreated <= date:
			return True
		else:
			return False

	def modifiedAfter(self, date):
		if self.dateModified > date:
			return True
		else:
			return False

	def modifiedBefore(self, date):
		if self.dateModified <= date:
			return True
		else:
			return False

	def biggerThan(self, size):
		if self.fileSize >= size:
			return True
		else:
			return False

	def smallerThan(self, size):
		if self.fileSize < size:
			return True
		else:
			return False

	def type(self):
		if self.fileType in FileContainer.textTypes:
			return 'text'
		elif self.fileType in FileContainer.imageTypes:
			return 'image'
		elif self.fileType in FileContainer.audioTypes:
			return 'audio'
		elif self.fileType in FileContainer.videoTypes:
			return 'video'
		else:
			return 'other'





