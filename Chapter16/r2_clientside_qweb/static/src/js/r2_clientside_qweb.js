odoo.define('r2_clientside_qweb', function(require)
{
    var registry = require('web.field_registry'),
        AbstractField = require('web.AbstractField');

    var FieldMany2OneButtons = AbstractField.extend({
        template: 'FieldMany2OneButtons',
        className: 'oe_form_field_many2one_buttons',
        supportedFieldTypes: ['many2one'],
        init: function()
        {
            this._super.apply(this, arguments);
            this.user_list = {
                1: {
                    name: 'Administrator',
                },
                4: {
                    name: 'Demo user',
                },
            };
        },
        events: {
            'click .btn': '_button_clicked',
        },
        _render: function()
        {
            this.renderElement();
        },
        _button_clicked: function(e)
        {
            this._setValue(
                parseInt(jQuery(e.target).attr('data-id'))
            );
        },
    });

    registry.add('many2one_buttons', FieldMany2OneButtons);

    return {
        FieldMany2OneButtons: FieldMany2OneButtons,
    }
});
