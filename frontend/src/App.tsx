import { useState } from "react"
import ClienteApi from "./components/ClienteApi"
import ClientePython from "./components/ClientePython"

//define os tipos possivel para aba ativa
type TabType = "python" | "api"

const App = () => {

  //Hook - useState
  const [activeTab, setActiveTab] = useState<TabType>("python");

  return (
    <div>
      <div>
        <h1>Painel Simple de APIs</h1>
        <div>
          <button onClick={() => setActiveTab("python")}>
            {activeTab === "python" ? "✓ " : ""}Clientes Python
          </button>

          <button onClick={() => setActiveTab("api")}>
            {activeTab === "api" ? "✓ " : ""}Clientes API
          </button>
        </div>

        {activeTab === "python" && <ClientePython />}
        {activeTab === "api" && <ClienteApi />}

      </div>
    </div>
  )
}

export default App
