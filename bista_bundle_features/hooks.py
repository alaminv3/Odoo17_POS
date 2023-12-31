import logging

from odoo import SUPERUSER_ID, api, models

_logger = logging.getLogger(__name__)


def uninstall_hook(env):
    _logger.info("Reverting Patches...")
    # models.BaseModel._revert_method("get_view")
    env = api.Environment(env.cr, SUPERUSER_ID, {})
    env["ir.model.fields"].with_context(_force_unlink=True).search(
        [("name", "=", "smart_search")]
    ).unlink()
    _logger.info("Done!")
