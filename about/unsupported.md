---
hidden: true
icon: ban
---

# Unsupported

FO is a Fabric pack for Minecraft: Java Edition. Because of this, it does not support the following platforms:

## Bedrock Edition

FO is a pack for Minecraft: Java Edition, so it does not support Bedrock at all.

However, one of [FO's principles](./#familiarity) is focusing on parity with Bedrock Edition if possible.

## Other Modpacks

FO does not officially support nor recommend being installed with other modpacks, because conflicts would most likely arise.

You may want to [add custom mods](../how-to/add-mods/) instead.

{% hint style="info" %}
If you still want to do it on your responsibility, you may install the other modpack first, then copy FO's files on it. See the [manual tab in the vanilla installation instructions](../how-to/install/vanilla.md).

Note that you will not be able to get help from FO, and probably not from the other modpack either.
{% endhint %}

## Other Loaders

FO is based on [Fabric](fabric.md), and does not support other mod loaders.

### NeoForge

FO does not support [NeoForge](https://neoforged.net/).

FO does not plan on ever supporting NeoForge, because it is slower, it takes longer to update, and it does not support Fabric's optimizations.

If you're coming from NeoForge, you can find a community-maintained [list of Fabric mods corresponding to NeoForge mods](https://gist.github.com/TrueCP6/4853f15015b210fd3b1e210e9e485f83). See [how to add mods to FO](../how-to/add-mods/). There is also work being done to support NeoForge mods on Fabric, via [PatchWork](https://patchworkmc.net/).

### Quilt

FO does not support [Quilt](https://quiltmc.org/).

FO is tracking the sustainability and popularity of Quilt in [issue #257](https://github.com/Fabulously-Optimized/fabulously-optimized/issues/257). If many mods decide to migrate to Quilt, FO may support it in the future.

## Game Clients

FO is not compatible with "game clients", including "PvP clients".

You may want to [add custom mods](../how-to/add-mods/) instead.

FO itself is not a client for the following reasons:

* We would have to maintain more code, which is beyond FO's objective
* We would need explicit permission from all mod authors
* The authors would likely receive no benefits from the client
* We would get less flexibility in what we can do with FO
* We would need a way to keep it sustainable, such as ads or similar

## Other Launchers

FO officially supports the [installation on five launchers](../how-to/install/). That does not mean the installation on other launchers is impossible, but FO will not be able to help you in such case.

### ATLauncher

ATLauncher is not supported because of its confusing and complex interface. However, if that changes, FO may support ATLauncher.

### GDLauncher Carbon

FO may support [GDLauncher Carbon](https://gdlauncher.com/en/blog/curseforge-partnership-announcement) in the future.

### GDLauncher Legacy

GDLauncher Legacy is not supported because it is outdated and it has other technical issues.

Follow these instructions to migrate to [Prism Launcher](https://prismlauncher.org/):

1. Open **GDLauncher Legacy**
2. Right-click on the previously-used instance
3. Click on **Open Folder**
4. Follow the [FO installation instructions for Prism Launcher](../how-to/install/prism-launcher.md)
5. In Prism Launcher, click on the **Folder** button on the left
6. Move the following files from the folder you opened in _step 3_ to the folder you opened in _step 5_:
   * `saves`: Your local worlds
   * `resourcepacks`: Your resource packs, if any. If you're asked to replace files, do not!
   * `shaders`: Your shaders, if any
   * `screenshots`: Your screenshots, if any
   * `server.dat`: Your multiplayer servers, if any
   * `options.txt`: Your custom options and keybinds, if any. If you want the [recommended FO settings](../info/options.md), do not copy it
7. Check if the instance in Prism Launcher works
8. Uninstall GDLauncher Legacy

### Pojav Launcher

Pojav Launcher is not supported because of the following drawbacks:

* Long installation process
* High energy usage
* Poor performance

However, FO may support Pojav Launcher in the future.

### PolyMC

{% hint style="danger" %}
PolyMC is compromised! You should switch away immediately!

Follow these instructions to migrate to [Prism Launcher](https://prismlauncher.org/), a safe fork of PolyMC.
{% endhint %}

1. Uninstall PolyMC
2. Install [Prism Launcher](https://prismlauncher.org/)
3. Open **Prism Launcher**. You should get a prompt
4. Pay attention to what the prompt says. If it says:
   * > It looks like you used PolyMC before. Do you want to migrate your data to the new location of Prism Launcher?
     * Click **Yes** to migrate automatically
   * > Old data from PolyMC was found, but you already have existing data for Prism Launcher. Sadly you will need to migrate yourself. Do you want to be reminded of the pending data migration next time you start Prism Launcher?
     1. Click **No** to close the prompt
     2. Open PolyMC's `instances` directory:
        * Windows: `%APPDATA%/PolyMC/instances`
        * macOS: `~/Library/Application Support/PolyMC/instances`
        * Linux: `~/.local/share/PolyMC/instances`
        * Portable: `PolyMC/instances`
     3. Copy all files and folders from that folder
     4. In Prism Launcher, click on **Folders**
     5. Click on **View Instance Folder**
     6. Paste the files you copied in _step 3_ in the folder you opened in _step 5_
     7. Close and reopen Prism Launcher. You should find all of your instances there
     8. Sign into your accounts and complete Prism Launcher's configuration
5. Follow the [FO installation instructions for Prism Launcher](../how-to/install/prism-launcher.md)

### Cracked launchers

FO does not support any launcher that lets you run the game without having purchased it. Choose and use one of the [five launchers supported by FO](../how-to/install/).

{% hint style="success" %}
There is a way to obtain Minecraft for cheaper: You can get a [gift code from a trusted reseller (affiliate link)](https://download.fo/minecraft)! Thank you!
{% endhint %}

#### TLauncher

{% hint style="danger" %}
TLauncher is malware! You should [reset your entire OS](https://howtogeek.com/202590/stop-trying-to-clean-your-infected-computer-just-nuke-it-and-reinstall-windows)!
{% endhint %}
