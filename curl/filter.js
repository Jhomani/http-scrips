const filter2 = encodeURIComponent(JSON.stringify({
	fields: ['id', 'objectId', 'createdAt', 'lastMessage'],
  orderBy: ['chatRooms.createdAt', 'DESC'],
  include: [
    {
      model: 'users',
      fields: ['id', "email", 'firstName', 'lastName', 'pushToken'],
      orderBy: ['id', 'DESC'],
      limit: 2,
      include: [
        {
          model: "files",
          fields: ['id', 'link']
        }
      ]
    },
    {
      model: 'objects',
      fields: ['id', 'createdAt'],
      include: [
        {
          model: "files",
          fields: ['id', 'link']
        }
      ]
    },
    {
      model: 'usersChats',
      fields: ['id', 'userId', 'chatRoomId', 'unreadMessages'],
			where: {
				userId: ['=', 3]
			},
			nested: true
    }
  ]
}));

const filter = encodeURIComponent(JSON.stringify({
  "market": "BINANCE",   
  "symbolId": "a57dfcc2-9be4-11eb-a8b3-0242ac130003",
  "timeFrame": 15
}));


console.log(filter);
