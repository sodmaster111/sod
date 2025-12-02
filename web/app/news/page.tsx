import Link from 'next/link'

interface NewsItem {
  id: number | string
  title: string | null
  summary: string | null
  created_at: string
}

async function fetchNews(): Promise<NewsItem[]> {
  const response = await fetch('http://backend:8000/api/news/list?limit=20', {
    // Cache on the server for a short time to keep content fresh while avoiding excessive requests
    next: { revalidate: 300 },
  })

  if (!response.ok) {
    throw new Error('Failed to load news')
  }

  return response.json()
}

export default async function NewsPage() {
  const news = await fetchNews()

  return (
    <main className="min-h-screen bg-slate-950 px-6 py-14 text-slate-100">
      <div className="mx-auto flex max-w-3xl flex-col gap-8">
        <header>
          <h1 className="text-3xl font-bold sm:text-4xl">Новости</h1>
          <p className="mt-2 text-slate-300">Свежие обновления проекта и материалы SODMASTER.</p>
        </header>

        <section className="flex flex-col gap-4">
          {news.length === 0 ? (
            <p className="text-slate-300">Пока нет новостей.</p>
          ) : (
            news.map((item) => (
              <article
                key={item.id}
                className="rounded-xl border border-slate-800 bg-slate-900/60 p-6 shadow-sm transition hover:border-slate-700"
              >
                <div className="flex items-start justify-between gap-4">
                  <div className="flex-1 space-y-2">
                    <h2 className="text-xl font-semibold text-slate-50">
                      {item.title?.trim() ? item.title : 'Без заголовка'}
                    </h2>
                    {item.summary && <p className="text-slate-200">{item.summary}</p>}
                    <p className="text-sm text-slate-400">
                      {new Date(item.created_at).toLocaleString('ru-RU')}
                    </p>
                  </div>
                  <div>
                    <Link
                      href={`/news/${item.id}`}
                      className="rounded-lg border border-slate-700 px-4 py-2 text-sm font-medium text-slate-100 transition hover:border-slate-500 hover:bg-slate-900"
                    >
                      Читать
                    </Link>
                  </div>
                </div>
              </article>
            ))
          )}
        </section>
      </div>
    </main>
  )
}
