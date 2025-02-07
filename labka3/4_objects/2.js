let user = {
  name: "John",
  sizes: {
      height: 182,
      width: 50
  }
  };

  let clone = Object.assign({}, user);

  alert( user.sizes === clone.sizes ); // true, same object

  user.sizes.width = 60;    // change a property from one place
  alert(clone.sizes.width); // 60, get the result from the other one