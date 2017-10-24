use hwDB;
show dbs;
show tables;
db.myCol.insert({"Man":[{"id":"2012", "이름":"정우희"},{"id":"2013", "이름":"grey"}]});
db.myCol.find({ "Man.이름": "정우희" });