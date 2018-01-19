odoo.define('r4_tests', function(require)
{
    var registry = require('web.field_registry'),
        AbstractField = require('web.AbstractField');

    var FieldMany2OneButtons = AbstractField.extend({
        template: 'FieldMany2OneButtons',
        className: 'oe_form_field_many2one_buttons',
        supportedFieldTypes: ['many2one'],
        events: {
            'click .btn': '_button_clicked',
        },
        willStart: function()
        {
            var deferred = new jQuery.Deferred(),
                self = this;
            self.user_list = {}
            this._rpc({
                model: this.field.relation,
                method: 'search_read',
                fields: ['display_name'],
                domain: this.field.domain,
            })
            .then(function(records)
            {
                _.each(records, function(record)
                {
                    self.user_list[record.id] = record;
                    self.user_list[record.id].name = record.display_name;
                });
                deferred.resolve();
            });
            return jQuery.when(
                this._super.apply(this, arguments),
                deferred
            );
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
