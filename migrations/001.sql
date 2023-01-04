CREATE EXTENSION IF NOT EXISTS POSTGIS;


CREATE TABLE br_uf(
    id SERIAL PRIMARY KEY,
    cd_uf VARCHAR(15),
    nm_uf VARCHAR(256),
    sigla VARCHAR(4),
    nm_regiao VARCHAR(256),
    "geometry" GEOMETRY
);