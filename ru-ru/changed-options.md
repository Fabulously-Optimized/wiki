# Изменённые настройки

Fabulously Optimized меняет некоторые стандартные настройки майнкрафта чтобы сделать ваш геймплей приятней.

Из-за того что эта сборка использует мод YOSBR, ваши настройки изменятся только если у вас нет `options.txt` файла, или каких-то специфичных для модов настроек в папке `config`, как если бы вы использовали чистый профиль. Это так-же значит что вы можете спокойно обновлять сборку без страха потерять ваши настройки!

### Настройки

| Опция                      | Описание                                                                                                                                                                                           | Стандарт  | Сборка | Причина изменения                                                                                                                                         |
| --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| autoJump                    | Заставляет игрока прыгать когда встречается блок высотой не выше еденицы                                                                                                                                               | true     | false   | В стандартной игре это больше раздражает чем помогает, многие игроки и так выключают эту опцию                                                                                   |
| snooperEnabled              | Отключает [Snooper](https://minecraft.fandom.com/wiki/Snooper), сервис анализа оборудования. Эта настройка была удалена из меню в 1.13, но всё-ещё существует в `options` (и включена по стандарту) по какой-то причине. | true     | false   | Просто на всякий случай, для улучшения приватности. В 1.18+ [Debugify](https://curseforge.com/minecraft/mc-mods/debugify) используется для реального противодействия этому. |
| darkMojangStudiosBackground | Делает экран загрузки чёрнобелым                                                                                                                                                               | false    | true    | Чёрный фон менее назойливый чем красный                                                                          |
| simulationDistance          | Дистанция работы редстоуна и спавна мобов                                                                                                                                                                    | 12       | 6       | Лучшая производительность, вне зависимости от того какую дальность прорисовки вы используете                                                                                      |
| guiScale                    | Размер меню и элементов интерфейса                                                                                                                                                               | 0        | 3       | 3 юзабельно на всех экранах, 0 (Авто) Может быть слишком большим на Full HD и экранах больших размеров                                                                 |
| maxFps                      | Максимальное количество кадров                                                                                                                                                                                 | 120      | 260     | 260 означает "неограниченно", эта опция была отключена для более приятного опыта для пользователей отключивших VSync (на быстрых компьютерах/мониторах)                                 |
| resourcePacks               | Определяет какие ресурспаки включены по стандарту                                                                                                                                                   | \[]      | ¹       | Включает стандартные паки модов' и эксклюзивный для FO - Mod Menu Helper                                                                                         |
| tutorialStep                | Следующий шаг [подсказок](https://minecraft.fandom.com/wiki/Tutorial\_hints)                                                                                                                  | movement | none    | Если вы знаете как у становить модпак, вам вероятно не нужны эти подсказки                                                                |
| skipMultiplayerWarning      | Пропускать ли [отказ от ответственности](https://minecraft.fandom.com/wiki/File:Multiplayer\_disclaimer.png) когда открываете экран мультиплеера                                                        | false    | true    | Мы ожидаем что наши пользователи уже знают что сторонние сервера не принадлежат Mojang Studios или Minecraft                             |
| joinedFirstServer           | Показывать ли подсказку о [социальных взаимодействиях](https://minecraft.fandom.com/wiki/Social\_Interactions\_screen)                                                                                 | false    | true    | Мы ожидаем что наши пользователи уже знают о том что вы можете открыть экран социальных взаимодействий на `З`                                                                      |
| chatPreview           | Показывать ли [предпросмотр чата](https://minecraft.fandom.com/wiki/Java_Edition_22w19a#General)                                                                                 | true    | false    | Отключено по соображениям привотности, чтобы сообщения не отправлялись на сервер пока вы их пишите, дабы избежать разных раздражающих предупреждений                                  |

¹ \["vanilla","Fabric Mods","lambdabettergrass/default","continuity/default","continuity/glass_pane_culling_fix","file/Mod Menu Helper.zip"]

### Привязка клавиш

| Опция                                 | Описание                                                            | Стандарт | Сборка | Причина изменения                                                                |
| ------------------------------------- | ------------------------------------------------------------------- | -------- | ------ | -------------------------------------------------------------------------------- |
| Стандарт: Сохранить инструменты       | Сохраняет ваши инструменты если эта кнопки и цифра были нажаты      | c        | none   | Эта кнопка часто используется для зума                                           |
| Zoomify/WI Zoom: Zoom                 | Приближение по нажатию на кнопку                                    | v        | c      | Эта кнопка часто используется для зума                                           |
| Zoomify: GUI                          | Открывает настройки мода Zoomify                                    | F8       | none   | Не требуется большинству игроков                                                 |
| AntiGhost: Обновить блоки вокруг себя | Просит сервер отправить блоки вокруг вас, чтобы отбаговать          | g        | none   | Случайные нажатия могу привести к проблемам, вместо этого используете **/ghost** |
| Iris: Перезагрузить шейдеры           | Перезагружает используемые шейдеры                                  | r        | none   | Не требуется большинству игроков                                                 |
| Iris: Экран выбора шейдеров           | Открывает меню выбора шейдеров                                      | o        | none   | Не требуется большинству игроков                                                 |
| Iris: Переключить шейдеры             | Отключает или включает шейдеры                                      | k        | none   | Не требуется большинству игроков                                                 |

Изменённые настройки модов вы можете найти в репозитории, в [.../yosbr/1.18.2/config](https://github.com/Fabulously-Optimized/fabulously-optimized/tree/main/Packwiz/1.18.2/config).

Так-же обратите внимание на [Minecraft Wiki: options.txt](https://minecraft.fandom.com/wiki/Options.txt#Java\_Edition)(англ) и [issue #30](https://github.com/Fabulously-Optimized/fabulously-optimized/issues/30)

### Исправленные баги

Fabulously Optimized включает в себя некоторые моды нацеленные на исправление багов.
[Аналагично политике включения модов](principles.md), они должны быть полезны для 70%+ пользователей для того чтобы быть включёнными (по типу просадков FPS, вылетов, специфичных для платформ проблем...).

| Ошибка на сайте Mojang                                | Описание                                                                   | Чем исправлено                                                                |
| ----------------------------------------------------- | -------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| [MC-26757](https://bugs.mojang.com/browse/MC-26757)   | Большие предметные подсказки могут быть обрезаны по краям экрана           | [ToolTipFix](https://www.curseforge.com/minecraft/mc-mods/tooltipfix)         |
| [MC-73186](https://bugs.mojang.com/browse/MC-73186)   | Зазоры между плоскостями в моделях предметов                               | [Item Model Fix](https://www.curseforge.com/minecraft/mc-mods/item-model-fix) |
| [MC-81098](https://bugs.mojang.com/browse/MC-81098)   | Обновления редстоуна вызывают лаги (Только в одиночной игре)               | [Lithium](https://www.curseforge.com/minecraft/mc-mods/lithium)               |
| [MC-89146](https://bugs.mojang.com/browse/MC-89146)   | Поршни забывают обновится когда их перезагружаешь                          | [Debugify](https://curseforge.com/minecraft/mc-mods/debugify)                 |
| [MC-112730](https://bugs.mojang.com/browse/MC-112730) | Луч маяка и структурные блоки рендерятся дважды за кадр                    | [Debugify](https://curseforge.com/minecraft/mc-mods/debugify)                 |
| [MC-121772](https://bugs.mojang.com/browse/MC-121772) | Невозможно скролить с зажатым шифтом в MacOS                               | [Debugify](https://curseforge.com/minecraft/mc-mods/debugify)                 |
| [MC-121884](https://bugs.mojang.com/browse/MC-121884) | Кастомные Сервер -> Клиент пакеты могут вызвать утечку ресурсов            | [MemoryLeakFix](https://www.curseforge.com/minecraft/mc-mods/memoryleakfix)   |
| [MC-122477](https://bugs.mojang.com/browse/MC-122477) | Linux/GNU: Открытие чата иногда вписывает 't'                              | [Debugify](https://curseforge.com/minecraft/mc-mods/debugify)                 |
| [MC-132488](https://bugs.mojang.com/browse/MC-132488) | Анимированные по тикам текстуры, крайне не оптимизированны                 | [Sodium](https://www.curseforge.com/minecraft/mc-mods/sodium)                 |
| [MC-140646](https://bugs.mojang.com/browse/MC-140646) | Текстовые поля не прокручиваются во время выделения текста с нажатым Shift | [Debugify](https://curseforge.com/minecraft/mc-mods/debugify)                 |
| [MC-145929](https://bugs.mojang.com/browse/MC-145929) | Текст действия сложно прочесть без фона                                    | [Debugify](https://curseforge.com/minecraft/mc-mods/debugify)                 |
| [MC-148149](https://bugs.mojang.com/browse/MC-148149) | Игра вылетает на Linux при попытке открыть ссылку                          | [Debugify](https://curseforge.com/minecraft/mc-mods/debugify)                 |
| [MC-162253](https://bugs.mojang.com/browse/MC-162253) | Просадки производительности когда переходишь края некоторых чанков         | [Debugify](https://curseforge.com/minecraft/mc-mods/debugify)                 |
| [MC-165595](https://bugs.mojang.com/browse/MC-165595) | Луч стража не рендерится когда кончается какой-то "Time" в level.dat       | [Sodium Extra](https://www.curseforge.com/minecraft/mc-mods/sodium-extra)     |
| [MC-172550](https://bugs.mojang.com/browse/MC-172550) | Блоки призраки иногда появляется при использовании мнгновеннго копания     | [AntiGhost](https://www.curseforge.com/minecraft/mc-mods/antighost)           |
| [MC-199467](https://bugs.mojang.com/browse/MC-199467) | Некоторые анимации перестают работать у существ проживжих слишком долго    | [Debugify](https://curseforge.com/minecraft/mc-mods/debugify)                 |
| [MC-226729](https://bugs.mojang.com/browse/MC-226729) | Проблема утечки памяти в нативных операциях                                | [MemoryLeakFix](https://www.curseforge.com/minecraft/mc-mods/memoryleakfix)   |
| [MC-227302](https://bugs.mojang.com/browse/MC-227302) | Мягкое освещение не работает как надо на водной глади                      | [Sodium](https://www.curseforge.com/minecraft/mc-mods/sodium)                 |  
| [MC-228976](https://bugs.mojang.com/browse/MC-228976) | Колизия существ работает в потоке рендерера                                | [Debugify](https://curseforge.com/minecraft/mc-mods/debugify)                 |
| [MC-235035](https://bugs.mojang.com/browse/MC-235035) | Сон в кастомном измерении с "natural" = false приводит к вылету            | [Debugify](https://curseforge.com/minecraft/mc-mods/debugify)                 |
| [MC-237493](https://bugs.mojang.com/browse/MC-237493) | Невозможно отключить сбор технический данных                               | [Debugify](https://curseforge.com/minecraft/mc-mods/debugify)                 |
| [MC-249059](https://bugs.mojang.com/browse/MC-249059) | Экран "загрузки территории" невозможно закрыть пока не пройдёт 2 секунды   | [Debugify](https://curseforge.com/minecraft/mc-mods/debugify)                 |

Если вы хотить включить ещё какие-то исправления в игре, смотрите [список исправленных багов в Debugify](https://github.com/W-OVERFLOW/Debugify/blob/1.18/PATCHED.md#unpatched-in-vanilla).

#### Предложение исправлений

Хотите чтобы баг был исправлен в Fabulously Optimized? Вот что вам нужно сделать:

1. Найдите этот баг в [багтрекере Mojang](https://bugs.mojang.com/projects/MC/issues?filter=allopenissues)
2. Предложите его, или посмотрите его статус в [багтрекере Debugify](https://github.com/W-OVERFLOW/Debugify/issues)
3. Когда фикс реализуют (или вы узнаете что он уже есть) в Debugify, [предложите option change в FO](https://github.com/Fabulously-Optimized/fabulously-optimized/issues/new?assignees=\&labels=option\&template=setting-request.yml)
4. Опишите баг, укажите мод который его испрвляет, и докажите что он важен для 70-80% пользователей
5. Если его примут, можете ожидать что он появится в следующей версии FO :)

### Настройка модов

Эта сборка уже настроена на лучшую производительность и простой опыт для большинства игроков.

Если вы хотите изменить что-то, вы скорее всего найдёте это в `Настройки...` -> `Настройки графики...`. Если у вас мощный компьютер, или хороший монитор, вы скорее всего захотите отключить здесь вертикальную синхронизацию.

Для других вещей по типу динамического освещения, улучшенной травы или зума:

1. Нажмите на `Моды`
2. Прочтите описания модов чтобы узнать что они делают
3. Если карандаш синий, вы можете настроить мод кликнув на кнопку конфигурации ![config](https://i.ibb.co/j35cBtn/image.png)
   * Если вы не видите карандашей, тогда у вас отключен ресурс-пак Mod Menu Helper по какой-то причине. Нажмите на `Готово` -> `Настройки...` -> `Пакеты Ресурсов...` -> `⏵` затем "Mod Menu Helper.zip" -> `Готово` -> и начните с первого пункта.

Если вы хотите отключить мод, [смотрите эту страничку вики](disabling-mods.md).

Если у вас остались ещё вопросы касательно модов, [то добро пожаловать в наш Discord!](https://discord.gg/yxaXtaQqdB)
