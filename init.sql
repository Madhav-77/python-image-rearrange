CREATE TABLE IF NOT EXISTS image_data (
    id SERIAL PRIMARY KEY,
    type TEXT NOT NULL,
    title TEXT NOT NULL,
    position INTEGER NOT NULL
);

INSERT INTO image_data (type, title, position) VALUES
('bank-draft', 'Bank Draft', 0),
('bill-of-lading', 'Bill of Lading', 1),
('invoice', 'Invoice', 2),
('bank-draft-2', 'Bank Draft 2', 3),
('bill-of-lading-2', 'Bill of Lading 2', 4)
ON CONFLICT DO NOTHING;
