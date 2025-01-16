--P31745
---------------------------------------------------
--Passa una matriu (llista de llistes) a una sola llista
flatten :: [[Int]] -> [Int]
flatten = foldl (++) []--més curt
--EL QUE HAVIA FET JO ->flatten llista = foldl (++) [] llista
--El primer element el concateno amb una llista buida i la resta 
--la concateno amb l'acumulaciód e concatenacions anteriors
---------------------------------------------------
--Retorna la llargada d'una string
myLength :: String -> Int
myLength [] = 0
myLength cadena = last (zipWith (\x y -> y) cadena llistaEnters)
    where llistaEnters = iterate (+1) 1
--Vaig "posant" l'string al costat d'una llista d'enters [1,2,3,...]
-- Afer zipWith de cadena llistaEnters em queda [1,2,3,4,5], pel que 
--la paraula té llargada 5 i em quedo el 5 (last) 
----------------------------------------------------
--Dona la volta a una llista (myReverse = reverse)
myReverse :: [Int] ->[Int]
myReverse llista = foldl (\xs x -> x:xs) [] llista
--Posa la llista buida radere de x0, després xo:llista buida radere de x1, ...x4x3x2x1x0[]
----------------------------------------------------
--Per cada subllista de la lista retorna un enter indicant quantes vegades 
--hi ha l'enter a buscar a cada llista
countIn :: [[Int]] -> Int -> [Int]
countIn llista x = map (func x) llista
    where 
        func x list = length (filter (== x) list)
-- al map -> a cada subllista d ela llsita li aplica func x, la qual compta la llargada 
--de la llista composta només pels elements filtrats de la llista original.
----------------------------------------------------
--Retorna la primera paraula d'un string
firstWord :: String -> String
firstWord sentence = takeWhile (/= ' ') (dropWhile (== ' ') sentence)
--primer descarto tots els espais que vagi llegint fins que llegeixo alguna cosa diferent 
--d'espai, pel que aquesta cosa serà la primera paraula (fins que torni a llegir un espai)