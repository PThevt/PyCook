import psycopg2
import time


def init_tables_in_database():
    try:
        conn = psycopg2.connect(
            user="pycook",
            password="pycook",
            host="pycook-database",
            port="5432",
            database="pycook"
        )
        cur = conn.cursor()
        init_recipes_table(cur, conn)
        init_ingredients_table(cur, conn)
        init_measurement_qty_table(cur, conn)
        init_measurement_units_table(cur, conn)
        init_recipe_ingredients_table(cur, conn)

        # fermeture de la connexion à la base de données
        cur.close()
        conn.close()
        print("La connexion PostgreSQL est fermée")
    except (Exception, psycopg2.Error) as error:
        print("An error is occurred while initializing the tables : ", error, flush=True)


def waiting_for_database_up():
    while True:
        try:
            conn = psycopg2.connect(
                user="pycook",
                password="pycook",
                host="pycook-database",
                port="5432",
                database="pycook")
            while True:
                cursor = conn.cursor()
                cursor.execute("SELECT count(*) FROM pg_database where datname in ('pycook')")
                result = cursor.fetchone()

                if result and len(result) > 0:
                    print("database pycook create successful")
                    break
                else:
                    print("database pycook not created... waiting...")
                    time.sleep(1)
                cursor.close()
            conn.close()
            break
        except (Exception, psycopg2.Error) as error:
            print("Database not responds.. waiting for pycook-database up: %s" % error)
            time.sleep(1)


def init_recipes_table(cur, conn):
    init_recipes_table_sql = """
                CREATE TABLE IF NOT EXISTS public.recipes
                (
                    id serial NOT NULL,
                    name character varying NOT NULL,
                    description character varying NOT NULL,
                    CONSTRAINT recipes_id_primary_key PRIMARY KEY (id)
                )
                TABLESPACE pg_default;
                ALTER TABLE IF EXISTS public.recipes
                OWNER to pycook;"""
    cur.execute(init_recipes_table_sql)
    conn.commit()
    print("Table 'recipes' created successfully !", flush=True)


def init_ingredients_table(cur, conn):
    init_ingredients_table_sql = """
                CREATE TABLE IF NOT EXISTS public.ingredients
                (
                    id serial NOT NULL,
                    name character varying NOT NULL,
                    CONSTRAINT ingredients_id_primary_key PRIMARY KEY (id)
                )
                TABLESPACE pg_default;
                ALTER TABLE IF EXISTS public.ingredients
                OWNER to pycook;
                """
    cur.execute(init_ingredients_table_sql)
    conn.commit()
    print("Table 'ingredients' created successfully !", flush=True)


def init_measurement_qty_table(cur, conn):
    init_measurement_qty_table_sql = """
                CREATE TABLE IF NOT EXISTS public.measurement_qty
                (
                    id serial NOT NULL,
                    amount character varying NOT NULL,
                    CONSTRAINT measurement_qty_id_primary_key PRIMARY KEY (id)
                )
                TABLESPACE pg_default;
                ALTER TABLE IF EXISTS public.measurement_qty
                OWNER to pycook;
                """
    cur.execute(init_measurement_qty_table_sql)
    conn.commit()
    print("Table 'measurement_qty' created successfully !", flush=True)


def init_measurement_units_table(cur, conn):
    init_measurement_units_table_sql = """
                CREATE TABLE IF NOT EXISTS public.measurement_units
                (
                    id serial NOT NULL,
                    unit character varying NOT NULL,
                    CONSTRAINT measurement_units_id_primary_key PRIMARY KEY (id)
                )
                TABLESPACE pg_default;
                ALTER TABLE IF EXISTS public.measurement_units
                OWNER to pycook;
                """
    cur.execute(init_measurement_units_table_sql)
    conn.commit()
    print("Table 'measurement_units' created successfully !", flush=True)


def init_recipe_ingredients_table(cur, conn):
    init_recipe_ingredients_table_sql = """
                CREATE TABLE IF NOT EXISTS public.recipe_ingredients
                (
                    recipe_id serial NOT NULL,
                    measurement_qty_id serial NOT NULL,
                    measurement_units_id serial NOT NULL,
                    ingredients_id serial NOT NULL,
                    CONSTRAINT recipe_ingredients_id_primary_key PRIMARY KEY (recipe_id, measurement_qty_id, measurement_units_id, ingredients_id),
                    CONSTRAINT recipe_id_foreign_key_to_recipe_ingredients FOREIGN KEY (recipe_id)
                    REFERENCES public.recipes (id) MATCH SIMPLE
                    ON UPDATE NO ACTION
                    ON DELETE NO ACTION
                    NOT VALID,
                    CONSTRAINT measurement_units_id_foreign_key__to_recipe_ingredients FOREIGN KEY (measurement_units_id)
                    REFERENCES public.measurement_units (id) MATCH SIMPLE
                    ON UPDATE NO ACTION
                    ON DELETE NO ACTION
                    NOT VALID,
                    CONSTRAINT measurement_qty_id_foreign_key_to_recipe_ingredients FOREIGN KEY (measurement_qty_id)
                    REFERENCES public.measurement_qty (id) MATCH SIMPLE
                    ON UPDATE NO ACTION
                    ON DELETE NO ACTION
                    NOT VALID,
                    CONSTRAINT ingredients_id_foreign_key_to_recipe_ingredients FOREIGN KEY (ingredients_id)
                    REFERENCES public.ingredients (id) MATCH SIMPLE
                    ON UPDATE NO ACTION
                    ON DELETE NO ACTION
                    NOT VALID
                )
                TABLESPACE pg_default;
                ALTER TABLE IF EXISTS public.recipe_ingredients
                OWNER to pycook;
                """
    cur.execute(init_recipe_ingredients_table_sql)
    conn.commit()
    print("Table 'recipe_ingredients' created successfully !", flush=True)
