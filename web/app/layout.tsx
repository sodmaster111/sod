import './globals.css'
import type { ReactNode } from 'react'

export const metadata = {
  title: 'SODMASTER — цифровой дом для веры и смысла',
  description: 'Автономный AI-проект для духовного контента: эмуна, Тора, поддержка и смысл на русском языке.',
}

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="he" dir="rtl">
      <body className="min-h-screen bg-slate-950 text-slate-50 antialiased">
        <main className="min-h-screen">
          {children}
        </main>
      </body>
    </html>
  )
}
