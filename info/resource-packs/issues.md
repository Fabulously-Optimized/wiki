---
hidden: true
---

# Resource Pack Issues

One of [FO's objectives](../../about/) is to [support OptiFine features](../../about/optifine.md), but unfortunately some problems with resource packs may arise.

This is because many times OptiFine's features are internally broken, or they change between versions, so external implementations try to mimic them but may fall short.

Here are some solutions you, as the user, may try to get your OptiFine resource packs working with FO. Many times, though, the problem has to be fixed by the creator.

## Old Versions

Some resource packs are built for versions of Minecraft older than what you may be playing on. If so, you may try to use the [Mojang-provided Slicer tool](https://github.com/Mojang/slicer) to convert them automatically. Alternatively, use the [unofficial mod by `agentdid127`](https://agentdid127.com/ResourcePackConverter).

## Broken Paths

You may see the following message while activating a broken resource pack:

![Contains broken paths](https://i.ibb.co/26cMtqr/Screenshot-20211116-191457.png)

You may try to apply the resource pack anyway, but you'll probably encounter many issues and glitches if you do so.

This is the creator's fault, who's using spaces or other non-standard characters in files' and folders' names. You should tell the creator to only use the following characters: `a-z0-9._-`

Read more on the [Minecraft Wiki's page](https://minecraft.wiki/w/Resource_location#Legal_characters).

## Full Brightness

Editing `options.txt` to change the game's brightness beyond 100% ("fullbright") has not worked since [Minecraft 1.19](https://bugs.mojang.com/browse/MC-51418). OptiFine-based resource packs of this kind might work with FO.

We recommend [adding a mod](../../how-to/add-mods/) like [Gamma Utils](https://modrinth.com/mod/gamma-utils) or [other similar mods](https://modrinth.com/mods?q=gamma&g=categories:fabric).

{% hint style="warning" %}
Beware: such changes to the game may be disallowed on some servers. Remember to verify mods you add are not against the rules.
{% endhint %}

## Invisible Block Entities

Some re-texturing of block entities may not work by default in FO.

{% tabs %}
{% tab title="Enhanced Block Entities" %}
1. In the Mod Menu, find "Enhanced Block Entities"
2. Click on the **Config** button ![config](https://i.ibb.co/j35cBtn/image.png)
3. Enable **Force Resource Pack Compatibility**
4. If you can't find such an option, disable optimization of broken blocks. For example, for chests disable **Enhanced Chests**
5. Click on **Done**
{% endtab %}

{% tab title="Better Beds" %}
Follow [instructions to disable the Better Beds mod](../../how-to/disable-mods/).
{% endtab %}

{% tab title="FastChest" %}
FO version 1.12.3 and older

1. In the Mod Menu, find "FastChest"
2. Click on the **Config** button ![config](https://i.ibb.co/j35cBtn/image.png)
3. Disable the mod
4. Click on **Done**
{% endtab %}
{% endtabs %}

## Core Shaders

[Core shaders](../mods/shaders.md), for example those which rearrange HUD elements, are not fully supported by FO.

![Resource packs may be incompatible with Sodium](https://github.com/Fabulously-Optimized/wiki/assets/8611110/0049c401-2922-4d03-976b-44bbf4fcc6a9)
![Resource packs are incompatible with Sodium](https://github.com/Fabulously-Optimized/wiki/assets/8611110/3116448a-53fe-4af0-9520-99c061694ba0)

## Custom Colors

Custom colors are only supported in FO version 5.9.0 or newer, or FO version 4.5.7 or older.

## Custom Entity Models

{% tabs %}
{% tab title="FO version 4.6.0 or newer" %}
If parts of the entities' bodies are missing, or custom mob shapes are not working:

1. In the Mod Menu, find "Entity Model Features"
2. Click on the **Config** button ![config](https://i.ibb.co/j35cBtn/image.png)
3. Set **Substitute missing model parts** to **Yes**
4. Click on **Save Changes**
5. Click on **Done**

Find more details on [Entity Model Features' issue tracker](https://github.com/Traben-0/Entity_Model_Features/issues) or on their [Discord server](https://discord.com/invite/rURmwrzUcz).
{% endtab %}

{% tab title="FO version 4.6.0 or older" %}
Find a [list of resource packs supported by CEM](https://github.com/dorianpb/cem/issues/9), and a [list of features supported by CEM](https://github.com/dorianpb/cem#differences).

In particular, this [version of Fresh Animations](https://www.curseforge.com/minecraft/texture-packs/fresh-animations/files/3705824) works. Discuss issues in the [Fresh Animations' issue](https://github.com/dorianpb/cem/issues/11).

1. In the Mod Menu, find "Custom Entity Models"
2. Click on the **Config** button ![config](https://i.ibb.co/j35cBtn/image.png)
3. Set **Use model creation fix?** to **No**
4. Click on **Save & Quit**
5. Click on **Done**
6. In a world, press **`F3`** + **`T`**. You'll see a loading screen
7. Verify if the models are displayed correctly
8. If not, custom models will not work. You should either:
   * Re-enable the option you changed in _step 3_, and disable the resource pack
   * Disable the **OptiFine** option, and keep the resource pack without the models
{% endtab %}
{% endtabs %}
