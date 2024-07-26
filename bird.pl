% Facts
can_fly('Sparrow').
can_fly('Eagle').
can_fly('Falcon').

cannot_fly('Penguin').
cannot_fly('Ostrich').
can_bird_fly(Bird) :-
    can_fly(Bird), !,
    format('~w can fly.~n', [Bird]).

can_bird_fly(Bird) :-
    cannot_fly(Bird),
    format('~w cannot fly.~n', [Bird]).
