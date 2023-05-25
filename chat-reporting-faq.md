# Chat Reporting FAQ

## About the system

### What is chat reporting?

In Minecraft 1.19.1 and up, players can report other players' chat messages to Mojang, which may result in a temporary or permanent ban from all multiplayer servers, on all versions of Minecraft: Java Edition.

### How are reports created?

[The official help page](https://help.minecraft.net/hc/en-us/articles/7149823936781-Player-Reporting-in-Minecraft-Java-Edition) states the following:

> Reporting can be accessed via the social interactions screen (default keybind is P) or via the pause menu. 
> 
> [...]
> 
> 1. A player creates a chat report, selects the offending messages, category and details, and submits it 
> 2. The report is sent to our team of Minecraft Investigators
> 3. A moderator reviews the report and the evidence and assigns an appropriate action (if any) 
> 4. If action is taken, the offending player’s account is suspended from online play for some duration of time or in extreme cases permanently 

### Why was it implemented?

[Minecraft: Java Edition Player Reporting FAQ](https://help.minecraft.net/hc/en-us/articles/7317376541197) states the following:

> [...] We need to provide safeguards that will help keep all our players safe and welcome in the online environments where they play Minecraft. Player Reporting will help to keep Minecraft communities free from hate speech, bullying, harassment, sexual solicitation, and personal threats. We believe that human moderation and community guidelines are critical to reducing harmful behavior and promoting healthy Minecraft online communities. 

### Why is it controversial?

Because the current implementation of it is vaguely described, unsustainable and unethical.

* **Banned from all multiplayer** - instead of getting punished on one server, you are getting punished on all, including Realms and others' LAN servers. Maybe you just got angry and sweared at someone on one server and want to go to another to relax again? Nope, cannot do that.

* **Some swearing is interpreted too strictly** - some swear words are interpreted as bannable offenses even if the players know each other and know that the other party will not get offended by it. [Read more from this Reddit post](https://www.reddit.com/r/Minecraft/comments/xfh3ee/suspended_from_playing_minecraft_for_swearing_in/)

* **Realms chat is constantly monitored** - [according to Our Commitment to Player Safety](https://help.minecraft.net/hc/en-us/articles/8047895358605-Our-Commitment-to-Player-Safety#h_01G95X76WR1PM97XBXDE7G25KE), they monitor all Realms chat and will take action regardless of whether you get reported and regardless of whether the other party actually took your message seriously or not. This was not possible before they introduced chat signing and global bans.

* **Realms subscriptions don't get cancelled** - if you get banned, Mojang will not automatically [pause the subscription](https://help.minecraft.net/hc/en-us/articles/4410000696077-Minecraft-Java-Edition-Realms-Billing-Issues-FAQ#h_01FGCST20673JYZ76PB9BN4BNK) of any Realms servers you own, meaning you'll continue to pay for server(s) you cannot access or control. This makes sense for short-term bans like up to a week, but any longer than that should give an explicit option at least.

* **Not sent to server admins** - sending reports to Mojang will result in different judgement and outcomes of the cases - while server admins could punish faster, with a shorter penalty, with different kinds of punishments like mutes and jails, Mojang can only ban people from the entirety of multiplayer or not punish at all.

* **Report reviewers lack context** - players can select 1-4 messages, to which the system will add up to 9 messages before the selected ones - at most 40 messages in total. That is a very partial context for serious offenses as it is missing player builds, signs, books, Discord/forum messages, daily general behavior etc.

* **Fairness doesn't scale** - Minecraft has a huge playerbase and if lots of players play it, lots can report each other as well. How can Mojang guarantee a _fair action_ to be done on _thousands_ of reports every day? The investigators may accidentally overlook a part of the conversation or misintepret the intent due to words used. Compare that to a single server that has less players, therefore less reports and less admins needed, appeals that are dealt with faster.

* **Categories don't match server rules** - for example, there can be an adult-only server that may discuss things like world politics, alcohol and drugs freely, but when an underage player stumbles upon it, they can report others for things that are clearly allowed and intended by the server.
   
* **Categories are vague** - for example, take the rule "impersonation". How can one be sure a person is who they claim to be with just a few lines of chat? Are they just going to assume it is a lie and ban them? At that point players can not even say who they are because they can get punished either way.

* **Ban reasons and appeals are vague** - [while there is a way to appeal](#is-there-a-way-to-appeal-the-ban), it is not described when and how many times it will be accepted. The fact that _some_ bans are temporary is not really the solution - an unjust ban is an unjust ban. [This issue has already been prevalent in Bedrock Edition.](https://youtu.be/kEfyaAq90kg?t=108)

* **Reports may not be sufficient** - in the case of most serious offenses (e.g. threatening, abuse, harassment), you should really feel that proper action is taken. With these reports, Mojang does not actually elaborate on [what their "appropriate actions" are](https://help.minecraft.net/hc/en-us/articles/7149823936781-Player-Reporting-in-Minecraft-Java-Edition#h_01GD13PG9R60SYNDV88FKFSHRH). They may send a player suicide prevention info for example, but there is no guarantee Mojang will contact the police for you. [Do it yourself!](#what-should-i-do-instead-when-someone-breaks-the-rules)

* **Servers can and do opt out** - most public servers, including Hypixel, have already opt out of the system. Obviously the system cannot work if servers opt out. This is another reason for the game to [add clear indication](#what-does-this-modpack-do-for-me) about whether a server enabled the system or not, instead of making players assume it is everywhere (or even nowhere).

This is a non-exhaustive list. People have voiced more concerns in various Minecraft communities and the feedback site, search around.

### Where can I learn more about it?

#### Explanatory videos

- [Explanation as of 1.19.3 by Aizistral](https://youtu.be/48H5nMQ_8Yg?t=79) (~7 min)
- [_Written_ technical explanation as of 1.19.3 by Aizistral](https://gist.github.com/Aizistral/61553d6d76b998da9a52afd49c9ead76#the-absolute-state-of-chat-reporting)
- [Explanation as of 1.19.2 by AntVenom](https://youtu.be/IKgucpgVraY) (~20 min)
- [Explanation as of 1.19.1-rc.1 by FitMC](https://youtu.be/rdoFUhd0EkI) (~10 min)
- [Timeline of events as of 1.19.1-rc.1 by TheMisterEpic](https://youtu.be/kEfyaAq90kg) (~14 min)
- [Technical explanation as of 1.19.2 by Aizistral](https://youtu.be/DobmW1ZUcbQ?t=10) (~48 min)
- [Clearing some misconceptions for 1.19.2 by Aizistral](https://youtu.be/bF_37BrWBSM?t=87) (~22 min)
   
All videos are suitable for describing the interactions and ethical concerns, but for technical details only videos about 1.19.3 and later versions are still relevant. Aizistral is the developer of [No Chat Reports](https://www.curseforge.com/minecraft/mc-mods/no-chat-reports).

#### Official posts

- [Help page](https://help.minecraft.net/hc/en-us/articles/7149823936781-Player-Reporting-in-Minecraft-Java-Edition)
- [FAQ](https://help.minecraft.net/hc/en-us/articles/7317376541197)
- [Why have I been banned FAQ](https://help.minecraft.net/hc/en-us/articles/4408964729869-Why-Have-I-Been-Banned-from-Minecraft-)
- [Our Commitment to Player Safety](https://help.minecraft.net/hc/en-us/articles/8047895358605-Our-Commitment-to-Player-Safety)
- [Community Standards](https://www.minecraft.net/en-us/community-standards)
- [How to report a player](https://help.minecraft.net/hc/en-us/articles/13019118732429#:~:text=MINECRAFT:%20JAVA)

#### History of changes

- **1.19** snapshot [22w17a](https://minecraft.fandom.com/wiki/Java_Edition_22w17a#Gameplay) introduced the concept of signed messages, which is a verification method that ensures each message was sent by that user and not the server. It also added a toggle for servers to prevent entering players who did not sign theirs, though the option was disabled by default.
   - [22w18a](https://minecraft.fandom.com/wiki/Java_Edition_22w18a#General) started signing the messages sent by `/say`, `/msg`, `/teammsg`, and `/me`.
   - [22w19a](https://minecraft.fandom.com/wiki/Java_Edition_22w19a#General) added an option for players to hide messages by other players who did not sign their messages.
   - Some snapshot also introduced a way to modify chat messages by filtering words, [presumably for Realms](#does-java-edition-have-a-profanity-filter).
- **1.19.1** snapshot [22w24a](https://minecraft.fandom.com/wiki/Java_Edition_22w24a#General) introduced the chat reporting interface.
   - [1.19.1-pre.1](https://minecraft.fandom.com/wiki/Java_Edition_1.19.1_Pre-release_1#General) introduced account-wide bans.
   - [1.19.1-rc.1](https://minecraft.fandom.com/wiki/Java_Edition_1.19.1_Release_Candidate_1) removed the "Extreme violence or gore", "Nudity or pornography", and "Profanity" categories. It was also Mojang's initial "final" plan of how the reporting system would work. Due to major exploits found by the community though, the release of 1.19.1 was postponed by a month.
   - [1.19.1-pre.2](https://minecraft.fandom.com/wiki/Java_Edition_1.19.1_Pre-release_2#General) introduced red bars and `(!)` indicators on unsigned messages, yellow bars and `(?)` indicators on "modified" messages. It also made the system enabled on new servers by default.
   - [1.19.1-pre.3](https://minecraft.fandom.com/wiki/Java_Edition_1.19.1_Pre-release_3#General_2) introduced gray indicators for system messages.
   - [1.19.1-pre.4](https://minecraft.fandom.com/wiki/Java_Edition_1.19.1_Pre-release_4#General) fixed an exploit where players could add new messages to a report that weren't there previously. It also introduced the concept of deleted messages, where the server can remove any message from the client.
   - [1.19.1-rc.2](https://minecraft.fandom.com/wiki/Java_Edition_1.19.1_Release_Candidate_2#General) introduced a warning toast to players entering a server where the server does not restrict the joining of non-signing users. Practically, this toast mostly affected vanilla and vanilla-like servers, as other servers quickly found a way to remove it.
 - **[1.19.2](https://minecraft.fandom.com/wiki/Java_Edition_1.19.2#Fixes)** fixed an exploit where some players could kick everyone else by abusing chat signing features.
 - **1.19.3** snapshot [22w42a](https://minecraft.fandom.com/wiki/Java_Edition_22w42a#Gameplay) removed red `(!)` indicators on unsigned messages and made the bar gray, modified messages changed the `(?)` indicator to gray and is no longer displayed if only the style was changed. Deleted messages are now displayed for 3 seconds and are replaced by a system message. Players are now able to join all servers and use most commands (except any that are related to messages) even if they don't sign their chat.
   - [22w43a](https://minecraft.fandom.com/wiki/Java_Edition_22w43a#General) introduced chat report drafts.
- **1.19.4** snapshot [23w03a](https://minecraft.fandom.com/wiki/Java_Edition_23w03a#General_2) made clients attempt to start signing their messages on server join, if it didn't happen on client start.
   - [1.19.4-pre.4](https://minecraft.fandom.com/wiki/Java_Edition_1.19.4_Pre-release_4#Fixes) fixed a bug where the user could get kicked due to signing requirement after changing their chat settings.
- _as of 1.20, no additional changes have been made_

### Can I be banned without anyone reporting me?

On Realms, yes. See [does Mojang monitor my chats](#does-mojang-monitor-my-chats).

On public servers, no. You can be banned by server admins throughout the same server or server network, but multiplayer-wide bans as described here must still be initiated by a player reporting another player's individual messages, [if the system is enabled on the server](#i-am-a-server-owner.-how-can-i-protect-my-users).

### Is there a way to appeal the ban?

Yes, if you [meet their criteria (see "how to submit an appeal...")](https://www.minecraft.net/en-us/community-standards#main-content:~:text=HOW%20TO%20SUBMIT%20AN%20APPEAL). It is unknown how many appeals are accepted.

1. [Open the Case Review request](https://help.minecraft.net/hc/en-us/requests/new?ticket_form_id=360003469452)
2. Select "Minecraft: Java" as the game.
3. Fill the form throughly with all information you have
4. Submit the form
5. Wait patiently for their response

If you own a Realm, you may want to [pause your subscription](https://help.minecraft.net/hc/en-us/articles/4410000696077-Minecraft-Java-Edition-Realms-Billing-Issues-FAQ#h_01FGCST20673JYZ76PB9BN4BNK) as well.

### What should I do instead when someone breaks the rules?

Do what you always did.

- If an user is being annoying, hide their messages by clicking the chat icon near the username in Social Interactions or, in some servers, `/ignore (username)`.
- If an user has broken the rules of the server, report it to server administration. This is usually done by `/report`, `/helpop`, server forum or Discord.
- If an user is talking about commiting suicide, talk to them and [give local help resources](https://en.wikipedia.org/wiki/List_of_suicide_crisis_lines). 
- If an user is doing or threatening illegal actions, report it to server admins and local police. Provide them with as much context as possible, including screenshots.

### How could Mojang improve the system?

In the best scenario, one of the following:

- Sending the reports to server admins instead of Mojang, as they have the most context to take the appropriate action
- Making the whole system opt-in (or out) as then only the servers that need this help would enable it
- Implementing the system only on Realms or other Mojang-partnering servers
- Not implementing the system at all because there are enough moderation tools built already

If core changes to the system will not be made, Mojang could still improve its communication about the feature in-game and on help pages:

- Make it clear that reports are sent to Mojang instead of server admins
- Add an indicator that shows the system is in place (on servers where it is)
- Use less cryptic terminology in errors related to the system
- Write a technical overview about the system's working so that users inclined would be able to read it from the official source

This is a non-exhaustive list. People have posted more ideas in various Minecraft communities and the feedback site, search around.

### I am a server owner. How can I protect my users?

See [server setup](server-setup.md#how-to-protect-your-users). If you are a player, you can send that page to your server admins.

### How does this affect Realms?

See [does Mojang monitor my chats](#does-mojang-monitor-my-chats).

### I want to give feedback to Mojang.

Great! Use the [official feedback site](https://feedback.minecraft.net/hc/en-us):
* [Give feedback on the chat reporting](https://feedback.minecraft.net/hc/en-us/community/posts/7320990094733-Player-Chat-Reporting-Feedback-)
* [The most popular request for reverting chat reporting](https://feedback.minecraft.net/hc/en-us/community/posts/6977558665997-Mojang-please-for-the-love-of-your-game-don-t-add-a-chat-report-feature-)

## Chat reporting and Fabulously Optimized

### What does this modpack do for me?

Fabulously Optimized has added a mod called [No Chat Reports](https://www.curseforge.com/minecraft/mc-mods/no-chat-reports) that informs you of the availability of chat reporting and makes your messages unreportable on servers that explicitly tell the client "chat reporting is optional here". It also reverts most of the vanilla chat indicators, as they are not as reliable and consistent as the modded ones.

As of 1.19.3, a resource pack called [Chat Reporting Helper](https://github.com/Fabulously-Optimized/fabulously-optimized/tree/main/Resource%20Packs/Chat%20Reporting%20Helper) is also added, which does the following:
  - Makes No Chat Reports icons more neutral
  - Makes relevant vanilla and No Chat Reports tooltips shorter, clearer, more accurate and unbiased
  
In order to get the status of the server, open the chat box (press `T`) and look at the right bottom corner:

- ![unknown](https://i.ibb.co/Yb1n6fW/unknown.png) - status not yet known, you must send one chat message to get it
- ![disabled](https://i.ibb.co/QDFzXCT/secure.png) - chat reporting is disabled for everyone
- ![optional](https://i.ibb.co/hstcjW7/neutral.png) - chat reporting is optional, Fabulously Optimized users opt-out by default
   - In some cases, it might be fully disabled but not reflected on the icon. You can confirm by seeing if you can report anyone on Social Interactions.  
- ![enabled](https://i.ibb.co/2YgMHpR/insecure.png) - chat reporting is enabled for everyone
- ![realms](https://i.ibb.co/gTxw84X/realms.png) - only on Realms: chat reporting is enabled for everyone and [everyone's chats are automatically monitored](#does-mojang-monitor-my-chats)

_(Expected different icons? Disable Chat Reporting Helper resource pack and [see No Chat Reports wiki.](https://github.com/Aizistral-Studios/No-Chat-Reports/wiki/Configuration-Files#option-showserversafety))_

The behaviour can be configured per-server, hover on the icon for more details.

### I don't want to join such servers at all!

If you don't think the ![enabled](https://i.ibb.co/2YgMHpR/insecure.png) icon is enough, you can also be prompted before sending a signed message or block sending all signed messages altogether (on such servers, you can only use commands then).

1. Click Mods
2. Search for "No Chat Reports" and click ![config](https://i.ibb.co/j35cBtn/image.png)
3. Set "Default signing mode" to `Prompt` or `Never`
4. `Save changes`

The behaviour can also be configured per-server, hover on the status icon (bottom right corner of the chatbox) for more details.

### Is No Chat Reports itself a risk?

No. The mod disables chat signing on servers that explicitly tell the clients "chat reporting is not required here!". In servers that enforce the system, chat signing will work as it does in vanilla.

### I think chat reporting is fair.

Understandable. If you join a server and see a ![enabled](https://i.ibb.co/2YgMHpR/insecure.png) in the bottom right corner of the chat, that server enforces the report system and the modpack will adhere to it, just like vanilla. 

In vanilla itself there is no such clear indication as the toast and chat line icons do not accurately work on every server, hence the mod.

## Alternative approaches
 
### Why not stay on 1.19?

- [The modpack opts out from chat reporting in 1.19.1+ as well](#what-does-this-modpack-do-for-me)
- [It is easy for server owners to disable chat reporting in 1.19.1+ anyway](#i-am-a-server-owner.-how-can-i-protect-my-users)
- Most mods are not interested in continuing to support it
- No Chat Reports is outdated on 1.19, so you cannot join all servers
- It is buggy, [1.19.1 fixed several bugs and crashes](https://minecraft.fandom.com/wiki/Java_Edition_1.19.1#Fixes)
- If you want to keep using it just for the sake of protest, remember that [1.19 already has the basis for chat reporting - the chat signatures](#history-of-changes).

If you want to stay on an older version, please use the latest version for 1.18.2.

_This section previously claimed that it may be possible for 1.19.1+ players to report 1.19 ones. This turned out to not be the case because [the signing system changed in 1.19.1](https://youtu.be/DobmW1ZUcbQ?t=681)._

### But my favorite server is afraid to update!

Alright, please [send them this link](server-setup.md#how-to-protect-your-users) to let them know they don't have to stay on 1.19 just to disable chat reporting.

### Why not stay on 1.18.2?

It is safe from reports, you are free to play it for as long as you like. Fabulously Optimized will still focus on optimizing the newest versions (including everything related to the chat reporting) rather than continuously updating the old one.

### Can I use exploits to break the system/avoid getting reported?

No, that makes you more likely to get banned. It is up to the server to decide whether they want the reporting system or not, use that information to choose the servers you play in.

Fabulously Optimized will not include or endorse any exploits.

### Can I encrypt my chat messages?

Yes. This is [mostly useful in Realms](#does-mojang-monitor-my-chats) and in public servers' private messages with friends, as long as you know how and where to use it.

In Fabulously Optimized the encryption button is currently hidden to reduce confusion, so you need to do the following to enable it:

1. Click Mods
2. Search for "No Chat Reports" and click ![config](https://i.ibb.co/j35cBtn/image.png)
3. Select `Technical` tab, set "Show encryption button" to `Yes`
4. `Save changes`
5. Join any world or server
6. Click your chat key, default `T`
7. Click the `🔒`. You'll see warnings and configuration for the encryption feature.

## Other questions

### Does Java Edition have a profanity filter?

Yes, but currently only on Realms chat. If you are an adult, you can disable it for yourself [in your minecraft.net profile](https://www.minecraft.net/en-us/msaprofile/accountsettings). [Learn more](https://help.minecraft.net/hc/en-us/articles/6160517019149)

Profanity by itself is no longer a category one can report other players for. **Swearing at friends, even jokingly, is bannable though** - read the next section for more info. 

Bedrock Edition has the filter on chat, signs, item names, books etc. across all servers and content, including singleplayer.

### Does Mojang monitor my chats?

Yes, but only on [Realms](https://support.xbox.com/en-US/help/games-apps/game-titles/minecraft-realms-overview) (Java and Bedrock) and [Featured Servers](https://help.minecraft.net/hc/en-us/articles/4408873961869-Minecraft-Dedicated-and-Featured-Servers-FAQ-) (only Bedrock).

[Our Commitment to Player Safety](https://help.minecraft.net/hc/en-us/articles/8047895358605-Our-Commitment-to-Player-Safety#h_01G95X76WR1PM97XBXDE7G25KE) says

> For Bedrock and Java Realms as well as partnered Bedrock servers, we leverage an automated proactive chat filtering system.
> 
> We use it to classify, filter, and escalate online harms for human review and moderation to promote safe and welcoming interactions on Minecraft games. That includes behaviors such as harassment, abuse, and hate speech.

Similarly, the [why have I been banned FAQ](https://help.minecraft.net/hc/en-us/articles/4408964729869-Why-Have-I-Been-Banned-from-Minecraft-) says

> Specifically, our highly trained moderation staff is looking at the most egregious violations in public Featured Servers and Realms [...]

Read [can I encrypt my chat messages](#can-i-encrypt-my-chat-messages) above for what can you do about it.

### Does Bedrock Edition also have chat reporting?

[Yes, it does.](https://help.minecraft.net/hc/en-us/articles/13019118732429) It is unknown if there is any way to prevent that there.

### I have more questions.

Write to `#support` [in our Discord](https://fabulously-optimized.github.io/discord).
