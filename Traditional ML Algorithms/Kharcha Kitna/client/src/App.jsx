import axios from "axios";
import { useState } from "react";

const YourComponent = () => {
  const [inputValue, setInputValue] = useState("");
  const [response, setResponse] = useState("");
  const [a, setA] = useState("");
  const [b, setB] = useState("");
  const [c, setC] = useState("");
  const [d, setD] = useState("");
  const [e, setE] = useState("");

  const sendString = async () => {
    try {
      // Send a POST request with the input value
      const result = await axios.post("http://localhost:8000/", {
        a : a,
        b : b,
        c : c,
        d : d,
        e : e
      });
      setResponse(result.data); // Set response from backend
    } catch (error) {
      console.error("Error sending data:", error);
    }
  };

  return (
    <div>
      <input
        type="text"
        value={a}
        onChange={(e) => setA(e.target.value)}
        placeholder="Enter text here"
      />
      <input
        type="text"
        value={b}
        onChange={(e) => setB(e.target.value)}
        placeholder="Enter text here"
      />
      <input
        type="text"
        value={c}
        onChange={(e) => setC(e.target.value)}
        placeholder="Enter text here"
      />
      <input
        type="text"
        value={d}
        onChange={(e) => setD(e.target.value)}
        placeholder="Enter text here"
      />
      <input
        type="text"
        value={e}
        onChange={(e) => setE(e.target.value)}
        placeholder="Enter text here"
      />
      <button
        onClick={(e) => {
          sendString();
          e.target.value = "";
        }}
      >
        Send String
      </button>
      <div>{response}</div>
    </div>
  );
};

export default YourComponent;
