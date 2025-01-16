--P90677
--(1) Crear un Foldl -> foldl op x [xs] aplica op x x0, després op resultat x1,...
myFoldl :: (a -> b -> a) -> a -> [b] -> a
myFoldl _ a [] = a
myFoldl op xo (x:xs) = myFoldl op (op xo x) xs

--(2) Crear un Foldr -> foldr op x [xs] aplica op x xn, després op resultat xn-1,...
myFoldr :: (a -> b -> b) -> b -> [a] -> b
myFoldr _ a [] = a
myFoldr op n (x:xs) = op x (myFoldr op n xs)

--(3) Crear un iterate -> iterate op x retorna x op(x), op(op(x))
myIterate :: (a-> a)-> a -> [a]
myIterate f x = x : myIterate f(f x)
--myIterate op n = [n] ++ myIterate op (op n) 

--(4) Crear un until -> tornar el primer element d'un iterate que compleix la condició
myUntil :: (a -> Bool) -> (a -> a) -> a -> a
myUntil cond op n
    | cond n = n
    | otherwise = myUntil cond op (op n)

--(5) Crear un map -> aplicar una funció a tot element de la llista i tornar la llista resultant

myMap :: (a -> b) -> [a] -> [b]
myMap f [] = []
myMap f (x:xs) = f x : myMap f xs

--(6) Crear una operació myFilter f xs on es retorna la llista d'elements que compleixen la condició f
myFilter :: (a -> Bool) -> [a] -> [a]
myFilter _ [] = []
myFilter f (x:xs)
    | f x = x : myFilter f xs
    | otherwise = myFilter f xs

--(7) Crear l'operació myAll que retorna si tots els elements compleixen la condició myAll odd llista = true o false
myAll :: (a -> Bool) -> [a] -> Bool
myAll _ [] = True
myAll f (x:xs) = f x && myAll f xs

--(8) Crear l'operació que busca si hi ha algun element que compleix la condició
myAny :: (a -> Bool) -> [a] -> Bool
myAny _ [] = False -- true -> false  i and -> or són els canvis respecte l'anterior
myAny f (x:xs) = f x || myAny f xs

--(9) Crear l'operació myZip, que uneix dues llistes
myZip :: [a] -> [b] -> [(a,b)]
myZip _ [] = []
myZip [] _ = []
myZip (a:as) (b:bs) = (a,b):(myZip as bs) 

--(10) Crear l'operció myZipWith que opera dues llistes 
myZipWith :: (a -> b -> c) -> [a] -> [b] -> [c]
myZipWith f _ [] = []
myZipWith f [] _ = []
myZipWith f (a:as) (b:bs) = (f a b):(myZipWith  f as bs) 

--s'hauria pogut reutilitzar myMap