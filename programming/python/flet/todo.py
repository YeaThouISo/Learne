import flet
from flet import (
    Checkbox,
    Column,
    Container,
    Dropdown,
    FloatingActionButton,
    IconButton,
    Page,
    Row,
    Tab,
    Tabs,
    Text,
    TextField,
    UserControl,
    colors,
    icons,
    border_radius,
    dropdown,
)

class Task(UserControl):
    def __init__(self, task_name, priority, task_status_change, task_delete):
        super().__init__()
        self.completed = False
        self.task_name = task_name
        self.priority = priority
        self.task_status_change = task_status_change
        self.task_delete = task_delete

    def build(self):
        self.display_task = Checkbox(
            value=False, label=self.task_name, on_change=self.status_changed
        )
        self.edit_name = TextField(expand=1)
        self.edit_priority = Dropdown(
            value=self.priority,
            options=[
                dropdown.Option("低"),
                dropdown.Option("中"),
                dropdown.Option("高"),
            ],
        )

        self.display_view = Row(
            alignment="spaceBetween",
            vertical_alignment="center",
            controls=[
                self.display_task,
                Text(f"優先度: {self.priority}"),
                Row(
                    spacing=0,
                    controls=[
                        IconButton(
                            icon=icons.CREATE_OUTLINED,
                            tooltip="編集",
                            on_click=self.edit_clicked,
                        ),
                        IconButton(
                            icons.DELETE_OUTLINE,
                            tooltip="削除",
                            on_click=self.delete_clicked,
                        ),
                    ],
                ),
            ],
        )

        self.edit_view = Row(
            visible=False,
            alignment="spaceBetween",
            vertical_alignment="center",
            controls=[
                self.edit_name,
                self.edit_priority,
                IconButton(
                    icon=icons.DONE_OUTLINE_OUTLINED,
                    icon_color=colors.GREEN,
                    tooltip="更新",
                    on_click=self.save_clicked,
                ),
            ],
        )
        return Column(controls=[self.display_view, self.edit_view])

    def edit_clicked(self, e):
        self.edit_name.value = self.display_task.label
        self.edit_priority.value = self.priority
        self.display_view.visible = False
        self.edit_view.visible = True
        self.update()

    def save_clicked(self, e):
        self.display_task.label = self.edit_name.value
        self.priority = self.edit_priority.value
        self.display_view.controls[1].value = f"優先度: {self.priority}"
        self.display_view.visible = True
        self.edit_view.visible = False
        self.update()

    def status_changed(self, e):
        self.completed = self.display_task.value
        self.task_status_change(self)

    def delete_clicked(self, e):
        self.task_delete(self)

class TodoApp(UserControl):
    def build(self):
        self.new_task = TextField(hint_text="何をする必要がありますか?", expand=True)
        self.priority = Dropdown(
            hint_text="優先度",
            options=[
                dropdown.Option("低"),
                dropdown.Option("中"),
                dropdown.Option("高"),
            ],
        )
        self.tasks = Column()
        self.search = TextField(hint_text="タスクを検索", on_change=self.search_tasks)

        self.filter = Tabs(
            selected_index=0,
            on_change=self.tabs_changed,
            tabs=[Tab(text="すべて"), Tab(text="未完了"), Tab(text="完了")],
        )

        self.priority_filter = Dropdown(
            hint_text="優先度でフィルタリング",
            on_change=self.priority_filter_changed,
            options=[
                dropdown.Option("すべて"),
                dropdown.Option("低"),
                dropdown.Option("中"),
                dropdown.Option("高"),
            ],
        )

        # アプリケーションのルートコントロール（つまり「ビュー」）に他のすべてのコントロールを含める
        return Column(
            width=600,
            controls=[
                Row(
                    controls=[
                        self.new_task,
                        self.priority,
                        FloatingActionButton(icon=icons.ADD, on_click=self.add_clicked),
                    ],
                ),
                self.search,
                Row(
                    controls=[
                        self.filter,
                        self.priority_filter,
                    ],
                ),
                self.tasks,
            ],
        )

    def add_clicked(self, e):
        task = Task(self.new_task.value, self.priority.value, self.task_status_change, self.task_delete)
        self.tasks.controls.append(task)
        self.new_task.value = ""
        self.priority.value = None
        self.update()

    def task_status_change(self, task):
        self.update()

    def task_delete(self, task):
        self.tasks.controls.remove(task)
        self.update()

    def update(self):
        status = self.filter.tabs[self.filter.selected_index].text
        priority = self.priority_filter.value

        for task in self.tasks.controls:
            task.visible = (
                (status == "すべて" or (status == "未完了" and not task.completed) or (status == "完了" and task.completed))
                and (priority == "すべて" or task.priority == priority)
                and (self.search.value.lower() in task.task_name.lower())
            )
        super().update()

    def tabs_changed(self, e):
        self.update()

    def priority_filter_changed(self, e):
        self.update()

    def search_tasks(self, e):
        self.update()

def main(page: Page):
    page.title = "ToDoアプリ"
    page.horizontal_alignment = "center"
    page.update()

    # アプリケーションインスタンスを作成
    app = TodoApp()

    # アプリケーションのルートコントロールをページに追加
    page.add(app)

flet.app(target=main)
