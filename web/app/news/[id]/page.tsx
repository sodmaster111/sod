import Link from 'next/link'

interface NewsDetail {
  id: string
  url?: string | null
  title?: string | null
  summary?: string | null
  spiritual?: string | null
  clean?: string | null
  telegram_post?: string | null
  created_at?: string | null
}

async function getNews(id: string): Promise<NewsDetail> {
  const baseUrl = process.env.NEXT_PUBLIC_BASE_URL ?? 'http://localhost:3000'
  const response = await fetch(`${baseUrl}/api/news/${encodeURIComponent(id)}`, {
    cache: 'no-store',
  })

  if (!response.ok) {
    throw new Error('Не удалось загрузить новость')
  }

  return response.json()
}

export default async function NewsDetailPage({
  params,
}: {
  params: { id: string }
}) {
  const news = await getNews(params.id)

  return (
    <main className="min-h-screen bg-slate-950 text-slate-100">
      <div className="mx-auto max-w-3xl px-6 py-12">
        <div className="flex flex-col gap-2 sm:flex-row sm:items-start sm:justify-between">
          <h1 className="text-3xl font-bold sm:text-4xl">
            {news.title?.trim() || 'Новость без заголовка'}
          </h1>
          {news.url ? (
            <a
              href={news.url}
              target="_blank"
              rel="noreferrer"
              className="text-sm text-slate-200 underline underline-offset-4 transition hover:text-white"
            >
              Источник
            </a>
          ) : null}
        </div>

        <section className="mt-4 border-t border-slate-800 pt-4">
          <h2 className="text-xl font-semibold">Краткое резюме</h2>
          <p className="mt-2 whitespace-pre-line text-slate-200">
            {news.summary?.trim() || '—'}
          </p>
        </section>

        <section className="mt-4 border-t border-slate-800 pt-4">
          <h2 className="text-xl font-semibold">Духовная трактовка</h2>
          <p className="mt-2 whitespace-pre-line text-slate-200">
            {news.spiritual?.trim() || '—'}
          </p>
        </section>

        <section className="mt-4 border-t border-slate-800 pt-4">
          <h2 className="text-xl font-semibold">Текст для Telegram</h2>
          <textarea
            readOnly
            value={news.telegram_post ?? ''}
            className="mt-2 w-full min-h-[160px] rounded-lg border border-slate-800 bg-slate-900/60 p-3 text-slate-100"
          />
        </section>

        <div className="mt-8 border-t border-slate-800 pt-4">
          <Link
            href="/news"
            className="text-slate-200 underline underline-offset-4 transition hover:text-white"
          >
            Вернуться назад
          </Link>
        </div>
      </div>
    </main>
  )
}
