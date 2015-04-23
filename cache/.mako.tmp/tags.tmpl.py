# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1429801452.836044
_enable_loop = True
_template_filename = u'/home/smatht/Documents/ISBlog/venv/lib/python2.7/site-packages/nikola/data/themes/base/templates/tags.tmpl'
_template_uri = u'tags.tmpl'
_source_encoding = 'utf-8'
_exports = [u'content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        cat_items = context.get('cat_items', UNDEFINED)
        items = context.get('items', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        title = context.get('title', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        cat_items = context.get('cat_items', UNDEFINED)
        items = context.get('items', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        title = context.get('title', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n<article class="tagindex">\n    <header>\n        <h1>')
        __M_writer(unicode(title))
        __M_writer(u'</h1>\n    </header>\n')
        if cat_items:
            if items:
                __M_writer(u'            <h2>')
                __M_writer(unicode(messages("Categories")))
                __M_writer(u'</h2>\n')
            __M_writer(u'        <ul class="postlist">\n')
            for text, link in cat_items:
                if text:
                    __M_writer(u'                <li><a class="reference" href="')
                    __M_writer(unicode(link))
                    __M_writer(u'">')
                    __M_writer(unicode(text))
                    __M_writer(u'</a></li>\n')
            __M_writer(u'        </ul>\n')
            if items:
                __M_writer(u'            <h2>')
                __M_writer(unicode(messages("Tags")))
                __M_writer(u'</h2>\n')
        if items:
            __M_writer(u'        <ul class="postlist">\n')
            for text, link in items:
                __M_writer(u'            <li><a class="reference listtitle" href="')
                __M_writer(unicode(link))
                __M_writer(u'">')
                __M_writer(unicode(text))
                __M_writer(u'</a></li>\n')
            __M_writer(u'        </ul>\n')
        __M_writer(u'</article>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"26": 0, "37": 2, "42": 32, "48": 4, "58": 4, "59": 7, "60": 7, "61": 9, "62": 10, "63": 11, "64": 11, "65": 11, "66": 13, "67": 14, "68": 15, "69": 16, "70": 16, "71": 16, "72": 16, "73": 16, "74": 19, "75": 20, "76": 21, "77": 21, "78": 21, "79": 24, "80": 25, "81": 26, "82": 27, "83": 27, "84": 27, "85": 27, "86": 27, "87": 29, "88": 31, "94": 88}, "uri": "tags.tmpl", "filename": "/home/smatht/Documents/ISBlog/venv/lib/python2.7/site-packages/nikola/data/themes/base/templates/tags.tmpl"}
__M_END_METADATA
"""
