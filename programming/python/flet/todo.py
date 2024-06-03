import flet
from flet import (
    Checkbox,
    Column,
    FloatingActionButton,
    IconButton,
    Page,
    Row,
    Tab,
    Tabs,
    TextField,
    UserControl,
    colors,
    icons,
)

# Taskという名前のユーザーコントロールクラスを作成します。これは、ToDoリストの各タスクを表します。
class Task(UserControl):
    # タスクの名前、状態変更関数、削除関数を引数とするコンストラクタを定義します。
    def __init__(self, task_name, task_status_change, task_delete):
        super().__init__()
        self.completed = False
        self.task_name = task_name
        self.task_status_change = task_status_change
        self.task_delete = task_delete

    # buildメソッドをオーバーライドして、タスクのUIを作成します。
    def build(self):
        # チェックボックスを作成します。これは、タスクの完了状態を表します。
        self.display_task = Checkbox(
            value=False, label=self.task_name, on_change=self.status_changed
        )
        # テキストフィールドを作成します。これは、タスクの名前を編集するためのものです。
        self.edit_name = TextField(expand=1)

        # タスクの表示ビューを作成します。これには、タスクの名前と、編集ボタンと削除ボタンが含まれています。
        self.display_view = Row(
            alignment="spaceBetween",
            vertical_alignment="center",
            controls=[
                self.display_task,
                Row(
                    spacing=0,
                    controls=[
                        IconButton(
                            icon=icons.CREATE_OUTLINED,
                            tooltip="Edit To-Do",
                            on_click=self.edit_clicked,
                        ),
                        IconButton(
                            icons.DELETE_OUTLINE,
                            tooltip="Delete To-Do",
                            on_click=self.delete_clicked,
                        ),
                    ],
                ),
            ],
        )

        # タスクの編集ビューを作成します。これには、テキストフィールドと保存ボタンが含まれています。
        self.edit_view = Row(
            visible=False,
            alignment="spaceBetween",
            vertical_alignment="center",
            controls=[
                self.edit_name,
                IconButton(
                    icon=icons.DONE_OUTLINE_OUTLINED,
                    icon_color=colors.GREEN,
                    tooltip="Update To-Do",
                    on_click=self.save_clicked,
                ),
            ],
        )
        return Column(controls=[self.display_view, self.edit_view])

    # 編集ボタンがクリックされたときの動作を定義します。これは、表示ビューを非表示にし、編集ビューを表示します。
    def edit_clicked(self, e):
        self.edit_name.value = self.display_task.label
        self.display_view.visible = False
        self.edit_view.visible = True
        self.update()

    # 保存ボタンがクリックされたときの動作を定義します。これは、タスクの名前を更新し、表示ビューを表示して編集ビューを非表示にします。
    def save_clicked(self, e):
        self.display_task.label = self.edit_name.value
        self.display_view.visible = True
        self.edit_view.visible = False
        self.update()

    # チェックボックスの状態が変更されたときの動作を定義します。これは、タスクの完了状態を更新します。
    def status_changed(self, e):
        self.completed = self.display_task.value
        self.task_status_change(self)

    # 削除ボタンがクリックされたときの動作を定義します。これは、タスクをToDoリストから削除します。
    def delete_clicked(self, e):
        self.task_delete(self)


# TodoAppという名前のユーザーコントロールクラスを作成します。これは、ToDoリストアプリケーション全体を表します。
class TodoApp(UserControl):
    # buildメソッドをオーバーライドして、アプリケーションのUIを作成します。
    def build(self):
        # 新しいタスクの名前を入力するためのテキストフィールドを作成します。
        self.new_task = TextField(hint_text="Whats needs to be done?", expand=True)
        # タスクを表示するためのコンテナを作成します。
        self.tasks = Column()

        # タスクのフィルターを作成します。これには、"all"、"active"、"completed"の3つのタブが含まれています。
        self.filter = Tabs(
            selected_index=0,
            on_change=self.tabs_changed,
            tabs=[Tab(text="all"), Tab(text="active"), Tab(text="completed")],
        )

        # アプリケーションのルートコントロール（つまり"view"）を作成し、その中にすべての他のコントロールを含めます。
        return Column(
            width=600,
            controls=[
                Row(
                    controls=[
                        self.new_task,
                        FloatingActionButton(icon=icons.ADD, on_click=self.add_clicked),
                    ],
                ),
                Column(
                    spacing=25,
                    controls=[
                        self.filter,
                        self.tasks,
                    ],
                ),
            ],
        )

    # 追加ボタンがクリックされたときの動作を定義します。これは、新しいタスクをToDoリストに追加します。
    def add_clicked(self, e):
        task = Task(self.new_task.value, self.task_status_change, self.task_delete)
        self.tasks.controls.append(task)
        self.new_task.value = ""
        self.update()

    # タスクの状態が変更されたときの動作を定義します。これは、アプリケーションのUIを更新します。
    def task_status_change(self, task):
        self.update()

    # タスクが削除されたときの動作を定義します。これは、タスクをToDoリストから削除し、アプリケーションのUIを更新します。
    def task_delete(self, task):
        self.tasks.controls.remove(task)
        self.update()

    # アプリケーションのUIを更新するメソッドを定義します。これは、現在選択されているフィルターに基づいて、各タスクの表示状態を更新します。
    def update(self):
        status = self.filter.tabs[self.filter.selected_index].text
        for task in self.tasks.controls:
            task.visible = (
                status == "all"
                or (status == "active" and task.completed == False)
                or (status == "completed" and task.completed)
            )
        super().update()

    # フィルターのタブが変更されたときの動作を定義します。これは、アプリケーションのUIを更新します。
    def tabs_changed(self, e):
        self.update()


# メイン関数を定義します。この関数は、アプリケーションのエントリーポイントとなります。
def main(page: Page):
    # ページのタイトルを設定します。
    page.title = "ToDo App"
    # ページの水平方向の配置を設定します。
    page.horizontal_alignment = "center"
    # ページの状態を更新します。
    page.update()

    # アプリケーションのインスタンスを作成します。
    app = TodoApp()

    # アプリケーションのルートコントロールをページに追加します。
    page.add(app)


# Fletアプリケーションを起動します。この関数は、アプリケーションのエントリーポイントを指定します。
flet.app(target=main)
