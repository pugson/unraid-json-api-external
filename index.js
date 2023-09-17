import express from "express";
import fetch from "node-fetch";

const app = express();

const port = process.env.PORT || 3203;
const server = process.env.SERVER || "192.168.1.111";

app.get("/ping", (req, res) => {
  res.json({ ok: true });
});

app.get("/*", async (req, res) => {
  try {
    const query = req.query.query;
    const unraid_api_url = `http://${server}/plugins/jsonapi/api.php?file=${query}`;

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

app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
