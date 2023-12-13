/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { SignTemplate } from "@sign/backend_components/sign_template/sign_template_action";


patch(SignTemplate.prototype, {
    async fetchTemplateData(){
        super.fetchTemplateData()
        return Promise.all([
            this.fetchSignModels(),
        ]);
    },

    async fetchSignModels() {
        this.signModels = await this.orm.call("ir.model", "search_read", [], {
            context: this.user.context,
        });
    }
});