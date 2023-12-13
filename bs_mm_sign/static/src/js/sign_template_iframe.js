/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { SignTemplateIframe } from "@sign/backend_components/sign_template/sign_template_iframe";


patch(SignTemplateIframe.prototype, {
    async updateSelectionOptions(optionIds) {
        const newIds = optionIds.filter((id) => !(id in this.selectionOptionsById));
        const newOptions = await this.orm.searchRead(
            "sign.item.option",
            [["id", "in", newIds]],
            ["id", "value"],
            { context: this.user.context }
        );
        for (const option of newOptions) {
            this.selectionOptionsById[option.id] = option;
        }
    }
})