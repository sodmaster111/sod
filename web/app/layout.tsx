import './globals.css'
import type { ReactNode } from 'react'

export const metadata = {
  title: 'SODMASTER',
  description: 'Local-first AI agency monorepo',
}

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en">
      <body className="min-h-screen bg-slate-950 text-slate-50">
        <header className="border-b border-slate-800 px-6 py-4">
          <h1 className="text-xl font-semibold">SODMASTER</h1>
          <p className="text-sm text-slate-300">Autonomous AI agency running on local LLMs</p>
        </header>
        <main className="max-w-4xl mx-auto px-6 py-8 space-y-6">
          {children}
        </main>
      </body>
    </html>
  )
}
