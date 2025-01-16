---P93632
---------------------------------------------------
-- Retorna si dues llistes són iguals
eql :: [Int] -> [Int] -> Bool 
eql l1 l2
    | length l1 /= length l2 = False
    | otherwise = and(zipWith (==)l1 l2)
---------------------------------------------------
--multiplica la llista d'entrada 
prod :: [Int]->Int
prod llista = foldl (*) 1 llista
---------------------------------------------------
--multiplica NOMÉS els elements parells de la llista d'entrada
prodOfEvens :: [Int] -> Int 
prodOfEvens = prod.filter even
--Jo m'havia complicat:
--prodOfEvens llista = foldl (*) 1 parells
    --where parells = filter even llista
---------------------------------------------------
 -- retorna totes les potències de 2 
powersOf2 :: [Int]
powersOf2 = iterate (*2) 1
---------------------------------------------------
scalarProduct :: [Float] -> [Float] -> Float --Retorna el producte escalar de les dues llistes
scalarProduct a b = foldl (+) 0 $ zipWith (*) a b

-- Jo també m'havia complicat
--scalarProduct l1 l2 = foldl (+) 0 productes --(sumo els productes de les llistes)
    --where productes = zipWith (*) l1 l2

--[2.0,1.0,5.0] [3.0,2.0,2.0] = [2*3+1*2+5*2]=[6+2+10]