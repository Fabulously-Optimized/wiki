# Изменённые настройки

Fabulously Optimized меняет некоторые стандартные настройки майнкрафта чтобы сделать ваш геймплей приятней.

Из-за того что эта сборка использует мод YOSBR, ваши настройки изменятся только если у вас нет `options.txt` файла, или каких-то специфичных для модов настроек в папке `config`, как если бы вы использовали чистый профиль. Это так-же значит что вы можете спокойно обновлять сборку без страха потерять ваши настройки!

### Настройки

| Опция                      | Описание                                                                                                                                                                                           | Стандарт  | Сборка | Причина изменения                                                                                                                                         |
| --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| autoJump                    | Заставляет игрока прыгать когда встречается блок высотой не выше еденицы                                                                                                                                               | true     | false   | В стандартной игре это больше раздражает чем помогает, многие игроки и так выключают эту опцию                                                                                   |
| snooperEnabled              | Отключает [Snooper](https://minecraft.fandom.com/wiki/Snooper), сервис анали оборудования. Эта настройка была удалена из меню в 1.13, но всё-ещё существует в `options` (и включена по стандарту) по какой-то причине. | true     | false   | Просто на всякий случай, для улучшения приватности. В 1.18+ [Debugify](https://curseforge.com/minecraft/mc-mods/debugify) используется для реального противодействия этому. |
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

| Опция                            | Описание                                                         | Стандарт | Сборка | Причина изменения                                                            |
| --------------------------------- | ------------------------------------------------------------------- | ------- | ------- | ----------------------------------------------------------------------- |
| Vanilla: Save Hotbar Activator    | Saves your hotbar if this key and a number key are held             | c       | none    | This key is more often used for zoom                                    |
| Zoomify/WI Zoom: Zoom             | Zooms the view when the key is held                                 | v       | c       | This key is more often used for zoom                                    |
| Zoomify: GUI                      | Opens the Zoomify mod settings                                      | F8      | none    | Not needed for most players                                             |
| AntiGhost: Reveal ghost blocks    | Asks the server to send blocks around you in order to un-glitch you | g       | none    | Accidental presses and holding can cause issues, use **/ghost** instead |
| Iris: Reload Shaders              | Reloads the applied shaders                                         | r       | none    | Not needed for most players                                             |
| Iris: Shaderpack Selection Screen | Opens the shader selection screen                                   | o       | none    | Not needed for most players                                             |
| Iris: Toggle Shaders              | Disables or enables shaders                                         | k       | none    | Not needed for most players                                             |

The changed mod settings can be found on the repo at [.../yosbr/1.18.2/config](https://github.com/Fabulously-Optimized/fabulously-optimized/tree/main/Packwiz/1.18.2/config).

See also: [Minecraft Wiki: options.txt](https://minecraft.fandom.com/wiki/Options.txt#Java\_Edition) and [issue #30](https://github.com/Fabulously-Optimized/fabulously-optimized/issues/30)

### Fixed bugs

Fabulously Optimized includes some mods that fix vanilla bugs.
[Similar to the mod inclusion policy](principles.md), they must be meaningful to 70%+ users to get enabled (e.g. FPS drops, crashes, platform-specific annoyances...).

| Mojang bug                                            | Description                                                                | Fixed by                                                                  |
| ----------------------------------------------------- | -------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| [MC-26757](https://bugs.mojang.com/browse/MC-26757)   | Large item tooltips can get cut off at the edges of the screen                                                  |[ToolTipFix](https://www.curseforge.com/minecraft/mc-mods/tooltipfix)             |
| [MC-73186](https://bugs.mojang.com/browse/MC-73186)   | Gaps between the faces of item models                                      |[Item Model Fix](https://www.curseforge.com/minecraft/mc-mods/item-model-fix)             |
| [MC-81098](https://bugs.mojang.com/browse/MC-81098)   | Redstone dust updates cause lag (Singleplayer only)                        |[Lithium](https://www.curseforge.com/minecraft/mc-mods/lithium)
| [MC-89146](https://bugs.mojang.com/browse/MC-89146)   | Pistons forget update when being reloaded                                  | [Debugify](https://curseforge.com/minecraft/mc-mods/debugify)             |
| [MC-112730](https://bugs.mojang.com/browse/MC-112730) | Beacon beam and structure block render twice per frame                     | [Debugify](https://curseforge.com/minecraft/mc-mods/debugify)             |
| [MC-121772](https://bugs.mojang.com/browse/MC-121772) | Can't scroll while holding SHIFT on macOS                                  | [Debugify](https://curseforge.com/minecraft/mc-mods/debugify)             |
| [MC-121884](https://bugs.mojang.com/browse/MC-121884)   | Server -> Client custom payload packets can leak resources               |[MemoryLeakFix](https://www.curseforge.com/minecraft/mc-mods/memoryleakfix) |
| [MC-122477](https://bugs.mojang.com/browse/MC-122477) | Linux/GNU: Opening chat sometimes writes 't'                               | [Debugify](https://curseforge.com/minecraft/mc-mods/debugify)             |
| [MC-132488](https://bugs.mojang.com/browse/MC-132488)   | Ticking animated textures is very inefficient                              |[Sodium](https://www.curseforge.com/minecraft/mc-mods/sodium)  |
| [MC-140646](https://bugs.mojang.com/browse/MC-140646) | Text fields don't scroll while selecting text with Shift                   | [Debugify](https://curseforge.com/minecraft/mc-mods/debugify)             |
| [MC-145929](https://bugs.mojang.com/browse/MC-145929) | Actionbar text may be difficult to read without text background enabled    | [Debugify](https://curseforge.com/minecraft/mc-mods/debugify)             |
| [MC-148149](https://bugs.mojang.com/browse/MC-148149) | Linux game crash when opening links                                        | [Debugify](https://curseforge.com/minecraft/mc-mods/debugify)             |
| [MC-162253](https://bugs.mojang.com/browse/MC-162253) | Lag spike when crossing certain chunk borders                              | [Debugify](https://curseforge.com/minecraft/mc-mods/debugify)             |
| [MC-165595](https://bugs.mojang.com/browse/MC-165595) | Guardian beam does not render when over a certain "Time" in level.dat | [Sodium Extra](https://www.curseforge.com/minecraft/mc-mods/sodium-extra) |
| [MC-172550](https://bugs.mojang.com/browse/MC-172550)   | Ghost blocks sometimes appear when insta-mining                                  |[AntiGhost](https://www.curseforge.com/minecraft/mc-mods/antighost)  
| [MC-199467](https://bugs.mojang.com/browse/MC-199467) | Certain entity animations stop after they've existed in world for too long | [Debugify](https://curseforge.com/minecraft/mc-mods/debugify)             |
| [MC-226729](https://bugs.mojang.com/browse/MC-226729)   | Memory leakage problem in native operations                         |[MemoryLeakFix](https://www.curseforge.com/minecraft/mc-mods/memoryleakfix)  |
| [MC-227302](https://bugs.mojang.com/browse/MC-227302)   | Smooth lighting doesn't work properly on the water surface                                |[Sodium](https://www.curseforge.com/minecraft/mc-mods/sodium) |  
| [MC-228976](https://bugs.mojang.com/browse/MC-228976) | Entity collision is run on render thread                                   | [Debugify](https://curseforge.com/minecraft/mc-mods/debugify)             |
| [MC-235035](https://bugs.mojang.com/browse/MC-235035) | Sleeping in a custom dimension with "natural" set to false causes crash    | [Debugify](https://curseforge.com/minecraft/mc-mods/debugify)             |
| [MC-237493](https://bugs.mojang.com/browse/MC-237493) | Telemetry cannot be disabled                                               | [Debugify](https://curseforge.com/minecraft/mc-mods/debugify)   |
| [MC-249059](https://bugs.mojang.com/browse/MC-249059) | Loading terrain screen cannot close before 2 seconds have passed           | [Debugify](https://curseforge.com/minecraft/mc-mods/debugify)             |

If you'd like to enable more bugfixes for your game, see [the fixed bug list for Debugify](https://github.com/W-OVERFLOW/Debugify/blob/1.18/PATCHED.md#unpatched-in-vanilla).

#### Requesting a bugfix

Want to get a bug fixed in Fabulously Optimized? Here's what you'll need to do:

1. Find the actual bug [in Mojang's bug tracker](https://bugs.mojang.com/projects/MC/issues?filter=allopenissues)
2. Request it or look at its status on [Debugify's bug tracker](https://github.com/W-OVERFLOW/Debugify/issues)
3. Once implemented (or confirmed to be) in Debugify, [request an option change in FO](https://github.com/Fabulously-Optimized/fabulously-optimized/issues/new?assignees=\&labels=option\&template=setting-request.yml)
4. Describe the bug, mention the mod that fixes it and why it is important to 70-80% of users
5. If accepted, expect the fix to be enabled in the next version of FO :)

### Configuring mods

The modpack is already configured for the best performance and simplest experience for most users.

If you want to configure something, you'll most likely find it on `Options...` -> `Video Settings...`. If you have a powerful computer or monitor, you may want to disable Vsync there.

For other things like dynamic lights, better grass and zoom:

1. Click `Mods`
2. Read the descriptions of the mods to see what they do
3. If the pencil is blue, you can configure the mod by clicking the config button ![config](https://i.ibb.co/j35cBtn/image.png)
   * If you don't see any pencils, you don't have the Mod Menu Helper resource pack enabled for some reason. Click `Done` -> `Options...` -> `Resource Packs...` -> `⏵` on "Mod Menu Helper.zip" -> `Done` -> go to point 1 of this tutorial

If you need to disable a mod, [see this wiki page](disabling-mods.md).

If you have more questions about the mods, [chat with us on Discord!](https://discord.gg/yxaXtaQqdB)
