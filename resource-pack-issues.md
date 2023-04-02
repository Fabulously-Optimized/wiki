# Resource pack issues

Fabulously Optimized supports [various OptiFine features](give-up-optifine.md), including resource pack extras. However, the implementation differs from mod to mod and some resource packs are accepted in OptiFine even if they are broken, so this page should help you fix some of those issues.

Before trying any of those things here, though, [make sure you are using the latest version](update-instructions.md).

### Broken paths

If you see this message while activating a resource pack:

![Contains broken paths](https://i.ibb.co/26cMtqr/Screenshot-20211116-191457.png)

This means the resource pack maker is **using spaces or other non-standard characters** in the file or folder names.

If this is the case, the modpack will warn you and allow overriding it, but note that various glitches may occur (miscolored or invisible blocks, lightning issues, broken textures...).

To fix that, please tell the resource pack maker to only use the following characters in file/folder names: `a-z0-9._-`.

### Invisible blocks

This may occur when the pack is using broken paths and is trying to change the models of some blocks, like chests.

#### Enhanced Block Entities

Enhanced Block Entities is the mod that makes various blocks faster on latest versions of FO. Some optimizations may not be supported by your resource packs, so here's how to configure it:

1. Click `Mods`
2. Search for "Enhanced Block Entities", click the config button ![config](https://i.ibb.co/j35cBtn/image.png)
3. Disable any blocks that seem broken to you. Usually disabling `Enhanced Chests` is enough.
4. Click `Done`

#### FastChest and Better Beds

Some versions of FO include these mods instead.

Chests:

1. Click `Mods`
2. Search for "FastChest", click the config button ![](https://i.ibb.co/j35cBtn/image.png)
3. Disable the mod, click `Done`.

Beds:

1. Close the game
2. Remove or disable the Better Beds mod from your launcher.
3. Start the game and see if it is fixed.

### Lighting problems

![Random colors on the wall](https://i.ibb.co/jbkg1PG/unknown.png)
If you are seeing problems with lighting, such as flickering light sources or lights of random colors, [try disabling](disabling-mods.md) Colormatic.

### Custom entity models

_Or "mobs with a custom shape"._

### 4.7.0 and newer

FO is now using a different mod that should have more compatibility. [Fresh Animations](https://www.curseforge.com/minecraft/texture-packs/fresh-animations) latest version is seamlessly supported, though it's addon may not be. Issues and workarounds are tracked [on the mod's Discord](https://discord.com/invite/rURmwrzUcz), in the channel `#emf-issues`.

### 4.6.0 and earlier

Partly supported. [Resource packs that should work are discussed here (cem#9)](https://github.com/dorianpb/cem/issues/9)

For Fresh Animations, [try this version](https://www.curseforge.com/minecraft/texture-packs/fresh-animations/files/3705824) with the instructions below [(discuss any issues here)](https://github.com/dorianpb/cem/issues/11).

If your resource pack's entities are supported but are still not displayed correctly, you can try this:

1. Click `Mods`
2. Search for "Custom Entity Models", click the config button (top right, above `Issues`)
3. Set "Use model creation fix?" to `No`
4. Click `Save & Quit` and `Done`
5. In your world, hold down `F3` (and `Fn` on laptops), press `T`
6. You'll see a short loading screen. After that, check if the models are displayed correctly.
7. If they still are not, set that setting back to `Yes` and disable your resource pack, wait for CEM to implement them.
   * Or if you want to continue using your resource pack without the models, disable the optifine setting in CEM to essentially disable the mod.

See also: [a list of supported entity types and features.](https://github.com/dorianpb/cem#differences)
