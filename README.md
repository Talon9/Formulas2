# Formulas
Learning Python to Process Formula Documents


Where I also try to understand GitHub!



DB_Configs.py

I left this out but it is essentially the following with your values:

        DRIVER_NAME= "SQL SERVER"
        SERVER_NAME = ""
        DATABASE_NAME = ""

        conn_string = f"""
                Driver={{{DRIVER_NAME}}};
                Server={SERVER_NAME};
                Database={DATABASE_NAME};
                Trust_Connection=yes;
            """
