# MultiMC

{% tabs %}
{% tab title="Default" %}

1. Download, install and launch [MultiMC](https://multimc.org) and Java
   * [Java 21](https://download.fo/java21) for Minecraft 1.21.x or [Java 25](https://download.fo/java25) for Minecraft 26.x
2. Click `Add Instance`
3. Select `Modrinth` tab from the left
4. Select "Fabulously Optimized"
5. Click `OK`
   * Optional: Select the version you want by selecting it on the dropdown before you click `OK`.
6. The modpack will now install.
7. Once installed, double-click the icon to play.

{% endtab %}
{% tab title="Auto-update" %}

1. Download, install and launch [MultiMC](https://multimc.org) and Java
   * [Java 21](https://download.fo/java21) for Minecraft 1.21.x or [Java 25](https://download.fo/java25) for Minecraft 26.x
2. Download the pack for your preferred Minecraft version: 
   * [26.1.2](https://github.com/Fabulously-Optimized/fabulously-optimized/releases/download/v13.2.0-alpha.3/Fabulously.Optimized.MC.26.1.2.auto-update.zip) | [1.21.11](https://github.com/Fabulously-Optimized/fabulously-optimized/releases/download/v12.0.0-alpha.2/Fabulously.Optimized.MC.1.21.11.auto-update.zip) | [1.21.10](https://github.com/Fabulously-Optimized/fabulously-optimized/releases/download/v11.1.0-beta.3/Fabulously.Optimized.MC.1.21.10.auto-update.zip) | [1.21.8](https://github.com/Fabulously-Optimized/fabulously-optimized/releases/download/v10.2.0-beta.4/Fabulously.Optimized.MC.1.21.8.auto-update.zip) | [1.21.5](https://github.com/Fabulously-Optimized/fabulously-optimized/releases/download/v9.1.0/Fabulously.Optimized.MC.1.21.5.auto-update.zip) | [1.21.4](https://github.com/Fabulously-Optimized/fabulously-optimized/releases/download/v6.6.0-alpha.8/Fabulously.Optimized.MC.1.21.4.auto-update.zip) | [1.21.1](https://github.com/Fabulously-Optimized/fabulously-optimized/releases/download/v6.6.0-alpha.8/Fabulously.Optimized.MC.1.21.1.auto-update.zip) | [1.20.6](https://github.com/Fabulously-Optimized/fabulously-optimized/releases/download/v5.12.0-beta.11/Fabulously.Optimized.MC.1.20.6.auto-update.zip) | [1.19.4](https://github.com/Fabulously-Optimized/fabulously-optimized/releases/download/v4.10.0/Fabulously.Optimized.MC.1.19.4.auto-update.zip) | [1.18.2](https://github.com/Fabulously-Optimized/fabulously-optimized/releases/download/v3.12.2/Fabulously.Optimized.MC.1.18.2.auto-update.zip) | [1.17.1](https://github.com/Fabulously-Optimized/fabulously-optimized/releases/download/v3.2.3/Fabulously.Optimized.MC.1.17.1.auto-update.zip) | [1.16.5](https://github.com/Fabulously-Optimized/fabulously-optimized/releases/download/v3.2.3/Fabulously.Optimized.MC.1.16.5.auto-update.zip)
   * Other versions can be found from [GitHub Releases](https://github.com/Fabulously-Optimized/fabulously-optimized/releases)
3. Drag the ZIP-archive to MultiMC window, and hit OK in the window that pops up.
4. Double-click that version you just created to download and launch the modpack

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

<details>
  <summary>How does this work?</summary>

It is a normal MultiMC modpack that simply launches [packwiz](https://github.com/comp500/packwiz), a mod handling tool on every start.

Every time you launch it, it asks the server whether the modpack has any updates. This means you do need internet access or you'll get an error (though you can skip the error).
If there are any, they will be downloaded and launched, otherwise the current game will launch. 

It does _not_ auto-update any individual mods outside of what is set in the the modpack.

</details>
{% endtabs %}

{% hint style="info" %}
Consider using Prism Launcher instead, as it has a similar interface but more features.
{% endhint %}