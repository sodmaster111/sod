export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="ru">
      <body className="bg-slate-950 text-slate-50">{children}</body>
    </html>
  );
}
