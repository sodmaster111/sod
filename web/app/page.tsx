export default function HomePage() {
  return (
    <div className="space-y-4">
      <h2 className="text-lg font-semibold">Welcome</h2>
      <p>
        This is the SODMASTER monorepo template. The backend uses FastAPI to talk to local-only
        LLM runtimes like Ollama, and the web app is a Next.js interface ready for expansion.
      </p>
      <div className="rounded border border-slate-800 bg-slate-900/60 p-4">
        <h3 className="font-semibold">Next steps</h3>
        <ul className="list-disc pl-5 space-y-1 text-sm text-slate-200">
          <li>Point the backend at your Ollama models via <code>SOD_DEFAULT_MODEL</code>.</li>
          <li>Wire the frontend to call <code>/agents/chat</code> for local inference.</li>
          <li>Extend <code>infra/docker-compose.yml</code> to orchestrate services on your server.</li>
        </ul>
      </div>
    </div>
  )
}
