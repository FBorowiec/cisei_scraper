CREATE TABLE IF NOT EXISTS person_info (
    id serial PRIMARY KEY,
    idx int,
    surname text NOT NULL,
    full_name text NOT NULL,
    age int,
    trip_date date,
    registration_place text,
    url text,
    details jsonb
);
