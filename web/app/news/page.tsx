"use client";

import Link from "next/link";
import { useEffect, useState } from "react";

type NewsItem = {
  id: number;
  title: string | null;
  summary: string;
  created_at: string;
};

export default function NewsPage() {
  const [items, setItems] = useState<NewsItem[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const load = async () => {
      try {
        const res = await fetch("/api/news/list");

        if (!res.ok) {
          throw new Error("Failed to fetch news");
        }

        const data: NewsItem[] = await res.json();
        setItems(data);
      } catch (e) {
        setError("Ошибка при запросе к серверу.");
        setItems([]);
      } finally {
        setLoading(false);
      }
    };

    load();
  }, []);

  return (
    <main className="min-h-screen bg-slate-950 text-slate-50">
      <div className="max-w-3xl mx-auto px-4 py-10">
        <h1 className="text-3xl font-semibold mb-6">Новости SODMASTER</h1>

        {loading && <p>Загрузка новостей.</p>}

        {!loading && error && (
          <p className="text-red-400 mb-4">{error}</p>
        )}

        {!loading && !error && items.length === 0 && (
          <p>Новостей пока нет.</p>
        )}

        {!loading && !error && items.length > 0 && (
          <ul className="space-y-4">
            {items.map((item) => (
              <li
                key={item.id}
                className="border border-slate-700 rounded-lg p-4 hover:border-slate-500 transition"
              >
                <h2 className="text-xl font-medium mb-1">
                  {item.title || "Новость без заголовка"}
                </h2>
                <p className="text-sm text-slate-300 line-clamp-3 mb-2">
                  {item.summary}
                </p>
                <div className="flex items-center justify-between text-xs text-slate-400">
                  <span>
                    {new Date(item.created_at).toLocaleString("ru-RU")}
                  </span>
                  <Link
                    href={`/news/${item.id}`}
                    className="text-sky-400 hover:text-sky-300"
                  >
                    Читать
                  </Link>
                </div>
              </li>
            ))}
          </ul>
        )}
      </div>
    </main>
  );
}
