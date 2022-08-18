# Language support

You can translate various parts of the pack!

## Translating mods

I support people using Minecraft in their language and would like to promote that in the modpack too. However, this is a _pack of mods_, so if you want to translate the pack, you must translate the mods.

1. [Check out the list of mods](https://github.com/Fabulously-Optimized/fabulously-optimized#included-mods)
2. On every page, find the Issues or Source link at the top
3. Read the readme, wiki and/or issues to see if there is already a translation platform. If yes, go there.
4. If not, go to Code tab and browse the folders in order: `src` -> `main` -> `resources` -> `assets` -> `(mod's name)` -> `lang` -> `en_us.json`
5. Open the file and copy its full text
6. Go back to `lang` folder, click Add file -> Create new file
7. You'll fork the project and have a new file window open. Name the file in the format `locale_code.json`, such as `et_ee.json`. [Locale codes can be found here](https://minecraft.fandom.com/wiki/Language#Languages)
8. Paste the text you copied and start translating the values **on the right**, e.g. in the example below you only replace the _Coolmod Options_ text:
   * `"coolmod.config.title": "Coolmod Options",`
9. Commit the file and create a pull request. If you're lucky, the mod author accepts it
10. If the language has been accepted, wait for the mod author to update their mod on CurseForge
11. Once the mod has been updated on CurseForge, simply wait for the next Fabulously Optimized update to see it :P

### Notable mods to translate

List of mods that contribute the most viewed strings in the modpack, click to get to their English language file/translation platform.

1. [Sodium Extra](https://crowdin.com/project/sodium-extra)
2. [Iris Shaders](https://github.com/IrisShaders/Iris/blob/trunk/src/main/resources/assets/iris/lang/en\_us.json)
3. [Cull Less Leaves](https://github.com/isXander/CullLessLeaves/blob/1.19/src/main/resources/assets/cull-less-leaves/lang/en_us.json) (appears in Video Settings)
4. [Mod Menu](https://crowdin.com/project/mod-menu)
5. [MidnightControls](https://github.com/TeamMidnightDust/MidnightControls/blob/1.19/src/main/resources/assets/midnightcontrols/lang/en_us.json)
6. Fabric API: [resource packs](https://github.com/FabricMC/fabric/blob/1.19.2/fabric-resource-loader-v0/src/main/resources/assets/fabric-resource-loader-v0/lang/en_us.json), [creative tabs](https://github.com/FabricMC/fabric/blob/1.19.2/fabric-item-groups-v0/src/main/resources/assets/fabric/lang/en_us.json)
7. [Zoomify](https://github.com/isXander/Zoomify/blob/1.19/src/main/resources/assets/zoomify/lang/en\_us.json)
8. [LambdaBetterGrass](https://github.com/LambdAurora/LambdaBetterGrass/blob/1.19/src/main/resources/assets/lambdabettergrass/lang/en\_us.json)
9. [LambDynamicLights](https://github.com/LambdAurora/LambDynamicLights/blob/1.19/src/main/resources/assets/lambdynlights/lang/en\_us)
10. [SpruceUI](https://github.com/LambdAurora/SpruceUI/blob/1.19/src/main/resources/assets/spruceui/lang/en\_us.json) (more strings used in LambdaBetterGrass and LambDynamicLights)
11. [Fabric Capes](https://github.com/CaelTheColher/Capes/blob/master/src/main/resources/assets/capes/lang/en\_us.json)
12. [Continuity](https://github.com/PepperCode1/Continuity/blob/main/src/main/resources/assets/continuity/lang/en\_us.json)
13. [CIT Resewn](https://github.com/SHsuperCM/CITResewn/blob/main/src/main/resources/assets/citresewn/lang/en\_us.json)
14. [Colormatic](https://github.com/kvverti/colormatic/blob/master/src/main/resources/assets/colormatic/lang/en\_us.json)
15. [CEM](https://github.com/dorianpb/cem/blob/main/src/main/resources/assets/cem/lang/en_us.json)
16. [Sodium](https://github.com/amnotbananaama/sodium-fabric-translations) (unofficial, but will be included in some way eventually)
17. [Cloth Config](https://crowdin.com/project/cloth-config) (global strings in some settings menus)
18. [Modrinth](https://crowdin.com/project/modrinth) (a mod platform that FO will fully support soon)

## Translating Mod Menu helper

Fabulously Optimized includes a resource pack "Mod Menu Helper" that shortly describes each mod's purpose and available options. By default it is in English, but I am open to accepting language translations, so simply follow this tutorial.

1. Make sure your Fabulously Optimized instance [is fully up to date](https://fabulously-optimized.gitbook.io/modpack/readme/update-instructions).
2. In your Fabulously Optimized instance, go to resource packs menu, click _Open Pack Folder_
3. Extract Mod Menu Helper.zip to a folder, then go inside it -> assets -> minecraft -> lang
4. Open en\_us.json and copy its full text
5. Create a new file in the format `locale_code.json`, such as `et_ee.json`. [Locale codes can be found here](https://minecraft.gamepedia.com/Language#Available\_languages)
6. Paste the text you copied and start translating the values **on the right**, e.g. in the example below you only replace the _Coolmod Options_ text:
   * `"coolmod.config.title": "Coolmod Options",`
7. Keep the text short and simple, you can add or remove words to make it fit better.
   * Do not change the color format (paragraph sign §), pencil emoji (🖉) or newlines (\n)
8. Test in-game by going into `Options...` -> `Resource Packs...`, deactivating "Mod Menu Helper.zip" and activating "Mod Menu Helper" instead, then looking at `Mods` in your language.
   * The lines **must be** fully visible in a maximised Full HD (1920×1080) screen using the default font. If your language uses the Unicode font by default, consider that instead.
   * Of course you can rephrase the sentences to make them more understandable and/or shorter for your language. On the second row you do not have to list all options that English has, just list as many as you can fit.
   * As you test, you can use F3+J to reload languages.
9. If you're satisfied with your translation, copy the full text.
10. [Click here](https://github.com/Fabulously-Optimized/fabulously-optimized/blob/main/Mod%20Menu%20Helper/assets/modmenu/lang/), then Add file -> Create new file
11. You'll fork the project and have a new file window open. Name the file the same way you did previously and paste the translation.
12. Commit the file and create a pull request. If your translation is properly formatted and fits into the rows, I will accept it
13. Wait for the next version for the modpack to see it in-game :P

## Translating the description

You can now translate the modpack's description! It will be posted as a spoiler below the English text.

1. Go to the [descriptions folder](https://github.com/Fabulously-Optimized/fabulously-optimized/tree/main/Description)
2. Click on `en_US.md`. Read it, see how it looks, then click `Raw` and copy the text.
3. Go back, click `Add file` -> `Create new file`
4. Paste and translate every sentence.
   * If your language has a local link (video, wiki etc), use that in the format `[text](link)`, otherwise use the English one by keeping the number as-is.
   * The multiplayer warning should be taken directly from the game. If you don't know what it says in your language, just write a placeholder and I'll fill it by myself.
5. [Create a new pull request](https://github.com/Fabulously-Optimized/fabulously-optimized/compare).
6. I'll review your text and if everything seems okay, will accept and publish it!
7. You can edit it at any time by repeating this process.
   * Make sure you click `🔄Fetch upstream` -> `Fetch and merge` to get the latest changes from the wiki.

## Translating the wiki

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
 
