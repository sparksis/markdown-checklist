[Markdown Checklist](https://github.com/FND/markdown-checklist)
[![build status](https://secure.travis-ci.org/FND/markdown-checklist.png)](http://travis-ci.org/FND/markdown-checklist)
[![coverage](https://coveralls.io/repos/FND/markdown-checklist/badge.png)](https://coveralls.io/r/FND/markdown-checklist)

a [Python Markdown](http://pythonhosted.org/Markdown/) extension for lists of
tasks with checkboxes

inspired by
[GitHub task lists](https://github.com/blog/1375-task-lists-in-gfm-issues-pulls-comments):

    * [ ] foo
    * [x] bar
    * [ ] baz

becomes

    <ac:task-list>
    <ac:task>
    <ac:task-id>1</ac:task-id>
    <ac:task-status>complete</ac:task-status>
    <ac:task-body>
    <span class="placeholder-inline-tasks">foo</span>
    </ac:task-body>
    </ac:task>
    <ac:task>
    <ac:task-id>2</ac:task-id>
    <ac:task-status>incomplete</ac:task-status>
    <ac:task-body>
    <span class="placeholder-inline-tasks">bar</span>
    </ac:task-body>
    </ac:task>
    <ac:task>
    <ac:task-id>3</ac:task-id>
    <ac:task-status>incomplete</ac:task-status>
    <ac:task-body>
    <span class="placeholder-inline-tasks">baz</span>
    </ac:task-body>
    </ac:task>
    </ac:task-list>

* a dash can be used instead of an asterisk for list items
* both upper- and lowercase "x" are accepted to activate checkboxes


Installation
------------

    $ pip install markdown-checklist


Usage
-----

    import markdown
    html = markdown.markdown(source, extensions=['markdown_checklist.extension'])

or

    import markdown
    from markdown_checklist.extension import ChecklistExtension
    html = markdown.markdown(source, extensions=[ChecklistExtension()])

There is also a small JavaScript/jQuery library to make checkboxes interactive:

    new Checklists("article", function(checkbox, callback) {
        var uri = checkbox.closest("article").find("h1 a").attr("href");
        jQuery.get(uri, callback);
    }, function(markdown, checkbox, callback) {
        var uri = checkbox.closest("article").find("h1 a").attr("href");
        jQuery.ajax({
            type: "put",
            uri: uri,
            data: markdown,
            success: callback
        });
    });

See included `checklists.js` for details.

GitHub Actions Workflow for CI
------------------------------

This project uses GitHub Actions for continuous integration. The workflow is defined in the `.github/workflows/ci.yml` file. It runs tests on push to the `master` branch and on pull request creation/synchronization.

GitHub Packages for Release
---------------------------

This project uses GitHub Packages for releasing new versions. The release process is defined in the `Makefile` and the GitHub Actions workflow. When a new version is released, a release object is created in GitHub Packages.
