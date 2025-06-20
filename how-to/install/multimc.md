---
hidden: true
---

# MultiMC

[MultiMC](https://multimc.org/) does not support automatic updates by default. However, FO has developed a custom MultiMC pack to perform updates automatically. Read more about the [MultiMC auto-updating pack](multimc.md#how-does-it-work)

{% tabs %}
{% tab title="Automatic Updates" %}
{% hint style="warning" %}
While this variant allows for automatic updates within a specific Minecraft version, it is more difficult to update across Minecraft versions and to disable FO's mods.

Consider using [Prism Launcher](prism-launcher.md), which has a similar interface and a version manager.
{% endhint %}

1. Download and install [Java 21](https://download.fo/java21)
2. Download FO's MultiMC pack for your preferred Minecraft version from [GitHub Releases](https://github.com/Fabulously-Optimized/fabulously-optimized/releases):

   <a class="button primary" href="https://github.com/Fabulously-Optimized/fabulously-optimized/releases/download/v6.6.0-alpha.8/Fabulously.Optimized.MC.1.21.5.auto-update.zip">1.21.5</a>
   <a class="button secondary" href="https://github.com/Fabulously-Optimized/fabulously-optimized/releases/download/v6.6.0-alpha.8/Fabulously.Optimized.MC.1.21.4.auto-update.zip">1.21.4</a>
   <a class="button secondary" href="https://github.com/Fabulously-Optimized/fabulously-optimized/releases/download/v6.6.0-alpha.8/Fabulously.Optimized.MC.1.21.1.auto-update.zip">1.21.1</a>
   <a class="button secondary" href="https://github.com/Fabulously-Optimized/fabulously-optimized/releases/download/v5.12.0-beta.11/Fabulously.Optimized.MC.1.20.6.auto-update.zip">1.20.6</a>
   <a class="button secondary" href="https://github.com/Fabulously-Optimized/fabulously-optimized/releases/download/v4.10.0/Fabulously.Optimized.MC.1.19.4.auto-update.zip">1.19.4</a>
   <a class="button secondary" href="https://github.com/Fabulously-Optimized/fabulously-optimized/releases/download/v3.12.2/Fabulously.Optimized.MC.1.18.2.auto-update.zip">1.18.2</a>
   <a class="button secondary" href="https://github.com/Fabulously-Optimized/fabulously-optimized/releases/download/v3.2.3/Fabulously.Optimized.MC.1.17.1.auto-update.zip">1.17.1</a>
   <a class="button secondary" href="https://github.com/Fabulously-Optimized/fabulously-optimized/releases/download/v3.2.3/Fabulously.Optimized.MC.1.16.5.auto-update.zip">1.16.5</a>
3. If you do not want the latest version, you can find older ones in [GitHub Releases](https://github.com/Fabulously-Optimized/fabulously-optimized/releases)
4. Open [**MultiMC**](https://multimc.org/)
5. Drag the `zip` file and drop it inside of MultiMC's window. A window should pop up
6. Click on <kbd>**OK**</kbd> in that window. Something should happen
7. Double-click on that window. The download should start
8. If you are asked to download a mod manually:
   1. Open the given address in your browser. The mod's page should open up
   2. Click on <kbd>**Cancel Launch**</kbd>
   3. Click on <kbd>**Download**</kbd>. A `jar` file should be downloaded
   4. Go back to **MultiMC**. You should find a new instance
   5. Click on the <kbd>**Fabulously Optimized**</kbd> instance
   6. Click on <kbd>**View Mods**</kbd>
   7. Drag the mod you downloaded in _step 8.3_ and drop it in the mod list
9. Click on <kbd>**Launch**</kbd>. Minecraft should open up
10. If you can see `Fabulously Optimized` in the bottom-right corner, you're done!

### How Does It Work?

The MultiMC auto-updating pack launches [`packwiz`](https://github.com/comp500/packwiz) every time it is opened. `packwiz` is a mod handling tool which will add and update any missing FO mods indicated in a `pack.toml` file.

Since the update checker runs on every launch, you'll get a skippable error if you play offline. The updater only manages FO's mods, not the [mods added manually](../add-mods/multimc.md). The updater does not work across Minecraft versions, so you'll need to install it again every time.

MultiMC does not natively support automatic updates of packs: see [issue #2640](https://github.com/MultiMC/MultiMC5/issues/2640) and [issue #3037](https://github.com/MultiMC/MultiMC5/issues/3057). FO chose to use `packwiz` because it is also used for the [vanilla installer](vanilla.md).
{% endtab %}

{% tab title="Easier Installation" %}
{% hint style="warning" %}
Installing FO through these instructions means that every update will require manual configuration.

Consider using [Prism Launcher](prism-launcher.md), which has a similar interface and a version manager.
{% endhint %}

1. Download and install [Java 21](https://download.fo/java21)
2. In [**MultiMC**](https://multimc.org/), click on <kbd>**Add Instance**</kbd>
3. Click on the <kbd>**Modrinth**</kbd> tab on the left
4. Click on <kbd>**Fabulously Optimized**</kbd>
5. If you do not want the latest version of FO, select the version you want from the dropdown
6. Click on <kbd>**OK**</kbd>. Once installed, something should happen
7. Double-click on the icon. Minecraft should open up
8. If you can see `Fabulously Optimized` in the bottom-right corner, you're done!
{% endtab %}
{% endtabs %}
