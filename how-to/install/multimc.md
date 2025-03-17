---
hidden: true
---

# MultiMC

[MultiMC](https://multimc.org/) does not support automatic updates by default. However, FO has developed a custom MultiMC pack to perform updates automatically. Read more about the [MultiMC auto-updating pack](multimc.md#how-does-it-work)

{% hint style="info" %}
You may also want to use one of the other [launchers supported by FO](./), which offer easier installation, updates and mod management.
{% endhint %}

{% tabs %}
{% tab title="Automatic Updates (recommended)" %}
1. Download and install [Java 21](https://download.fo/java21)
2. Download FO's MultiMC pack for your preferred Minecraft version from [GitHub Releases](https://github.com/Fabulously-Optimized/fabulously-optimized/releases):
   * [`1.21.4`](https://github.com/Fabulously-Optimized/fabulously-optimized/releases/download/v6.5.0-beta.3/Fabulously.Optimized.MC.1.21.4.auto-update.zip)
   * [`1.21.3`](https://github.com/Fabulously-Optimized/fabulously-optimized/releases/download/v6.4.0-alpha.5/Fabulously.Optimized.MC.1.21.3.auto-update.zip)
   * [`1.21.1`](https://github.com/Fabulously-Optimized/fabulously-optimized/releases/download/v6.3.0/Fabulously.Optimized.MC.1.21.1.auto-update.zip)
   * [`1.20.6`](https://github.com/Fabulously-Optimized/fabulously-optimized/releases/download/v5.12.0-beta.11/Fabulously.Optimized.MC.1.20.6.auto-update.zip)
   * [`1.19.4`](https://github.com/Fabulously-Optimized/fabulously-optimized/releases/download/v4.10.0/Fabulously.Optimized.MC.1.19.4.auto-update.zip)
   * [`1.18.2`](https://github.com/Fabulously-Optimized/fabulously-optimized/releases/download/v3.12.2/Fabulously.Optimized.MC.1.18.2.auto-update.zip)
   * [`1.17.1`](https://github.com/Fabulously-Optimized/fabulously-optimized/releases/download/v3.2.3/Fabulously.Optimized.MC.1.17.1.auto-update.zip)
   * [`1.16.5`](https://github.com/Fabulously-Optimized/fabulously-optimized/releases/download/v3.2.3/Fabulously.Optimized.MC.1.16.5.auto-update.zip)
3. If you do not want the latest version, you can find older ones in [GitHub Releases](https://github.com/Fabulously-Optimized/fabulously-optimized/releases)
4. Open [**MultiMC**](https://multimc.org/)
5. Drag the `zip` file and drop it inside of MultiMC's window. A window should pop up
6. Click **OK** in that window. Something should happen <!-- TODO: what though?? -->
7. Double-click on that window. The download should start
8. If you are asked to download a mod manually:
   1. Open the given address in your browser. The mod's page should open up
   2. Click on **Cancel Launch**
   3. Click on **Download**. A `jar` file should be downloaded
   4. Go back to **MultiMC**
   5. Click on the instance you just created
   6. Click on **View Mods**
   7. Drag the mod you downloaded in _step 8.3_ and drop it in the mod list
9. Click on **Launch**. Minecraft should open up
10. If you can see `Fabulously Optimized` in the bottom-right corner, you're done!

## How Does It Work?

The MultiMC auto-updating pack launches [`packwiz`](https://github.com/comp500/packwiz) every time it is opened. `packwiz` is a mod handling tool which will add and update any missing FO mods indicated in a `pack.toml` file.

Since the update checker runs on every launch, you'll get a skippable error if you play offline. The updater only manages FO's mods, not the [mods added manually](../add-mods/multimc.md). The updater does not work across Minecraft versions, so you'll need to install it again every time.

MultiMC does not natively support automatic updates of packs: see [issue #2640](https://github.com/MultiMC/MultiMC5/issues/2640) and [issue #3037](https://github.com/MultiMC/MultiMC5/issues/3057). FO chose to use `packwiz` because it is also used for the [vanilla installer](vanilla.md).

Before FO 6.0.0, the MultiMC auto-updating pack was distributed on CurseForge, but that has changed for the following reasons:

* CurseForge's UI for downloading the MultiMC auto-updating pack became confusing
* The pack had to be re-uploaded on every update, which was often unnecessary
* The pack's downloads via CurseForge [might not support FO](https://support.curseforge.com/en/support/solutions/articles/9000197898-rewards-program-terms-of-service#1.-Description-of-Rewards-Program) as previously thought
* The pack proved to have unexpected issues that do not exist with other launchers
{% endtab %}

{% tab title="Easier Installation" %}
1. Download and install [Java 21](https://download.fo/java21)
2. In [**MultiMC**](https://multimc.org/), click on **Add Instance**
3. Click on the **Modrinth** tab on the left
4. Click on **Fabulously Optimized**
5. If you do not want the latest version of FO, select the version you want from the dropdown
6. Click on **OK**. Once installed, something should happen <!-- TODO: what though ?? -->
7. Double-click on the icon. Minecraft should open up
8. If you can see `Fabulously Optimized` in the bottom-right corner, you're done!
{% endtab %}
{% endtabs %}
