# Инструкции по установке

**Предпочитаете видеоинструкции вместо текста? ** [**Нажмите здесь!**](https://github.com/Fabulously-Optimized/fabulously-optimized#reviews)

### [Лаунчер CurseForge](https://download.curseforge.com)

1. Перейдите в [Files](https://www.curseforge.com/minecraft/modpacks/fabulously-optimized/files)
2. Нажмите `Install` на последней версии в CurseForge.
3. Жмите Accept в выпавшем окне (если появится), загрузка должна начаться.

Или если лаунчер уже запущен:

1. Выберите _Minecraft_ из сетки или на боковой панели.
2. Найдите "Fabulously Optimized".
3. Нажмите `Install`

### [MultiMC](https://multimc.org)

1.17 требует Java 16+, 1.18 требует Java 17+. [Get Java](https://www.oracle.com/java/technologies/downloads/)

1. Перейдите в [Files](https://www.curseforge.com/minecraft/modpacks/fabulously-optimized/files)
2. Нажмите `Download` на последней **MultiMC версии**.
   * Не видите MultiMC версию? Нажмите на название нужной вам CurseForge версии и прокрутите вниз, там вы найдете вариант для MultiMC.
      * Или поищите его в боковой панели, в разделе "server packs".
   * Если вы не видите никаких модов в zip-архиве или видите только один, вы скачали не ту версию.
3. Перетащите ZIP-архив в окно MultiMC.

### [MultiMC](https://multimc.org) (автообновление)

1.17 требует Java 16+, 1.18 требует Java 17+. [Get Java](https://www.oracle.com/java/technologies/downloads/)

1. Зайдите в [readme](https://github.com/Fabulously-Optimized/fabulously-optimized#downloads), нажмите "Alternative Downloads".
2. Нажмите на номер нужной вам версии в разделе MultiMC (auto-update).
3. Перетащите ZIP-архив в окно MultiMC
4. Если вас попросят загрузить определенный jar, это означает, что нам не разрешено его включать в сборку, и вы должны добавить его вручную:
   1. Скопируйте его url в свой браузер
   2. Нажмите `Cancel Launch`
   3. Нажмите `Download` на моде
   4. В MultiMC щелкните правой кнопкой мыши на сборке -> View Mods
   5. Перетащите загруженный мод в список модов
   6. Нажмите `Launch`

### [GDLauncher](https://gdevs.io)

**Пожалуйста, убедитесь, что ваш GDLauncher нужной версии (v1.1.14 или более поздней версии - см. настройки) перед установкой FO. [Самый простой способ сделать это - скачать заново](https://gdevs.io/#downloadContainer) (нет необходимости предварительно удалять его).**.

1. Нажмите ➕ в левом нижнем углу
2. Выберите вкладку `CurseForge`
3. Найдите "Fabulously Optimized".
4. Нажмите `Download Latest`.
5. Нажмите ➡️ в правом нижнем углу.

### [Minecraft Launcher](https://www.minecraft.net/en-us/download) (Ванилла)

Для macOS или Linux [вам нужна Java](https://www.oracle.com/java/technologies/downloads/), чтобы запустить установщик Fabric.

1. Скачайте и установите [Fabric Loader](https://fabricmc.net/use/) **версию 0.14.8**.
   * Более старые версии сборки - 1.12.3 и 2.7.3 требуют Fabric Loader 0.13.3.
2. Откройте Minecraft Launcher, нажмите `Installations` и затем нажмите 📂 в установке Fabric.
3. Перейдите в [Files](https://www.curseforge.com/minecraft/modpacks/fabulously-optimized/files) на CurseForge.
4. Нажмите `Download` на последней **MultiMC версии** сборки.
   * Не видите MultiMC версию? Нажмите на название нужной вам CurseForge версии и прокрутите вниз, там вы найдете MultiMC вариант.
      * Или поищите его в боковой панели, в разделе "server packs".
   * Если вы не видите никаких модов в zip-архиве или видите только один, вы скачали не ту версию.
5. Откройте zip-файл, перейдите к _Fabulously Optimized x.x.x_ > _.minecraft_.
6. Скопируйте **все папки** из папки .minecraft в zip-архиве в свою папку .minecraft; если потребуется - замените файлы.
7. Если вам также нужны [стандартные настройки FO](changed-options.md), удалите `options.txt` (ваши ванильные настройки будут сброшены).
8. Запустите профиль Fabric
9. Если вы видите надпись "Fabulously Optimized" в правом нижнем углу, все готово!

Простой установщик для ванильного launcher [скоро появится](https://github.com/Fabulously-Optimized/fabulously-optimized/issues/110)!

### Modrinth

[FO официльно есть на Modrinth.](https://modrinth.com/modpack/fabulously-optimized) Однако, в настоящее время он является экспериментальным и пока нет официального лаунчера, поэтому никаких инструкций или поддержки не предоставляется.

Тем временем вы можете `♡ Подписаться` на проект, чтобы получать уведомления об обновлениях 🙂

### Другие лаунчеры

Технически вы можете установить его в _некоторые_ другие лаунчеры, поддерживающие модпаки с CurseForge, или в _любой_ лаунчер, следуя ванильным инструкциям. Однако мы не оказываем никакой поддержки для подобных лаунчеров.

### Серверы

Поддерживается любой сервер, установка или изменения не требуются. Смотрите [установка сервера](server-setup.md) для получения дополнительной информации.

### Quilt

Были вопросы о том, можно ли установить Fabulously Optimized с [Quilt](https://quiltmc.org). Ответ: возможно, пока моды Fabric все еще поддерживаются в нем, но мы не предоставляем никакой поддержки для этого. [(Однако, вы можете спросить в Дискорде Quilt.)](https://discord.quiltmc.org/).

Если возникнет необходимость, Fabulously Optimized переедет в Quilt, и тогда он будет полностью поддерживаться. Подробнее читайте в [issue #257](https://github.com/Fabulously