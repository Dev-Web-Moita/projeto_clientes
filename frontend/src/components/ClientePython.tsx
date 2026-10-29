import { useEffect, useState } from "react"

interface Cliente {
  id: number
  nome: string
  email: string
  telefone?: string
  empresa?: string
  active: boolean
}

const ClientePython = () => {
  const [clientes, setClientes] = useState<Cliente[]>([])
  const [loading, setLoading] = useState(true)
  const [erro, setErro] = useState<string | null>(null)

  useEffect(() => {
    const carregarClientes = async () => {
      try {
        const resposta = await fetch("http://localhost:8000/api/clientes")

        if (!resposta.ok) {
          throw new Error("Erro ao buscar clientes")
        }

        const dados: Cliente[] = await resposta.json()
        setClientes(dados)
      } catch (error) {
        console.error(error)
        setErro("Não foi possível carregar os clientes.")
      } finally {
        setLoading(false)
      }
    }

    carregarClientes()
  }, [])

  return (
    <div>
      <h2>Clientes cadastrados</h2>

      {loading && <p>Carregando clientes...</p>}
      {erro && <p>{erro}</p>}

      {!loading && !erro && clientes.length === 0 && (
        <p>Nenhum cliente cadastrado.</p>
      )}

      {!loading && !erro && clientes.length > 0 && (
        <ul>
          {clientes.map((cliente) => (
            <li key={cliente.id}>
              <strong>{cliente.nome}</strong> - {cliente.email}
              {cliente.telefone ? ` | Tel: ${cliente.telefone}` : ""}
              {cliente.empresa ? ` | Empresa: ${cliente.empresa}` : ""}
            </li>
          ))}
        </ul>
      )}
    </div>
  )
}

export default ClientePython
