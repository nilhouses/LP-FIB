--P98957
-- "<-" és com un "pertany"
--UEP! No puc fer servir enumeracions del tipus [1..] [2..] etc
----------------------------------------------------------------------------------
ones :: [Integer]
ones = iterate id 1
--ones =1:ones
----------------------------------------------------------------------------------
nats :: [Integer] --nombres naturals
nats = iterate (+1) 0
----------------------------------------------------------------------------------
ints :: [Integer]
ints = iterate (\x-> if x > 0 then -x else -x+1) 0
----------------------------------------------------------------------------------
--[0,1,3,6,10,15,21,28,...]
triangulars :: [Integer]
triangulars = tail $ scanl (+) 0 nats --sense el tail seria [0,0,1,3,6,10,15,21,28]
----------------------------------------------------------------------------------
--[1,1,2,6,24,...]
factorials :: [Integer] -- n! = n(n-1)!  --> 
factorials = scanl (*) 1 (tail nats)
----------------------------------------------------------------------------------
--[0,1,1,2,3,5,8,13,...]
fibs :: [Integer]
fibs = 0:1: zipWith (+) fibs (tail fibs)
----------------------------------------------------------------------------------
--[2,3,5,7,11,13,17,19,...]
primes :: [Integer]
primes  = garbell natsMajors2
    where 
        garbell (p : xs) = p : garbell [x | x <- xs, mod x p /= 0]

natsMajors2 :: [Integer]
natsMajors2 = iterate (+1) 2
----------------------------------------------------------------------------------
--[1,2,3,4,5,6,8,9,…] Només tenen 2,3 i 5 com a divisors primers
hammings :: [Integer]
hammings = 1 : map (2*) hammings `merge` map (3*) hammings `merge` map (5*) hammings
  where merge (x:xs) (y:ys)
          | x < y = x : xs `merge` (y:ys)
          | x > y = y : (x:xs) `merge` ys
          | otherwise = x : xs `merge` ys
----------------------------------------------------------------------------------
lookNsay :: [Integer]
lookNsay = iterate count 1

count :: Integer -> Integer
count a = read $ next $ show a

next :: [Char] -> [Char]
next [] = []
next llista = (show n) ++ [primero] ++ next resta --show passa a string un nombre
  where
    primero = head llista
    n = length $ takeWhile (== primero) llista
    resta = dropWhile (== primero) llista

----------------------------------------------------------------------------------

tartaglia :: [[Integer]]
tartaglia = iterate operador [1]
    where operador xs = zipWith (+) ([0] ++ xs) (xs ++ [0])