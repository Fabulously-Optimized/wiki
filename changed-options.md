# Changed options

Fabulously Optimized changes some default options of Minecraft to improve your gameplay.

Because the pack is using YOSBR, the options will only change if you do not have `options.txt` or mod-specific files in `config` folder already, e.g. by using a clean profile. That also means you can freely update the pack without losing your settings!

**P.S. This table has 5 columns. Scroll right if you can't see them!**

### Options

| Option | Description | Vanilla | Modpack | Reason for Change |
| - | - | - | - | - |
| advancedItemTooltips | Enables ["advanced" tooltip info](https://www.online-tech-tips.com/wp-content/uploads/2021/01/Armor-Tooltips-610x571.png) on items - item ID and durability, and exact color hex code for dyed armor | false | true | These are useful for much more than just debugging - if you're using commands, want to know the exact durability value, learning English, etc. Plus, this setting is hidden in the debug menu, so many people might not know about it. |
| darkMojangStudiosBackground | Makes the Mojang Studios splash screen white-on-black instead of white-on-red | false | true | Black background is less intrusive than red, partial Bedrock Edition parity |
| enableVsync | Toggle [VSync](https://en.wikipedia.org/wiki/Screen_tearing#Vertical_synchronization), a FPS-limiting system | true | false | Disabling VSync by default helps users instantly see the benefits of FO, reduces input lag and increases framerate when using shaders. The benefits of enabling or disabling it vary by system; also note that FO has an option to use Adaptive VSync on some systems. |
| guiScale | Size of the menu and interface elements | 0 | 3 | 3 is more usable on most screens, 0 (Auto) can get too large on Full HD and larger screens, including most Macs' "Retina" displays |
| incompatibleResourcePacks | A list of resource packs that have been forcefully enabled, despite being marked as incompatible | \[] | (varies) | Mod-provided resource packs that have old manifest version but are known to be compatible. Usually contains just [Continuity](https://www.curseforge.com/minecraft/mc-mods/continuity)'s resource packs, but values may vary by FO version. |
| joinedFirstServer | Whether to display the hint for [Social Interactions](https://minecraft.wiki/w/Social\_Interactions\_screen) | false | true | I expect my users to already know that Social Interactions can be opened with `P`; the screen is easily discoverable by the "Player Reporting" button |
| maxFps | The maximum framerate | 120 | 260 | 260 means "unlimited", which allows you to see the full FPS that your system is capable of |
| onboardAccessibility | Indicates whether the user has not seen the accessibility onboarding screen | true | false | Minecraft already has an easily accessible accessibility button in the main menu, this screen just creates annoyances for the majority who don't need it. [Read more about accessibility in FO](accessibility.md) |
| operatorItemsTab | Shows operator-only items (command blocks, lights, barriers, etc.) in a Creative inventory tab, when you have operator access (`/op`) | false | true | It is useful and it only appears when you have the permission for it, so it's weird Mojang even made it an option |
| resourcePacks | Adjusts which resource packs are enabled by default | \[] | ¹ | Enabled [mod-provided and FO-exclusive resource packs](#resource-packs) by default |
| lang | Adjusts the game's language | en_us | (your OS language) | Enables user's system language by default, for usability, accessibility and discoverability purposes - courtesy of [Language Reload](https://www.curseforge.com/minecraft/mc-mods/language-reload). Not available for all launchers and operating systems. |
| simulationDistance | Redstone and mob spawning distance | 12 | 6 | Better performance regardless of the rendering distance you use |
| skipMultiplayerWarning | Whether to skip [the legal disclaimer](https://minecraft.wiki/w/File:Multiplayer\_disclaimer.png) when opening the multiplayer screen | false | true | I expect my users to already know that the third party servers are not owned or monitored by Mojang Studios or Microsoft. |
| telemetryOptInExtra | Sets the telemetry (analytics data collection) toggle to "minimal". | false | false | While "minimal" is the default right now anyway, it may not always be the case, hence the enforcement by FO. [Debugify](https://curseforge.com/minecraft/mc-mods/debugify) is used to disable it entirely though, so this is also just a fallback. |
| tutorialStep | The next step of [tutorial hints](https://minecraft.wiki/w/Tutorial\_hints) | movement | none | If you know how to install a modpack, you probably don't need those tutorials anymore |

¹ `["vanilla","fabric","continuity:glass_pane_culling_fix","continuity:default","file/SodiumTranslations.zip","file/Mod Menu Helper.zip","file/Chat Reporting Helper.zip","file/Fast Better Grass.zip"]`

**Changed mod settings can be found on the repo at [.../yosbr/1.21.1/config](https://github.com/Fabulously-Optimized/fabulously-optimized/tree/main/Packwiz/1.21.1/config).**

### Telemetry

**Telemetry Data Collection**, previously known as **Snooper**, refers to Minecraft's and potentially mods', launchers' methods of collecting analytics about the user, usually in a limited form to preserve privacy. [Minecraft's telemetry options are detailed here.](https://minecraft.wiki/w/Snooper)

While telemetry is not always bad, as it may help developers better support their content for users' devices (e.g. to see where performance can be improved) it can be unwanted and unexpected for privacy concerns. 

As of 1.20.2, Minecraft does not have an option to fully disable telemetry, so in this modpack such option is added by [Debugify](https://curseforge.com/minecraft/mc-mods/debugify). The reason for disabling vanilla telemetry is that

1. it collects too much data even in minimal configuration (e.g. user's Xbox ID)
2. it skews Mojang's data due to being modded - Mojang may see that users already have good performance, but it does not actually reflect the vanilla game

[The modpack's stance](principles.md) is to disable all forms of telemetry by default, letting users to choose to opt-in to it manually when wanted. However, it is important to note that the modpack cannot disable any telemetry collected by user's launcher or operating system.

### Keybinds

**P.S. This table has 5 columns. Scroll right if you can't see them!**

| Option                            | Description                                                         | Default | Modpack | Reason for Change                                                            |
| --------------------------------- | ------------------------------------------------------------------- | ------- | ------- | ----------------------------------------------------------------------- |
| Vanilla: Save Hotbar Activator    | Saves your hotbar if this key and a number key are held             | c       | none    | This key is more often used for zoom                                    |
| Zoomify: Zoom             | Zooms the view when the key is held                                 | v       | c       | This key is more often used for zoom                                    |
| Zoomify: Secondary zoom                      | Activates the secondary zoom option                                      | F6      | none    | Not needed for most players                                             |
| Iris: Reload Shaders              | Reloads the applied shaders                                         | r       | none    | Not needed for most players                                             |
| Iris: Shaderpack Selection Screen | Opens the shader selection screen                                   | o       | none    | Not needed for most players                                             |
| Iris: Toggle Shaders              | Disables or enables shaders                                         | k       | none    | Not needed for most players                                             |
| FabricSkyboxes: Toggle mod              | Disables or enables custom skyboxes                                         | Numpad 0       | none    | Not needed for most players                                             |
| OptiGUI: Copy inspection to clipboard              | Copies OptiGUI's debug info                                         | F12       | none    | Not needed for most players                                             |

### Resource packs

Fabulously Optimized enables relevant mod-provided resource packs and bundles some resource packs for better experience.

- [Mod Menu Helper](https://github.com/Fabulously-Optimized/fabulously-optimized/tree/main/Resource%20Packs/Mod%20Menu%20Helper) (FO-exclusive) - explains what each mod does in a consistent and clear way on Mod Menu
- [Chat Reporting Helper](https://www.curseforge.com/minecraft/texture-packs/chat-reporting-helper) - explains [chat reporting](chat-reporting-faq.md) in a clear way by simplifying vanilla and No Chat Reports tooltips and No Chat Reports icons
- [Fast Better Grass](https://www.curseforge.com/minecraft/texture-packs/fast-better-grass) - imitates OptiFine's "Better Grass" (fast mode)
- [Translations for Sodium](https://www.curseforge.com/minecraft/texture-packs/translations-for-sodium) - adds unofficial translations for Sodium (video settings)

The resource packs use minimal resources, [can be translated to your language](language-support.md) and they will work with other resource packs.

### Fixed bugs

Fabulously Optimized includes some mods that fix vanilla bugs.
[Similar to the mod inclusion policy](principles.md), they must be meaningful to 70%+ users to get enabled (e.g. FPS drops, crashes, platform-specific annoyances...).

| Mojang bug                                            | Description                                                                | Fixed by                                                                  |
| ----------------------------------------------------- | -------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| [MC-577](https://bugs.mojang.com/browse/MC-577)   | Mouse buttons block all inventory controls that are not default   | [Debugify](https://curseforge.com/minecraft/mc-mods/debugify)     |
| [MC-22882](https://bugs.mojang.com/browse/MC-22882) | Ctrl + Q won't work on Mac                                                   | [Debugify](https://curseforge.com/minecraft/mc-mods/debugify)             |
| [MC-59810](https://bugs.mojang.com/browse/MC-59810)   | Cannot break blocks while sprinting (Ctrl+Click = right click on macOS)    | [Debugify](https://curseforge.com/minecraft/mc-mods/debugify)     |
| [MC-73186](https://bugs.mojang.com/browse/MC-73186)   | Gaps between the faces of item models                                      | [Item Model Fix](https://www.curseforge.com/minecraft/mc-mods/item-model-fix) |
| [MC-81098](https://bugs.mojang.com/browse/MC-81098)   | Redstone dust updates cause lag (Singleplayer only)                        | [Lithium](https://www.curseforge.com/minecraft/mc-mods/lithium)           |
| [MC-89146](https://bugs.mojang.com/browse/MC-89146)   | Pistons forget update when being reloaded                                  | [Debugify](https://curseforge.com/minecraft/mc-mods/debugify)             |
| [MC-90683](https://bugs.mojang.com/browse/MC-90683)   | "Received unknown passenger" - Entities with differing render distances as passengers outputs error                                  | [Debugify](https://curseforge.com/minecraft/mc-mods/debugify)             |
| [MC-112730](https://bugs.mojang.com/browse/MC-112730) | Beacon beam and structure block render twice per frame                     | [Debugify](https://curseforge.com/minecraft/mc-mods/debugify)             |
| [MC-121884](https://bugs.mojang.com/browse/MC-121884) | Server -> Client custom payload packets can leak resources                 | [MemoryLeakFix](https://www.curseforge.com/minecraft/mc-mods/memoryleakfix) |
| [MC-122477](https://bugs.mojang.com/browse/MC-122477) | Linux/GNU: Opening chat sometimes writes 't'                               | [Debugify](https://curseforge.com/minecraft/mc-mods/debugify)             |
| [MC-132488](https://bugs.mojang.com/browse/MC-132488) | Ticking animated textures is very inefficient                              | [Sodium](https://www.curseforge.com/minecraft/mc-mods/sodium)             |
| [MC-154966](https://bugs.mojang.com/browse/MC-154966) | Hunger and experience bar invisible on horses and all other animal mounts  | [Better Mount Hud](https://www.curseforge.com/minecraft/mc-mods/better-mount-hud) | 
| [MC-165595](https://bugs.mojang.com/browse/MC-165595) | Guardian beam does not render when over a certain "Time" in level.dat      | [Sodium Extra](https://www.curseforge.com/minecraft/mc-mods/sodium-extra) |
| [MC-199467](https://bugs.mojang.com/browse/MC-199467) | Certain entity animations stop after they've existed in world for too long | [Debugify](https://curseforge.com/minecraft/mc-mods/debugify)             |
| [MC-226729](https://bugs.mojang.com/browse/MC-226729) | Memory leakage problem in native operations                                | [MemoryLeakFix](https://www.curseforge.com/minecraft/mc-mods/memoryleakfix) |
| [MC-227302](https://bugs.mojang.com/browse/MC-227302) | Smooth lighting doesn't work properly on the water surface                 | [Sodium](https://www.curseforge.com/minecraft/mc-mods/sodium)             |  
| [MC-228976](https://bugs.mojang.com/browse/MC-228976) | Entity collision is run on render thread                                   | [Lithium](https://www.curseforge.com/minecraft/mc-mods/lithium)             |
| [MC-237493](https://bugs.mojang.com/browse/MC-237493) | Telemetry cannot be disabled                                               | [Debugify](https://curseforge.com/minecraft/mc-mods/debugify)             |
| [MC-237493](https://bugs.mojang.com/browse/MC-263865) | Fullscreen state isn't saved                                               | [Debugify](https://curseforge.com/minecraft/mc-mods/debugify)             |

If you'd like to enable more bugfixes for your game, see [the fixed bug list for Debugify](https://github.com/W-OVERFLOW/Debugify/blob/1.20/PATCHED.md#unpatched-in-vanilla).

#### Requesting a bugfix

Want to get a bug fixed in Fabulously Optimized? Here's what you'll need to do:

1. Find the actual bug [in Mojang's bug tracker](https://bugs.mojang.com/projects/MC/issues?filter=allopenissues)
2. Request it or look at its status on [Debugify's bug tracker](https://github.com/W-OVERFLOW/Debugify/issues)
3. Once implemented (or confirmed to be) in Debugify, [request an option change in FO](https://github.com/Fabulously-Optimized/fabulously-optimized/issues/new?assignees=\&labels=option\&template=setting-request.yml)
4. Describe the bug, mention the mod that fixes it and why it is important to 70-80% of users
5. If accepted, expect the fix to be enabled in the next version of FO :)

### Configuring mods

The modpack is already configured for the best performance and simplest experience for most users.

If you want to configure something, you'll most likely find it on `Options...` → `Video Settings...`. If you have a powerful computer or monitor, you may want to disable Vsync there.

For other things like dynamic lights, shaders and zoom:

1. Click `Mods`
2. Read the descriptions of the mods to see what they do
3. If `🛠️` or `✏️` is blue, you can configure the mod by clicking the config button ![config](https://i.ibb.co/j35cBtn/image.png)
   * If you don't see the `🛠️` or `✏️` emoji, you don't have the Mod Menu Helper resource pack enabled for some reason. Click `Done` → `Options...` → `Resource Packs...` → `⏵` on "Mod Menu Helper.zip" → `Done` → go to point 1 of this tutorial

If you need to disable a mod, [see this wiki page](disabling-mods.md).

If you have more questions about the mods, [chat with us on Discord!](https://fabulously-optimized.github.io/discord)
