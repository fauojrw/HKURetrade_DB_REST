CREATE TABLE User (
    UID INTEGER PRIMARY KEY,
    email TEXT,
    name TEXT,
    rating INTEGER
);

CREATE TABLE Buyer (
    UID INTEGER PRIMARY KEY,
    FOREIGN KEY (UID) REFERENCES User(UID)
);

CREATE TABLE Seller (
    UID INTEGER PRIMARY KEY,
    FOREIGN KEY (UID) REFERENCES User(UID)
);

CREATE TABLE Commodity (
    CID INTEGER PRIMARY KEY,
    Seller_UID INTEGER,
    price REAL,
    text_info TEXT,
    FOREIGN KEY (Seller_UID) REFERENCES Seller(UID)
);

CREATE TABLE Pictures (
    CID INTEGER,
    pictures BLOB,
    PRIMARY KEY (CID),
    FOREIGN KEY (CID) REFERENCES Commodity(CID)
);

CREATE TABLE Buyer_buy_Commodity (
    Buyer_UID INTEGER,
    Seller_UID INTEGER,
    Commodity_CID INTEGER,
    rate INTEGER,
    pay_time DATETIME,
    has_paid INTEGER,
    collect_time DATETIME,
    has_collected INTEGER,
    PRIMARY KEY (Buyer_UID, Seller_UID, Commodity_CID),
    FOREIGN KEY (Buyer_UID) REFERENCES Buyer(UID),
    FOREIGN KEY (Seller_UID) REFERENCES Seller(UID),
    FOREIGN KEY (Commodity_CID) REFERENCES Commodity(CID)
);