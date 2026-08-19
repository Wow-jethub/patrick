# Three Lines Explainer — разбор исходника

**Исходник:** `Downloads/video_2026-08-19_22-10-49.mp4` · 1:41 · 848×464 · 30 fps · **без звуковой дорожки**
**Стиль исходника:** whiteboard-анимация «рукописный» шрифт, тёмно-синий фон с сеткой,
фиолетовые/зелёные акценты — палитра основного JetUP, не Legends. Язык — немецкий.

## Покадровая структура (тайминги ~)

| Время | Метка | Содержание |
|---|---|---|
| 0:00–0:15 | DER START | «150 + 100» (DU — твоя часть) |
| 0:15–0:30 | ALLES HÄNGT AN DREI LINIEN | Drei Linien: Breite × Tiefe · Volumen bleibt liegen · Einsatz wächst von selbst |
| 0:30–0:45 | LINIE 1 | «10 direkt · 10 Ebenen tief» — диаграмма структуры |
| 0:45–1:00 | LINIE 2 | «Volumen bleibt liegen» — растущий бар-чарт с трендом |
| 1:00–1:15 | LINIE 3 | «Der Einsatz wächst»: 150 beim Start → erst prüfen → mehr, wenn es trägt. «Niemand fängt gross an — fast alle erhöhen später» |
| 1:15–1:30 | KURZ | Lot-Kommission (pro Bewegung) · Profit Share (am Ergebnis) · Infinity Bonus (über die Tiefe) · Global Pool (aus dem Ganzen) |
| 1:30–1:41 | DAS IST DAS GANZE BILD | «250 rein. Drei Linien. Zehn Ebenen tief. Alles andere ist Detail. Frag die Person, die dich eingeladen hat.» JETUP |

## Сверка цифр с каноном (git pull 19.08.2026)

| Цифра в исходнике | Канон | Статус |
|---|---|---|
| 10 прямых → 10 уровней | `JETUP_CORE.md` §92: депозит $250 → 3 уровня; 4+ прямых → +1 уровень; 10 прямых → все 10 | ✅ сходится |
| 4 потока дохода | `30_partner_mechanics.md`: Lot Commissions · Profit Share · Infinity Bonus · Global Pool | ✅ сходится |
| Квалификация 250 | `30_partner_mechanics.md` §42: минимум 250 USD активного трейдинга | ✅ сходится |
| **150 + 100 = 250** | В канон-репе разбивки «150 партнёрство + 100 промо» **нет** (`CANON_AH_PROMPT_EVA.md` строка 152: «ждёт решения Якова»; `HANDOFF_AGENT_CHAT_BUILD.md`: цифра убрана из агента). При этом в отправленных роликах Colin/UK-team она используется (`CONTENT_LEDGER.md` §476, §872) | ⚠️ **требует подтверждения Якова** |

## Что меняем в версии Legends

- Палитра: обсидиан `#0A0A0A`, золото `#C69B3C` ≤15% кадра, шампань-канты. Один металл, без фиолетового/зелёного.
- Шрифты: Cormorant Garamond (заголовки) · JetBrains Mono (метки, цифры) — вместо рукописного.
- Титры EN (правило `onscreen-text-english`), исходник был DE.
- Добавляем то, чего в исходнике нет: озвучка (ElevenLabs, style:0), звуковая подложка, интро на медальоне Golden Dynasty, дисклеймер (в кадре есть числа — обязателен).
- Формат: 1920×1080, ~1:40.
