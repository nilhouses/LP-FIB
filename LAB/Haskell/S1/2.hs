myLength :: [Int] -> Int
myLength [] = 0
myLength n = 1 + myLength(tail n)
--------------------------------------------------
myMaximum :: [Int] -> Int
myMaximum [h] = h
myMaximum (h:t) = max h (myMaximum t)
----------------------------------------------------
average :: [Int] -> Float
average l = fromIntegral (mySuma l) / fromIntegral (myLength l)

mySuma:: [Int] -> Int
mySuma [] = 0
mySuma (x:l) = x + mySuma l
-------------------------------------------------
buildPalindrome :: [Int] -> [Int]
buildPalindrome l = (reverse l) ++ l
--------------------------------------------------
remove :: [Int] -> [Int] -> [Int]
remove [] _ = []
remove (x:xs) d
  |elem x d = remove xs d -- continuo amb la resta de la llista
  |otherwise = x : remove xs d -- afegeixo x a la llista i segueixo amb la resta
--------------------------------------------
flatten :: [[Int]] -> [Int]
flatten [] = []
flatten l = (head l) ++ flatten (tail l)
----------------------------------------------
oddsNevens :: [Int] ->([Int],[Int])
oddsNevens [] = ([],[])
oddsNevens (x:xs) -- recorda, x es el primer element i xs la cua de la llista
  | odd x = (x:a, b)
  | otherwise = (a, x:b)
  where
    (a,b) = oddsNevens xs -- (x:xs) es fa per recÃ³rrer la llista , on x es el primer element i xs la resta
-----------------------------------------------
primeDivisors :: Int -> [Int]
primeDivisors x
  | isPrime x = [x]
  | otherwise =  reverse (primeDivRec x (x-1))

primeDivRec :: Int -> Int -> [Int]
primeDivRec _ 0 = []
primeDivRec x y
  | mod x y == 0 && isPrime y = y : primeDivRec x (y-1)
  | otherwise = primeDivRec x (y-1)

isPrime :: Int -> Bool
isPrime n
  | n < 2 = False
  | otherwise  = isPrimeRec n (n-1)

isPrimeRec :: Int -> Int -> Bool
isPrimeRec x y
  | y == 1 = True
  | mod x y == 0 = False
  | otherwise = isPrimeRec x (y-1)

