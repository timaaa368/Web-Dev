function showPrimes(n) {
  let primes = [];
  for (let i = 2; i < n; i++) {
      if (!isPrime(i)) continue;
      primes.push(i);
  }
  console.log(primes.join(", "));
  }

  function isPrime(n) {
  for (let i = 2; i < n; i++) {
      if (n % i == 0) return false;
  }
  return true;
  }

  showPrimes(50); 