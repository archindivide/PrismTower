#generate seed for a random room
def randomRoom:
	room = int(random()*20);
	return room;

#determine if there is an enemy in the room (currently .2 chance)
def isEnemy:
	chanceOfEnemy = .2;
	possible = int(random()*100);
	if possible < (chanceOfEnemy * 100):
		return true;
	else
		return false;

#function for randomly generating the map
def generateMap:
	#minimum number of rooms
	minRooms = 10;
	#possible extra amount of rooms
	additionalRooms = 10;
	#total number of rooms (currently between 10 and 20)
	totalRooms = int(minRooms + random()*additionalRooms)
	
	roomCollection = []
	
	for x in totalRooms:
		roomCollection.append(randomRoom)
	
	