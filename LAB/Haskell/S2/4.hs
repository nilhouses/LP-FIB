import Distribution.Compat.Lens (_1)
--P71775
--(1) Countif cond llista retorna el nombre d'elements 
--de la llista que compleixen la condició
countIf :: (Int -> Bool) -> [Int] -> Int
countIf _ [] = 0
countIf f (x:xs)
    | f x = 1 + countIf f xs
    | otherwise = countIf f xs

--(2) Pam llista llista funcions retorni totes les llistes per cada funció
pam :: [Int] -> [Int-> Int] -> [[Int]]
pam _ [] = []
pam llista (f:fs) = map f llista : pam llista fs

--(3) pam2 llista llista funcions retorna la llista de llistes on per cada 
--element de la primera llista obtinc una llista nova on els elements son 
--l'element original amb cada operació
pam2 :: [Int] -> [Int-> Int] -> [[Int]]
pam2 xs fs = [[f x | f <- fs] | x <- xs]
--la part lila son els elements de cada subllista i les llistes grans partiran de tots els 
--elements de x, EXEMPLE --> pam2 [1,2,3] [(+1),(*2),(^2)] = [[2,2,1],[3,4,4],[4,6,9]]
--Aqui pilla l'1 com a x i crea una llista on hi aplica totes les f, després agafa el 2, i al final el 3

--ALTERNATIVA
--pam2 llista funcions = [map ($ x) funcions | x <- llista]
-- aplica x a les funcions on x es un element de la llista
--s'aniràn recorrent tots els elements de llista i se li aniran aplicant totes les funcions

--(4) filterFoldl fa un foldl dels valors de la llista que compleixen la propietat donada 
filterFoldl :: (Int -> Bool) -> (Int -> Int -> Int) -> Int -> [Int] -> Int 
filterFoldl prop func valor llista = foldl func valor llistaFiltrada
    where llistaFiltrada = filter prop llista --llista que compleix la propietat

--(5) 
insert :: (Int -> Int -> Bool) -> [Int] -> Int -> [Int]
insert _ [] a = [a]
insert func (x:xs) n
    | func n x = n:x:xs -- si es compleix la condició inserta
    | otherwise = x:insert func xs n --sino segueix buscant

insertionSort :: (Int -> Int -> Bool) -> [Int] -> [Int]
insertionSort _ []= [] 
insertionSort func llista = foldl (insert func) [] llista
--perque recorda que foldl f x xs amb x buit aplica la funcio a xs