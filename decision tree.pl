% Facts
parent('John', 'Alice').
parent('John', 'Bob').
parent('Alice', 'Carol').
parent('Alice', 'David').
parent('Bob', 'Eve').

% Rule to find a child of a given parent
child(Parent, Child) :-
    parent(Parent, Child).

% Rule to find siblings (children of the same parent)
sibling(Person1, Person2) :-
    parent(Parent, Person1),
    parent(Parent, Person2),
    Person1 \= Person2.

% Rule to find a grandparent of a given person
grandparent(Grandparent, Grandchild) :-
    parent(Grandparent, Parent),
    parent(Parent, Grandchild).

