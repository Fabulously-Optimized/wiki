# Language support

You can translate the mods themselves and the modpack-specific content. All modpack-specific translations are licensed under [CC0](https://www.tldrlegal.com/license/creative-commons-cc0-1-0-universal), meaning they can be freely copied, modified, republished and so on.

## Mods

I support people using Minecraft in their language and would like to promote that in the modpack too. However, this is a _pack of mods_, so if you want to translate the entire pack, you should translate its mods as well.

1. [Check out the list of mods](https://github.com/Fabulously-Optimized/fabulously-optimized/blob/main/INCLUDED-MODS.md#smooth) and click the name of the mod you want to translate
2. On every page, find the Issues or Source link at the top
3. Read the readme, wiki and/or issues to see if there is already a translation platform. If yes, go there.
4. If not, go to Code tab and browse the folders in order: `src` → `main` → `resources` → `assets` → `(mod's name)` → `lang` → `en_us.json`
5. Open the file and copy its full text
6. Go back to `lang` folder, click Add file → Create new file
7. You'll fork the project and have a new file window open. Name the file in the format `locale_code.json`, such as `et_ee.json`. [Locale codes can be found here](https://minecraft.wiki/w/Language#Languages)
8. Paste the text you copied and start translating the values **on the right**, e.g. in the example below you only replace the _Coolmod Options_ text:
   * `"coolmod.config.title": "Coolmod Options",`
9. Commit the file and create a pull request. If you're lucky, the mod author accepts it
10. If the language has been accepted, wait for the mod author to update their mod on CurseForge
11. Once the mod has been updated on CurseForge, simply wait for the next Fabulously Optimized update to see it :P

### Notable mods to translate

List of mods that contribute the most viewed phrases in the modpack, click to get to their English language file/translation platform.

1. [Sodium](https://crowdin.com/project/sodium-fabric) (unofficial, but bundled in FO)
2. [Sodium Extra](https://crowdin.com/project/sodium-extra)
3. [Iris Shaders](https://github.com/IrisShaders/Iris/blob/1.20-new/src/main/resources/assets/iris/lang/en_us.json)
4. [MoreCulling](https://github.com/fxmorin/MoreCulling/blob/master/src/main/resources/assets/moreculling/lang/en_us.json) (appears in Video Settings)
5. [Mod Menu](https://crowdin.com/project/mod-menu)
6. [MidnightControls](https://github.com/TeamMidnightDust/MidnightControls/blob/1.20.1/src/main/resources/assets/midnightcontrols/lang/en_us.json)
7. Fabric API: [resource packs](https://github.com/FabricMC/fabric/blob/1.20.2/fabric-resource-loader-v0/src/main/resources/assets/fabric-resource-loader-v0/lang/en_us.json), [creative tabs](https://github.com/FabricMC/fabric/blob/1.20.2/fabric-item-group-api-v1/src/main/resources/assets/fabric/lang/en_us.json)
8. [Zoomify](https://github.com/isXander/Zoomify/blob/1.20/src/main/resources/assets/zoomify/lang/en_us.json)
9. [Fabric Capes](https://github.com/CaelTheColher/Capes/blob/architectury/common/src/main/resources/assets/capes/lang/en_us.json)
10. [Continuity](https://github.com/PepperCode1/Continuity/blob/1.19/dev/src/main/resources/assets/continuity/lang/en_us.json)
11. [CIT Resewn](https://github.com/SHsuperCM/CITResewn/blob/main/src/main/resources/assets/citresewn/lang/en_us.json)

## Modpack

Fabulously Optimized [is translated on Crowdin](https://crowdin.com/project/fabulously-optimized). Here are the steps:

1. Join [the Fabulously Optimized project](https://crowdin.com/project/fabulously-optimized)
2. Start translating the file you prefer. The files are listed in the order of priority.
   * You can vote for existing suggestions with ➕ and ➖ buttons
   * In the comments you can discuss the specific phrase, ask for more info, report wrong translations etc.
   * File-specific tips and requirements [are listed below](#mod-menu-helper)
3. [Join our Discord](https://fabulously-optimized.github.io/discord) for a yellow rank and a possibility to become a proofreader in your language.
   * Yellow rank requirement is translating any file to 100%; it also gives you access to some hidden channels ;)
4. As a proofreader, read over every string, [test MMH in-game](#testing-tutorial) and approve ✔️ everything that looks correct. **Any file must be 100% approved before it gets pushed to FO.**   
   * For example, if you fully translate two files but fully approve one, then only the fully approved file will be published at the moment.
6. Wait for the next release of FO to see your translations live!
7. You'll get an email and/or Discord notification when there are new phrases to translate. Then just repeat from step 3!

### Mod Menu Helper

Bundled resource pack "Mod Menu Helper" shortly describes each mod's purpose and available options.

* The phrases have very specific length requirements, so you must test them after translating [with the instructions below](#testing-tutorial).
   * The lines **must be** fully visible in a maximised Full HD (1920×1080) screen using the default font. If your language uses the Unicode font by default, consider that instead.
   * [There is an online tool](https://fabulously-optimized.github.io/Mod-Menu-Helper-Size-Checker/) that helps you assume how long the string might be, but it is not 100% accurate.
   * If you don't have a Full HD display, you can also emulate it in-game: `Options...` → `Video Settings...` → `Fullscreen Resolution: 1920x1080@60 (24 bit)` → `Fullscreen: 🔲` → `Apply` → `Done`
     * If you get any issues, press `Shift` + `P` within the video settings, to get the vanilla video settings and revert fullscreen options there.
     * The numbers after `@` may vary. 
* Feel free to rephrase the sentences to make them more understandable and/or shorter for your language. In the options row, list as many options as you can fit.
* Keep paragraph sign (§), tools emoji (⚒️), arrows emoji (🔀) and newlines as they are on the original.

#### Testing tutorial

1. Select your language on Crowdin
2. Select `Mod Menu Helper`
3. Click `≡` on the left, then `Download`. You'll get a file in the format _language_code.json_.
   * Is the button grayed out? Make sure you're browsing "Mod Menu Helper", not "all strings".
4. Run Fabulously Optimized
5. Go to `Options...` → `Resource Packs...` → `Open Pack Folder`
6. Open `Mod Menu Helper.zip` → `assets` → `fo` → `lang`
   * On macOS, opening the ZIP will create a new folder, so open that one.
7. Drag the file you downloaded into the archive
8. Go back to the game, `Done` → `Done`
   * On macOS, activate the `Mod Menu Helper` (without .zip) resource pack first.
9. Play any world or server
10. Hold down `F3` and press `T`
11. Press `Esc` → `Mods`. Look around and make sure everything fits.
    * Use maximized window or fullscreen, Full HD (1920×1080) screen, GUI scale 3, default font.
12. Press `Back` → `Options...` → `Resource Packs...`. Look around and make sure everything fits. 
13. If not everything fits yet, change the translation on Crowdin and repeat from step 3.

### Chat Reporting Helper

Bundled resource pack "Chat Reporting Helper" simplifies some vanilla and No Chat Reports phrases to make chat reporting availability and interactions easier to understand.

* In-game testing is needed only for the resource pack description - [use MMH's instructions](#testing-tutorial).
* Some phrases refer to similar vanilla or No Chat Reports' phrases. Read the phrase descriptions for instructions.
* Untranslated languages use the original phrases instead of Chat Reporting Helper's, so your translation helps improve the consistency by a lot!
* For a more complete translation, you might also want to [translate No Chat Reports](https://github.com/Aizistral-Studios/No-Chat-Reports/blob/1.20-Unified/src/main/resources/assets/nochatreports/lang/en_us.json).

### Fast Better Grass

Bundled resource pack "Fast Better Grass" imitates the OptiFine's Better Grass' "fast mode". 

* The resource pack description is translated within [Mod Menu Helper](#mod-menu-helper), to keep the original pack small and simple.

### Sodium

Unofficial resource pack that adds translations to Sodium. Managed by the creator of Fabulously Optimized and the creator of Sodium Extra, but is an independent project.

* [Translated on Crowdin](https://crowdin.com/project/sodium-fabric)
* Translations are published every Saturday, so any FO version to come after that will get it.
* Translations do not require approval to be published, however proofreading would still be preferred to ensure quality.
* You are more likely to be accepted as a proofreader if you have previous translation work on FO or other Minecraft-related projects.

### Listing description

Listing description translations are posted as a spoiler tag below the English text.

* Sometimes the tags get messed up on import. Please ensure they are `<0>`text`</0>`, `<1>`text`</1>` or similar to the original, _not_ `<a href=...>`text`</0>`.
* "English" must be translated as the name of your language, in your language. If relevant, add the region in parentheses.
* If your language has a localized review video, use that in video URL and thumbnail URL. Otherwise just keep the English one.
   * The video must not show launchers and installation methods that don't match the wiki at the time of publishing.
* Crowdin supports "translation preview", which shows the description as it will appear on the listing. Look for the eye icon 👁️.
* Listing translations are currently less prioritized and will be published to listings less often. Thank you for your patience.

### Wiki

The wiki is not accepting translations because there are too many pages to translate and the translations get outdated very fast.
