-- P29040

-- INSERTION SORT

-- RECORDA, PER RECÓRRER UNA LLISTA PUC FER QUE ENTRI COM A PARÀMETRE DE MANERA x:xs DIRECTAMENT

insert :: [Int] -> Int -> [Int]--llista ordenada
insert [] x = [x]
insert (i:llista) x
    | i < x = i:(insert llista x)
    | otherwise = x:i:llista

isort :: [Int] -> [Int]
isort [] = []
isort (x:xs) = insert (isort xs) x
------------------------------------------------------
--SELECTION SORT

remove :: [Int] -> Int -> [Int]
remove [] _ = [] --el cas base imprescindible
remove (x:xs) n
    | x == n = xs
    | otherwise =  x:remove xs n

ssort :: [Int] -> [Int]
ssort [] = []
ssort list = min:ssort(remove list min)
    where min = minimum list
--------------------------------------------------------
--MERGE SORT
merge :: [Int] -> [Int] -> [Int]
merge [] llista = llista
merge llista [] = llista
merge (n1:llista1) (n2:llista2)
    | n1 < n2  =  n1:merge llista1 (n2:llista2)
    | otherwise = n2: merge (n1:llista1) llista2
--fet per fusionar dues llistes ordenades

msort :: [Int] -> [Int]
msort [] = []
msort [x] = [x]
msort llista = merge (msort l) (msort r)
    where
        l = take n llista
        r = drop n llista
        n = div (length llista) 2
--dividir i vèncer literalment
---------------------------------------------------------
--QUICK SORT
qsort :: [Int] -> [Int]
qsort [] = []
qsort (pivot:l) = qsort menors ++ [pivot] ++ qsort majors
    where
        menors = [x | x <- l, x < pivot]
        majors = [x | x <- l, x >= pivot] --notació interessant
------------------------------------------------------------
genQsort ::Ord a => [a] -> [a] -- Forma general!
genQsort [] = []
genQsort (pivot:l) = genQsort menors ++ [pivot] ++ genQsort majors
    where
        menors = [x | x <- l, x < pivot]
        majors = [x | x <- l, x >= pivot] --notació interessant


