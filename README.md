this is a simple [maubot](https://github.com/maubot/maubot) plugin which interacts with a [matrix-registration](https://github.com/zeratax/matrix-registration) deployment and generates invite tokens.

###Warning
this bot currently only works with matrix-registration versions 0.7.x. Newer implementations (currently in development as of this comment) use different api endpoints and logic, and I haven't written those changes into this code. PRs are welcomed!

modify the config to point to your matrix-registration url, include your admin secret to authenticate, and ensure that you're in the list of approved users.

once your bot is running, simply use the command

    !invite generate

to generate a token with some generic text you can copy-paste when sharing it with your invitee!

to check the status of a specific token, use

    !invite status MyTokenName

and similarly to list all tokens in the database, use

    !invite list

to revoke a token, use

    !invite revoke MyTokenName

please note: i haven't made the json output of those responses pretty. sorry not sorry.
