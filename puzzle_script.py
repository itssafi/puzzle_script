import sys


class RestaurantPuzzle(object):
    """
    Class for solving Jurgensville Restaurant Puzzle
    """
    def read_csv_file(self, kwargs):
        """
        Reading csv file reacord and put into a dictionary
        """
        self.restaurant_details = {}
        csv_file = kwargs['csv_file']
        with open(csv_file) as file_obj:
            for line in file_obj:
                line = line.rstrip()
                list_items = line.split(', ')
                restaurant_id = list_items.pop(0)
                if list_items:
                    cost = list_items.pop(0)
                    dinner_items = list(list_items)
                    dinner_items.insert(0, float(cost))
                    if restaurant_id not in self.restaurant_details.keys():
                        self.restaurant_details[restaurant_id] = [dinner_items]
                    else:
                        self.restaurant_details[restaurant_id].append(dinner_items)

        return self.restaurant_details

    def get_restaurant_id_and_min_cost(self, kwargs):
        """
        It will return restaurant id and minimum cost of dinner
        """
        self.flag = 0
        self.rest_no = 0
        self.cost_list = []
        self.id_and_cost = {}
        self.search_items = kwargs['item_list']

        if len(self.search_items) < 1:
            print 'Please pass search item...!'
            return

        self.restaurant_details = self.read_csv_file(kwargs)

        for key in self.restaurant_details.keys():
            temp_list = []
            cost = []
            for items in self.restaurant_details[key]:
                if set(items).issuperset(self.search_items):
                    self.set_values(key, items[0])

                else:
                    temp_list.extend(items)
                    cost.append(items[0])

            if set(temp_list).issuperset(self.search_items):
                self.set_values(key, sum(cost))

        # Checking if more than one restaurant found for search item/items
        if self.rest_no > 1:
            value_list = {}
            for value in self.id_and_cost:
                value_list[value] = min(self.id_and_cost[value])

            restaurant_id =  min(value_list, key=value_list.get)
            print restaurant_id, min(value_list.values())

        # Checking for one restaurant found for search item/items
        elif self.rest_no == 1:
            print self.id_and_cost.keys()[0], min(self.id_and_cost.values()[0])

        # Checking if search item/items not found 
        if self.flag == 0:
            print 'Nil'

    def set_values(self, rest_id, cost):
        if rest_id not in self.id_and_cost.keys():
            self.id_and_cost[rest_id] = [cost]
        else:
            self.id_and_cost[rest_id].append(cost)
        self.rest_no += 1
        self.flag = 1


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
