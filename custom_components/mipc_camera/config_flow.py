from types import MappingProxyType
from voluptuous import Schema, Required

from homeassistant.config_entries import ConfigFlow
from homeassistant.data_entry_flow import FlowResult
from homeassistant.core import HomeAssistant, callback
from homeassistant.exceptions import HomeAssistantError

from .camera import MIPCCamera
from .const import DOMAIN, LOGGER
from .utils import CannotConnect, InvalidAuth, SessionError


@callback
def async_get_schema(defaults: dict[str, str] | MappingProxyType[str, str]) -> Schema:
    return Schema(
        {
            Required("username", default=defaults.get("username", "")): str,
            Required("password", default=defaults.get("password", "")): str,
        }
    )


class MIPCFlowHandler(ConfigFlow, domain=DOMAIN):
    """Handle a config flow for MIPC Camera."""

    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, str] | None = None
    ) -> FlowResult:
        """Handle the initial step."""
        errors: dict[str, str] = {}
        if user_input is not None:
            try:
                camera = MIPCCamera(
                    username=user_input["username"], password=user_input["password"]
                )
                if not await camera.auth(hass=self.hass):
                    raise CannotConnect

            except CannotConnect:
                errors["base"] = "cannot_connect"
            except InvalidAuth:
                errors["base"] = "invalid_auth"
            except SessionError:
                errors["base"] = "session_error"
            except Exception:  # pylint: disable=broad-except
                LOGGER.exception("Unexpected exception")
                errors["base"] = "unknown"
            else:
                return self.async_create_entry(
                    title=f"MIPC Account : {user_input['username']}",
                    data={},
                    options={
                        "username": user_input["username"],
                        "password": user_input["password"]
                    },
                )
        else:
            user_input = {}

        return self.async_show_form(
            step_id="user", data_schema=async_get_schema(user_input), errors=errors
        )
