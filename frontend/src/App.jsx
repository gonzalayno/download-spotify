import { useState } from "react";

export default function App() {
  const [url, setUrl] = useState("");
  const [message, setMessage] = useState("");

  const handleDownload = async () => {
    const response = await fetch("http://127.0.0.1:8000/download/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ url }),
    });

    const data = await response.json();
    setMessage(data.message);
  };

  return (
    <div className="flex flex-col items-center justify-center h-screen bg-gray-900 text-white">
      <h1 className="text-2xl font-bold">Descargar Música con SpotDL</h1>
      <input
        className="p-2 mt-4 w-96 text-black rounded"
        type="text"
        placeholder="Pega el enlace de YouTube"
        value={url}
        onChange={(e) => setUrl(e.target.value)}
      />
      <button
        className="mt-4 p-2 bg-blue-500 rounded"
        onClick={handleDownload}
      >
        Descargar
      </button>
      {message && <p className="mt-4">{message}</p>}
    </div>
  );
}
