--P93588
--Emula el map usant llistes per comprensió.
myMap :: (a -> b) -> [a] -> [b]
myMap f llista = [f x | x <- llista]
--myMap (*2) [1..5] = [2,4,6,8,10]
----------------------------------------------------------------------------------
--Emula filter usant llistes per comprensió.
myFilter :: (a -> Bool) -> [a] -> [a] 
myFilter propietat llista = [x | x <-llista, propietat x] 
--myFilter odd [1..5] = [1,3,5]
----------------------------------------------------------------------------------
--Emula el zipWith usant llistes per comprensió i zip.
myZipWith :: (a -> b -> c) -> [a] -> [b] -> [c]
myZipWith op la lb = [op a b |(a,b) <- zip la lb]
--myZipWith (*) [1..4] [1..4] = [1,4,9,16]
----------------------------------------------------------------------------------
--Donades dues llistes d'enters la i lb, genera la llista de parells tq a % b == 0
thingify :: [Int] -> [Int] -> [(Int, Int)]
thingify la lb = [(a,b) | a <- la, b <- lb, mod a b == 0]
--thingify [1..6] [1..3] = [(1,1),(2,1),(2,2),(3,1),(3,3),(4,1),(4,2),(5,1),(6,1),(6,2),(6,3)]
----------------------------------------------------------------------------------
--que, donat un natural no nul, genera la llista ordenada amb els seus factors
factors :: Int -> [Int]
factors n = [x | x <- [1..n], mod n x == 0]
--factors 24 = [1,2,3,4,6,8,12,24]