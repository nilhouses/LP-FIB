--Queues, programa sessió 4
data Queue a = Queue [a] [a]
     deriving (Show)
--cua = Queue [2,8,5] [4,7]
--que representa la cua on el primer és el 2 i segueix amb 8, 5, 7 i 4

create :: Queue a
create = Queue [] []

push :: a -> Queue a -> Queue a
push elem (Queue x y) = Queue x (elem:y)


--El pop es fa treient el primer de la primera llista, si en té, i sinó, passant els de la segona
-- llista cap a la primera (en l’ordre correcte) i agafant el primer tot deixant la resta.

pop :: Queue a -> Queue a
pop (Queue [] []) = Queue [] []
pop (Queue [] y) = Queue (tail$reverse y) []
pop (Queue x y) = Queue (tail x) y

top :: Queue a -> a
top (Queue [] y) = head $ reverse y
top (Queue x y) = head x

empty :: Queue a -> Bool
empty (Queue [] []) = True
empty _ = False

-------------------
--Dues cues són iguals? Funció

instance Eq a => Eq (Queue a)
    where
        (Queue x1 y1) == (Queue x2 y2) = x1 ++ reverse y1 == x2 ++ reverse y2


------------------------------------------------------------------------------------------
--P50086
instance Functor Queue
    where fmap f (Queue x1 x2) = Queue (fmap f x1) (fmap f x2)


translation :: Num b => b -> Queue b -> Queue b
translation num cola = fmap (+num) cola

-------------------------------------------------------------------------------------------
--Aplicatiu, necessari per la mònada
-- (<*>) :: f (a -> b) -> (f a -> f b)
-- pure :: a -> f a
instance Applicative Queue
    where
        (Queue [x] []) <*> q   = Queue [] [x] <*> q
        (Queue [] [x]) <*> q   = Queue [x] [] <*> q
        pure x                 = Queue [x] []

merge :: Queue a -> Queue a -> Queue a
merge (Queue x1 y1) (Queue x2 y2) = Queue (x1 ++ reverse y1) (x2 ++ reverse y2)

-------------------------------------------------------------------------------------------
--Mònada
-- return :: a -> m a                  --Empaqueta
-- (>>=)  :: m a -> (a -> m b) -> m b  --desempaqueta, aplica i empaqueta
-- (>>)   :: m a -> m b -> m b         --és purament estètica
instance Monad Queue
    where
        return x = Queue [x] []
        (Queue x y)  >>= f =  foldl merge create (map f (x ++ (reverse y)))

kfilter :: (p -> Bool) -> Queue p -> Queue p
kfilter p q = do
    x <- q
    if (p x) then return x else (Queue [] [])

