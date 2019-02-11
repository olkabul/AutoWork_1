#constants
import inspect

URL = "http://gfn-brio03:9200/portal/#/login"
USERNAME = "brio_admin"
PASSWORD = "xxxxxx"


def whoami():
    return inspect.stack()[1][3]