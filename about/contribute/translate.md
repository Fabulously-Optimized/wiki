---
hidden: true
icon: language
---

# Translate

In accordance to the [Accessibility principle](../README.md#accessibility), one of FO's objectives is making it accessible to everyone, regardless of their language. This is why we support and welcome translations of FO and of its mods.

The following parts of FO are translatable:

* [Mods](../../info/mods/) (not managed by FO)
* [Resource Packs](../../info/resource-packs/)
* [Installer](../../how-to/install/vanilla.md)
* [Website](https://download.fo/)

## Mods

1. Check out the [list of mods in FO](../../info/mods/). The most important mods are:
   * [Sodium](#sodium)
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
5. If not, find the path where language files are memorized, generally under the **Code** tab, in `src/main/resources/assets/mod-name/lang/en_us.json` (sometimes under a `common/` folder)
6. Copy that file's content
7. In the `lang` folder, click on **Add file**
8. Click on **Create new file**. This should fork the repo
9. Name the file following the [language codes format](https://minecraft.wiki/w/Language#Languages). For example `et_ee.json`
10. Paste the content you copied in _step 6_
11. Start translating the values inside of the quotes, on the right side of the colon. For example:

   ```json
   "cool-mod.config.title": "Cool Mod Options",
   ```

   Translate `Cool Mod Options` only!
12. Commit the file
13. Create a pull request.
14. You're now done, you just have to wait:
   * The author must accept your translations
   * The mod must be updated to include your contribution
   * FO must be updated to include the new version of the mod

### Sodium

Sodium does not support translations natively, but the creators of Sodium Extra and FO have created an independent resource pack to add translations to Sodium. FO includes the [Translations for Sodium resource pack](../../info/resource-packs/#translations-for-sodium).

To translate Sodium, open its [unofficial page on Crowdin](https://crowdin.com/project/sodium-fabric). Translations are published every Saturday, and FO versions right after will include them.

Read more about [localization in Sodium natively](https://github.com/CaffeineMC/sodium-fabric/issues/2304).

## Resource Packs

{% hint style="info" %}
FO's translations are licensed under [CC0](https://choosealicense.com/licenses/cc0-1.0).
{% endhint %}

{% tabs %}
{% tab title="Translator" %}
1. Join the [FO project on Crowdin](https://crowdin.com/project/fabulously-optimized) <!-- TODO: https://download.fo/crowdin ? -->
2. Translate the files you prefer. Files are sorted according to the priority
3. Vote for existing suggestions with the **Plus** and **Minus** buttons
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
   1. Open **Options...**
   2. Open **Video Settings...***
   3. Set **Fullscreen Resolution** to **1920x1080@60 (24 bit)** (The number after `@` may vary)
   4. Check the **Fullscreen** checkbox
   5. Click on **Apply**
   6. If you're experiencing issues, press **`Shift`** + **`P`** to reset to default settings
   7. Click on **Done**
* The [online translations tester](https://fabulously-optimized.github.io/Mod-Menu-Helper-Size-Checker) <!-- TODO: https://download.fo/size-checker ? --> may help, but does not replace in-game testing
* Feel free to rephrase sentences if you see fit
* In the options row, list as many of them as you can fit
* Do NOT change the strings' format! Keep paragraph signs `§`, the tools `⚒️` and arrows `🔀` emoji, and newlines `\n` intact

To test the translation in-game:

1. In Crowdin, open the **Mod Menu Helper** file (not _All strings_!)
2. Click on the menu button in the top-left corner
3. Click on the **Download** button. You'll get a `xx_xx.json` file
4. In Minecraft, open **Options...**
5. Open **Resource Packs...**
6. Click on **Open Pack Folder**
7. Open the `Mod Menu Helper.zip` file. If the `zip` file gets extracted, open the extracted folder
8. Navigate to `assets/fo/lang`
9. Drag the file you downloaded in _step 3_ and drop it into the folder you opened in _step 9_
10. In Minecraft, if the `zip` file got extracted in _step 8_, activate it
11. Click on **Done**
12. Click on **Done**
13. Open a world or a server, and press **`F3`** + **`T`** to reload the resource pack
14. In the main menu, click on the **Mods** button to open the Mod Menu
15. Make sure the translations fit the criteria above
16. Click on **Back**
17. Click on **Options...**
18. Click on **Resource Packs...**
19. Make sure the translations fit the criteria above
{% endtab %}
{% endtabs %}

## Website

{% hint style="info" %}
FO's translations are licensed under [CC0](https://choosealicense.com/licenses/cc0-1.0).
{% endhint %}

The website is almost entirely translatable, except the wiki, which would get outdated very quickly.

Do NOT change the strings' format! If the original says `[Hello World!][1]`, you should only translate `Hello World!`

Translation testing is recommended for proofreaders:

1. Approve all translations on Crowdin. You may have to wait for some time
2. Find the latest ["New Crowdin updates" pull request on GitHub](https://github.com/Fabulously-Optimized/fabulously-web/pulls?q=is:pr+is:open+New+Crowdin+updates)
3. Find a comment by the user `vercel`
4. Click on **Visit Preview** in that comment
5. Navigate the website and make sure translations are correct

## Installer

{% hint style="info" %}
FO's translations are licensed under [CC0](https://choosealicense.com/licenses/cc0-1.0).
{% endhint %}

Most messages on the installer, except for some very detailed errors, are translatable.

However, translation testing is not very easy, so it's not required.
