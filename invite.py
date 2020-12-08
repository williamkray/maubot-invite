from typing import Optional, Type

from mautrix.util.config import BaseProxyConfig, ConfigUpdateHelper
from maubot import Plugin, MessageEvent
from maubot.handlers import command

import requests
import json
import datetime

class Config(BaseProxyConfig):
    def do_update(self, helper: ConfigUpdateHelper) -> None:
        helper.copy("admin_secret")
        helper.copy("reg_url")
        helper.copy("admins")
        helper.copy("expiration")

class Invite(Plugin):
    async def start(self) -> None:
        await super().start()
        self.config.load_and_update()

    @classmethod
    def get_config_class(cls) -> Type[BaseProxyConfig]:
        return Config

    async def can_manage(self, evt: MessageEvent) -> bool:
        if evt.sender in self.config["admins"]:
            return True
        else:
            await evt.respond("You don't have permission to manage invitations for this server.")
            return False

    @command.new(name="invite", help="Generate a unique invitation code to this matrix homeserver", \
            require_subcommand=True)
    async def invite(self, evt: MessageEvent) -> None:
        pass

    @invite.subcommand("generate", help="Generate a new invitation token.")
    async def generate(self, evt: MessageEvent) -> None:
        await evt.mark_read()

        if not await self.can_manage(evt):
            return

        ex_date = datetime.datetime.strftime( \
                (datetime.date.today() + datetime.timedelta(days=self.config["expiration"])), \
                "%m.%d.%Y")
        headers = {
            'Authorization': f"SharedSecret {self.config['admin_secret']}",
            'Content-Type': 'application/json'
            }
        
        try:
            response = requests.request("POST", f"{self.config['reg_url']}/token", headers=headers, \
                    json={"one_time": True, "ex_date": ex_date})
        except Exception as e:
            await evt.respond(f"request failed: {e.message}")
            return None
        try:
            token = response.json()['name']
        except Exception as e:
            await evt.respond(f"I got a bad response back, sorry, something is borked. \n\
                    {response.json()}")
            self.log.exception(e)
            return None
        
        await evt.respond('<br />'.join(
            [
                f"Invitation token {token} created! You may share the following message with your invitee:",
                f"",
                f"Your unique url for registering is:",
                f"{self.config['reg_url']}/register?token={token}",
                f"This invite token will expire in {self.config['expiration']} days.",
                f"If it expires before use, you must request a new token."
            ]
            ), allow_html=True)
