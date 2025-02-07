// let room = {
//     number: 23
//   };
  
//   let meetup = {
//     title: "Conference",
//     participants: [{name: "John"}, {name: "Alice"}],
//     place: room // meetup references room
//   };
  
//   room.occupiedBy = meetup; // room references meetup
  
//   alert( JSON.stringify(meetup, ['title', 'participants', 'place', 'name', 'number']) );
//   /*
//   {
//     "title":"Conference",
//     "participants":[{"name":"John"},{"name":"Alice"}],
//     "place":{"number":23}
//   }
//   */



  let room = {
    number: 23
  };
  
  let meetup = {
    title: "Conference",
    participants: [{name: "John"}, {name: "Alice"}],
    place: room // meetup references room
  };
  
  room.occupiedBy = meetup; // room references meetup
  
  alert( JSON.stringify(meetup, function replacer(key, value) {
    alert(`${key}: ${value}`);
    return (key == 'occupiedBy') ? undefined : value;
  }));
  
  /* key:value pairs that come to replacer:
  :             [object Object]
  title:        Conference
  participants: [object Object],[object Object]
  0:            [object Object]
  name:         John
  1:            [object Object]
  name:         Alice
  place:        [object Object]
  number:       23
  occupiedBy: [object Object]
  */