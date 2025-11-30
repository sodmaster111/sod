export default function HomePage() {
  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-semibold">Автономное AI-агентство для распространения иудаизма</h1>
      <p className="text-slate-700">
        SODMASTER — это цифровой проект, который использует локальные модели искусственного интеллекта для
        создания и распространения вдохновляющего контента об эмуна, Торе и заповедях на русском языке.
      </p>
      <div className="flex gap-3 flex-wrap">
        <a
          href="#"
          className="rounded bg-slate-900 px-4 py-2 text-white hover:bg-slate-800 transition"
        >
          Вступить в WhatsApp-группу
        </a>
        <a
          href="#"
          className="rounded border border-slate-300 px-4 py-2 text-slate-900 hover:bg-slate-100 transition"
        >
          Подписаться на Telegram-канал
        </a>
      </div>
      <div className="grid gap-4 md:grid-cols-3">
        <div className="rounded border border-slate-200 bg-white p-4 shadow-sm">
          <h3 className="font-semibold text-lg">Изучение Торы</h3>
          <p className="text-sm text-slate-700">
            Короткие объяснения недельных глав, идеи из Талмуда и комментарии мудрецов, которые помогают
            углубить понимание Торы каждый день.
          </p>
        </div>
        <div className="rounded border border-slate-200 bg-white p-4 shadow-sm">
          <h3 className="font-semibold text-lg">Ежедневная молитва</h3>
          <p className="text-sm text-slate-700">
            Краткие тексты молитв, отрывки из Теилим и слова хизук, поддерживающие концентрацию и внутренний
            настрой на связь со Всевышним.
          </p>
        </div>
        <div className="rounded border border-slate-200 bg-white p-4 shadow-sm">
          <h3 className="font-semibold text-lg">Поддерживающее сообщество</h3>
          <p className="text-sm text-slate-700">
            Участники получают поддержку, вдохновение и напоминания о добрых делах, чтобы двигаться к цели
            вместе и помогать друг другу.
          </p>
        </div>
      </div>
    </div>
  )
}
