/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { Many2OneField } from "@web/views/fields/many2one/many2one_field";
import { useService } from "@web/core/utils/hooks";
const { whenReady, onWillStart } = owl;

var modelList = [];

(async function boot() {
    await whenReady();
})();


patch(Many2OneField.prototype, {
    setup() {
        this.orm = useService("orm");
        this.modelLists = []
        this.disableCreateEditPerm = false


//        onWillStart(async ()=> {
//            const crntModel = this.props.record.fields[this.props.name].relation;
//            const crntModelData = await this.orm.searchRead('ir.model', [['model','=', crntModel]], ["model", "disable_create_edit"]);
//            if(crntModelData.length >= 1 && crntModelData[0].disable_create_edit){
//                this.disableCreateEditPerm = true
//            } else {
//                this.disableCreateEditPerm = false
//            }
//            console.log('Model Data is', this.disableCreateEditPerm);
//            this.computeActiveActions(this.props);
//        });

        super.setup(...arguments);
    },

    computeActiveActions(props) {
        if(this.disableCreateEditPerm){
            this.props.canQuickCreate = false
            this.state.activeActions = {
                create: false,
                createEdit: false,
                write: false,
            };
        } else {
            this.state.activeActions = {
                create: props.canCreate,
                createEdit: props.canCreateEdit,
                write: props.canWrite,
            };
        }
    }

//    async getDisableCreateEditValue(modelName){
//        const modelData = await this.orm.searchRead('ir.model', [['model','=', modelName]], ["model", "disable_create_edit"]);
//        console.log('ModelData = ', modelData);
//        if(modelData.length >= 1){
//            return modelData[0].disable_create_edit
//        }
//        else {return false}
//    },

//    async getModelValue(){
//        let crnt_model = this.props.relation || this.props.record.fields[this.props.name].relation;
//        const createEditDisablePerm = await this.orm.searchRead('ir.model', [['model','=', crnt_model]], ["model", "disable_create_edit"]);
//        console.log("In getModelValue : ", createEditDisablePerm);
//        if(createEditDisablePerm.length >= 1 && createEditDisablePerm[0].disable_create_edit){
//            this.createEditPerm = true
//        } else {
//            this.createEditPerm = false
//        }
//        this.computeActiveActions(this.props);
//    },

//    computeActiveActions(props) {
//        let self = this;
//        let crnt_model = this.props.relation || this.props.record.fields[this.props.name].relation;
//        if (crnt_model == 'res.partner'){
//            this.state.activeActions = {
//                create: false,
//                createEdit: false,
//                write: false,
//            };
//        }else{
//            this.state.activeActions = {
//                create: props.canCreate,
//                createEdit: props.canCreateEdit,
//                write: props.canWrite,
//            };
//        }
//    },
});
