# Backup and uninstall instructions

Sometimes you might want to reinstall the modpack or remove old instances of it. Here's how to do it.

## Backup

Before uninstalling the modpack, it is highly recommended to back up the contents you've made in it.

1. Open the `minecraft` folder:

{% tabs %}
{% tab title="CurseForge App" %}
Right click on the modpack tile → `Open Folder`
{% endtab %}
{% tab title="Modrinth App" %}
Right click on the modpack tile → `📂 Open folder`
{% endtab %}
{% tab title="Prism Launcher" %}
Right click on the instance → `Folder` → `.minecraft`
{% endtab %}
{% tab title="MultiMC" %}
Right click on the instance → `Minecraft Folder`
{% endtab %}
{% tab title="Minecraft Launcher" %}
Click `Installations` → hover on the instance → click `📁`
{% endtab %}
{% endtabs %}

2. Find the folders you want to back up.
   * `saves` - your local worlds
   * `resourcepacks` - if you added any (it is not needed to copy [the modpack defaults](changed-options.md#resource-packs))
   * `shaders` - if you use any
   * `screenshots` - screenshots you've taken with F2 or F9
   * `servers.dat` - your multiplayer servers
   * `config` - your mod options
   * `options.txt` - if you want to keep your vanilla option and all hotkey changes
3. Copy the chosen folders or their contents to your preferred location, such as Desktop or Documents.
4. When you reinstall the modpack, copy the folders/contents back to the aforementioned location.

## Uninstall

### CurseForge App

1. Open CurseForge App
2. Go to `My Modpacks`
3. Right click on Fabulously Optimized
4. Click `🗑️ Delete Profile`
5. Click `Delete`

### Modrinth App

1. Open Modrinth App
2. Open `|||\` "Library"
3. Right click on Fabulously Optimized
4. Click `🗑️ Delete`
5. Click `🗑️ Delete`

### Prism Launcher

1. Open Prism Launcher
2. Click on Fabulously Optimized
3. Click `🗑️ Delete`
4. Click `Yes`

### MultiMC/MultiMC (auto-update)

1. Open MultiMC
2. Click on Fabulously Optimized
3. Click `Delete`
4. Click `Yes`

### Minecraft Launcher (vanilla)

1. Open Minecraft Launcher, click on `Installations`
2. Hover on the `Fabulously Optimized` installation, click 📂
   * If you installed using the manual instructions, you'll instead see a `fabric-loader-x.x.x` installation (where x.x.x refers to the version number).
3. Delete `mods`, `config` and optionally `resourcepacks` folders
   * If you selected "Use a different `.minecraft` folder for this version?" during the install, your folder path will be `.../.minecraft/fabulously-optimized-x.x.x` instead of just `.../.minecraft`. 
In that case you may delete the entire `fabulously-optimized-x.x.x` folder (where x.x.x refers to the version number).
5. Go to `versions` folder inside `.minecraft` and delete all folders prefixed with `fabric-loader-`
6. Back in the launcher, hover on the installation and press `...`, then `Delete`
7. Press `Delete`
