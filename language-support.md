# Language support

You can translate various parts of the pack!

## Mods

I support people using Minecraft in their language and would like to promote that in the modpack too. However, this is a _pack of mods_, so if you want to translate the pack, you must translate the mods too.

1. [Check out the list of mods](https://github.com/Fabulously-Optimized/fabulously-optimized/blob/main/INCLUDED-MODS.md#smooth) and click the name of the mod you want to translate
2. On every page, find the Issues or Source link at the top
3. Read the readme, wiki and/or issues to see if there is already a translation platform. If yes, go there.
4. If not, go to Code tab and browse the folders in order: `src` → `main` → `resources` → `assets` → `(mod's name)` → `lang` → `en_us.json`
5. Open the file and copy its full text
6. Go back to `lang` folder, click Add file → Create new file
7. You'll fork the project and have a new file window open. Name the file in the format `locale_code.json`, such as `et_ee.json`. [Locale codes can be found here](https://minecraft.fandom.com/wiki/Language#Languages)
8. Paste the text you copied and start translating the values **on the right**, e.g. in the example below you only replace the _Coolmod Options_ text:
   * `"coolmod.config.title": "Coolmod Options",`
9. Commit the file and create a pull request. If you're lucky, the mod author accepts it
10. If the language has been accepted, wait for the mod author to update their mod on CurseForge
11. Once the mod has been updated on CurseForge, simply wait for the next Fabulously Optimized update to see it :P

### Notable mods to translate

List of mods that contribute the most viewed strings in the modpack, click to get to their English language file/translation platform.

1. [Sodium Extra](https://crowdin.com/project/sodium-extra)
2. [Iris Shaders](https://github.com/IrisShaders/Iris/blob/trunk/src/main/resources/assets/iris/lang/en_us.json)
3. [MoreCulling](https://github.com/fxmorin/MoreCulling/blob/master/src/main/resources/assets/moreculling/lang/en_us.json) (appears in Video Settings)
4. [Mod Menu](https://crowdin.com/project/mod-menu)
5. [MidnightControls](https://github.com/TeamMidnightDust/MidnightControls/blob/1.19/src/main/resources/assets/midnightcontrols/lang/en_us.json)
6. Fabric API: [resource packs](https://github.com/FabricMC/fabric/blob/1.19.3/fabric-resource-loader-v0/src/main/resources/assets/fabric-resource-loader-v0/lang/en_us.json), [creative tabs](https://github.com/FabricMC/fabric/blob/1.19.3/fabric-item-groups-v0/src/main/resources/assets/fabric/lang/en_us.json)
7. [Zoomify](https://github.com/isXander/Zoomify/blob/1.19/src/main/resources/assets/zoomify/lang/en_us.json)
8. [Fabric Capes](https://github.com/CaelTheColher/Capes/blob/master/src/main/resources/assets/capes/lang/en_us.json)
9. [Continuity](https://github.com/PepperCode1/Continuity/blob/main/src/main/resources/assets/continuity/lang/en_us.json)
10. [CIT Resewn](https://github.com/SHsuperCM/CITResewn/blob/main/src/main/resources/assets/citresewn/lang/en_us.json)

## Mod Menu Helper

Bundled resource pack "Mod Menu Helper" shortly describes each mod's purpose and available options.

1. Make sure your Fabulously Optimized instance [is fully up to date](update-instructions.md).
2. In your Fabulously Optimized instance, go to resource packs menu, click _Open Pack Folder_
3. Extract Mod Menu Helper.zip to a folder, then go inside it → assets → fo → lang
4. Open en\_us.json and copy its full text
   * Looks ugly? That's because it's minified JSON. [You can copy a prettier version from here](https://raw.githubusercontent.com/Fabulously-Optimized/fabulously-optimized/main/Resource%20Packs/Mod%20Menu%20Helper/assets/fo/lang/en_us.json) and translate that instead (they are identical).
5. Create a new file in the format `locale_code.json`, such as `et_ee.json`. [Locale codes can be found here](https://minecraft.gamepedia.com/Language#Available\_languages)
6. Paste the text you copied and start translating the values **on the right**, e.g. in the example below you only replace the _Coolmod Options_ text:
   * `"coolmod.config.title": "Coolmod Options",`
7. Keep the text short and simple, you can add or remove words to make it fit better.
   * Do not change the color format (paragraph sign §), pencil emoji (🖉) or newlines (\n)
8. Test in-game by going into `Options...` → `Resource Packs...`, deactivating "Mod Menu Helper.zip" and activating "Mod Menu Helper" instead, then looking at `Mods` in your language.
   * The lines **must be** fully visible in a maximised Full HD (1920×1080) screen using the default font. If your language uses the Unicode font by default, consider that instead.
   * Of course you can rephrase the sentences to make them more understandable and/or shorter for your language. On the second row you do not have to list all options that English has, just list as many as you can fit.
   * As you test, you can use F3+J to reload languages.
9. If you're satisfied with your translation, copy the full text.
10. [Click here](https://github.com/Fabulously-Optimized/fabulously-optimized/blob/main/Resource%20Packs/Mod%20Menu%20Helper/assets/fo/lang/), then `Add file` → `Create new file`
11. You'll fork the project and have a new file window open. Name the file the same way you did previously and paste the translation.
12. Commit the file and create a pull request (you'll see the button for it). If your translation is properly formatted and fits into the rows, I will accept it.
13. Wait for the next version for the modpack to see it in-game :P

**P.S. If you didn't follow this tutorial and instead just made a PR on GitHub, [there is now an online tool](https://fabulously-optimized.github.io/Mod-Menu-Helper-Size-Checker/) that can help you approximate whether the sentences will fit.**

## Chat Reporting Helper

Bundled resource pack "Chat Reporting Helper" simplifies some vanilla and No Chat Reports strings to make chat reporting easier to understand.

1. Go to [Chat Reporting Helper's language folder](https://github.com/Fabulously-Optimized/fabulously-optimized/tree/main/Resource%20Packs/Chat%20Reporting%20Helper/assets/fo/lang)
2. Click `Add file` -> `Create new file` and name it `locale_code.json`, such as `et_ee.json`. [Locale codes can be found here](https://minecraft.gamepedia.com/Language#Available\_languages)
3. Open [the Chat Reporting Helper's file](https://github.com/Fabulously-Optimized/fabulously-optimized/blob/main/Resource%20Packs/Chat%20Reporting%20Helper/assets/fo/lang/en_us.json) in a new tab
4. Open [vanilla language files](https://github.com/InventivetalentDev/minecraft-assets/tree/1.19.3/assets/minecraft/lang) in a new tab and click on your language file
5. Using the two files you have opened, translate the strings
   * Use vanilla strings for reference where relevant, but mostly follow the Chat Reporting Helper ones
   * Unlike with Mod Menu Helper, the strings are less constrained in width, so you don't necessarily have to test them in-game.
6. When done, commit the changes.
7. Create a pull request (you'll see the button for it). If your translation is properly formatted and faithful, I will accept it
8. Wait for the next version for the modpack to see it in-game :P

## Listing description

Listing description translations are posted as a spoiler tag below the English text.

1. Go to the [descriptions folder](https://github.com/Fabulously-Optimized/fabulously-optimized/tree/main/Description)
2. Click on `en_US.md`. Read it, see how it looks, then click `Raw` and copy the text.
3. Go back, click `Add file` → `Create new file`
4. Paste and translate every sentence.
   * If your language varies by region (like English, Spanish and others do), you can include the country in parentheses. Otherwise feel free to skip it.
   * If your language has a localized review video, use that. Otherwise use the English one.
5. [Create a new pull request](https://github.com/Fabulously-Optimized/fabulously-optimized/compare).
6. I'll review your text and if everything seems okay, will accept and publish it!
7. You can edit it at any time by repeating this process.
   * Make sure you click `🔄Fetch upstream` → `Fetch and merge` to get the latest changes from the wiki.

## Wiki

The wiki is no longer accepting translations because it required translating too many pages and translations got outdated very fast.
