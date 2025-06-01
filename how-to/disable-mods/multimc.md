---
hidden: true
---

# MultiMC

{% hint style="danger" %}
Do NOT disable "API" or "library" mods, because the other mods need them.
{% endhint %}

Instructions vary depending on whether you had installed FO on MultiMC with the easier installation or with automatic updates.

<!-- TODO: instructions for manual installation? -->

{% tabs %}
{% tab title="Windows" %}
{% hint style="info" %}
Tutorial by [Ultrasonic1209](https://github.com/Ultrasonic1209) based on [Remty5's workaround](https://github.com/Fabulously-Optimized/fabulously-optimized/issues/81).
{% endhint %}

1. Open **MultiMC**
2. Right-click on <kbd>**Fabulously Optimized**</kbd>
3. Click on the <kbd>**Instance Folder**</kbd> button
4. While holding <kbd>⇧ Shift</kbd>, right-click inside of the folder
5. Click on <kbd>**Open in Terminal**</kbd> or <kbd>**Open with PowerShell**</kbd> or similar
6. Run the following commands to download the scripts that will disable the mods:

    ```powershell
    (Invoke-WebRequest -Uri "https://raw.githubusercontent.com/Fabulously-Optimized/fabulously-optimized/main/Packwiz/pre-launch.ps1" -OutFile "pre-launch.ps1")
    (Invoke-WebRequest -Uri "https://raw.githubusercontent.com/Fabulously-Optimized/fabulously-optimized/main/Packwiz/post-exit.ps1" -OutFile "post-exit.ps1")
    ```

    This should download two files: `pre-launch.ps1` and `post-exit.ps1`
7. Open `pre-launch.ps1` in a text editor. You should find a list of mods starting on _line 4_
8. Copy the name of the mod you want to disable
9. Paste the name of the mod in the line you found in _step 7_
10. Disable more mods by adding them under _line 4_ with the same format
11. Go back to **MultiMC**
12. Click on <kbd>**Fabulously Optimized**</kbd>
13. Click on <kbd>**Edit Instance**</kbd>
14. Replace the pre-launch command with the following:

```powershell
powershell -ExecutionPolicy Bypass -File ..\pre-launch.ps1
```

15. Replace the post-exit command with the following:

```powershell
powershell -ExecutionPolicy Bypass -File ..\pre-launch.ps1
```
{% endtab %}

{% tab title="Linux and macOS" %}
{% hint style="info" %}
Tutorial by [RaptaG](https://github.com/RaptaG) based on [Remty5's workaround](https://github.com/Fabulously-Optimized/fabulously-optimized/issues/81).
{% endhint %}

{% hint style="warning" %}
Not fully tested on macOS!
{% endhint %}

1. Open **MultiMC**
2. Right-click on <kbd>**Fabulously Optimized**</kbd>
3. Click on the <kbd>**Instance Folder**</kbd> button
4. Right-click inside of the folder
5. Click on <kbd>**Open in Terminal**</kbd>
   * On macOS follow [instructions to get the Terminal there](https://petenetlive.com/KB/Article/0001060)
6. Install [`jq`](https://stedolan.github.io/jq/download), which will automatically adapt the script to your Minecraft version
7. Run the following commands to download the scripts that will disable the mods:

    ```sh
    curl -Os 'https://raw.githubusercontent.com/Fabulously-Optimized/fabulously-optimized/main/Packwiz/pre-launch.sh' | curl -Os 'https://raw.githubusercontent.com/Fabulously-Optimized/fabulously-optimized/main/Packwiz/post-exit.sh' && chmod +x pre-launch.sh post-exit.sh
    ```

    This should download two files: `pre-launch.ps1` and `post-exit.ps1`
8. Open `pre-launch.ps1` in a text editor. You should find a list of mods starting on _line 6_
9. Copy the name of the mod you want to disable
10. Paste the name of the mod in the line you found in _step 8_
11. Disable more mods by adding them under _line 6_ with the same format
12. If you leave a line empty, delete the corresponding one starting on _line 28_
13. If you need to disable more than 6 mods, add lines both under `mod5=` and `$mod5.jar\`
14. Go back to **MultiMC**
15. Click on <kbd>**Fabulously Optimized**</kbd>
16. Click on <kbd>**Edit Instance**</kbd>
17. Replace the pre-launch command with the following:

```sh
../pre-launch.ps1
```

18. Replace the post-exit command with the following:

```sh
../pre-launch.ps1
```
{% endtab %}
{% endtabs %}
