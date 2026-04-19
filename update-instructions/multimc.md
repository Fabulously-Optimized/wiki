# MultiMC

{% tabs %}
{% tab title="Default" %}

{% hint style="info" %}
Consider [switching to Prism Launcher](../install-instructions/prism-launcher.md) or using the [MultiMC (auto-update) variant](../install-instructions/multimc.md#auto-update) instead for an easier update process. 
{% endhint %}

1. Click `Add Instance`
2. Select `Modrinth` tab from the left
3. Select "Fabulously Optimized"
4. Click on the version dropdown
5. Select the version that matches your current or has a newer Minecraft version
6. Click `OK`. The modpack will now install.
7. Click that version you just created, then `Minecraft Folder`
8. Click the previous version, then `Minecraft Folder`
9. Copy the important files and folders over:
   * `saves` - your local worlds
   * `resourcepacks` - if you added any (it is not needed to copy [the modpack defaults](changed-options.md#resource-packs))
   * `shaders` - if you use any
   * `screenshots` - screenshots you've taken with F2 or F9
   * `servers.dat` - your multiplayer servers
   * `options.txt` - if you want to keep your vanilla option and all hotkey changes
   * Ignore the `Copy all 3 folders!` file, that's for vanilla launcher users 
10. Close the folders and run the new version
11. If everything looks right, delete the old version

{% hint style="warning" %}
Never update to an older version, this could corrupt your worlds and settings!

Never update to an alpha or beta from a release version, [install a separate instance](../install-instructions/multimc.md) for testing.
{% endhint %}

{% endtab %}

{% tab title="Auto-update" %}

{% tabs %}
{% tab title="Same Minecraft version" %}

1. Run the existing version, wait for the progress bar to fill up
   * If you get a popup "This modpack uses new versions of the following...", just click `Update`.
2. Check the version difference in the bottom right corner.

{% endtab %}

{% tab title="Newer Minecraft version" %}

{% hint style="info" %}
Before updating, ensure that the modpack [has already been built for that Minecraft version](https://modrinth.com/modpack/fabulously-optimized/versions).
{% endhint %}

1. Go to the existing instance, click `Edit Instance`
2. Go to `Settings` on the left, then `Custom commands`
3. On `Pre-launch command`, you see a long text. Scroll to the rightmost edge.
4. It will say something like _.../main/Packwiz/**1.21.11**/pack.toml_. Change the Minecraft version to a newer one.
5. Click `Launch`.
6. You should see a popup saying "This modpack uses newer versions of the following..." - click `Update`.
7. You're done - the instance is now using an updated Minecraft version.

{% hint style="warning" %}
Never update to an older version, this could corrupt your worlds and settings!

Never update to an alpha or beta from a release version, [install a separate instance](../install-instructions/multimc.md) for testing.
{% endhint %}

{% endtab %}
{% endtabs %}

<details>
  <summary>Got asked to download a mod manually?</summary>

  If you get asked to download a specific jar, it means we are not allowed to bundle it and you must add it manually:

  1. Copy and paste the given address to your browser
  2. Click `Cancel Launch`
  3. Click `Download` on the mod
  4. On MultiMC, click on the instance, then click `View Mods`
  5. Drag the downloaded mod into the mod list
  6. Click `Launch`

</details>

{% endtab %}
{% endtabs %}