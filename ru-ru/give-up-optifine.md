# Конец эры OptiFfine

Одна из целей Fabulously Optimized это реализация функционала из [OptiFine](https://optifine.net/home), чтобы сделать уход от него более плавным для пользователей.

Вот список функций OptiFine'a которые на данный момент момент поддерживаются в этой сборке:

✔️ = **Поддерживается**

🚧 = **Частично поддерживается**

🔜 = **Скоро будет поддерживаться**

❌ = **Не поддерживается**

### Графика

| Функция               | Поддерживается? | Мод реализующий функцию                                                                                                                                                                                                                                                                                  |
| --------------------- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Переключение анимаций     | ✔️            | [Sodium Extra](https://www.curseforge.com/minecraft/mc-mods/sodium-extra)                                                                                                                                                                                                                                  |
| Плащи                 | ✔️            | [Fabric Capes](https://www.curseforge.com/minecraft/mc-mods/capes) ([Tutorial](free-cape.md))                                                                                                                                                                                                              |
| Переключение деталей        | ✔️            | [Sodium Extra](https://www.curseforge.com/minecraft/mc-mods/sodium-extra)                                                                                                                                                                                                                                  |
| Динамическое освещение        | ✔️            | [Lambda Dynamic Lights](https://www.curseforge.com/minecraft/mc-mods/lambdynamiclights)                                                                                                                                                                                                                    |
| Переключение других мелочей | ✔️            | [Sodium Extra](https://www.curseforge.com/minecraft/mc-mods/sodium-extra)                                                                                                                                                                                                                                  |
| Переключение частиц      | ✔️            | [Sodium Extra](https://www.curseforge.com/minecraft/mc-mods/sodium-extra)                                                                                                                                                                                                                                  |
| Производительность           | ✔️            | [Sodium](https://www.curseforge.com/minecraft/mc-mods/sodium), [Lithium](https://www.curseforge.com/minecraft/mc-mods/lithium), [Starlight](https://www.curseforge.com/minecraft/mc-mods/starlight) [etc.](https://github.com/Fabulously-Optimized/fabulously-optimized/blob/main/INCLUDED-MODS.md#smooth) |
| Умные Листья¹         | ✔️            | [Cull Less Leaves](https://www.curseforge.com/minecraft/mc-mods/cull-less-leaves)                                                                                                                                                                                                                          |
| Zoom²                  | ✔️            | [Zoomify](https://www.curseforge.com/minecraft/mc-mods/zoomify)                                                                                                                                                                                                                                            |
| Шейдеры               | 🚧            | [Iris](https://www.curseforge.com/minecraft/mc-mods/irisshaders) ([Инструкция](getting-shaders.md)). Некоторые шейдеры не работают. [PBR текстуры не поддерживаются](https://discord.com/channels/774352792659820594/774354933436645478/967251726304415784) [(тут)](https://discord.gg/jQJnav2jPu).                      |
| Уровень мягкого освещения | ❌             | В моде [Sodium Extra](https://www.curseforge.com/minecraft/mc-mods/sodium-extra) есть  [issue](https://github.com/FlashyReese/sodium-extra-fabric/issues/125) по этому поводу.                                                                                                                                    |
| 32+ дальность прорисовки  | ❌             | Используйте [Bobby](https://www.curseforge.com/minecraft/mc-mods/bobby) [(почему этого нет в FO?)](https://github.com/Fabulously-Optimized/fabulously-optimized/issues/46#issuecomment-1067105734).                                                                                                                  |

### Пользовательские ресурспаки

| Функция                      | Поддерживается? | Мод реализующий функцию                                                                                                                                                                     |
| --------------------------- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Анимированные текстуры      | ✔️            | [Animatica](https://www.curseforge.com/minecraft/mc-mods/animatica)                                                                                                                           |
| Улучшенная Трава/Снег³      | ✔️            | [LambdaBetterGrass](https://www.curseforge.com/minecraft/mc-mods/lambdabettergrass)                                                                                                           |
| Соединённые текстуры        | ✔️            | [Continuity](https://www.curseforge.com/minecraft/mc-mods/continuity)                                                                                                                         |
| Пользовательские цвета      | ✔️            | [Colormatic](https://www.curseforge.com/minecraft/mc-mods/colormatic)                                                                                                                         |
| Пользовательские GUI        | ✔️            | [OptiGUI](https://www.curseforge.com/minecraft/mc-mods/optigui)                                                                                                                               |
| Пользовательские предметы   | ✔️            | [CIT Resewn](https://www.curseforge.com/minecraft/mc-mods/cit-resewn)                                                                                                                         |
| Светящиеся блоки            | ✔️            | [Continuity](https://www.curseforge.com/minecraft/mc-mods/continuity)                              |
| Светящиеся существа         | ✔️            | [Entity Texture Features](https://www.curseforge.com/minecraft/mc-mods/entity-texture-features-fabric)                                                                                        |
| HD шрифты                   | ✔️            | [Поддерживается в ванилле с 1.13.](https://minecraft.fandom.com/wiki/Java\_Edition\_1.13-pre6#Changes) [Можете скачать парочку из моегоо профиля](https://www.curseforge.com/members/robotkoer/projects)                                                                                             |
| HD скриншоты                | ✔️            | [Fabrishot](https://www.curseforge.com/minecraft/mc-mods/fabrishot)                                                                                                                           |
| Натуральные текстуры        | ✔️            | [Подерживается в ванилле с 1.8](https://minecraft.fandom.com/wiki/Java\_Edition\_14w17a#Model%20format%20improvements)                                                                            |
| Случайные существа          | ✔️            | [Entity Texture Features](https://www.curseforge.com/minecraft/mc-mods/entity-texture-features-fabric)                                                                                        |
| Заставка ресурспака         | ✔️            | [Puzzle](https://www.curseforge.com/minecraft/mc-mods/puzzle)                                                                                                                                 |
| Пользовательские модели существ | 🚧            | [Custom Entity Models](https://www.curseforge.com/minecraft/mc-mods/custom-entity-models-cem). [Не поддерживает пока всех существ](https://github.com/dorianpb/cem#current-state-of-this-mod). |                                             |
| Анизотропная фильтрация     | ❌             | [Это было обсуждено в дискоре](https://discord.com/channels/756612889787498627/876567546390777856/978673913770950687) [(тут)](https://discord.gg/7rnTYXu)                             |
| Пользовательское небо       | ❌             | Смотрите [#72](https://github.com/Fabulously-Optimized/fabulously-optimized/issues/72)                                                                                                             |


¹ Не идентично OptiFine'у так-как людям не нравилось как это выглядело. Если вы хотите чтобы было идентично:

1. [Отключите Cull Less Leaves](disabling-mods.md)
2. [Установите](adding-more-mods.md) оригинальный [Cull Leaves](https://www.curseforge.com/minecraft/mc-mods/cull-leaves)
3. Активируйте встроенный в Cull Leaves ресурспак
4. Отключите "Use Block Face Culling" в <kbd>Настройки</kbd> -> <kbd>Видео опции...</kbd> -> <kbd>Продвинутые</kbd>.

² По стандарту не соответствует OptiFine'у, поэтому-что люди предпочли более плавный zoom. Чтобы сделать как в OptiFine:

1. Жмите на кнопку <kbd>Моды</kbd>, найдите там `Zoomify`, кликните на него, и в левом верхнем углу жмите на иконку `Configure`.
2. Во вкладке `Behaviour`, установите `Zoom Transition` в `Instant`
3. Во вкладке `Scrolling`, переключите `Enable Scroll Zoom` в `OFF`
4. Во вкладке `Controls`, переключите `Relative Sensitivity` в `OFF` и переставьте `Cinematic Camera` в `ON`

³ Улучшенный снег опциональный, потому-что затрагивает текстуры, что заставляет его выглядеть странно с некоторыми ресурспаками:

1. Кликните на <kbd>Моды</kbd>, найдите `LambdaBetterGrass`, кликните на него, и в левом верхнем углу жмите на иконку `Configure`.
2. Установите `Улучшенный снег` в `ON`

---

В добавок ко всему, вам может понравится:

* Лучшей совместимостью модов
* [Простой установкой](https://github.com/Fabulously-Optimized/fabulously-optimized#downloads) для различных лаунчеров
* [Парочкой дополнительный функций](https://github.com/Fabulously-Optimized/fabulously-optimized/blob/main/INCLUDED-MODS.md#functional) которых нет в OptiFine

Мы всё-ещё в процессе добавлении всех функций OptiFine'a. Если вы заинтерисованы в том что ещё предстоить добавить, взгляните на [этот список](https://github.com/Fabulously-Optimized/fabulously-optimized/issues?q=is:issue%20is:open%20label:parity).

Если вы испытываете какие-то проблемы с ресурспака использующими возможности OptiFine'a, обратите внимание на [это](resource-pack-issues.md)

_Смотрите также:_ [_Рекоммендуемые альтернативы OptiFine'у на Fabric_](https://lambdaurora.dev/optifine\_alternatives)_, это список, который вдохновил нас на создание этой сборки._