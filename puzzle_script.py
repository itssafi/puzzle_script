import sys


class RestaurantPuzzle(object):
    """
    Class for solving Jurgensville Restaurant Puzzle
    """
    def get_restaurant(self, kwargs):
        """
        It will return restaurant id and minimum cost of dinner
        """
        # Reading csv file reacord and put into a dictionary
        restaurant_details = {}
        csv_file = kwargs['csv_file']
        with open(csv_file) as file_obj:
            for line in file_obj:
                line = line.rstrip()
                #import pdb; pdb.set_trace()
                list_items = line.split(', ')
                restaurant_id = list_items.pop(0)
                cost = list_items.pop(0)
                dinner_items = list(list_items)
                cost_and_item = {float(cost) : dinner_items}
                if restaurant_id not in restaurant_details.keys():
                    restaurant_details[restaurant_id] = [cost_and_item]
                else:
                    restaurant_details[restaurant_id].append(cost_and_item)

        flag = 0
        rest_no = 0
        total_cost = 0
        cost_list = []
        id_and_cost = {}
        no_of_item = len(kwargs['item_list'])
        for key in restaurant_details:
            items_list = []
            cost_list = []
            for search_item in restaurant_details[key]:
                for cost, item in search_item.iteritems():
                    import pdb; pdb.set_trace()
                    print item
                    if kwargs['item_list'] == item:
                        id_and_cost[key] = cost
                        rest_no += 1
                        flag = 1
                        continue
                    elif sorted(kwargs['item_list']) == sorted(item):
                        id_and_cost[key] = cost
                        rest_no += 1
                        flag = 1
                        continue
                if len(kwargs['item_list']) > 1:
                    items_list.extend(search_item.values()[0])
                    cost_list.extend(search_item.keys())

            if set(items_list).issuperset(kwargs['item_list']):
                id_and_cost[key] = sum(cost_list)
                rest_no += 1
                flag = 1

        if rest_no > 1:
            print min(id_and_cost.values())
        elif rest_no == 1:
            print id_and_cost.keys()[0], id_and_cost.values()[0]
        if flag == 0:
            print 'Nil'


if __name__ == '__main__':
    param_dict = {'csv_file' : sys.argv[1], 'item_list' : None}
    del sys.argv[0]
    del sys.argv[0]
    param_dict['item_list'] = sys.argv
    restn = RestaurantPuzzle()
    restn.get_restaurant(param_dict)
