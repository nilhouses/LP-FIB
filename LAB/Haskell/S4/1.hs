--P97301
--data Either a b = 
--      Left a |Right b
fizzBuzz :: [Either Int String]
fizzBuzz = map f [0..]
    
--amb la seg func estic dient que el cas incorrecte (left) retorna un int i el correcte (right) retorna una string
f :: Int -> Either Int String    
f x
    |x `mod` 15 == 0 = Right "FizzBuzz"
    |x `mod` 3 == 0 = Right "Fizz"
    |x `mod` 5 == 0 = Right "Buzz"
    |otherwise = Left x
--[Right "FizzBuzz",Left 1,Left 2,Right "Fizz",Left 4,Right "Buzz",Right "Fizz",Left 7]
