# Avatar Shots «выход Патрика» — разбор и готовый промт (ON HOLD)

**Статус: пауза по слову Якова 19.08.2026 — не рендерить до его «да».**

## Исходник
- HeyGen video id `84e359d14526427ca9e74515515e5953` (Seedance2 / Avatar Shots)
- 15 с, 9:16, 720×1280, completed. Копия: `patrick_shot_v1.mp4`, кадры `shot_*.jpg`
- Сцена: тройка идёт по luxury-холлу с люстрами, позади толпа в костюмах

## Проблема
В центре кадра — **сгенерированный посторонний** (седой, синий костюм). Патрик
(лысый, щетина, чёрный блейзер) задвинут вправо. Патрик должен идти в центре, вести.

## Решение (готово к запуску)
Один аватар-референс вместо нескольких — тогда Seedance не «выберет» другого лидера:
- Группа: **Patrick Lehner** `24f3cfa984ed427b91efec0e64b412fe` (51 лук)
- Лук: **«Patrick Lehner in black blazer»** `2dd3b5378d5041aa8d7e7af2803cfd36`
  (чёрный блейзер + чёрная футболка, мрамор с золотом — точный канон Legends)
- Параметры: 15 с · 9:16 · 720p (60 кредитов; 1080p = 150)

Промт (проверен по формуле 6 шагов, ~95 слов):

```
Patrick, a bald man with light stubble in a tailored black blazer over a black shirt,
walks front and center down a grand luxury hotel corridor, golden chandeliers above,
black marble and warm gold reflections on polished floor. He leads alone: four
anonymous executives in dark suits walk a full step behind him, flanking symmetrically,
slightly out of focus. Calm, confident, eyes locked on camera. Camera tracks backwards
at his pace, keeping Patrick centered, medium-wide. Cinematic prestige, film grain,
black-and-gold grade. Deep slow bass pulse building. Avoid jitter, avoid identity drift,
avoid anyone walking beside or ahead of the leader.
```

## Путь запуска (когда будет «да»)
- Предпочтительно: MCP HeyGen (generative-пул, в 3.6× дешевле) — **коннектор сейчас
  отвалился**, Якову переподключить в настройках коннекторов claude.ai
- Запасной: REST-ключ из `heygen_videos/.env` — работает, но списывает USD-кошелёк
