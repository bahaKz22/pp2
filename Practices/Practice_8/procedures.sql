\CREATE OR REPLACE PROCEDURE upsert_contact(p_name VARCHAR, p_phone VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM baha WHERE name = p_name) THEN
        UPDATE baha SET phone = p_phone WHERE name = p_name;
    ELSE
        INSERT INTO baha(name, phone) VALUES(p_name, p_phone);
    END IF;
END;
$$;

CREATE OR REPLACE PROCEDURE delete_contact(p TEXT)
LANGUAGE plpgsql AS $$
BEGIN
    DELETE FROM baha
    WHERE name = p OR phone = p;
END;
$$;

CREATE OR REPLACE PROCEDURE insert_many()
LANGUAGE plpgsql AS $$
DECLARE
    names TEXT[] := ARRAY['a', 'b', 'c'];
    phones TEXT[] := ARRAY['111', '222', 'bad'];
    i INT;
BEGIN
    FOR i IN 1..array_length(names, 1) LOOP
        IF phones[i] ~ '^[0-9]+$' THEN
            INSERT INTO baha(name, phone) VALUES(names[i], phones[i]);
        ELSE
            RAISE NOTICE 'Wrong phone: %', phones[i];
        END IF;
    END LOOP;
END;
$$;