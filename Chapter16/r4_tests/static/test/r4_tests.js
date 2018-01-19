odoo.define('r4.tests', function (require) {
    var test_utils = require('web.test_utils'),
        FormView = require('web.FormView');

    QUnit.module(
        'r4',
        {
            beforeEach: function()
            {
                this.data = {
                    'res.partner': {
                        fields: {
                            user_id: {
                                string: 'User id',
                                type: 'many2one',
                                relation: 'res.users',
                            },
                        },
                        records: [
                            {
                                id: 1,
                                user_id: 1,
                            },
                        ],
                    },
                    'res.users': {
                        fields: {
                            display_name: {
                                string: 'Display name',
                                type: 'char',
                            },
                        },
                        records: [
                            {
                                id: 1,
                                display_name: 'Administrator',
                            },
                            {
                                id: 4,
                                display_name: 'Demo user',
                            },
                        ],
                    },
                };
            },
        },
        function()
        {
            QUnit.test('Test many2one_buttons widget', function(assert) {
                assert.expect(2);
                var view = test_utils.createView({
                    View: FormView,
                    model: 'res.partner',
                    data: this.data,
                    arch: '<form><field name="user_id" widget="many2one_buttons" /></form>',
                });
                assert.strictEqual(2, view.$('.btn').length);
                view.on('field_changed', view, function(e)
                {
                    assert.strictEqual(1, e.data.changes.user_id.id);
                });
                view.$('.btn[data-id=1]').click();
            });
        }
    );
});
