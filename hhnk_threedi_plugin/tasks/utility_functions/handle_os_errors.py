from ...gui.errors.os_error import handle_os_error


def check_os_error(task, cond, error):
    res = handle_os_error(error)
    task.set_result(res)
    cond.wakeAll()
