odoo.define('r1_widgets', function(require)
{
    var registry = require('web.field_registry'),
        AbstractField = require('web.AbstractField');

    var FieldMany2OneButtons = AbstractField.extend({
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
            var self = this;
            this.$el.empty();
            _.each(this.user_list, function(description, id)
            {
                self.$el.append(
                    jQuery('<button>').attr({
                        'data-id': id,
                        'class': 'btn btn-default btn-sm',
                    })
                    .text(description.name)
                    .toggleClass(
                        'btn-primary',
                        self.value ? self.value.res_id == id : false
                    )
                );
            });
            this.$el.find('button').
                prop('disabled', this.mode == 'readonly');
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
