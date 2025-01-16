--P80618
--Queues
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
pop (Queue x y) = Queue(tail x) y

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