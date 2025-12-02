export default function Home() {
  return (
    <main className="min-h-screen bg-slate-950 text-slate-50">
      <section className="px-6 py-16 max-w-5xl mx-auto text-center space-y-6">
        <p className="text-sm uppercase tracking-[0.3em] text-slate-400">SODMASTER</p>
        <h1 className="text-4xl sm:text-5xl font-bold leading-tight">
          SODMASTER — цифровой дом веры и Торы
        </h1>
        <p className="text-lg sm:text-xl text-slate-300 max-w-3xl mx-auto">
          Проект на базе искусственного интеллекта, который помогает распространять слова Торы, веры и вдохновения через сайт, Телеграм и другие каналы.
        </p>
        <div className="flex flex-col sm:flex-row gap-4 justify-center">
          <a
            href="#"
            className="inline-flex items-center justify-center rounded-full bg-emerald-500 px-6 py-3 text-base font-semibold text-slate-950 hover:bg-emerald-400 transition"
          >
            Присоединиться к группе «Лохамей а-Шем»
          </a>
          <a
            href="#"
            className="inline-flex items-center justify-center rounded-full border border-slate-500 px-6 py-3 text-base font-semibold hover:border-emerald-400 hover:text-emerald-300 transition"
          >
            Подписаться на канал SODMASTER
          </a>
        </div>
      </section>

      <section className="px-6 py-14 bg-slate-900/40">
        <div className="max-w-5xl mx-auto space-y-6">
          <h2 className="text-3xl font-semibold text-center">Кому подходит</h2>
          <div className="grid md:grid-cols-3 gap-6">
            <div className="p-6 rounded-2xl bg-slate-900 border border-slate-800">
              <h3 className="text-xl font-semibold mb-2">Ученикам и ищущим</h3>
              <p className="text-slate-300">
                Получайте доступ к наставлениям, разбору недельных глав и кратким ответам на вопросы веры.
              </p>
            </div>
            <div className="p-6 rounded-2xl bg-slate-900 border border-slate-800">
              <h3 className="text-xl font-semibold mb-2">Сообществам и раввинам</h3>
              <p className="text-slate-300">
                Используйте материалы проекта для уроков, публикаций и общения с учениками в цифровой среде.
              </p>
            </div>
            <div className="p-6 rounded-2xl bg-slate-900 border border-slate-800">
              <h3 className="text-xl font-semibold mb-2">Тем, кто ищет вдохновение</h3>
              <p className="text-slate-300">
                Подписывайтесь на обновления, чтобы находить поддержку и слова, которые укрепляют веру ежедневно.
              </p>
            </div>
          </div>
        </div>
      </section>

      <section className="px-6 py-14">
        <div className="max-w-5xl mx-auto space-y-6">
          <h2 className="text-3xl font-semibold text-center">Как это работает</h2>
          <div className="grid md:grid-cols-3 gap-6 text-slate-300">
            <div className="p-6 rounded-2xl bg-slate-900/60 border border-slate-800">
              <p className="text-slate-200 font-semibold mb-2">1. Сбор мудрости</p>
              <p>Алгоритмы собирают тексты, уроки и ответы учителей Торы, чтобы сохранить их в цифровом формате.</p>
            </div>
            <div className="p-6 rounded-2xl bg-slate-900/60 border border-slate-800">
              <p className="text-slate-200 font-semibold mb-2">2. Анализ и подготовка</p>
              <p>Искусственный интеллект структурирует материалы, выделяет ключевые мысли и переводит их в удобный формат.</p>
            </div>
            <div className="p-6 rounded-2xl bg-slate-900/60 border border-slate-800">
              <p className="text-slate-200 font-semibold mb-2">3. Распространение</p>
              <p>Готовые материалы публикуются на сайте, в Телеграм-каналах и других площадках, чтобы слово достигало больше людей.</p>
            </div>
          </div>
        </div>
      </section>

      <section className="px-6 py-14 bg-slate-900/40">
        <div className="max-w-4xl mx-auto text-center space-y-4">
          <h2 className="text-3xl font-semibold">Наше видение</h2>
          <p className="text-lg text-slate-300">
            SODMASTER стремится стать местом, где духовные знания сохраняются и распространяются с помощью современных технологий.
            Мы верим, что объединяя традицию и цифровые инструменты, можно вдохновлять, укреплять веру и расширять доступ к Торе для каждого.
          </p>
        </div>
      </section>
    </main>
  );
}
