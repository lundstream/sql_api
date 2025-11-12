import { useState } from "react";

function App() {
  const [server, setServer] = useState("");
  const [database, setDatabase] = useState("");
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [tables, setTables] = useState([]);
  const [data, setData] = useState([]);
  const [selectedTable, setSelectedTable] = useState("");
  //const apiBase = import.meta.env.VITE_API; // dynamisk via build-arg
  const apiBase = "http://backend:8011";  // hårdkodad

  const connect = async () => {
    const res = await fetch(`${apiBase}/connect`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ server, database, username, password }),
    });
    const json = await res.json();
    if (json.status === "connected") {
      setTables(json.tables);
      setData([]);
      setSelectedTable("");
    } else {
      alert("Kunde inte ansluta: " + json.detail);
      setTables([]);
      setData([]);
      setSelectedTable("");
    }
  };

  const loadTable = async (table) => {
    setSelectedTable(table);
    const res = await fetch(`${apiBase}/tables/${table}`);
    const json = await res.json();
    setData(json);
  };

  return (
    <div style={{ padding: 20, fontFamily: "sans-serif" }}>
      <h2>MSSQL REST API Viewer</h2>

      <div style={{ marginBottom: 10 }}>
        <input
          placeholder="Server (t.ex. 192.168.1.50\\SQLEXPRESS)"
          value={server}
          onChange={(e) => setServer(e.target.value)}
          style={{ width: 400 }}
        /><br/>
        <input
          placeholder="Databas"
          value={database}
          onChange={(e) => setDatabase(e.target.value)}
          style={{ width: 400, marginTop: 5 }}
        /><br/>
        <input
          placeholder="Användare"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          style={{ width: 400, marginTop: 5 }}
        /><br/>
        <input
          placeholder="Lösenord"
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          style={{ width: 400, marginTop: 5 }}
        /><br/>
        <button onClick={connect} style={{ marginTop: 10 }}>Anslut</button>
      </div>

      {tables.length > 0 && (
        <div>
          <h3>Tabeller</h3>
          <ul>
            {tables.map((t) => (
              <li key={t} style={{ cursor: "pointer" }} onClick={() => loadTable(t)}>
                {t}
              </li>
            ))}
          </ul>
        </div>
      )}

      {selectedTable && (
        <div>
          <h3>Data från {selectedTable}</h3>
          <table border="1" cellPadding="5" style={{ borderCollapse: "collapse" }}>
            <thead>
              <tr>
                {data[0] && Object.keys(data[0]).map((col) => <th key={col}>{col}</th>)}
              </tr>
            </thead>
            <tbody>
              {data.map((row, i) => (
                <tr key={i}>
                  {Object.values(row).map((val, j) => <td key={j}>{val}</td>)}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}

export default App;
