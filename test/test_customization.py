from markdown import markdown

from markdown_checklist.extension import ChecklistExtension


def render_item(caption, checked):
    status = 'complete' if checked else 'incomplete'
    template = """
<ac:task>
<ac:task-id>{id}</ac:task-id>
<ac:task-status>{status}</ac:task-status>
<ac:task-body>
<span class="placeholder-inline-tasks">{caption}</span>
</ac:task-body>
</ac:task>
    """.strip()
    return template.format(id=render_item.counter, status=status, caption=caption)

render_item.counter = 1


def test_checklists():
    source = """
* [ ] foo
* [x] bar
* [ ] baz
    """.strip()

    expected = """
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
    """.strip()

    html = markdown(source,
            extensions=[ChecklistExtension(render_item=render_item)])
    assert html == expected
