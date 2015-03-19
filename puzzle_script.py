import sys


class RestaurantPuzzle(object):
    """
    Class for solving Jurgensville Restaurant Puzzle
    """
    def read_csv_file(self, kwargs):
        """
        Reading csv file reacord and put into a dictionary
        """
        restaurant_details = {}
        csv_file = kwargs['csv_file']
        with open(csv_file) as file_obj:
            for line in file_obj:
                line = line.rstrip()
                list_items = line.split(', ')
                restaurant_id = list_items.pop(0)
                cost = list_items.pop(0)
                dinner_items = list(list_items)
                cost_and_item = {float(cost) : dinner_items}
                if restaurant_id not in restaurant_details.keys():
                    restaurant_details[restaurant_id] = [cost_and_item]
                else:
                    restaurant_details[restaurant_id].append(cost_and_item)

        return restaurant_details

    def get_restaurant_id_and_min_cost(self, kwargs):
        """
        It will return restaurant id and minimum cost of dinner
        """
        flag = 0
        rest_no = 0
        cost_list = []
        id_and_cost = {}
        no_of_item = len(kwargs['item_list'])

        restaurant_details = self.read_csv_file(kwargs)

        # Checking search item/items passed or not
        if no_of_item < 1:
            print 'Please pass search item...!'
            return

        for key in restaurant_details:
            items_list = []
            cost_list = []
            for search_item in restaurant_details[key]:
                temp_list = []
                cost = 0
                for cost, item in search_item.iteritems():
                    temp_list.extend(item)
                    cost = cost

                    # Checking for single item for single cost
                    if kwargs['item_list'] == item:
                        id_and_cost[key] = cost
                        rest_no += 1
                        flag = 1
                        continue

                    # Checking for items for single cost present in each restaurant  
                    elif sorted(kwargs['item_list']) == sorted(item):
                        id_and_cost[key] = cost
                        rest_no += 1
                        flag = 1
                        continue

                # Checking for multiple items in each restaurant
                if set(temp_list).issuperset(kwargs['item_list']):
                    id_and_cost[key] = cost
                    rest_no += 1
                    flag = 1
                    continue

                # Checking for all items in each restaurant
                if len(kwargs['item_list']) > 1:
                    items_list.extend(search_item.values()[0])
                    cost_list.extend(search_item.keys())
            if set(items_list).issuperset(kwargs['item_list']):
                id_and_cost[key] = sum(cost_list)
                rest_no += 1
                flag = 1

        # Checking if more than one restaurant found for search item/items
        if rest_no > 1:
            restaurant_id =  min(id_and_cost, key=id_and_cost.get)
            print restaurant_id, min(id_and_cost.values())

        # Checking for one restaurant found for search item/items
        elif rest_no == 1:
            print id_and_cost.keys()[0], id_and_cost.values()[0]

        # Checking if search item/items not found 
        if flag == 0:
            print 'Nil'


if __name__ == '__main__':
    try:
        param_dict = {'csv_file' : sys.argv[1], 'item_list' : None}
        del sys.argv[0]
        del sys.argv[0]
        param_dict['item_list'] = sys.argv
        restn = RestaurantPuzzle()
        restn.get_restaurant_id_and_min_cost(param_dict)
    except Exception, err:
        print "Error occured due to '%s'" %err
