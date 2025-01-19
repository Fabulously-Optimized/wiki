---
hidden: true
---

# MultiMC

{% hint style="danger" %}
**You should ALWAYS [make backups](../backup/multimc.md) before updating**.

As with any other piece of software, updates may go wrong for many reasons, including but not limited to: the launcher, the hardware, your custom configuration, the mods you added... and, rarely, FO as well.
{% endhint %}

{% hint style="success" %}
If you had installed [FO on MultiMC **with** automatic updates](../install/multimc.md#automatic-updates), and you're not updating to a newer version of Minecraft, you just need to open the existing versions.

If you get a popup saying **This modpack uses new versions of the following...**, click on the **Update** button.
{% endhint %}

If you had installed [FO on MultiMC **without** automatic updates](../install/multimc.md#easier-installation), or if you're updating to a new version of Minecraft:

1. Follow the [FO installation instructions for MultiMC](../install/multimc.md) again. This will create a new instance
2. In **MultiMC**, click on the previous version
3. Click on **Minecraft Folder**
4. Click on the new version as well
5. Click on **Minecraft Folder**
6. Copy the following files from the folder you opened in _step 3_ to the folder you opened in _step 5_:
   * `saves`: Your local worlds
   * `resourcepacks`: Your resource packs, if any. If you're asked to replace files, do not!
   * `shaders`: Your shaders, if any
   * `screenshots`: Your screenshots, if any
   * `server.dat`: Your multiplayer servers, if any
   * `options.txt`: Your custom options and keybinds, if any. If you want the [recommended FO settings](../info/options.md), do not copy it
7. Once you've moved them, launch the new instance. Minecraft should open up
8. If you can see the newly installed version in the bottom-right corner, you can delete the previous version from _step 2_
