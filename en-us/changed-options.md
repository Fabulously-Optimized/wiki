# Changed options

Fabulously Optimized changes some default options of Minecraft to improve your gameplay.

Because the pack is using YOSBR, the options will only change if you do not have `options.txt` or mod-specific files in `config` folder already, e.g. by using a clean profile. That also means you can freely update the pack without losing your settings!

### Options

| Option                      | Description                                                                                                                                                                                           | Vanilla  | Modpack | Reason for Change                                                                                                                                         |
| --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| autoJump                    | Makes the player jump when approaching a 1-height block                                                                                                                                               | true     | false   | Many people consider it annoying and therefore disable it                                                                                   |
| snooperEnabled              | Toggles [Snooper](https://minecraft.fandom.com/wiki/Snooper), the legacy analytics service. The setting was removed in 1.13 but it still exists in options (and defaults to enabled) for some reason. | true     | false   | Just in case you use the same profile on MC 1.13 or older, to improve privacy. |
| operatorItemsTab | Shows operator-only items in a Creative inventory tab, when you have operator access (`/op`)                                                                                                                                                               | false    | true    | It is useful and it only appears when you have the permission for it, so it's weird Mojang even made it an option        |
| darkMojangStudiosBackground | Makes the splash screen black and white                                                                                                                                                               | false    | true    | Black background is less intrusive than red, partial Bedrock Edition parity                                                                          |
| simulationDistance          | Redstone and mob spawning distance                                                                                                                                                                    | 12       | 6       | Better performance regardless of the rendering distance you use                                                                                      |
| guiScale                    | Size of the menu and interface elements                                                                                                                                                               | 0        | 3       | 3 is usable on all screens, 0 (Auto) can get too large on Full HD and larger screens                                                                 |
| maxFps                      | The maximum framerate                                                                                                                                                                                 | 120      | 260     | 260 means "unlimited", this is changed for better UX when VSync is disabled by the user (on fast computers/monitors)                                 |
| resourcePacks               | Adjusts which resource packs are enabled by default                                                                                                                                                   | \[]      | ¹       | Enabled mods' default packs and FO-exclusive Mod Menu Helper                                                                                         |
| tutorialStep                | The next step of [tutorial hints](https://minecraft.fandom.com/wiki/Tutorial\_hints)                                                                                                                  | movement | none    | If you know how to install a modpack, you probably don't need those tutorials anymore                                                                |
| skipMultiplayerWarning      | Whether to skip [the legal disclaimer](https://minecraft.fandom.com/wiki/File:Multiplayer\_disclaimer.png) when opening the multiplayer screen                                                        | false    | true    | I expect my users to already know that the third party servers are not owned or monitored by Mojang Studios or Microsoft. A more relevant warning is added to Realms by [No Chat Reports](https://www.curseforge.com/minecraft/mc-mods/no-chat-reports).                            |
| joinedFirstServer           | Whether to display the hint for [Social Interactions](https://minecraft.fandom.com/wiki/Social\_Interactions\_screen)                                                                                 | false    | true    | I expect my users to already know that Social Interactions can be opened with `P`                                                                    |
| telemetryOptInExtra                 | Sets the [telemetry](https://minecraft.fandom.com/wiki/Java_Edition_22w46a#General_2) toggle to "minimal".                                                                                          | false     | false   | While "minimal" is the default right now anyway, it may not always be the case. [Debugify](https://curseforge.com/minecraft/mc-mods/debugify) is used to disable it entirely though.                        |

¹ \["vanilla","Fabric Mods","lambdabettergrass/default","continuity/default","continuity/glass_pane_culling_fix","file/Mod Menu Helper.zip","file/Chat Reporting Helper.zip","midnightcontrols/bedrock"]

### Keybinds

| Option                            | Description                                                         | Default | Modpack | Reason for Change                                                            |
| --------------------------------- | ------------------------------------------------------------------- | ------- | ------- | ----------------------------------------------------------------------- |
| Vanilla: Save Hotbar Activator    | Saves your hotbar if this key and a number key are held             | c       | none    | This key is more often used for zoom                                    |
| Zoomify/WI Zoom: Zoom             | Zooms the view when the key is held                                 | v       | c       | This key is more often used for zoom                                    |
| Zoomify: GUI                      | Opens the Zoomify mod settings                                      | F8      | none    | Not needed for most players                                             |
| AntiGhost: Reveal ghost blocks    | Asks the server to send blocks around you in order to un-glitch you | g       | none    | Accidental presses and holding can cause issues, use **/ghost** instead |
| Iris: Reload Shaders              | Reloads the applied shaders                                         | r       | none    | Not needed for most players                                             |
| Iris: Shaderpack Selection Screen | Opens the shader selection screen                                   | o       | none    | Not needed for most players                                             |
| Iris: Toggle Shaders              | Disables or enables shaders                                         | k       | none    | Not needed for most players                                             |

The changed mod settings can be found on the repo at [.../yosbr/1.19.3/config](https://github.com/Fabulously-Optimized/fabulously-optimized/tree/main/Packwiz/1.19.3/config).

See also: [Minecraft Wiki: options.txt](https://minecraft.fandom.com/wiki/Options.txt#Java\_Edition)

### Fixed bugs

Fabulously Optimized includes some mods that fix vanilla bugs.
[Similar to the mod inclusion policy](principles.md), they must be meaningful to 70%+ users to get enabled (e.g. FPS drops, crashes, platform-specific annoyances...).

| Mojang bug                                            | Description                                                                | Fixed by                                                                  |
| ----------------------------------------------------- | -------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| [MC-59810](https://bugs.mojang.com/browse/MC-59810)   | Cannot break blocks while sprinting (Ctrl+Click = right click on macOS)    | [Debugify](https://curseforge.com/minecraft/mc-mods/debugify)     |
| [MC-73186](https://bugs.mojang.com/browse/MC-73186)   | Gaps between the faces of item models                                      | [Item Model Fix](https://www.curseforge.com/minecraft/mc-mods/item-model-fix) |
| [MC-81098](https://bugs.mojang.com/browse/MC-81098)   | Redstone dust updates cause lag (Singleplayer only)                        | [Lithium](https://www.curseforge.com/minecraft/mc-mods/lithium)           |
| [MC-89146](https://bugs.mojang.com/browse/MC-89146)   | Pistons forget update when being reloaded                                  | [Debugify](https://curseforge.com/minecraft/mc-mods/debugify)             |
| [MC-90683](https://bugs.mojang.com/browse/MC-90683)   | "Received unknown passenger" - Entities with differing render distances as passengers outputs error                                  | [Debugify](https://curseforge.com/minecraft/mc-mods/debugify)             |
| [MC-112730](https://bugs.mojang.com/browse/MC-112730) | Beacon beam and structure block render twice per frame                     | [Debugify](https://curseforge.com/minecraft/mc-mods/debugify)             |
| [MC-121772](https://bugs.mojang.com/browse/MC-121772) | Can't scroll while holding SHIFT on macOS                                  | [Debugify](https://curseforge.com/minecraft/mc-mods/debugify)             |
| [MC-121884](https://bugs.mojang.com/browse/MC-121884) | Server -> Client custom payload packets can leak resources                 | [MemoryLeakFix](https://www.curseforge.com/minecraft/mc-mods/memoryleakfix) |
| [MC-122477](https://bugs.mojang.com/browse/MC-122477) | Linux/GNU: Opening chat sometimes writes 't'                               | [Debugify](https://curseforge.com/minecraft/mc-mods/debugify)             |
| [MC-132488](https://bugs.mojang.com/browse/MC-132488) | Ticking animated textures is very inefficient                              | [Sodium](https://www.curseforge.com/minecraft/mc-mods/sodium)             |
| [MC-140646](https://bugs.mojang.com/browse/MC-140646) | Text fields don't scroll while selecting text with Shift                   | [Debugify](https://curseforge.com/minecraft/mc-mods/debugify)             |
| [MC-154966](https://bugs.mojang.com/browse/MC-154966) | Hunger and experience bar invisible on horses and all other animal mounts  | [Better Mount Hud](https://www.curseforge.com/minecraft/mc-mods/better-mount-hud) | 
| [MC-162253](https://bugs.mojang.com/browse/MC-162253) | Lag spike when crossing certain chunk borders                              | [Starlight](https://www.curseforge.com/minecraft/mc-mods/starlight)             |
| [MC-165595](https://bugs.mojang.com/browse/MC-165595) | Guardian beam does not render when over a certain "Time" in level.dat      | [Sodium Extra](https://www.curseforge.com/minecraft/mc-mods/sodium-extra) |
| [MC-172550](https://bugs.mojang.com/browse/MC-172550) | Ghost blocks sometimes appear when insta-mining                            | [AntiGhost](https://www.curseforge.com/minecraft/mc-mods/antighost)       |
| [MC-199467](https://bugs.mojang.com/browse/MC-199467) | Certain entity animations stop after they've existed in world for too long | [Debugify](https://curseforge.com/minecraft/mc-mods/debugify)             |
| [MC-226729](https://bugs.mojang.com/browse/MC-226729) | Memory leakage problem in native operations                                | [MemoryLeakFix](https://www.curseforge.com/minecraft/mc-mods/memoryleakfix) |
| [MC-227302](https://bugs.mojang.com/browse/MC-227302) | Smooth lighting doesn't work properly on the water surface                 | [Sodium](https://www.curseforge.com/minecraft/mc-mods/sodium)             |  
| [MC-228976](https://bugs.mojang.com/browse/MC-228976) | Entity collision is run on render thread                                   | [Lithium](https://www.curseforge.com/minecraft/mc-mods/lithium)             |
| [MC-237493](https://bugs.mojang.com/browse/MC-237493) | Telemetry cannot be disabled                                               | [Debugify](https://curseforge.com/minecraft/mc-mods/debugify)             |

If you'd like to enable more bugfixes for your game, see [the fixed bug list for Debugify](https://github.com/W-OVERFLOW/Debugify/blob/1.19/PATCHED.md#unpatched-in-vanilla).

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

For other things like dynamic lights, better grass and zoom:

1. Click `Mods`
2. Read the descriptions of the mods to see what they do
3. If the pencil is blue, you can configure the mod by clicking the config button ![config](https://i.ibb.co/j35cBtn/image.png)
   * If you don't see any pencils, you don't have the Mod Menu Helper resource pack enabled for some reason. Click `Done` → `Options...` → `Resource Packs...` → `⏵` on "Mod Menu Helper.zip" → `Done` → go to point 1 of this tutorial

If you need to disable a mod, [see this wiki page](disabling-mods.md).

If you have more questions about the mods, [chat with us on Discord!](https://discord.gg/yxaXtaQqdB)
