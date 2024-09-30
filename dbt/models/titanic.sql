SELECT
    passenger_id AS id,
    CASE WHEN survived = 0 THEN false ELSE true END AS survived,
    pclass AS class,
    name,
    sex,
    age,
    sib_sp AS siblings_spouses,
    parch AS parents_children,
    ticket,
    fare,
    CASE
        WHEN embarked = 'C' THEN 'Cherbourg'
        WHEN embarked = 'Q' THEN 'Queenstown'
        WHEN embarked = 'S' THEN 'Southampton'
    END AS embarked,
    cabin
FROM {{ source("raw", "titanic") }}
