import ckan.lib.helpers as h
import ckan.plugins as p
import ckan.plugins.toolkit as tk

from six.moves.urllib.parse import quote_plus


class googledocsPlugin(p.SingletonPlugin):
    p.implements(p.IConfigurer)
    p.implements(p.IResourceView)

    def update_config(self, config_):
        tk.add_template_directory(config_, "templates")
        tk.add_public_directory(config_, "public")
        tk.add_resource("fanstatic", "googledocs")

    def info(self):
        return {
            "name": "googledocs_view",
            "title": tk._("Google Docs Previewer"),
            "default_title": tk._("Preview"),
            "always_available": False,
            "iframed": False,
        }

    def setup_template_variables(self, context, data_dict):
        url = quote_plus(data_dict["resource"]["url"])
        return {
            "resource_url": url
        }

    def can_view(self, data_dict):
        supported_formats = [
            "DOC", "DOCX", "XLS",
            "XLSX", "XLSB", "PPT", "PPTX",
            "PPS", "PPSX", "ODT", "ODS", "ODP", "TIFF"
        ]
        try:
            pkg_private = data_dict.get("package",{}).get("private", False)
            if not pkg_private:
                res = data_dict.get("resource",{}).get("format", "").upper()
                return res in supported_formats
            else:
                return False
        except Exception:
            return False

    def view_template(self, context, data_dict):
        return "googledocs/preview.html"

    def form_template(self, context, data_dict):
        return "googledocs/form.html"
