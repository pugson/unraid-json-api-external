const express = require("express");
const fetch = require("node-fetch");

const app = express();

app.get("/ping", (req, res) => {
  res.json({ ok: true });
});

app.get("/", (req, res) => {
  const query = req.query.query;
  const unraid_api_url = `http://localhost/plugins/jsonapi/api.php?file=${query}`;

  fetch(unraid_api_url)
    .then((response) => response.json())
    .then((data) =>
      res.json({
        ok: true,
        data,
      })
    )
    .catch((error) => {
      console.error(error);
      res.status(500).json({ error: "Internal Server Error" });
    });
});

const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
