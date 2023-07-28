const express = require("express");
const bodyParser = require("body-parser");
const mysql = require("mysql");

const app = express();
const port = 3000;

let cors = require("cors");
app.use(cors());

const db = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "33533",
  database: "helpdesk",
});

db.connect((err) => {
  if (err) throw err;
  console.log("Connected to the database.");
});

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

// Login API endpoint
app.post("/login", (req, res) => {
  const { username, password } = req.body;

  // Validate user credentials against the user database table.
  const query = `SELECT * FROM users WHERE username = ? AND pass = ?`;
  db.query(query, [username, password], (err, result) => {
    if (err) {
      console.log(err);
      res.status(500).json({ success: false });
    } else {
      if (result.length === 1) {
        const userType = result[0].user_type;
        res.json({ success: true, userType });
      } else {
        res.json({ success: false });
      }
    }
  });
});

// Define the API endpoint for updating the helpdesk request status
app.post("/updateHelpdeskRequest", (req, res) => {
  const { requestId, status } = req.body;

  const sql = "UPDATE helpdesk_requests SET status = ? WHERE id = ?";
  db.query(sql, [status, requestId], (err, result) => {
    if (err) {
      console.error("Error updating the database:", err);
      res.status(500).json({ error: "Failed to update the request status" });
    } else {
      res.json({ message: "Request status updated successfully" });
    }
  });
});

// API endpoint to submit helpdesk requests
app.post("/submitHelpdeskRequest", (req, res) => {
  const { name, email, operating, subject, message } = req.body;

  const query =
    "INSERT INTO helpdesk_requests (name, email,operating, subject, message) VALUES (?, ?,?, ?, ?)";
  db.query(query, [name, email, operating, subject, message], (err, result) => {
    if (err) {
      console.log(err);
      res.status(500).json({ success: false });
    } else {
      res.json({ success: true, data: result });
    }
  });
});

// Define the API endpoint to fetch helpdesk requests
app.get("/getHelpdeskRequests", (req, res) => {
  const query = "SELECT * FROM helpdesk_requests";

  db.query(query, (err, result) => {
    if (err) {
      console.log(err);
      res.status(500).json({ success: false });
    } else {
      // Helpdesk requests fetched successfully from the database
      res.json({ success: true, helpdeskRequests: result });
    }
  });
});
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
