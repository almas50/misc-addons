# Copyright 2018 Dinar Gabbasov <https://it-projects.info/team/GabbasovDinar>
# Copyright 2018 Kolushov Alexandr <https://it-projects.info/team/KolushovAlexandr>
# License MIT (https://opensource.org/licenses/MIT).
{
    "name": """Upload Multiple Attachments""",
    "summary": """The technical module to upload multiple attachments at once""",
    "category": "Extra Tools",
    # "live_test_url": "",
    "images": [],
    "version": "13.0.1.0.0",
    "application": False,
    "author": "IT-Projects LLC, Dinar Gabbasov, Kolushov Alexandr",
    "support": "apps@itpp.dev",
    "website": "https://it-projects.info/team/GabbasovDinar",
    "license": "Other OSI approved licence",  # MIT
    "price": 10.00,
    "currency": "EUR",
    "depends": ["web"],
    "external_dependencies": {"python": [], "bin": []},
    "data": ["views/template.xml"],
    "qweb": ["static/src/xml/web_kanban.xml"],
    "demo": [],
    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,
    "uninstall_hook": None,
    "auto_install": False,
    "installable": False,
}
