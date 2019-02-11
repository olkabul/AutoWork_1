#constants
import inspect

URL = "http://gfn-brio03:9200/portal/#/login"
USERNAME = "brio_admin"
PASSWORD = "brio_admin"


def whoami():
    return inspect.stack()[1][3]