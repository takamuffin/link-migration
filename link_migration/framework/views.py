# -*- coding: utf-8 -*-

from textwrap import dedent
import sys

import termcolor


class FormatterMessage(object):

    def __init__(self, submodule):
        self.doc_migration = self.ident(submodule.header(), 16)
        self.doc_up = self.ident(submodule.doc_up(), 12).strip()
        self.doc_down = self.ident(submodule.doc_down(), 12).strip()
        self.version_migrate = f'{submodule.version}'
        self.archive_name = submodule.filename()
        self.execute = submodule.execute
        self.term_color = "white" if self.execute else "yellow"

    def message(self, method):
        top_line = termcolor.colored(f'{self.version_migrate} - {self.archive_name} -- Dry Run: {not self.execute}', self.term_color)
        output = (
            f'{top_line}\n'
            f'  {termcolor.colored(method.upper(), self.term_color)} - '
            f'{termcolor.colored(self.doc_up if method == "upgrade" else self.doc_down, self.term_color)}\n\n'
            f'{termcolor.colored(self.doc_migration, "blue")}\n'
        )

        return output

    def ident(self, text, space=18):
        text = dedent(text)
        lines = text.split("\n")
        text_ident = " "*space
        text = text_ident + ("\n" + text_ident).join(lines)
        return text

    def message_error(self, method, error):
        message_error = f'{termcolor.colored(error, "red")}'
        return message_error


class TerminalMessages(object):

    def __init__(self, migrations, **kwargs):
        self.migrations = migrations
        print("Running command: link_migration %s" % " ".join(sys.argv[1:]))

    def current_version(self):
        print(self.migrations.current_version)

    def make_message(self, method, migration):
        print(FormatterMessage(migration).message(method=method))

    def error_message(self, method, migration, error):
        print(FormatterMessage(migration).message_error(method, error))
