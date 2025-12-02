import './globals.css'
import type { ReactNode } from 'react'

export const metadata = {
  title: 'SODMASTER — הבית הדיגיטלי לאמונה ולתורה',
  description: 'פרויקט בינה מלאכותית עצמאי שמפיץ דברי תורה, אמונה והשראה בערוצים דיגיטליים.',
}

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="he" dir="rtl">
      <body className="min-h-screen bg-slate-950 text-slate-100 antialiased">
        <main className="min-h-screen">
          {children}
        </main>
      </body>
    </html>
  )
}
