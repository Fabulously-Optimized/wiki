I support people using Minecraft in their language and would like to promote that in the modpack too. However, this is a _pack of mods_, so if you want to translate the pack, you must translate the mods.

### Translating Mod Menu helper

Fabulously Optimized includes a resource pack "Mod Menu Helper" that shortly describes each mod's purpose and available options. By default it is in English, but I am open to accepting language translations, so simply follow this tutorial.

1. In your Fabulously Optimized instance, go to resource packs menu, click _Open Pack Folder_
2. Extract Mod Menu Helper.zip to a folder, then go inside it -> assets -> minecraft -> lang
3. Open en_us.json and copy its full text
4. Create a new file in the format `locale_code.json`, such as `et_ee.json`. [Locale codes can be found here](https://minecraft.gamepedia.com/Language#Available_languages)
5. Paste the text you copied and start translating the values **on the right**, e.g. in the example below you only replace the _Coolmod Options_ text:

```
"coolmod.config.title": "Coolmod Options",
```

6. Keep the text short and simple, you can add or remove words to make it fit better. 
   * Do not change the color format (paragraph sign), pencil emoji or newlines (\n)
7. Test in-game by going into `Options...` -> `Resource Packs...`, deactivating "Mod Menu Helper.zip" and activating "Mod Menu Helper" instead, then looking at `Mods` in your language.
   * The lines **must be** fully visible in a maximised Full HD (1920×1080) screen using the default font. If your language uses the Unicode font by default, consider that instead.
   * As you test, you can use F3+J to reload languages.
8. If you're satisfied with your translation, copy the full text.
9. [Click here](https://github.com/Fabulously-Optimized/fabulously-optimized/blob/main/Mod%20Menu%20Helper/assets/modmenu/lang/), then Add file -> Create new file
10. You'll fork the project and have a new file window open. Name the file the same way you did previously and paste the translation.
11. Commit the file and create a pull request. If your translation is properly formatted and fits into the rows, I will accept it
12. Wait for the next version for the modpack to see it in-game :P

### Translating mods

1. [Check out the list of mods](https://github.com/Madis0/fabulously-optimized#included-mods)
2. On every page, find the Issues or Source link at the top
3. Read the readme, wiki and/or issues to see if there is already a translation platform. If yes, go there.
4. If not, go to Code tab and browse the folders in order:
`src` -> `main` -> `resources` -> `assets` -> `(mod's name)` -> `lang` -> `en_us.json`
5. Open the file and copy its full text
6. Go back to `lang` folder, click Add file -> Create new file
7. You'll fork the project and have a new file window open. Name the file in the format `locale_code.json`, such as `et_ee.json`. [Locale codes can be found here](https://minecraft.gamepedia.com/Language#Available_languages)
8. Paste the text you copied and start translating the values **on the right**, e.g. in the example below you only replace the _Coolmod Options_ text:

```
"coolmod.config.title": "Coolmod Options",
```

9. Commit the file and create a pull request. If you're lucky, the mod author accepts it
10. If the language has been accepted, wait for the mod author to update their mod on Curseforge
11. Once the mod has been updated on Curseforge, simply wait for the next Fabulously Optimized update to see it :P

### Notable mods to translate

List of mods that contribute the most viewed strings in the modpack, click to get to their English language file/translation platform.

1. [Sodium Extra](https://github.com/FlashyReese/sodium-extra-fabric/blob/1.17.x/dev/src/main/resources/assets/sodium-extra/lang/en_us.json)
1. ~~[Sodium](https://github.com/CaffeineMC/sodium-fabric/issues/44)~~ (localization currently on hiatus)
1. [Iris Shaders](https://github.com/IrisShaders/Iris/blob/trunk/src/main/resources/assets/iris/lang/en_us.json)
1. [Mod Menu](https://hosted.weblate.org/engage/fabric-modmenu/)
1. [LambdaBetterGrass](https://github.com/LambdAurora/LambdaBetterGrass/blob/1.18/src/main/resources/assets/lambdabettergrass/lang/en_us.json)
1. [LambDynamicLights](https://github.com/LambdAurora/LambDynamicLights/blob/1.18/src/main/resources/assets/lambdynlights/lang/en_us.json)
1. [Zoomify](https://github.com/isXander/Zoomify/blob/1.18/src/main/resources/assets/zoomify/lang/en_us.json)
1. [SpruceUI](https://github.com/LambdAurora/SpruceUI/blob/1.18/src/main/resources/assets/spruceui/lang/en_us.json) (more strings used in LambdaBetterGrass and LambDynamicLights)
1. [Fabric Capes](https://github.com/CaelTheColher/Capes/blob/master/src/main/resources/assets/capes/lang/en_us.json)
1. [Continuity](https://github.com/PepperCode1/Continuity/blob/main/src/main/resources/assets/continuity/lang/en_us.json)
1. [CIT Resewn](https://github.com/SHsuperCM/CITResewn/blob/main/src/main/resources/assets/citresewn/lang/en_us.json)
1. [Colormatic](https://github.com/kvverti/colormatic/blob/master/src/main/resources/assets/colormatic/lang/en_us.json)
1. [CEM](https://github.com/dorianpb/cem/blob/1.18/src/main/resources/assets/cem/lang/en_us.json)
1. [Not Enough Crashes](https://github.com/natanfudge/Not-Enough-Crashes/blob/1.18/common/src/main/resources/assets/notenoughcrashes/lang/en_us.json)
1. [Cloth Config](https://crowdin.com/project/cloth-config) (global strings in some settings menus)
