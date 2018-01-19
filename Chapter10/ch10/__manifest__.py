# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Odoo cookbook 11 - Chapter 10",
    "version": "11.0.1.0.0",
    "author": "Odoo cookbook",
    "license": "AGPL-3",
    "category": "Odoo cookbook",
    "summary": "All the code from chapter 10",
    "depends": [
        'base',
        # that's for the later recipes
        'project',
        # that's for the last recipe
        'hr_timesheet',
    ],
    "data": [
        "views/r01_add_a_menu_item_and_window_action.xml",
        "views/r02_have_an_action_open_a_specific_view.xml",
        "views/r03_04_adding_content_and_widgets_to_a_form_view.xml",
        "views/r05_passing_parameters_to_forms_and_actions_context.xml",
        "views/r06_defining_filters_on_record_lists_domain.xml",
        "views/r07_list_views.xml",
        "views/r08_search_views.xml",
        "views/r09_changing_existing_views_view_inheritance.xml",
        "views/r13_kanban_views.xml",
        "views/r15_calendar_and_gantt_views.xml",
        "views/r16_graph_and_pivot_views.xml",
    ],
}
