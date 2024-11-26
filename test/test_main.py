from markdown import markdown

from markdown_checklist.extension import ChecklistExtension


def test_checklists():
    source = """
Hello World
===========

* [ ] foo
* [x] bar
* [ ] baz

lorem ipsum
    """.strip()

    html = markdown(source)
    assert html == """
<h1>Hello World</h1>
<ul>
<li>[ ] foo</li>
<li>[x] bar</li>
<li>[ ] baz</li>
</ul>
<p>lorem ipsum</p>
    """.strip()

    expected = """
<h1>Hello World</h1>
<ac:task-list>
<ac:task>
<ac:task-id>1</ac:task-id>
<ac:task-status>incomplete</ac:task-status>
<ac:task-body>
<span class="placeholder-inline-tasks"> foo</span>
</ac:task-body>
</ac:task>
<ac:task>
<ac:task-id>2</ac:task-id>
<ac:task-status>complete</ac:task-status>
<ac:task-body>
<span class="placeholder-inline-tasks"> bar</span>
</ac:task-body>
</ac:task>
<ac:task>
<ac:task-id>3</ac:task-id>
<ac:task-status>incomplete</ac:task-status>
<ac:task-body>
<span class="placeholder-inline-tasks"> baz</span>
</ac:task-body>
</ac:task>
</ac:task-list>
<p>lorem ipsum</p>
    """.strip()

    html = markdown(source, extensions=[ChecklistExtension()])
    assert html == expected

    html = markdown(source, extensions=['markdown_checklist.extension'])
    assert html == expected


def test_syntax_variations():
    source = """
Hello World
===========

- [x] foo
- [ ] bar
- [X] baz

lorem ipsum
    """.strip()

    html = markdown(source, extensions=[ChecklistExtension()])
    assert html == """
<h1>Hello World</h1>
<ac:task-list>
<ac:task>
<ac:task-id>1</ac:task-id>
<ac:task-status>complete</ac:task-status>
<ac:task-body>
<span class="placeholder-inline-tasks"> foo</span>
</ac:task-body>
</ac:task>
<ac:task>
<ac:task-id>2</ac:task-id>
<ac:task-status>incomplete</ac:task-status>
<ac:task-body>
<span class="placeholder-inline-tasks"> bar</span>
</ac:task-body>
</ac:task>
<ac:task>
<ac:task-id>3</ac:task-id>
<ac:task-status>complete</ac:task-status>
<ac:task-body>
<span class="placeholder-inline-tasks"> baz</span>
</ac:task-body>
</ac:task>
</ac:task-list>
<p>lorem ipsum</p>
    """.strip()


def test_class():
    source = """
* [x] foo
* [ ] bar
* [X] baz

----

* [ ] lorem
* [x] ipsum
* [ ] ...
    """.strip()

    html = markdown(source, extensions=[ChecklistExtension()])
    assert html == """
<ac:task-list>
<ac:task>
<ac:task-id>1</ac:task-id>
<ac:task-status>complete</ac:task-status>
<ac:task-body>
<span class="placeholder-inline-tasks"> foo</span>
</ac:task-body>
</ac:task>
<ac:task>
<ac:task-id>2</ac:task-id>
<ac:task-status>incomplete</ac:task-status>
<ac:task-body>
<span class="placeholder-inline-tasks"> bar</span>
</ac:task-body>
</ac:task>
<ac:task>
<ac:task-id>3</ac:task-id>
<ac:task-status>complete</ac:task-status>
<ac:task-body>
<span class="placeholder-inline-tasks"> baz</span>
</ac:task-body>
</ac:task>
</ac:task-list>
<hr />
<ac:task-list>
<ac:task>
<ac:task-id>1</ac:task-id>
<ac:task-status>incomplete</ac:task-status>
<ac:task-body>
<span class="placeholder-inline-tasks"> lorem</span>
</ac:task-body>
</ac:task>
<ac:task>
<ac:task-id>2</ac:task-id>
<ac:task-status>complete</ac:task-status>
<ac:task-body>
<span class="placeholder-inline-tasks"> ipsum</span>
</ac:task-body>
</ac:task>
<ac:task>
<ac:task-id>3</ac:task-id>
<ac:task-status>incomplete</ac:task-status>
<ac:task-body>
<span class="placeholder-inline-tasks"> ...</span>
</ac:task-body>
</ac:task>
</ac:task-list>
    """.strip()
