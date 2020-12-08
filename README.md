this is a simple [maubot](https://github.com/maubot/maubot) plugin which interacts with a [matrix-registration](https://github.com/zeratax/matrix-registration) deployment and generates invite tokens.

modify the config to point to your matrix-registration url, include your admin secret to authenticate, and ensure that you're in the list of approved users.

once your bot is running, simply use the command

    !invite generate

to generate a token with some generic text you can copy-paste when sharing it with your invitee!

future plans to manage existing tokens seem like a good idea, although i don't know if i'll have the energy to implement. PRs are welcome!
