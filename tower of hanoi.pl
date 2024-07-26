
hanoi(0, _, _, _) :- !.
hanoi(N, Source, Auxiliary, Destination) :-
    N > 0,
    M is N - 1,
    hanoi(M, Source, Destination, Auxiliary),
    move(Source, Destination),
    hanoi(M, Auxiliary, Source, Destination).
move(Source, Destination) :-
    format('Move disk from ~w to ~w~n', [Source, Destination]).

