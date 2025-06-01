---
hidden: true
icon: language
---

# Translate

In accordance to the [Accessibility principle](../#accessibility), one of FO's objectives is making it accessible to everyone, regardless of their language. This is why we support and welcome translations of FO and of its mods.

## Mods

1. Check out the [list of mods in FO](../../info/mods/). The most important mods are:
   * [Sodium](translate.md#sodium)
   * [Sodium Extra](https://crowdin.com/project/sodium-extra)
   * [Mod Menu](https://crowdin.com/project/mod-menu)
   * [Fabric API and Installer](https://crowdin.com/project/fabricmc)
   * [Iris](https://github.com/IrisShaders/Iris/blob/multiloader-new/common/src/main/resources/assets/iris/lang/en_us.json)
   * [MoreCulling](https://github.com/fxmorin/MoreCulling/blob/master/common/src/main/resources/assets/moreculling/lang/en_us.json)
   * [Controlify](https://github.com/isXander/Controlify/blob/1.20.x/dev/src/main/resources/assets/controlify/lang/en_us.json)
   * [Zoomify](https://github.com/isXander/Zoomify/blob/multiversion/dev/src/main/resources/assets/zoomify/lang/en_us.json)
   * [Fabric Capes](https://github.com/CaelTheColher/Capes/blob/architectury/common/src/main/resources/assets/capes/lang/en_us.json)
   * [Continuity](https://github.com/PepperCode1/Continuity/blob/1.19.3/dev/src/main/resources/assets/continuity/lang/en_us.json)
   * [CIT Resewn](https://github.com/SHsuperCM/CITResewn/blob/main/src/main/resources/assets/citresewn/lang/en_us.json)
2. For each mod you want to translate, open its page
3. Find the link to Source code
4. Read the mod's documentation to understand if translations happen on a translation platform
5. If not, find the path where language files are memorized, generally under the <kbd>**Code**</kbd> tab, in `src/main/resources/assets/mod-name/lang/en_us.json` (sometimes under a `common/` folder)
6. Copy that file's content
7. In the `lang` folder, click on the <kbd>**Add file**</kbd> button
8. Click on the <kbd>**Create new file**</kbd> button. This should fork the repo
9. Name the file following the [language codes format](https://minecraft.wiki/w/Language#Languages). For example `en_ud.json`
10. Paste the content you copied in _step 6_
11. Start translating the values inside of the quotes, on the right side of the colon. For example:

    ```json
    "cool-mod.config.title": "Cool Mod Options",
    ```

    Translate `Cool Mod Options` only!
12. Commit the file
13. Create a pull request
14. You're now done, you just have to wait:
    * The author must accept your translations
    * The mod must be updated to include your contribution
    * FO must be updated to include the new version of the mod

### Sodium

Sodium does not support translations natively, but the creators of Sodium Extra and FO have created an independent resource pack to add translations to Sodium. FO includes the [Translations for Sodium resource pack](../../info/resource-packs/#translations-for-sodium).

To translate Sodium, open its [unofficial page on Crowdin](https://crowdin.com/project/sodium-fabric). Translations are published every Saturday, and FO versions right after will include them.

Read more about [localization in Sodium natively](https://github.com/CaffeineMC/sodium-fabric/issues/2304).

## Resource Packs

{% tabs %}
{% tab title="Translator" %}
1. Join the [FO project on Crowdin](https://download.fo/crowdin)
2. Translate the files you prefer. Files are sorted according to the priority
3. Vote for existing suggestions with the <kbd>**Plus**</kbd> and <kbd>**Minus**</kbd> buttons
4. Discuss or ask for information in the comments
5. Join the [FO Discord server](https://download.fo/discord) to get a yellow rank for translating a file to 100%. The rank gives access to some secret channels ;)
6. You'll get an email and a Discord notification when there are new phrases to translate
{% endtab %}

{% tab title="Proofreader" %}
1. To become a proofreader, you must ask on the Discord server after getting the yellow rank
2. Check and approve all strings. Files must be 100% approved to be accepted
3. Test the [Mod Menu Helper resource pack](../../info/resource-packs/#mod-menu-helper) and [Chat Reporting Helper](../../info/resource-packs/#chat-reporting-helper)'s description in-game

The resource pack must be tested because there are specific length requirements:

* Translations must be fully visible in a maximized Full HD 1920×1080 window, with the default font, or with the Unicode font if required. You can emulate such a window in-game:
  1. Open <kbd>**Options...**</kbd>
  2. Open <kbd>**Video Settings...**</kbd>
  3. Set <kbd>**Fullscreen Resolution**</kbd> to <kbd>`1920x1080@60 (24 bit)`</kbd> (The number after `@` may vary)
  4. Check the <kbd>**Fullscreen**</kbd> checkbox
  5. Click on <kbd>**Apply**</kbd>
  6. If you're experiencing issues, press <kbd>⇧ Shift</kbd> + <kbd>P</kbd> to reset to default settings
  7. Click on <kbd>**Done**</kbd>
* The [online translations tester](https://download.fo/size-checker) may help, but does not replace in-game testing
* Feel free to rephrase sentences if you see fit
* In the options row, list as many of them as you can fit
* Do NOT change the strings' format! Keep paragraph signs `§`, the tools `⚒️` and arrows `🔀` emoji, and newlines `\n` intact

To test the translation in-game:

1. In Crowdin, open the **Mod Menu Helper** file (not _All strings_!)
2. Click on the <kbd>**menu**</kbd> button in the top-left corner
3. Click on the <kbd>**Download**</kbd> button. You'll get a `xx_xx.json` file
4. In Minecraft, open <kbd>**Options...**</kbd>
5. Open <kbd>**Resource Packs...**</kbd>
6. Click on <kbd>**Open Pack Folder**</kbd>
7. Open the `Mod Menu Helper.zip` file. If the `zip` file gets extracted, open the extracted folder
8. Navigate to `assets/fo/lang`
9. Drag the file you downloaded in _step 3_ and drop it into the folder you opened in _step 9_
10. In Minecraft, if the `zip` file got extracted in _step 8_, activate it
11. Click on <kbd>**Done**</kbd>
12. Click on <kbd>**Done**</kbd>
13. Open a world or a server, and press <kbd>F3</kbd> + <kbd>T</kbd> (sometimes <kbd>Fn</kbd> + <kbd>F3</kbd> + <kbd>T</kbd>) to reload the resource pack
14. In the main menu, click on the <kbd>**Mods**</kbd> button to open the Mod Menu
15. Make sure the translations fit the criteria above
16. Click on <kbd>**Back**</kbd>
17. Click on <kbd>**Options...**</kbd>
18. Click on <kbd>**Resource Packs...**</kbd>
19. Make sure the translations fit the criteria above
{% endtab %}
{% endtabs %}

## Website

The website is almost entirely translatable, except the wiki, which would get outdated very quickly.

Do NOT change the strings' format! If the original says `[Hello World!][1]`, you should only translate `Hello World!`

Translation testing is recommended for proofreaders:

1. Approve all translations on Crowdin. You may have to wait for some time
2. Find the latest ["New Crowdin updates" pull request on GitHub](https://github.com/Fabulously-Optimized/website/pulls?q=is:pr+is:open+New+Crowdin+updates)
3. Find a comment by the user `vercel`
4. Click on the <kbd>**Visit Preview**</kbd> link in that comment
5. Navigate the website and make sure translations are correct

## Installer

Most messages on the installer, except for some very detailed errors, are translatable.

However, translation testing is not very easy, so it's not required.
