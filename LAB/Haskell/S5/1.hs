--P70540
data Expr = Val Int | Add Expr Expr | Sub Expr Expr | Mul Expr Expr | Div Expr Expr
----------------------------------------------------------------------------------

eval1 :: Expr -> Int
eval1 (Val x) = x
eval1 (Add x y) = eval1 x + eval1 y
eval1 (Sub x y) = eval1 x - eval1 y
eval1 (Mul x y) = eval1 x * eval1 y
eval1 (Div x y) = div (eval1 x) (eval1 y)

----------------------------------------------------------------------------------

eval2 :: Expr -> Maybe Int 
eval2 (Val x) = return x -- aplica el Just
eval2 (Add x y) = opera2 (+) (eval2 x) (eval2 y)
eval2 (Sub x y) = opera2 (-) (eval2 x) (eval2 y)
eval2 (Mul x y) = opera2 (*) (eval2 x) (eval2 y)
eval2 (Div x y) 
    | eval2 y == Just 0 = Nothing
    | otherwise = opera2 div (eval2 x) (eval2 y)

opera2 :: (Int -> Int -> Int) -> Maybe Int -> Maybe Int -> Maybe Int --de dos valors Maybe en retorna un altre maybe 
opera2 op e1 e2 = do x <- e1 --treu el Just, o propaga un Nothing, si n'hi ha
                     y <- e2
                     Just (op x y)

----------------------------------------------------------------------------------

eval3 :: Expr -> Either String Int --left missatgeError |  right valor
eval3 (Val x) = Right x
eval3 (Add x y) = opera3 (+) x y
eval3 (Sub x y) = opera3 (-) x y
eval3 (Mul x y) = opera3 (*) x y
eval3 (Div x y) = do
    xv <- eval3 x         
    case ry of
        Right 0 -> Left "div0"
        Right v -> return $ div xv v --aplica el just a la divisió
        err -> err
    where 
        ry = eval3 y


opera3 :: (Int -> Int -> Int) -> Expr -> Expr -> Either String Int --de dos valors Maybe en retorna un altre maybe 
opera3 op e1 e2 = do x <- eval3 e1 --treu el Right, o propaga un Left, si n'hi ha
                     y <- eval3 e2
                     Right (op x y)


--EXEMPLE
--Mul (Add (Val 2) (Val 3)) (Sub (Val 2) (Val 3))

--Primer intenta resoldre la multiplicació, com que no té el primer argument (x) el calcula:
--opera3 (+) (Val 2) (Val 3) => Right (2 + 3) => Right 5
--Add (Val 2) (Val 3) -> Right(2+3) = Right(5)

--Segon intenta resoldre la multiplicació, com que no té el segon argument (y) el calcula:
--opera3 (-) (Val 2) (Val 3) => Right (2 - 3) => Right (-1)
--Sub (Val 2) (Val 3)-> Right(2-3) = Right(-1)

--Per últim ho intenta, cridant a opera3
--opera3 (*) (Right 5) (Right (-1)) => Right (5 * (-1)) => Right (-5)
