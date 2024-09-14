import { useState, useEffect, useRef } from "react";
import "./App.css";

function App() {
  const [message, setMessage] = useState("");
  const [chats, setChats] = useState([]);
  const [isTyping, setIsTyping] = useState(false);
  
  const [yearEntered, setYearEntered] = useState("");
  const [graduationYear, setGraduationYear] = useState("");
  const [majorInput, setMajorInput] = useState("");
  const [majors, setMajors] = useState([]);
  const [minorInput, setMinorInput] = useState("");
  const [minors, setMinors] = useState([]);

  const chatEndRef = useRef(null);

  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [chats]);

  const handleAddMajor = () => {
    if (majorInput.trim() !== "") {
      setMajors([...majors, majorInput]);
      setMajorInput("");
    }
  };

  const handleAddMinor = () => {
    if (minorInput.trim() !== "") {
      setMinors([...minors, minorInput]);
      setMinorInput("");
    }
  };

  const chat = async (e, message) => {
    e.preventDefault();

    if (!message) return;
    setIsTyping(true);

    let msgs = chats;
    msgs.push({ role: "user", content: message });
    setChats([...msgs]);

    setMessage("");

    // Simulate async chat response
    setTimeout(() => {
      msgs.push({ role: "assistant", content: "This is a response from the advisor." });
      setChats([...msgs]);
      setIsTyping(false);
    }, 1000);
  };

  return (
    <main className="container-fluid d-flex flex-column vh-100">
      <h1 className="text-center py-4">Advisor</h1>
      
      <section className="input-section row mb-4">
        <div className="input-group col-md-6 mb-3">
          <label>Year Entered: </label>
          <select
            className="form-control"
            value={yearEntered}
            onChange={(e) => setYearEntered(e.target.value)}
          >
            <option value="">Year Enrolled</option>
            {/* Add more year options here */}
          </select>
        </div>

        <div className="input-group col-md-6 mb-3">
          <label>Expected Graduation Year: </label>
          <select
            className="form-control"
            value={graduationYear}
            onChange={(e) => setGraduationYear(e.target.value)}
          >
            <option value="">Expected Graduation</option>
            {/* Add more year options here */}
          </select>
        </div>

        <div className="input-group col-md-6 mb-3">
          <label>Major(s): </label>
          <div className="input-group">
            <input
              type="text"
              className="form-control"
              value={majorInput}
              onChange={(e) => setMajorInput(e.target.value)}
              placeholder="Enter your major(s)"
            />
            <button type="button" className="btn btn-primary" onClick={handleAddMajor}>
              Add Major
            </button>
          </div>
          <ul className="list-group mt-3">
            {majors.map((major, index) => (
              <li key={index} className="list-group-item">{major}</li>
            ))}
          </ul>
        </div>

        <div className="input-group col-md-6 mb-3">
          <label>Minor(s): </label>
          <div className="input-group">
            <input
              type="text"
              className="form-control"
              value={minorInput}
              onChange={(e) => setMinorInput(e.target.value)}
              placeholder="Enter your minor(s)"
            />
            <button type="button" className="btn btn-primary" onClick={handleAddMinor}>
              Add Minor
            </button>
          </div>
          <ul className="list-group mt-3">
            {minors.map((minor, index) => (
              <li key={index} className="list-group-item">{minor}</li>
            ))}
          </ul>
        </div>
      </section>

      <section className="chat-section flex-grow-1 overflow-auto mb-3">
        {chats && chats.length
          ? chats.map((chat, index) => (
              <div key={index} className={`chat-bubble ${chat.role === "user" ? "user-bubble" : "assistant-bubble"} mb-2`}>
                <strong>{chat.role === "user" ? "You" : "Advisor"}:</strong> {chat.content}
              </div>
            ))
          : ""}
        <div ref={chatEndRef} />
      </section>

      <form action="" onSubmit={(e) => chat(e, message)} className="chat-input">
        <div className="input-group">
          <input
            type="text"
            name="message"
            value={message}
            placeholder="How can I Advise you?..."
            onChange={(e) => setMessage(e.target.value)}
            className="form-control"
          />
          <button type="submit" className="btn btn-secondary">Send</button>
        </div>
      </form>
    </main>
  );
}

export default App;


 


