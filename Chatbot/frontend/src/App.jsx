import { useState } from "react";
import "./App.css";

function App() {
  const [message, setMessage] = useState("");
  const [chats, setChats] = useState([]);
  const [isTyping, setIsTyping] = useState(false);
  
  // New states for the dropdown inputs
  const [yearEntered, setYearEntered] = useState("");
  const [graduationYear, setGraduationYear] = useState("");
  const [major, setMajor] = useState("");
  const [minor, setMinor] = useState("");

  const chat = async (e, message) => {
    e.preventDefault();

    if (!message) return;
    setIsTyping(true);
    scrollTo(0, 1e10);

    let msgs = chats;
    msgs.push({ role: "user", content: message });
    setChats(msgs);

    setMessage("");

    fetch("http://localhost:5000/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        message,
      }),
    })
      .then((response) => response.json())
      .then((data) => {
        msgs.push({ role: "assistant", content: data.output });
        setChats(msgs);
        setIsTyping(false);
        scrollTo(0, 1e10);
      })
      .catch((error) => {
        console.log(error);
      });
  };

  return (
    <main>
      <h1>Advise.ai</h1>
      
      {/* Dropdown input section */}
      <section className="input-section">
        <div className="input-group">
          <label>Year Entered: </label>
          <select value={yearEntered} onChange={(e) => setYearEntered(e.target.value)}>
            <option value="">Year Enrolled</option>
            <option value="2020 Fall">2020 Fall</option>
            <option value="2020 Spring">2020 Spring</option>
            <option value="2021 Fall">2021 Fall</option>
            <option value="2021 Spring">2021 Spring</option>
            <option value="2022 Fall">2022 Fall</option>
            <option value="2022 Spring">2022 Spring</option>
            <option value="2023 Fall">2023 Fall</option>
            <option value="2023 Spring">2023 Spring</option>
          </select>
        </div>
        <div className="input-group">
          <label>Expected Graduation Year: </label>
          <select value={graduationYear} onChange={(e) => setGraduationYear(e.target.value)}>
            <option value="">Expected Graduation</option>
            <option value="2024 Fall">2024 Fall</option>
            <option value="2024 Spring">2024 Spring</option>
            <option value="2025 Fall">2025 Fall</option>
            <option value="2025 Spring">2025 Spring</option>
            <option value="2026 Fall">2026 Fall</option>
            <option value="2026 Spring">2026 Spring</option>
            <option value="2027 Fall">2027 Fall</option>
            <option value="2027 Spring">2027 Spring</option>
          </select>
        </div>
        <div className="input-group">
          <label>Major(s): </label>
          <select value={major} onChange={(e) => setMajor(e.target.value)}>
            <option value="">Select Major</option>
            <option value="CMDA">CMDA</option>
            <option value="Computer Science">Computer Science</option>
            <option value="Mathematics">Mathematics</option>
            <option value="Finance">Finance</option>
            {/* Add more options here */}
          </select>
        </div>
        <div className="input-group">
          <label>Minor(s): </label>
          <select value={minor} onChange={(e) => setMinor(e.target.value)}>
            <option value="">Select Minor</option>
            <option value="Mathematics">Mathematics</option>
            <option value="Statistics">Statistics</option>
            <option value="Finance">Finance</option>
            {/* Add more options here */}
          </select>
        </div>
      </section>

      <section>
        {chats && chats.length
          ? chats.map((chat, index) => (
              <p key={index} className={chat.role === "user" ? "user" : "assistant"}>
                <span>
                  <b>{chat.role}</b>
                </span>
                <span>:</span>
                <span>{chat.content}</span>
              </p>
            ))
          : ""}
      </section>

      <div className={isTyping ? "" : "hide"}>
        <p>
          <i>{isTyping ? "Typing" : ""}</i>
        </p>
      </div>

      <form action="" onSubmit={(e) => chat(e, message)}>
        <input
          type="text"
          name="message"
          value={message}
          placeholder="Hello, how may I Advise you?..."
          onChange={(e) => setMessage(e.target.value)}
        />
      </form>
    </main>
  );
}

export default App;
