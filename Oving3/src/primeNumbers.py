def primes():
    myPrimes = []
    count = 0
    while len(myPrimes) < 1000:
        if count > 1:
            for i in range(2, count):
                if (count % i) == 0:
                    break
            else:
                myPrimes.append(count)
        count += 1
    return myPrimes


if __name__ == '__main__':
    prime = primes()
    print(prime)
