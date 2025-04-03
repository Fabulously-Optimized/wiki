# Resource pack issues

Fabulously Optimized supports [various OptiFine features](give-up-optifine.md), including resource pack extras. However, the implementation differs from mod to mod and some resource packs are accepted in OptiFine even if they are broken, so this page should help you fix some of those issues.

### Older versions

Is the resource pack actually built for the version you're running? If not, check for the latest version or use a converter tool like [this one](https://www.planetminecraft.com/mod/minecraft-1-12-1-13-1-14-1-15-resource-pack-converter/) or [the official one](https://github.com/Mojang/slicer).

### Broken paths

If you see this message while activating a resource pack:

![Contains broken paths](https://i.ibb.co/26cMtqr/Screenshot-20211116-191457.png)

This means the resource pack maker is **using spaces or other non-standard characters** in the file or folder names.

If this is the case, the modpack will warn you and allow overriding it, but note that various glitches may occur (miscolored or invisible blocks, lightning issues, broken textures...).

To fix that, please tell the resource pack maker to only use the following characters in file/folder names: `a-z0-9._-`.

See also: [Minecraft Wiki article about this](https://minecraft.wiki/w/Resource_location#Legal_characters)

### Fullbright

_Or "game brightness beyond 100%"_.

Currently the vanilla resource pack and a direct options.txt edit **do not work**, OptiFine-based resource packs _might work_. Either way, it is recommended to just [add a mod](adding-more-mods.md), such as [Gamma Utils](https://modrinth.com/mod/gamma-utils) or [other simpler ones](https://modrinth.com/mods?q=fullbright&e=client&g=categories:fabric).

Fabulously Optimized does not plan to add "fullbright" methods beyond its current [dynamic lighting](give-up-optifine.md), because it would take away from vanilla gameplay's night vision and may be disallowed on certain servers' rules.

### Invisible blocks

This may occur when the pack is using broken paths and is trying to change the models of some blocks, like chests.

#### Enhanced Block Entities

Enhanced Block Entities is the mod that makes various blocks faster on most versions of FO. Some optimizations may not be supported by your resource packs, so here's how to configure it:

1. Click `Mods`
2. Search for "Enhanced Block Entities", click the config button ![config](https://i.ibb.co/j35cBtn/image.png)
3. Enable "Force Resource Pack Compatibility"
   * If that doesn't help or the option is not visible, disable any blocks that seem broken to you. Usually disabling `Enhanced Chests` is enough.
4. Click `Done`

#### Better Beds

Some versions of FO include Better Beds instead.

1. Close the game
2. Remove or disable the Better Beds mod from your launcher.
3. Start the game and see if it is fixed.

#### FastChest (FO 1.12.3 and older)

1. Click `Mods`
2. Search for "FastChest", click the config button ![](https://i.ibb.co/j35cBtn/image.png)
3. Disable the mod, click `Done`.

### Core shaders/incompatible with Sodium

![Resource packs may be incompatible with Sodium](https://github.com/Fabulously-Optimized/wiki/assets/8611110/0049c401-2922-4d03-976b-44bbf4fcc6a9)
![Resource packs are incompatible with Sodium](https://github.com/Fabulously-Optimized/wiki/assets/8611110/3116448a-53fe-4af0-9520-99c061694ba0)

Does the resource pack change the UI beyond usual means (e.g. rearrange HUD elements)? 

That means it may depend on [core shaders](getting-shaders.md#core-shaders), which are not fully supported on FO.

### Custom colors

Please ensure you're using FO 5.9.0 or newer; or FO 4.5.7 or older.

### Custom entity models

_Or "mobs with a custom shape"._

[Fresh Animations](https://www.curseforge.com/minecraft/texture-packs/fresh-animations)' latest version is fully supported. 

If the entities are missing parts of their body, try this:

1. Click `Mods`
2. Search for "Entity Model Features", click the config button (top right, above `Issues`)
3. Set "Substitute missing model parts" to `Yes`
4. Click `Save changes` and `Done`

Issues and workarounds are tracked [on the mod's Discord](https://discord.com/invite/rURmwrzUcz) or [GitHub](https://github.com/Traben-0/Entity_Model_Features/issues).

<details>
  <summary>Legacy versions - 4.6.0 and earlier</summary>

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

</details>
