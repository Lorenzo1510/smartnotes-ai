import React, { useState } from "react";
import LoginForm from "./components/LoginForm";

function App() {
  const [token, setToken] = useState<string | null>(null);

  if (!token) {
    return <LoginForm onLogin={setToken} />;
  }

  return <div>✅ Sei loggato! Token: {token}</div>;
}

export default App;
