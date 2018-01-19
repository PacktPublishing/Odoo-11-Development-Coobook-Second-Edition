odoo.define('r3_snippets', function(require)
{
    "use strict";
    var rpc = require('web.rpc'),
        Animation = require('website.content.snippets.animation');


    Animation.registry.book_snippet = Animation.Class.extend({
        selector: '.book_snippet',
        start: function()
        {
            var self = this,
                number = 3;
            _.each(this.$el.attr('class').split(/\s+/), function(cls)
            {
                if(cls.indexOf('book_snippet-show') == 0)
                {
                    number = parseInt(cls.substring('book_snippet-show'.length));
                }
            });
            this.$el.find('td').parents('tr').remove();
            rpc.query({
                model: 'library.book',
                method: 'search_read',
                domain: [],
                fields: ['name', 'date_release'],
                sortBy: ['date_release desc'],
                limit: number,
            })
            .then(function(data)
            {
                var $table = self.$el.find('table');
                _.each(data, function(book)
                {
                    $table.append(
                        jQuery('<tr />')
                        .append(
                            jQuery('<td />').text(book.name),
                            jQuery('<td />').text(book.date_release)
                        )
                    );
                })
            });
        },
    });
});
