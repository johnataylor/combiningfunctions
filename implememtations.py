
def get_work_order_details(arguments):

    print('get_work_order_details(' + str(arguments) + ')')

    work_order_id = arguments["work_order_id"]

    match work_order_id:
        case '00052':
            return '{\n"createdOn": "06/22/2023",\n"work_order_type": "installation",\n"status": "in progress",\n"summary": "install car tires"\n}\n'
        case '00042':
            return '{\n"createdOn": "06/22/2023",\n"work_order_type": "repair",\n"status": "pending",\n"summary": "fix car"\n}\n'
        case '52341':
            return '{\n"createdOn": "06/22/2023",\n"work_order_type": "installation",\n"status": "in progress",\n"summary": "tow hitch"\n}\n'
        case _:
            return "no idea"

def get_work_orders_by_account(arguments):

    print('get_work_orders_by_account(' + str(arguments) + ')')

    return '[{"work_order_id": "00052"},\n{"work_order_id": "00042"},\n{"work_order_id": "52341"}]\n'

functionImplementations = {
    "get_work_order_details": get_work_order_details,
    "get_work_orders_by_account": get_work_orders_by_account,
}
