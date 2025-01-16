--P37072
--Arbres binaris
--DEFINICIÓ d'un arbre binari 
data Tree a = Node a (Tree a) (Tree a) | Empty
    deriving (Show)

--ENTRADA (lectura arbre)
--let t7 = Node 7 Empty Empty
--let t6 = Node 6 Empty Empty
--let t5 = Node 5 Empty Empty
--let t4 = Node 4 Empty Empty
--let t3 = Node 3 t6 t7
--let t2 = Node 2 t4 t5
--let t1 = Node 1 t2 t3
--let t1' = Node 1 t3 t2

size :: Tree a -> Int --nombre nodes
size Empty = 0
size (Node _ left right) = 1 + size left + size right

height :: Tree a -> Int --alçada arbre
height Empty = 0
height (Node _ left right) = 1 + max (height left)(height right)

equal :: Eq a => Tree a -> Tree a -> Bool --si dos arbres són iguals
equal Empty Empty = True
equal Empty _ = False
equal _ Empty = False
equal (Node a la ra) (Node b lb rb)
    |a==b && equal la lb && equal ra rb = True
    |otherwise = False


isomorphic :: Eq a => Tree a -> Tree a -> Bool -- si un arbre es pot obtenir amb el simètric de l'altre
isomorphic Empty Empty = True
isomorphic Empty _ = False
isomorphic _ Empty = False
isomorphic (Node a la ra) (Node b lb rb)
    | a /= b = False
    | otherwise = (isomorphic la lb && isomorphic ra rb)||(isomorphic la rb && isomorphic ra lb)

preOrder :: Tree a -> [a] -- arrel, esquerra, dreta
preOrder Empty = []
preOrder (Node a left right) = [a] ++ preOrder left ++ preOrder right

postOrder :: Tree a -> [a] -- esquerra, dreta, arrel
postOrder Empty = []
postOrder (Node a left right) = postOrder left ++ postOrder right ++ [a]

inOrder :: Tree a -> [a] --  -- esquerra, arrel, dreta
inOrder Empty = []
inOrder (Node a left right) = inOrder left ++ [a] ++ inOrder right
------------------------------------------------------------------------
--BFS
breadthFirst :: Tree a -> [a]
breadthFirst Empty = []
breadthFirst a = breadthRec [a]

breadthRec :: [Tree a] -> [a]
breadthRec [] = []
breadthRec (Empty:xs) = breadthRec xs
breadthRec ((Node a left right):xs) = a: breadthRec (xs ++ [left]++[right])
--Per recórrer un arbre agafa només el node i mira els altres nodes del mateix nivell abans de mirar 
--les fulles (arbres) left i right
------------------------------------------------------------------------
--Donats recorregut preOrdre i recorregut inOrdre d'un arbre retorna l'arbre Original, l'arbre no té elements repetits

build :: Eq a => [a] -> [a] -> Tree a --Objectiu separar l'arbre en 2 (build lpre lin) (build rpre rin)
build [] [] = Empty
build [x] [y] = Node x Empty Empty--llistes 1 sol elem
build (n:pre) ind = Node n (build lpre lin) (build rpre rin)
    where
        lin = takeWhile (/= n) ind --subarbre que penja de l'esquerra d'n en Inordre
        lastl = last lin  --últim element de la llista anterior (El necessito per trobar lpre i rpre)
        rin = tail $ dropWhile (/= n) ind --subarbre que penja de la dreta d'n en Inordre
        lpre = takeWhile (/= lastl) pre ++ [lastl]
        rpre = tail $ dropWhile (/= lastl) pre

--L'idea és que al preOrdre primer rebo l'arrel i puc buscar a l'inordre els seus dos arbres a l'esquerre i a la dreta de l'arrel
--PE
--[1,2,4,5,3] [4,2,5,1,3] 
-- lin = 4,2,5
--lastl = 5
-- rin = 3
--lpre = 2,4,5
--rpre = 3
------------------------------------------------------------------------
--Donats dos arbres aplica l'operació entre  els nodes que coincideixen, és a dir:
--      3               2                 5
--    6    7     i    4    5     =     10   12      si l'operació fos sumar 
overlap :: (a -> a -> a) -> Tree a -> Tree a -> Tree a 
overlap _ Empty Empty = Empty
overlap _ a Empty = a
overlap _ Empty b = b
overlap f (Node x left right) (Node y esq dret) = Node (f x y) (overlap f left esq) (overlap f right dret)
