import asyncio

from .libs.android import R__drawable
from .libs.android.app import AlertDialog__Builder
from .libs.android.content import DialogInterface__OnClickListener


class OnClickListener(DialogInterface__OnClickListener):
    def __init__(self, fn=None, value=None):
        super().__init__()
        self._fn = fn
        self._value = value

    def onClick(self, _dialog, _which):
        if self._fn:
            self._fn(self._value)


class BaseDialog:
    def __init__(self):
        loop = asyncio.get_event_loop()
        self.future = loop.create_future()
        # self.future = asyncio.create_future()

    def __eq__(self, other):
        raise RuntimeError("Can't check dialog result directly; use await or an on_result handler")

    def __bool__(self):
        raise RuntimeError("Can't check dialog result directly; use await or an on_result handler")

    def __await__(self):
        return self.future.__await__()


class TextDialog(BaseDialog):
    def __init__(self, window, title, message, positive_text, negative_text=None, icon=None, on_result=None):
        """Create Android textual dialog.

        - window: Toga Window
        - title: Title of dialog
        - message: Message of dialog
        - positive_text: Button label where clicking it returns True (or None to skip)
        - negative_text: Button label where clicking it returns False (or None to skip)
        - icon: Integer used as an Android resource ID number for dialog icon (or None to skip)
        """
        super().__init__()

        builder = AlertDialog__Builder(window.app.native)
        builder.setCancelable(False)
        builder.setTitle(title)
        builder.setMessage(message)
        if icon is not None:
            builder.setIcon(icon)

        if positive_text is not None:
            builder.setPositiveButton(
                positive_text,
                OnClickListener(self.completion_handler, True)
            )
        if negative_text is not None:
            builder.setNegativeButton(
                negative_text,
                OnClickListener(self.completion_handler, False)
            )
        builder.show()

    def completion_handler(self, return_value: bool) -> None:
        if self.on_result:
            self.on_result(self, return_value)

        self.future.set_result(return_value)


class InfoDialog(TextDialog):
    def __init__(self, window, title, message, on_result=None):
        super().__init__(
            window=window,
            title=title,
            message=message,
            positive_text="OK",
            on_result=on_result,
        )


class QuestionDialog(TextDialog):
    def __init__(self, window, title, message, on_result=None):
        super().__init__(
            window=window,
            title=title,
            message=message,
            positive_text="Yes",
            negative_text="No",
            on_result=on_result,
        )


class ConfirmDialog(TextDialog):
    def __init__(self, window, title, message, on_result=None):
        super().__init__(
            window=window,
            title=title,
            message=message,
            positive_text="OK",
            negative_text="Cancel",
            on_result=on_result,
        )


class ErrorDialog(TextDialog):
    def __init__(self, window, title, message, on_result=None):
        super().__init__(
            window=window,
            title=title,
            message=message,
            positive_text="OK",
            icon=R__drawable.ic_dialog_alert,
            on_result=on_result,
        )
