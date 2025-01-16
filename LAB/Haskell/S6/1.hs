--P87974
main :: IO ()
main = do
    nom <-getLine
    if (head nom) == 'A'|| (head nom) == 'a' then 
        putStrLn "Hello!"
    else 
        putStrLn "Bye!"
