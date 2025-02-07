function checkSpam(str) {
    let lowerStr = str.toLowerCase();
  
    return lowerStr.includes('vitamin') || lowerStr.includes('xxx');
  }
  
  alert( checkSpam('buy ViTAminA now') );
  alert( checkSpam('free xxxxx') );
  alert( checkSpam("innocent rabbit") );
  