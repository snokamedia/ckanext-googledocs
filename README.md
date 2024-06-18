# ckanext-googledocs

This plugin provides the option of using the [Microsoft Office Web
Viewer](https://www.microsoft.com/en-us/microsoft-365/blog/2013/04/10/office-web-viewer-view-office-documents-in-a-browser/)
for previewing both MS Office and OpenOffice documents as an
IResourceView

## Supported formats

This plugin will attempt to preview the following formats

> \"DOC\", \"DOCX\", \"XLS\", \"XLSX\", \"XLSB\", \"PPT\", \"PPTX\", \"PPS\",
> \"PPSX\", \"ODT\", \"ODS\", \"ODP\"

## Installation

To install ckanext-googledocs:

1.  Clone this repository into the place where you normally install
    extensions, by default this will be /usr/lib/ckan/default/src/

2.  Activate your CKAN virtual environment, for example:

        . /usr/lib/ckan/default/bin/activate

3.  Install the ckanext-googledocs Python package into your virtual
    environment:

        cd ckanext-googledocs
        python setup.py install

4.  Add `googledocs_view` to the `ckan.plugins` setting in your CKAN
    config file (by default the config file is located at
    `/etc/ckan/default/production.ini`).

5.  If you wish for views to be created automatically for you, then you
    should add `googledocs_view` to the end of the
    `ckan.views.default_views` option in your config file.

    > ckan.views.default\_views = \... googledocs\_view

6.  Restart CKAN. For example if you\'ve deployed CKAN with Apache on
    Ubuntu:

        sudo service apache2 reload

    or if you\'re using `supervisor`:

        sudo supervisorctl restart ckan-uwsgi:\*

## FAQ

Q: It doesn\'t work, my documents aren\'t previewing

A: For this extension to work, the documents to be previewed must be
accessible to the wider internet (i.e. the Dataset Package is PUBLIC, not PRIVATE), 
and will only work if you use a hostname, and not just an IP address.
