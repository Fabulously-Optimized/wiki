# Chat Reporting FAQ

### What's the deal with chat reporting?

In Minecraft 1.19.1 and up, players can report other players' chat messages to Mojang, which may result in a temporary or permanent ban from all multiplayer servers, on all versions of Minecraft: Java Edition.

See [the official help page](https://help.minecraft.net/hc/en-us/articles/7149823936781-Player-Reporting-in-Minecraft-Java-Edition) to read about the reporting interaction and offense categories or keep reading to see how it affects you.

### Why is it bad?

* **Banned from all multiplayer** - instead of getting punished on one server, you are getting punished on all, including Realms and others' LAN servers. Maybe you just got angry and sweared at someone on one server and want to go to another to relax again? Nope, cannot do that.

* **Realms subscriptions don't get cancelled** - if you get banned, Mojang will not automatically cancel any Realms servers you own, meaning you'll continue to pay for server(s) you cannot access or control. This makes sense for short-term bans like up to a week, but any longer than that should give an explicit option at least.

* **Not sent to server admins** - sending reports to Mojang will result in different judgement and outcomes of the cases - while server admins could punish faster, with a shorter penalty, with different kinds of punishments like mutes and jails, Mojang can only ban people from the entirety of multiplayer or not punish at all.

* **Report reviewers lack context** - players can select 1-4 messages, to which the system will add up to 7 messages before and 2 after the selected ones - at most 40 messages in total. That is a very partial context for serious offenses as it is missing player builds, signs, books, Discord/forum messages, daily general behavior etc.

* **Fairness doesn't scale** - Minecraft has a huge playerbase and if lots of players play it, lots can report each other as well. How can Mojang guarantee a _fair action_ to be done on _thousands_ of reports every day? Compare that to a single server that has less players, therefore less reports and less admins needed.

* **Categories don't match server rules** - for example, there can be an adult-only server that may discuss things like alcohol freely, but when an underage player stumbles upon it, they can report others for things that are clearly allowed and intended by the server.
   
* **Categories are vague** - for example, take the rule "impersonation". How can one be sure a person is who they claim to be with just a few lines of chat? Are they just going to assume it is a lie and ban them? At that point players can not even say who they are because they can get punished either way.

* **Ban reasons and appeals are vague** - [while there is a way to appeal](#what-if-i-still-got-banned), it is not described when and how many times it will be accepted. The fact that _some_ bans are temporary is not really the solution - an unjust ban is an unjust ban. [This issue has already been prevalent in Bedrock Edition.](https://youtu.be/kEfyaAq90kg?t=108)

This is a non-exhaustive list. People have voiced more concerns in various Minecraft communities and the feedback site, search around.

#### Explanatory videos

- [Simple explanation](https://youtu.be/rdoFUhd0EkI)
- [Timeline of events](https://youtu.be/kEfyaAq90kg)
- [Technical explanation (as of 1.19.2)](https://youtu.be/DobmW1ZUcbQ?t=10)
- [Clearing others' misconceptions](https://youtu.be/bF_37BrWBSM?t=87)

_Some parts of the videos may be out of date, mainly the report categories and exploits. Problems with ethics and overall technical approach still remain._

#### Official posts

- [Blog post](https://www.minecraft.net/en-us/article/addressing-player-chat-reporting-tool)
- [FAQ](https://help.minecraft.net/hc/en-us/articles/7317376541197)

### What does FO do to protect me?

Fabulously Optimized has added a mod called [No Chat Reports](https://www.curseforge.com/minecraft/mc-mods/no-chat-reports) that informs you of the availability of chat reporting and makes your messages unreportable on servers that do not require it. It also reverts most of the chat indicators added in 1.19.1, because they clutter the screen and are misleading in many cases.

Look at the right corner of the chat window:
- ![red ⚠️](https://i.ibb.co/tzd8CvB/red.png) - you are vulnerable, any chat messages you send may be reported and used against you.
- ![yellow ℹ️](https://i.ibb.co/YXQdJRr/yellow.png) - nobody can report your messages. Depending on the server, other players may see a red bar on the left of the message, ![red markings](https://i.ibb.co/ftRMqHL/exclamation.png) on the right and if they enable the vanilla `Only Show Secure Chat` option, they may not see your chat messages at all. 
  - In practice, these mentioned chat side effects will likely only occur on few vanilla servers that upgrade from 1.19. Most servers will take a stance to either enforce or disable chat reporting for everyone.
  - Unfortunately ![yellow ℹ️](https://i.ibb.co/YXQdJRr/yellow.png) is what most 1.19+ servers will show, even if the server has additional protections in place. You can assume the state of reportability by looking at the availability of report button in Social Interactions, or just ask an admin.
- ![green ✅](https://i.ibb.co/LPXNKRM/green.png) - you can chat securely. Nobody can report anyone, nobody has a red bar or ![red markings](https://i.ibb.co/ftRMqHL/exclamation.png) on the chat and nobody's chat will get hidden by `Only Show Secure Chat`.

The report button itself still works on servers that allow reporting. _Please use it only in case of real danger!_

Also, FO has disabled chat previews since the first 4.0.0 alpha, this protects your messages from being sent to the server before you actually press Enter.

### Is No Chat Reports itself a risk?

No. All it does in the client (and therefore in FO) is to disable chat signing on most servers and enable it for only those that demand it, plus show an icon/tooltip to indicate the current state of the server.

### Can I use exploits to break the system/avoid getting reported?

No, that makes you more likely to get banned. It is up to the server to decide whether they want the reporting system or not, use that information to choose the servers you play in.

Fabulously Optimized will not include or endorse any exploits.
 
### Why not stay on 1.19?

Despite the report button not being there, the chat signing already exists in it, so it is not any safer than 1.19.1+. If you want to stay on an older version, please use the latest version for 1.18.2.

### Why not stay on 1.18.2?

It is safe from reports so you are free to play it for as long as you like. The modpack will still focus on "fixing" the new version(s) rather than continuously updating the old one.  

### What if someone really breaks the rules?

Do what you always did.

- If an user is being annoying, hide their messages by clicking the chat icon near the username in Social Interactions or, in some servers, `/ignore (username)`.
- If an user has broken the rules of the server, report it to server administration. This is usually done by `/report`, `/helpop`, server forum or Discord.
- If an user is talking about commiting suicide, talk to them and [give local help resources](https://en.wikipedia.org/wiki/List_of_suicide_crisis_lines). 
- If an user is doing or threatening illegal actions, report it to server admins and local police. Provide them with as much context as possible, including screenshots.

### What if I still got banned?

If you feel like you've been banned unfairly, [see "How to submit a case review" here to appeal](https://www.minecraft.net/en-us/community-standards#main-content). Fill the form throughly with any information you have and make sure you select "Minecraft: Java" as the game. After submitting simply wait for their response and hope for the best.

Fabulously Optimized does not condone any form of ban evasion, do not even ask.

### I am a server owner. How can I protect my users?

See [server setup](server-setup.md). If you are a player, you can send that page to your server admins.

[As said above](#what-does-fo-do-to-protect-me), most of those methods will still show ![yellow ℹ️](https://i.ibb.co/YXQdJRr/yellow.png) in chat, so do inform your users as well.

### I want to give feedback to Mojang.

Great! Use the [official feedback site](https://feedback.minecraft.net/hc/en-us):
* [Give feedback on the chat reporting](https://feedback.minecraft.net/hc/en-us/community/posts/7320990094733-Player-Chat-Reporting-Feedback-)
* [The most popular request for reverting chat reporting](https://feedback.minecraft.net/hc/en-us/community/posts/6977558665997-Mojang-please-for-the-love-of-your-game-don-t-add-a-chat-report-feature-)
* [Overall snapshot category](https://feedback.minecraft.net/hc/en-us/community/topics/360001692331-Minecraft-Java-Edition-Snapshots?sort_by=votes)

### What would make the system fair?

One of the following:

- Sending the reports to server admins instead of Mojang would be the most preferable, as they have the most context to take the appropriate action and players would have a consistent way of reporting on every server.
- Making the whole system opt-in (or out) would also be reasonable as then only the servers that need this help would enable it.
- Implementing the system only on Realms or other Mojang-partnering servers.
- Not implementing the system at all because there are enough moderation tools built already.

This is a non-exhaustive list. People have posted more ideas in various Minecraft communities and the feedback site, search around.

### I still think the system is fair.

Understandable. 

If you join a server and see a ![red ⚠️](https://i.ibb.co/tzd8CvB/red.png) in the bottom right corner of the chat, that server enforces the report system and FO will adhere to it, just like vanilla. Because of that, having [No Chat Reports](https://www.curseforge.com/minecraft/mc-mods/no-chat-reports) does benefit you as well, because in vanilla itself there is no such clear indication (the toast and chat line icons do not accurately work on every server).

If you still want, you can [disable the mod](disabling-mods.md) No Chat Reports on your instance, which will disable the button-based chat indicator and show chat line-based vanilla indicators instead.

### I actually came here to learn, when will FO 4.x.x stable be released?

[Probably August, but more specifically whenever I'm confident in releasing it.](https://github.com/Fabulously-Optimized/fabulously-optimized/issues/343)

### I have more questions.

Write to `#support` [in our Discord](https://discord.gg/yxaXtaQqdB).
