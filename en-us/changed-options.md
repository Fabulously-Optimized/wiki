Fabulously Optimized changes some default options of Minecraft to improve your gameplay. 

Because the pack is using YOSBR, the options will only change if you do not have `options.txt` or mod-specific files in `config` folder already, e.g. by using a clean profile. That also means you can freely update the pack without losing your settings!

## Options

| Option | Description | Vanilla | Modpack | Why changed? |
|-|-|-|-|-|
| autoJump | Makes the player jump when approaching a 1-height block | true | false | In vanilla it is more annoying than useful, many people disable it |
| snooperEnabled | Toggles [Snooper](https://minecraft.fandom.com/wiki/Snooper), a hardware analytics service.  The setting was removed in 1.13 but it still exists in options (and defaults to enabled) for some reason. | true | false | Just in case, to improve privacy. In 1.18+ [TieFix](https://www.curseforge.com/minecraft/mc-mods/tiefix) is used to actually enforce it. |
| darkMojangStudiosBackground | Makes the splash screen black and white | false | true | Black background is less intrusive than red, partial Bedrock Edition parity |
| gamma | Screen brightness | 0.0 | 0.5 | Better view at night and in dark caves, +50% compared to vanilla's Moody, 1.18 parity for other versions |
| simulationDistance | Redstone and mob spawning distance | 12 | 6 | Better performance regardless of the rendering distance you use |
| guiScale | Size of the menu and interface elements | 0 | 3 | 3 is usable on all screens, 0 (Auto) can get too large on Full HD and larger screens |
| resourcePacks | Adjusts which resource packs are enabled by default | [] | ¹ | Enabled mods' default packs and FO-exclusive Mod Menu Helper
| tutorialStep | The next step of [tutorial hints](https://minecraft.fandom.com/wiki/Tutorial_hints) | movement | none | If you know how to install a modpack, you probably don't need those tutorials anymore |
| skipMultiplayerWarning | Whether to skip [the legal disclaimer](https://minecraft.fandom.com/wiki/File:Multiplayer_disclaimer.png) when opening the multiplayer screen | false | true | I expect my users to already know that the third party servers are not owned or monitored by Mojang Studios or Microsoft |
| joinedFirstServer | Whether to display the hint for [Social Interactions](https://minecraft.fandom.com/wiki/Social_Interactions_screen) | false | true | I expect my users to already know that Social Interactions can be opened with P |

¹ ["vanilla","Fabric Mods","lambdabettergrass/default","continuity/default","continuity/glass_pane_culling_fix","cullleaves/smartleaves","file/Mod Menu Helper.zip"]

## Keybinds

| Option | Description | Default | Modpack | Why changed? |
|-|-|-|-|-|
| Vanilla: Save Hotbar Activator | Saves your hotbar if this key and a number key are held | c | none | This key is more often used for zoom |
| Zoomify/WI Zoom: Zoom | Zooms the view when the key is held | v | c | This key is more often used for zoom |
| Zoomify: GUI | Opens the Zoomify mod settings | F8 | none | Not needed for most players |
| AntiGhost: Reveal ghost blocks | Asks the server to send blocks around you in order to un-glitch you | g | none | Accidental presses and holding can cause issues, use **/ghost** instead |
| Iris: Reload Shaders | Reloads the applied shaders | r | none | Not needed for most players |
| Iris: Shaderpack Selection Screen | Opens the shader selection screen | o | none | Not needed for most players |
| Iris: Toggle Shaders | Disables or enables shaders | k | none | Not needed for most players |

The changed mod settings can be found on the repo at [.../yosbr/1.18.1/config](https://github.com/Madis0/fabulously-optimized/tree/main/Packwiz/1.18.1/config).

See also: [Minecraft Wiki: options.txt](https://minecraft.fandom.com/wiki/Options.txt#Java_Edition) and [issue #30](https://github.com/Madis0/fabulously-optimized/issues/30)
