for (let char of "test") {
    // triggers 4 times: once for each character
    alert( char ); // t, then e, then s, then t
  }



  let str = '𝒳😂';
  for (let char of str) {
      alert( char ); // 𝒳, and then 😂
  }