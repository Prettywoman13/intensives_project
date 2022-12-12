from django.db import models, connection


class ItemManager(models.Manager):
    def add_parent(self, type: str, text: str):
        with connection.cursor() as cursor:
            cursor.execute(
                """
                insert into questions_item(type, text, path) values
                (%s, %s, '{}'::integer[] ||
                (select last_value from questions_item_id_seq));
                """,
                [type, text],
            )
        return "ok"

    def add_child(self, type: str, text: str, parent_id: int):
        with connection.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO questions_item (type, text, path) values
                (%s,
                 %s,
                (SELECT path FROM questions_item WHERE id = %s) ||
                (select currval('questions_item_id_seq')::integer));
                """,
                [type, text, parent_id],
            )
        return "ok"
