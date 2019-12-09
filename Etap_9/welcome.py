#!/usr/bin/env python
# -*- coding: utf-8 -*-
def index(req, name=''):

        html = '<html>'
        html += 'Witaj ' + name
#name.replace("<", "&lt;").replace(">","&gt;")
        html += '<p>Miło mi Cię poznać.</p>'
        html += '</html>'
        return html
