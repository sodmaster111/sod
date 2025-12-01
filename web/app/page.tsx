export default function Page() {
  return (
    <main className="min-h-screen bg-slate-950 text-slate-100">
      <section className="mx-auto flex max-w-6xl flex-col gap-10 px-6 py-16 lg:flex-row lg:items-center">
        <div className="flex-1 space-y-6">
          <h1 className="text-4xl font-bold leading-tight sm:text-5xl">
            SODMASTER — цифровой дом для веры и смысла
          </h1>
          <p className="text-lg text-slate-200 sm:text-xl">
            SODMASTER — автономный AI-проект, который использует локальные модели искусственного интеллекта, чтобы
            создавать и распространять вдохновляющие послания об эмуна, Торе и внутренней силе на русском языке.
            Проект помогает людям чувствовать поддержку, смысл и связь с Творцом в цифровом мире.
          </p>
          <div className="flex flex-wrap gap-4">
            <a
              href="https://t.me/sodmaster_online"
              className="rounded-lg bg-slate-100 px-5 py-3 text-slate-900 transition hover:bg-white hover:shadow-lg"
            >
              Открыть Telegram-канал
            </a>
            <a
              href="#about"
              className="rounded-lg border border-slate-700 px-5 py-3 text-slate-100 transition hover:border-slate-500 hover:bg-slate-900"
            >
              О проекте
            </a>
          </div>
        </div>
        <div className="flex-1 rounded-xl border border-slate-800 bg-slate-900/60 p-6 shadow-lg">
          <p className="text-center text-lg font-semibold text-slate-100">
            Локальный AI · Без внешних облаков · Сфокусировано на духовном контенте
          </p>
        </div>
      </section>

      <section id="about" className="bg-slate-900/40">
        <div className="mx-auto max-w-5xl space-y-6 px-6 py-14">
          <h2 className="text-3xl font-bold sm:text-4xl">Что такое SODMASTER?</h2>
          <div className="space-y-4 text-lg text-slate-200">
            <p>
              SODMASTER — духовно-технологический проект, который соединяет силу локального искусственного интеллекта и
              ценности еврейской традиции, чтобы делиться светом и поддержкой.
            </p>
            <p>
              Проект не заменяет живого раввина и настоящую общину, а дополняет их, помогая находить ответы и вдохновение
              там, где это удобно и доступно.
            </p>
            <p>
              Цель SODMASTER — дарить поддержку, свет и смысл тем, кто ищет связь с Творцом в современном цифровом мире.
            </p>
          </div>
        </div>
      </section>

      <section className="mx-auto max-w-6xl px-6 py-14">
        <h2 className="text-3xl font-bold sm:text-4xl">Как это работает</h2>
        <div className="mt-8 grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
          <div className="rounded-xl border border-slate-800 bg-slate-900/60 p-6 shadow">
            <h3 className="text-xl font-semibold">AI-агенты</h3>
            <p className="mt-3 text-slate-200">
              Несколько ролей — раввин, редактор, планировщик — создают и отбирают вдохновляющий контент.
            </p>
          </div>
          <div className="rounded-xl border border-slate-800 bg-slate-900/60 p-6 shadow">
            <h3 className="text-xl font-semibold">Локальные модели</h3>
            <p className="mt-3 text-slate-200">
              Все процессы работают на собственном сервере без обращения к открытым облакам для сохранения приватности и
              независимости.
            </p>
          </div>
          <div className="rounded-xl border border-slate-800 bg-slate-900/60 p-6 shadow">
            <h3 className="text-xl font-semibold">Каналы распространения</h3>
            <p className="mt-3 text-slate-200">
              Материалы публикуются на сайте и в Telegram, а в будущем — в WhatsApp и других каналах.
            </p>
          </div>
        </div>
      </section>

      <section className="bg-slate-900/40">
        <div className="mx-auto max-w-5xl px-6 py-14">
          <h2 className="text-3xl font-bold sm:text-4xl">Для кого этот проект</h2>
          <ul className="mt-6 space-y-3 list-disc pl-5 text-lg text-slate-200">
            <li>Для тех, кому сейчас тяжело и нужен хизук и поддержка.</li>
            <li>Для тех, кто ищет смысл и ответы на вопросы веры.</li>
            <li>Для тех, кто любит технологии, но не хочет терять связь с духовностью.</li>
          </ul>
        </div>
      </section>

      <section className="mx-auto max-w-5xl px-6 py-14">
        <h2 className="text-3xl font-bold sm:text-4xl">Присоединиться к SODMASTER</h2>
        <p className="mt-4 text-lg text-slate-200">
          Сейчас основной канал SODMASTER — это Telegram. Подключайтесь, чтобы получать свежие материалы и поддержку.
        </p>
        <div className="mt-6">
          <a
            href="https://t.me/sodmaster_online"
            className="inline-flex rounded-lg bg-slate-100 px-5 py-3 text-slate-900 transition hover:bg-white hover:shadow-lg"
          >
            Открыть канал в Telegram
          </a>
        </div>
      </section>
    </main>
  )
}
