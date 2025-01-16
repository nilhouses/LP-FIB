 
absValue :: Int -> Int
absValue n
   | n >= 0 = n
   | otherwise = -n


power :: Int -> Int -> Int
power  _ 0 = 1
power  x p
   | even p     = mig * mig
   | otherwise  = mig * mig * x
   where
   meitat_exponent = p`div`2
   mig = power x meitat_exponent


isPrime :: Int -> Bool
isPrime n
    | n < 2 = False
    | otherwise  = isPrimeRec n 2

isPrimeRec :: Int -> Int -> Bool
isPrimeRec n actual
   | actual * actual > n = True
   | mod n actual == 0 = False
   | otherwise = isPrimeRec n (actual + 1)


slowFib :: Int -> Int
slowFib n
   |  n < 2 = n
   |  otherwise = slowFib (n-1) + slowFib (n-2)


quickFib :: Int -> Int
quickFib n
   |  n < 2 = n
   |  otherwise = snd(taula n)

taula :: Int -> (Int,  Int)
taula 1 = (0,1)
taula n = (snd x, fst x + snd x)
    where
        x = taula(n-1)


--Extra
factorial :: Integer -> Integer
factorial 0 = 1
factorial n = n + factorial (n - 1)

