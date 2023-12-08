CREATE TABLE credit(
    id INTEGER primary key NOT NULL,
    title_id INTEGER NOT NULL,
    NAME VARCHAR(255),
    charactor VARCHAR(255),
    role VARCHAR(255),
    foreign key (title_id) references title(id)
);
