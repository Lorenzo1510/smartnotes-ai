import React, { useEffect, useState } from "react";
import axios from "axios";

const Home: React.FC = () => {
  const [message, setMessage] = useState("");

  useEffect(() => {
    const fetchNotes = async () => {
      try {
        const token = localStorage.getItem("token");
        const res = await axios.get("http://localhost:8000/notes/me", {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });
        setMessage(res.data.message);
      } catch (err) {
        setMessage("Errore nel recupero delle note.");
      }
    };

    fetchNotes();
  }, []);

  return (
    <div>
      <h2>Home</h2>
      <p>{message}</p>
    </div>
  );
};

export default Home;
