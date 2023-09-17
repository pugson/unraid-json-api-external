import express from "express";
import fetch from "node-fetch";

const app = express();

app.get("/ping", (req, res) => {
  res.json({ ok: true });
});

app.get("/", async (req, res) => {
  try {
    const query = req.query.query;
    const unraid_api_url = `http://localhost/plugins/jsonapi/api.php?file=${query}`;

    const response = await fetch(unraid_api_url);
    const data = await response.json();

    res.json({
      ok: true,
      data,
    });
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: "Internal Server Error" });
  }
});

const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
