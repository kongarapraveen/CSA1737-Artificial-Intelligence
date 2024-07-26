% Facts
planet('Mercury', 4879, 57.9).
planet('Venus', 12104, 108.2).
planet('Earth', 12742, 149.6).
planet('Mars', 6779, 227.9).
planet('Jupiter', 139820, 778.5).
planet('Saturn', 116460, 1427.0).
planet('Uranus', 50724, 2871.0).
planet('Neptune', 49244, 4497.1).

% Find diameter of a planet
diameter(Name, Diameter) :-
    planet(Name, Diameter, _).

% Find distance from the Sun of a planet
distance(Name, Distance) :-
    planet(Name, _, Distance).

% Find planets within a certain distance range from the Sun
planets_within_distance(Min, Max, Name) :-
    planet(Name, _, Distance),
    Distance >= Min,
    Distance =< Max.

% Find planets larger than a given diameter
planets_larger_than(Diameter, Name) :-
    planet(Name, PlanetDiameter, _),
    PlanetDiameter > Diameter.
