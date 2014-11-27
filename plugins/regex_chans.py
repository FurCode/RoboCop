from sqlalchemy import Table, Column, UniqueConstraint, String

from cloudbot import hook
from cloudbot.util import botvars

table = Table(
    "regex_chans",
    botvars.metadata,
    Column("connection", String),
    Column("channel", String),
    Column("status", String),
    UniqueConstraint("connection", "channel")
)

# Default value.
# If True, all channels without a setting will have regex enabled
# If False, all channels without a setting will have regex disabled
default_enabled = True

<<<<<<< HEAD
db_ready = []


def db_init(conn, db):
    global db_ready
    if conn not in db_ready:
        db.execute("CREATE TABLE IF NOT EXISTS regexchans(channel PRIMARY KEY, status)")
        db.commit()
        db_ready.append(conn)
=======
>>>>>>> ec0a73b4a4600de997bcd097636a4aac081bc307

@hook.onload()
def load_cache(db):
    """
    :type db: sqlalchemy.orm.Session
    """
    global status_cache
    status_cache = {}
    for row in db.execute(table.select()):
        conn = row["connection"]
        chan = row["channel"]
        status = row["status"]
        status_cache[(conn, chan)] = status


def set_status(db, conn, chan, status):
    """
    :type db: sqlalchemy.orm.Session
    :type conn: str
    :type chan: str
    :type status: str
    """
    if (conn, chan) in status_cache:
        # if we have a set value, update
        db.execute(
            table.update().values(status=status).where(table.c.connection == conn).where(table.c.channel == chan))
    else:
        # otherwise, insert
        db.execute(table.insert().values(connection=conn, channel=chan, status=status))
    db.commit()


def delete_status(db, conn, chan):
    db.execute(table.delete().where(table.c.connection == conn).where(table.c.channel == chan))
    db.commit()


<<<<<<< HEAD
def list_status(db):
    row = db.execute("SELECT * FROM regexchans").fetchall()
    result = None
    for values in row:
        if result:
            result += u", {}: {}".format(values[0], values[1])
        else:
            result = u"{}: {}".format(values[0], values[1])
    return result


@hook.sieve
def sieve_regex(bot, inp, func, kind, args):
    db = bot.get_db_connection(inp.conn)
    db_init(inp.conn.name, db)
    if kind == 'regex' and inp.chan.startswith("#") and func.__name__ != 'factoid':
        chanstatus = get_status(db, inp.chan)
        if chanstatus != "ENABLED" and (chanstatus == "DISABLED" or not default_enabled):
            print u"Denying input.raw={}, kind={}, args={} from {}".format(inp.raw, kind, args, inp.chan)
=======
@hook.sieve()
def sieve_regex(bot, event, _hook):
    if _hook.type == "regex" and event.chan.startswith("#") and _hook.plugin.title != "factoids":
        status = status_cache.get((event.conn.name, event.chan))
        if status != "ENABLED" and (status == "DISABLED" or not default_enabled):
            bot.logger.info("[{}] Denying {} from {}".format(event.conn.readable_name, _hook.function_name, event.chan))
>>>>>>> ec0a73b4a4600de997bcd097636a4aac081bc307
            return None
        bot.logger.info("[{}] Allowing {} to {}".format(event.conn.readable_name, _hook.function_name, event.chan))

    return event


<<<<<<< HEAD
@hook.command(permissions=["botcontrol"])
def enableregex(inp, db=None, message=None, notice=None, chan=None, nick=None, conn=None):
    db_init(conn.name, db)
    inp = inp.strip().lower()
    if not inp:
=======
@hook.command(autohelp=False, permissions=["botcontrol"])
def enableregex(text, db, conn, chan, nick, message, notice):
    text = text.strip().lower()
    if not text:
>>>>>>> ec0a73b4a4600de997bcd097636a4aac081bc307
        channel = chan
    elif text.startswith("#"):
        channel = text
    else:
        channel = "#{}".format(text)

    message("Enabling regex matching (youtube, etc) (issued by {})".format(nick), target=channel)
    notice("Enabling regex matching (youtube, etc) in channel {}".format(channel))
    set_status(db, conn.name, channel, "ENABLED")
    load_cache(db)


<<<<<<< HEAD
@hook.command(permissions=["botcontrol"])
def disableregex(inp, db=None, message=None, notice=None, chan=None, nick=None, conn=None):
    db_init(conn.name, db)
    inp = inp.strip().lower()
    if not inp:
=======
@hook.command(autohelp=False, permissions=["botcontrol"])
def disableregex(text, db, conn, chan, nick, message, notice):
    text = text.strip().lower()
    if not text:
>>>>>>> ec0a73b4a4600de997bcd097636a4aac081bc307
        channel = chan
    elif text.startswith("#"):
        channel = text
    else:
        channel = "#{}".format(text)

    message("Disabling regex matching (youtube, etc) (issued by {})".format(nick), target=channel)
    notice("Disabling regex matching (youtube, etc) in channel {}".format(channel))
    set_status(db, conn.name, channel, "DISABLED")
    load_cache(db)


<<<<<<< HEAD
@hook.command(permissions=["botcontrol"])
def resetregex(inp, db=None, message=None, notice=None, chan=None, nick=None, conn=None):
    db_init(conn.name, db)
    inp = inp.strip().lower()
    if not inp:
=======
@hook.command(autohelp=False, permissions=["botcontrol"])
def resetregex(text, db, conn, chan, nick, message, notice):
    text = text.strip().lower()
    if not text:
>>>>>>> ec0a73b4a4600de997bcd097636a4aac081bc307
        channel = chan
    elif text.startswith("#"):
        channel = text
    else:
        channel = "#{}".format(text)

    message("Resetting regex matching setting (youtube, etc) (issued by {})".format(nick), target=channel)
    notice("Resetting regex matching setting (youtube, etc) in channel {}".format(channel))
    delete_status(db, conn.name, channel)
    load_cache(db)


<<<<<<< HEAD
@hook.command(permissions=["botcontrol"])
def regexstatus(inp, db=None, chan=None, conn=None):
    db_init(conn.name, db)
    inp = inp.strip().lower()
    if not inp:
=======
@hook.command(autohelp=False, permissions=["botcontrol"])
def regexstatus(text, conn, chan):
    text = text.strip().lower()
    if not text:
>>>>>>> ec0a73b4a4600de997bcd097636a4aac081bc307
        channel = chan
    elif text.startswith("#"):
        channel = text
    else:
<<<<<<< HEAD
        channel = u"#{}".format(inp)

    return u"Regex status for {}: {}".format(channel, get_status(db, channel))


@hook.command(permissions=["botcontrol"])
def listregex(inp, db=None, conn=None):
    db_init(conn.name, db)
    return list_status(db)
=======
        channel = "#{}".format(text)
    status = status_cache.get((conn.name, chan))
    if status is None:
        if default_enabled:
            status = "ENABLED"
        else:
            status = "DISABLED"
    return "Regex status for {}: {}".format(channel, status)


@hook.command(autohelp=False, permissions=["botcontrol"])
def listregex(conn):
    values = []
    for (conn_name, chan), status in status_cache.values():
        if conn_name != conn.name:
            continue
        values.append("{}: {}".format(chan, status))
    return ", ".join(values)
>>>>>>> ec0a73b4a4600de997bcd097636a4aac081bc307
