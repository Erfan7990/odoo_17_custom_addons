# Part of Odoo. See LICENSE file for full copyright and licensing details.

import base64
import fnmatch
import hashlib
import inspect
import json
import logging
import re
import requests
import threading

from lxml import etree, html
from psycopg2 import sql
from werkzeug import urls
from werkzeug.datastructures import OrderedMultiDict
from werkzeug.exceptions import NotFound

from odoo import api, fields, models, tools, http, release, registry
from odoo.addons.http_routing.models.ir_http import RequestUID, slugify, url_for
from odoo.addons.website.models.ir_http import sitemap_qs2dom
from odoo.addons.website.tools import similarity_score, text_from_html, get_base_domain
from odoo.addons.portal.controllers.portal import pager
from odoo.addons.iap.tools import iap_tools
from odoo.exceptions import AccessError, MissingError, UserError, ValidationError
from odoo.http import request
from odoo.modules.module import get_manifest
from odoo.osv.expression import AND, OR, FALSE_DOMAIN, get_unaccent_wrapper
from odoo.tools.translate import _, xml_translate
from odoo.tools import escape_psql, pycompat


class InheritWebsite(models.Model):
    _inherit = 'website'
    _description = 'Inherit Website'

    def _default_logo(self):
        with tools.file_open('custom_website/static/src/img/content/icons/default_cart.svg', 'rb') as f:
            return base64.b64encode(f.read())

    cart_icon = fields.Binary('Cart', help="Display this cart icon on the website.")
    wishlist_icon = fields.Binary('wishlist icon', help="Display this cart icon on the website.")
    search_icon = fields.Binary('Search icon', help="Display this cart icon on the website.")
    hamburger_icon = fields.Binary('Hamburger', help="Display this Hamburger icon on the website.")
    navbar_icon_svg = fields.Binary(
        string="Navbar Icon (SVG)",
        help="Upload a custom SVG icon for the website navbar"
        )