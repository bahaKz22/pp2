-- Procedure 1: Add a phone number to an existing contact
CREATE OR REPLACE PROCEDURE add_phone(p_contact_name VARCHAR, p_phone VARCHAR, p_type VARCHAR)
LANGUAGE plpgsql AS $$
DECLARE
    v_contact_id INTEGER;
BEGIN
    SELECT id INTO v_contact_id FROM contacts WHERE name = p_contact_name LIMIT 1;
    
    IF v_contact_id IS NOT NULL THEN
        INSERT INTO phones (contact_id, phone, type) VALUES (v_contact_id, p_phone, p_type);
        RAISE NOTICE 'Phone % added to contact %.', p_phone, p_contact_name;
    ELSE
        RAISE EXCEPTION 'Contact % not found.', p_contact_name;
    END IF;
END;
$$;

-- Procedure 2: Move a contact to a group (creates group if it doesn't exist)
CREATE OR REPLACE PROCEDURE move_to_group(p_contact_name VARCHAR, p_group_name VARCHAR)
LANGUAGE plpgsql AS $$
DECLARE
    v_group_id INTEGER;
    v_contact_id INTEGER;
BEGIN
    SELECT id INTO v_contact_id FROM contacts WHERE name = p_contact_name LIMIT 1;
    
    IF v_contact_id IS NULL THEN
        RAISE EXCEPTION 'Contact % not found.', p_contact_name;
    END IF;

    -- Check if group exists, insert if it doesn't
    SELECT id INTO v_group_id FROM groups WHERE name = p_group_name;
    IF v_group_id IS NULL THEN
        INSERT INTO groups (name) VALUES (p_group_name) RETURNING id INTO v_group_id;
    END IF;

    UPDATE contacts SET group_id = v_group_id WHERE id = v_contact_id;
    RAISE NOTICE 'Contact % moved to group %.', p_contact_name, p_group_name;
END;
$$;

-- Function 3: Advanced search across all fields and multiple phones
CREATE OR REPLACE FUNCTION search_contacts(p_query TEXT)
RETURNS TABLE (
    contact_name VARCHAR, 
    contact_email VARCHAR, 
    group_name VARCHAR, 
    phone_number VARCHAR, 
    phone_type VARCHAR
)
LANGUAGE plpgsql AS $$
BEGIN
    RETURN QUERY
    SELECT c.name::VARCHAR, c.email::VARCHAR, g.name::VARCHAR, p.phone::VARCHAR, p.type::VARCHAR
    FROM contacts c
    LEFT JOIN groups g ON c.group_id = g.id
    LEFT JOIN phones p ON c.id = p.contact_id
    WHERE c.name ILIKE '%' || p_query || '%'
       OR c.email ILIKE '%' || p_query || '%'
       OR p.phone ILIKE '%' || p_query || '%';
END;
$$;