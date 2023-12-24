import dal.role_dao as dao


def manager():
    return dao.manager()


def buyer():
    return dao.buyer()


def seller():
    return dao.seller()
