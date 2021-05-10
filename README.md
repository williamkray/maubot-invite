this is a simple [maubot](https://github.com/maubot/maubot) plugin which interacts with a [matrix-registration](https://github.com/zeratax/matrix-registration) deployment and generates invite tokens.

modify the config to point to your matrix-registration url, include your admin secret to authenticate, and ensure that you're in the list of approved users.

*please note* that matrix-registration versions BELOW 0.9.0 have different API endpoints, expected date structures, json
arguments, etc. and require the `legacy_mr` value in your config to be set to `True`! If your matrix-registration
instance is 0.9.0 or greater, leave this as `false`.

once your bot is running, simply use the command

    !invite generate

to generate a token with some generic text you can copy-paste when sharing it with your invitee!

to check the status of a specific token, use

    !invite status MyTokenName

and similarly to list all tokens in the database, use

    !invite list

to revoke a token, use

    !invite revoke MyTokenName

