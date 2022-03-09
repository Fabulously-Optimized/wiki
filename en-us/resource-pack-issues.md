Fabulously Optimized supports [various Optifine features](https://github.com/Fabulously-Optimized/fabulously-optimized/wiki/Give-up-Optifine), including resource pack extras. However, the implementation differs from mod to mod and some resource packs are accepted in Optifine even if they are broken, so this page should help you fix some of those issues.

Before trying any of those things here, though, [make sure you are using the latest version](https://github.com/Fabulously-Optimized/fabulously-optimized/wiki/Update-instructions).

## Broken paths

If you see this message while activating a resource pack:

![Contains broken paths](https://i.ibb.co/26cMtqr/Screenshot-20211116-191457.png)

This means the resource pack maker is **using spaces or other non-standard characters** in the file or folder names.

If this is the case, the modpack will warn you and allow overriding it, but note that various glitches may occur (miscolored or invisible blocks, lightning issues, broken textures...).

To fix that, please tell the resource pack maker to only use the following characters in file/folder names: `a-z0-9/._-`.

## Invisible blocks

This may occur when the pack is using broken paths and is trying to change the models of some blocks, like chests.

#### Enhanced Block Entities

Enhanced Block Entities is the mod that makes various blocks faster on latest versions of FO. Some optimizations may not be supported by your resource packs, so here's how to configure it:

1. Click `Mods`
1. Search for "Enhanced Block Entities", click the config button ![](https://i.ibb.co/j35cBtn/image.png)
1. Disable any blocks that seem broken to you. Usually disabling `Enhanced Chests` is enough.
1. Click `Done`

#### FastChest and Better Beds

Some versions of FO include these mods instead. For chests:

1. Click `Mods`
1. Search for "FastChest", click the config button ![](https://i.ibb.co/j35cBtn/image.png)
1. Disable the mod, click `Done`.

For beds:

1. Close the game
1. Remove or disable the Better Beds mod from your launcher.
1. Start the game and see if it is fixed.

## Custom entity models

_Or "mobs with a custom shape"._

Partly supported. [See here for a list of supported entity types and features.](https://github.com/dorianpb/cem#differences)

If your resource pack's entities are supported but are still not displayed correctly, you can try this:

1. Click `Mods`
1. Search for "Custom Entity Models", click the config button (top right, above `Issues`)
1. Set "Use model creation fix?" to `No`
1. Click `Save & Quit` and `Done`
1. In your world, hold down `F3` (and `Fn` on laptops), press `T`
1. You'll see a short loading screen. After that, check if the models are displayed correctly.
1. If they still are not, set that setting back to `Yes` and wait for CEM to implement them.

See also: [cem#9](https://github.com/dorianpb/cem/issues/9)

## Emissive textures
_Or "making any block light up"._

Currently not supported with resource packs, see [Continuity#7](https://github.com/PepperCode1/Continuity/issues/7).
However, if you can run shaders and want to highlight the ores, use [Complementary](https://www.curseforge.com/minecraft/customization/complementary-shaders) or [Prismarine](https://www.curseforge.com/minecraft/customization/prismarine-shader).

## Custom sky

_Or "custom skymap"._

Currently not supported with resource packs, follow [issue #72](https://github.com/Fabulously-Optimized/fabulously-optimized/issues/72) for details.
Or, if you can run shaders, [BSL](https://bitslablab.com/bslshaders/) can change clouds for example and [AstraLex](https://www.curseforge.com/minecraft/customization/astralex-shader-bsl-edit) can change the sky.

