--P87082
------------------------------------ BODY MASS INDEX
bmi :: Double -> Double -> Double
bmi m h = m / (h * h)
------------------------------------
howFat :: Double -> Double-> String
howFat w h
    | x < 18 = "underweight"
    | 18 < x && x <= 25 = "normal weight"
    | 25 < x && x <= 30 = "overweight"
    | 30 < x && x <= 40 = "obese"
    | otherwise = "severely obese" 
    where x = bmi w h
------------------------------------
main :: IO()
main = do
    line <- getLine
    if (head line) == '*' then
        return () -- no torno res, fi del main
    else
        do
        let w = words line
        let name = w !! 0
        let weight = read(w !! 1) --string -> Double (Al que jo li assigni)
        let height = read(w !! 2)
        putStrLn(name ++ ": " ++ (howFat weight height))
        main --per fer el bucle