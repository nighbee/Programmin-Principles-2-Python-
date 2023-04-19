CREATE TABLE contacts(
contact_id SERIAL PRIMARY KEY,
fname VARCHAR(50) NOT NULL,
lname VARCHAR(50) NOT NULL ,
);
CREATE TABLE contact_details(
 detail_id SERIAL PRIMARY KEY,
contact_id INTEGER NOT NULL REFERENCES contacts(contact_id),
phone_number VARCHAR(20),
);
