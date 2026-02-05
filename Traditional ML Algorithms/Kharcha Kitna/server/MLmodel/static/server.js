const express = require("express");
const axios = require("axios");
const cors = require("cors");

const app = express();
const port = 8000;

app.use(cors()); // Enable CORS
app.use(express.json()); // Middleware to parse JSON request bodies

// Define your POST route
app.post("/", async (req, res) => {
  const { a,b,c,d,e } = req.body; // Extract the string from the request body
  try {
    // Forward the string to the Flask server
    const response = await axios.post("http://localhost:5001/flask-endpoint", {
      a,
      b,
      c,
      d,
      e
    });
    res.json(response.data); // Send the response from Flask back to the React frontend
  } catch (error) {
    console.error("Error forwarding data to Flask:", error);
    res.status(500).send("Error");
  }
});

app.listen(port, () => {
  console.log(`Express server listening at http://localhost:${port}`);
});
