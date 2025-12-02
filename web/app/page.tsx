export default function Page() {
  return (
    <main className="min-h-screen bg-slate-950 text-slate-100" dir="rtl">
      <section className="mx-auto flex max-w-6xl flex-col gap-10 px-6 py-16 text-right lg:flex-row lg:flex-row-reverse lg:items-center">
        <div className="flex-1 space-y-6">
          <h1 className="text-4xl font-bold leading-tight sm:text-5xl">
            SODMASTER — הבית הדיגיטלי לאמונה ולתורה
          </h1>
          <p className="text-lg text-slate-200 sm:text-xl">
            פרויקט בינה מלאכותית שמפיץ דברי תורה, אמונה והשראה לעולם, דרך אתר, בוטים וקבוצות. המטרה היא לתת מקום
            דיגיטלי בטוח, מחזק ונגיש לכל מי שמחפש חיבור ומשמעות.
          </p>
          <div className="flex flex-wrap justify-end gap-4">
            <a
              href="https://chat.whatsapp.com"
              className="rounded-xl bg-slate-100 px-6 py-3 font-semibold text-slate-900 shadow transition hover:bg-white hover:shadow-lg"
            >
              הצטרפות לקבוצת הווטסאפ
            </a>
            <a
              href="https://t.me/sodmaster_online"
              className="rounded-xl border border-slate-700 px-6 py-3 font-semibold text-slate-100 shadow transition hover:border-slate-500 hover:bg-slate-900"
            >
              הצטרפות לערוץ הטלגרם
            </a>
          </div>
        </div>
        <div className="flex-1 rounded-xl border border-slate-800 bg-slate-900/60 p-6 shadow-lg">
          <p className="text-center text-lg font-semibold text-slate-100">
            AI מקומי · בלי תלות בעננים חיצוניים · ממוקד בתוכן רוחני
          </p>
        </div>
      </section>

      <section id="about" className="bg-slate-900/40">
        <div className="mx-auto max-w-5xl space-y-6 px-6 py-14 text-right">
          <h2 className="text-3xl font-bold sm:text-4xl">מה זה SODMASTER?</h2>
          <div className="space-y-4 text-lg text-slate-200">
            <p>
              SODMASTER הוא פרויקט רוחני-טכנולוגי שמשלב מודלי בינה מלאכותית מקומיים עם ערכי המסורת היהודית כדי להפיץ
              אור, השראה ותמיכה.
            </p>
            <p>
              המיזם לא מחליף רב חי או קהילה, אלא מוסיף כלים דיגיטליים שמספקים תשובות, חיזוק ותוכן מבוסס אמונה במקום
              ובזמן שנוח למשתמשים.
            </p>
            <p>
              החזון הוא לחזק אנשים שמחפשים קשר עם הבורא, ולאפשר להם לקבל תוכן נקי, אמין ומעורר גם במרחב הדיגיטלי.
            </p>
          </div>
        </div>
      </section>

      <section className="mx-auto max-w-6xl px-6 py-14 text-right">
        <h2 className="text-3xl font-bold sm:text-4xl">איך זה עובד</h2>
        <div className="mt-8 grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
          <div className="rounded-xl border border-slate-800 bg-slate-900/60 p-6 shadow">
            <h3 className="text-xl font-semibold">סוכני AI</h3>
            <p className="mt-3 text-slate-200">
              רב וירטואלי, עורך ומנהל תוכן עובדים יחד כדי ליצור, לסנן ולהתאים מסרים מעוררי השראה.
            </p>
          </div>
          <div className="rounded-xl border border-slate-800 bg-slate-900/60 p-6 shadow">
            <h3 className="text-xl font-semibold">מודלים מקומיים</h3>
            <p className="mt-3 text-slate-200">
              כל התהליכים פועלים על תשתית פרטית ללא תלות בעננים חיצוניים, כדי לשמור על פרטיות ועל עצמאות טכנולוגית.
            </p>
          </div>
          <div className="rounded-xl border border-slate-800 bg-slate-900/60 p-6 shadow">
            <h3 className="text-xl font-semibold">ערוצי הפצה</h3>
            <p className="mt-3 text-slate-200">
              התוכן מופץ באתר, בערוץ הטלגרם ובקרוב גם בקבוצות ווטסאפ וערוצים נוספים.
            </p>
          </div>
        </div>
      </section>

      <section className="bg-slate-900/40">
        <div className="mx-auto max-w-5xl px-6 py-14 text-right">
          <h2 className="text-3xl font-bold sm:text-4xl">למי הפרויקט מיועד</h2>
          <ul className="mt-6 space-y-3 list-disc pr-5 text-lg text-slate-200">
            <li>למי שעובר תקופה מאתגרת וזקוק לחיזוק, עידוד ומילה טובה.</li>
            <li>למי שמחפש משמעות, תשובות ושיח אמונה בגישה מכבדת ומאוזנת.</li>
            <li>למי שאוהב טכנולוגיה, אבל רוצה לשמור על חיבור עמוק לרוחניות ולמסורת.</li>
          </ul>
        </div>
      </section>

      <section className="mx-auto max-w-5xl px-6 py-14 text-right">
        <h2 className="text-3xl font-bold sm:text-4xl">הצטרפו ל-SODMASTER</h2>
        <p className="mt-4 text-lg text-slate-200">
          הערוץ המרכזי כרגע הוא הטלגרם. הצטרפו כדי לקבל תכנים חדשים, הודעות חיזוק ועדכונים על התפתחות המיזם.
        </p>
        <div className="mt-6">
          <a
            href="https://t.me/sodmaster_online"
            className="inline-flex rounded-lg bg-slate-100 px-5 py-3 text-slate-900 transition hover:bg-white hover:shadow-lg"
          >
            לפתוח את ערוץ הטלגרם
          </a>
        </div>
      </section>
    </main>
  )
}
