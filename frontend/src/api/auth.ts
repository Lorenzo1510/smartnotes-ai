export async function login(username: string, password: string): Promise<string> {
  const response = await fetch("http://localhost:8000/login", {
    method: "POST",
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
    },
    body: new URLSearchParams({
      username,
      password,
    }),
  });

  if (!response.ok) {
    const err = await response.text();
    console.error("Errore login:", err); // DEBUG
    throw new Error("Login fallito");
  }

  const data = await response.json();
  return data.access_token;
}
