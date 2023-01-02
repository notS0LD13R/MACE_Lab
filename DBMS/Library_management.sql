-- create database library;
use library; 



CREATE TABLE IF NOT EXISTS author (
    author_id INT,
    name VARCHAR(25),
    email VARCHAR(25),
    phone_number INT,
    stat VARCHAR(25),
    primary key (author_id)
);
CREATE TABLE IF NOT EXISTS book_author (
    book_id INT,
    author_id INT,
    foreign key (author_id) references author(author_id)
);
CREATE TABLE IF NOT EXISTS publisher (
    publisher_id INT,
    name VARCHAR(25),
    address VARCHAR(25),
    primary key (publisher_id)
);
CREATE TABLE IF NOT EXISTS member (
    member_id INT,
    name VARCHAR(25),
    branch_code VARCHAR(25),
    roll_number INT,
    phone_number INT,
    email_id VARCHAR(25),
    date_of_join DATE,
    stat VARCHAR(25),
    primary key (member_id)
);


CREATE TABLE IF NOT EXISTS language (
    language_id INT,
    name CHAR(25),
    primary key (language_id)
);
CREATE TABLE IF NOT EXISTS late_fee_rule (
    fromdays DATE,
    todays DATE,
    amount INT
);
CREATE TABLE IF NOT EXISTS book (
    book_id INT,
    title VARCHAR(25),
    language_id INT,
    mrp FLOAT,
    publisher_id INT,
    published_date DATE,
    volume INT,
    stat VARCHAR(25),
    primary key (book_id),
    foreign key (language_id) references language(language_id),
    foreign key (publisher_id) references publisher(publisher_id)
    
);
CREATE TABLE IF NOT EXISTS book_issue (
    issue_id INT,
    date_of_issue DATE,
    book_id INT,
    member_id INT,
    expected_date_of_return DATE,
    stat VARCHAR(25),
    primary key (issue_id),
    foreign key (book_id) references book(book_id),
    foreign key (member_id) references member(member_id)
);

CREATE TABLE IF NOT EXISTS book_return (
    issue_id INT,
    actual_date_of_return DATE,
    latedays INT,
    latefee FLOAT,
    foreign key (issue_id) references book_issue(issue_id)
);