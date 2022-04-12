# Language support

I support people using Minecraft in their language and would like to promote that in the modpack too. However, this is a _pack of mods_, so if you want to translate the pack, you must translate the mods.

### Translating Mod Menu helper

Fabulously Optimized includes a resource pack "Mod Menu Helper" that shortly describes each mod's purpose and available options. By default it is in English, but I am open to accepting language translations, so simply follow this tutorial.

1. In your Fabulously Optimized instance, go to resource packs menu, click _Open Pack Folder_
2. Extract Mod Menu Helper.zip to a folder, then go inside it -> assets -> minecraft -> lang
3. Open en\_us.json and copy its full text
4. Create a new file in the format `locale_code.json`, such as `et_ee.json`. [Locale codes can be found here](https://minecraft.gamepedia.com/Language#Available\_languages)
5. Paste the text you copied and start translating the values **on the right**, e.g. in the example below you only replace the _Coolmod Options_ text:

```
"coolmod.config.title": "Coolmod Options",
```

1. Keep the text short and simple, you can add or remove words to make it fit better.
   * Do not change the color format (paragraph sign §), pencil emoji (🖉) or newlines (\n)
2. Test in-game by going into `Options...` -> `Resource Packs...`, deactivating "Mod Menu Helper.zip" and activating "Mod Menu Helper" instead, then looking at `Mods` in your language.
   * The lines **must be** fully visible in a maximised Full HD (1920×1080) screen using the default font. If your language uses the Unicode font by default, consider that instead.
   * As you test, you can use F3+J to reload languages.
3. If you're satisfied with your translation, copy the full text.
4. [Click here](https://github.com/Fabulously-Optimized/fabulously-optimized/blob/main/Mod%20Menu%20Helper/assets/modmenu/lang/), then Add file -> Create new file
5. You'll fork the project and have a new file window open. Name the file the same way you did previously and paste the translation.
6. Commit the file and create a pull request. If your translation is properly formatted and fits into the rows, I will accept it
7. Wait for the next version for the modpack to see it in-game :P

### Translating mods

1. [Check out the list of mods](https://github.com/Madis0/fabulously-optimized#included-mods)
2. On every page, find the Issues or Source link at the top
3. Read the readme, wiki and/or issues to see if there is already a translation platform. If yes, go there.
4. If not, go to Code tab and browse the folders in order: `src` -> `main` -> `resources` -> `assets` -> `(mod's name)` -> `lang` -> `en_us.json`
5. Open the file and copy its full text
6. Go back to `lang` folder, click Add file -> Create new file
7. You'll fork the project and have a new file window open. Name the file in the format `locale_code.json`, such as `et_ee.json`. [Locale codes can be found here](https://minecraft.fandom.com/wiki/Language#Languages)
8. Paste the text you copied and start translating the values **on the right**, e.g. in the example below you only replace the _Coolmod Options_ text:

```
"coolmod.config.title": "Coolmod Options",
```

1. Commit the file and create a pull request. If you're lucky, the mod author accepts it
2. If the language has been accepted, wait for the mod author to update their mod on Curseforge
3. Once the mod has been updated on Curseforge, simply wait for the next Fabulously Optimized update to see it :P

#### Notable mods to translate

List of mods that contribute the most viewed strings in the modpack, click to get to their English language file/translation platform.

1. [Sodium Extra](https://github.com/FlashyReese/sodium-extra-fabric/blob/1.17.x/dev/src/main/resources/assets/sodium-extra/lang/en\_us.json)
2. [~~Sodium~~](https://github.com/CaffeineMC/sodium-fabric/issues/44) (localization currently on hiatus)
3. [Iris Shaders](https://github.com/IrisShaders/Iris/blob/trunk/src/main/resources/assets/iris/lang/en\_us.json)
4. [Mod Menu](https://hosted.weblate.org/engage/fabric-modmenu/)
5. [LambdaBetterGrass](https://github.com/LambdAurora/LambdaBetterGrass/blob/1.18/src/main/resources/assets/lambdabettergrass/lang/en\_us.json)
6. [LambDynamicLights](https://github.com/LambdAurora/LambDynamicLights/blob/1.18/src/main/resources/assets/lambdynlights/lang/en\_us.json)
7. [Zoomify](https://github.com/isXander/Zoomify/blob/1.18/src/main/resources/assets/zoomify/lang/en\_us.json)
8. [SpruceUI](https://github.com/LambdAurora/SpruceUI/blob/1.18/src/main/resources/assets/spruceui/lang/en\_us.json) (more strings used in LambdaBetterGrass and LambDynamicLights)
9. [Fabric Capes](https://github.com/CaelTheColher/Capes/blob/master/src/main/resources/assets/capes/lang/en\_us.json)
10. [Continuity](https://github.com/PepperCode1/Continuity/blob/main/src/main/resources/assets/continuity/lang/en\_us.json)
11. [CIT Resewn](https://github.com/SHsuperCM/CITResewn/blob/main/src/main/resources/assets/citresewn/lang/en\_us.json)
12. [Colormatic](https://github.com/kvverti/colormatic/blob/master/src/main/resources/assets/colormatic/lang/en\_us.json)
13. [CEM](https://github.com/dorianpb/cem/blob/1.18/src/main/resources/assets/cem/lang/en\_us.json)
14. [Not Enough Crashes](https://github.com/natanfudge/Not-Enough-Crashes/blob/1.18/common/src/main/resources/assets/notenoughcrashes/lang/en\_us.json)
15. [Cloth Config](https://crowdin.com/project/cloth-config) (global strings in some settings menus)

### Translating the wiki

You can also translate this wiki. It is up to you, whether you want to do a single overview page or translate multiple pages into your language.

1. [Go to wiki repo](https://github.com/Fabulously-Optimized/wiki) and hit `Fork`
2. Click `Add file` -> `Create new file`
   * If you want to do a single page, name the file [locale\_code](https://minecraft.fandom.com/wiki/Language#Languages).md, e.g. `es_es.md`
   * If you want to do a set of pages, name the first file [locale\_code](https://minecraft.fandom.com/wiki/Language#Languages)/readme.md, e.g. `es_es/readme.md`
     * Other pages will then be in that language code folder. You may keep the file names in your language, but please try to keep it ASCII (no non-English characters).
3. Fill the page(s) with content and click `Commit new file`
4. [Create a new pull request](https://github.com/Fabulously-Optimized/wiki/compare).
5. I'll review your page and if everything seems okay, will accept it!
6. You can add contents to your pages at any time by repeating this process.
   * Make sure you click `🔄Fetch upstream` -> `Fetch and merge` to get the latest changes from the wiki.
