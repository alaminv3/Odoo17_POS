/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { _t } from "@web/core/l10n/translation";
import { SignTemplateBody } from "@sign/backend_components/sign_template/sign_template_body";
import { CustomSignTemplateIframe } from "./sign_template_iframe";


patch(SignTemplateBody.prototype, {

//    This method is overridden to add placeholder into name if exist
    prepareTemplateData() {
        const updatedSignItems = {};
        const Id2UpdatedItem = {};
        const items = this.iframe?.signItems ?? {};
        for (const page in items) {
            for (const id in items[page]) {
                const signItem = items[page][id].data;
                if (signItem.updated) {
                    Id2UpdatedItem[id] = signItem;
                    const responsible = signItem.responsible;
//                    const model_model = signItem.model_model;
                    updatedSignItems[id] = {
                        type_id: signItem.type_id[0],
                        required: signItem.required,
                        name: signItem.placeholder.length ? signItem.placeholder : signItem.name,
                        alignment: signItem.alignment,
                        option_ids: signItem.option_ids,
                        responsible_id: responsible,
//                        model_id: model_model,
                        page: page,
                        posX: signItem.posX,
                        posY: signItem.posY,
                        width: signItem.width,
                        height: signItem.height,
                    };

                    if (id < 0) {
                        updatedSignItems[id]["transaction_id"] = id;
                    }
                }
            }
        }
        return [updatedSignItems, Id2UpdatedItem];
    },

    /**
    This method is overridden to use our custom sign_template_iframe class as iframe.
    Because we added model and fields criteria and their corresponding methods to update them
    Previously SignTemplateIframe class was used to make iframe. Now CustomSignTemplateIframe will be used
    which is inherited from SignTemplateIframe class.
    */
    doPDFPostLoad() {
        this.preventDroppingImagesOnViewerContainer();
        this.iframe = new CustomSignTemplateIframe(
            this.PDFIframe.el.contentDocument,
            this.env,
            {
                rpc: this.rpc,
                orm: this.orm,
                popover: this.popover,
                dialog: this.dialog,
                user: this.user,
            },
            {
                signItemTypes: this.props.signItemTypes,
                signItems: this.props.signItems,
                signRoles: this.props.signRoles,
//                signModels: this.props.signModels,
                hasSignRequests: this.props.hasSignRequests,
                signItemOptions: this.props.signItemOptions,
                saveTemplate: () => this.saveTemplate(),
                rotatePDF: () => this.rotatePDF(),
            }
        );
    }
});