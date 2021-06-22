/**Create 'stores' table and add 100 rows of random data****/
DROP TABLE IF EXISTS stores;

CREATE TABLE stores(
    id VARCHAR,
    PRIMARY KEY(id),
    data JSON
);


INSERT INTO stores(id, data)
SELECT md5(RANDOM()::TEXT), 
jsonb_build_object(
    'name', md5(random()::text), 
    'brand', md5(random()::text),
    'minAmount', floor(random() * 10 )::int,
    'maxAmount', floor(random() * (80-100+1) + 100)::int,
    'discount', floor(random() * 5)::int,
    'tags',json_build_array('tag1','tag2','tag3'),
    'credentials',null
    )
FROM GENERATE_SERIES(1,100);