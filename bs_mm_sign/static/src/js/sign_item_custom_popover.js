/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { SignItemCustomPopover } from "@sign/backend_components/sign_template/sign_item_custom_popover";


patch(SignItemCustomPopover.prototype, {
    get recordProps() {
        return {
            mode: "edit",
            resModel: "sign.item",
            resId: this.props.id,
            fieldNames: this.signItemFieldsGet,
            activeFields: this.signItemFieldsGet,
            onRecordChanged: async (record, changes) => {
                if (changes.option_ids) {
                    let added_ids = [], removed_ids = [];
                    for (let item of changes.option_ids){
                        if(item[0] == 3){
                            removed_ids.push(item[1]);
                        } else if(item[0] == 4){
                            added_ids.push(item[1]);
                        }
                    }
                    let newOptionIds = [...new Set([...this.state.option_ids, ...added_ids])];
                    newOptionIds = newOptionIds.filter(option_id => !removed_ids.includes(option_id));
                    this.state.option_ids = newOptionIds;
                    return this.props.updateSelectionOptions(newOptionIds);
                }
                if (changes.responsible_id) {
                    const id = changes.responsible_id;
                    this.state.responsible = id;
                    return this.props.updateRoles(id);
                }
            },
        };
    }
})