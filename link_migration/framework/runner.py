# -*- coding: utf-8 -*-

import click
import importlib
import sys
import os
import termcolor
import traceback
import io
from contextlib import redirect_stdout

from link_migration.framework.version import VERSION
from link_migration.framework.model import DiscoverMigrations
from link_migration.framework.views import TerminalMessages

sys.path.insert(0, os.getcwd())

@click.command()
@click.option('-u/-d', '--up/--down', 'upgrade', default=None, help="Execute python methods to upgrade or downgrade the database.")
@click.option('-t', '--to-version', help="Migrate to a specific version. The path (up/down) is automatically determined.")
@click.option('--dry-run/--no-dry-run', default=True, is_flag=True, prompt='Dry run?', show_default=True, help="Dry run the migration to see what will be executed.")
@click.option('-v', '--version', is_flag=True, help="Version of actual migration.")
@click.option('--package-version', is_flag=True, help="Displays link_migration's version and exit.")
@click.option('-c', '--config', default="link_migration.example_migrations.conf", show_default=True, help="Specify a custom configuration file.")
@click.option('-m', '--make-migration', is_flag=True, help='Unsupported currently.')
def link_migration(*args, **kwargs):
    kwargs['config'] = importlib.import_module(kwargs['config'])

    discovered_migrations = DiscoverMigrations(**kwargs)
    terminal_message = TerminalMessages(discovered_migrations, **kwargs)

    if kwargs['package_version']:
        print(f'Package Version: {termcolor.colored(VERSION, "blue")}', flush=True)

    if kwargs['version']:
        print(f'Current Migration Version: {terminal_message.migrations.current_version}', flush=True)

    if kwargs['upgrade'] is not None and kwargs['to_version']:
        print(f'Cannot run migrations. Please specify only Up, Down, or To', flush=True)

    if kwargs['upgrade'] is not None or kwargs['to_version']:
        migrate_type = {
            (True, False): discovered_migrations.upgrade,
            (False, False): discovered_migrations.downgrade,
            (None, True): discovered_migrations.specified
        }[(kwargs['upgrade'], bool(kwargs['to_version']))]

        migrations_to_execute = list(discovered_migrations.migrations(migrate_type))
        migrate_type = discovered_migrations.upgrade if discovered_migrations.is_up() else discovered_migrations.downgrade

        if not migrations_to_execute:
            print(termcolor.colored(
                f'No migrations need to be executed, already at the correct version: {terminal_message.migrations.current_version}',
                "green"
            ), flush=True)

        try:
            for migration in migrations_to_execute:
                terminal_message.make_message(migrate_type, migration)
                with io.StringIO() as buf, redirect_stdout(buf):
                    getattr(migration, migrate_type)()
                    output = buf.getvalue()
                terminal_message.print_message(output, 'magenta')
        except Exception as e:
            print(traceback.format_exc())
            terminal_message.error_message(migrate_type, migration, e)
            sys.exit()
    else:
        print('Please specify upgrade/downgrade or to-version. -h to view help.')


if __name__ == '__main__':
    link_migration()
