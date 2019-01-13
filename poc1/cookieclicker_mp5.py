"""
Cookie Clicker Simulator
"""

import simpleplot

# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(40)

import poc_clicker_provided as provided

import math

# Constants
#SIM_TIME = 10000000000.0
SIM_TIME = 10000000000.0

class ClickerState:
    """
    Simple class to keep track of the game state.
    """
    
    def __init__(self):
        self._total_cookies = 0.0
        self._current_cookies = 0.0
        self._current_time = 0.0
        self._cps = 1.0 # cookies per second
        self._history = [(0.0, None, 0.0, 0.0)]
        
    def __str__(self):
        """
        Return human readable state
        """
        prt_str = "Current time: " + str(self._current_time) + \
        "\nCurrent cookies: " + str(self._current_cookies) + \
        "\nCPS: " + str(self._cps) + \
        "\nTotal cookies: " + str(self._total_cookies)
        
        return prt_str
        
    def get_cookies(self):
        """
        Return current number of cookies 
        (not total number of cookies)
        
        Should return a float
        """
        return self._current_cookies
    
    def get_cps(self):
        """
        Get current CPS

        Should return a float
        """
        return self._cps
    
    def get_time(self):
        """
        Get current time

        Should return a float
        """
        return self._current_time
    
    def get_history(self):
        """
        Return history list

        History list should be a list of tuples of the form:
        (time, item, cost of item, total cookies)

        For example: [(0.0, None, 0.0, 0.0)]

        Should return a copy of any internal data structures,
        so that they will not be modified outside of the class.
        """
        return list(self._history)

    def time_until(self, cookies):
        """
        Return time until you have the given number of cookies
        (could be 0.0 if you already have enough cookies)

        Should return a float with no fractional part
        """
        if self._current_cookies < cookies:
            time = (cookies - self._current_cookies)/self._cps
            return math.ceil(time)
        else:
            return 0.0
    
    def wait(self, time):
        """
        Wait for given amount of time and update state

        Should do nothing if time <= 0.0
        """
        if time > 0.0:
            self._current_time += time
            self._current_cookies += self._cps*time
            self._total_cookies += self._cps*time
    
    def buy_item(self, item_name, cost, additional_cps):
        """
        Buy an item and update state

        Should do nothing if you cannot afford the item
        """
        if self._current_cookies >= cost:
            self._cps += additional_cps
            self._current_cookies -= cost
            self._history.append((self._current_time, item_name, cost, self._total_cookies))
   
    
def simulate_clicker(build_info, duration, strategy):
    """
    Function to run a Cookie Clicker game for the given
    duration with the given strategy.  Returns a ClickerState
    object corresponding to the final state of the game.
    """

    # Clone the build_info object
    build_clone = build_info.clone()
    
    # Create new ClickerState object
    cs_obj = ClickerState()
    
    while cs_obj.get_time() <= duration:
        
        # Call strategy function to determine which item to purchase
        # if strategy function returns None, break out of the loop
#        print "\n" + str(cs_obj) + "\n"
        time_left = duration - cs_obj.get_time()
#        print "Time left: ", time_left
        item_name = strategy(cs_obj.get_cookies(), cs_obj.get_cps(), cs_obj.get_history(), time_left, build_clone)
#        print "Item name: ", item_name
        
        if item_name is None:
            break
        
        # Determine how much time must elapse until it is possible to purchase
        # item. If you have to wait past the duration of the simulation to
        # purchase the item, you should end the simulation.
        
        cost = build_clone.get_cost(item_name)
#        print "Cost: ", cost
        time_wait = cs_obj.time_until(cost)
#        print "Wait time: ", time_wait
        
        if time_wait > time_left:
            break
        
        # Wait until that time.
        cs_obj.wait(time_wait)
        
        # Buy the item
        additional_cps = build_clone.get_cps(item_name)
#        print "Added cps: ", additional_cps
        cs_obj.buy_item(item_name, cost, additional_cps)
        
        # Update build information
        build_clone.update_item(item_name)
    
    # if time is left, allow cookies to accumulate for the remainder of time left
    cs_obj.wait(time_left)
    
    # buy more items if possible
    item_name = strategy(cs_obj.get_cookies(), cs_obj.get_cps(), cs_obj.get_history(), time_left, build_clone)
    
    if item_name is not None:
        cost = build_clone.get_cost(item_name)
        additional_cps = build_clone.get_cps(item_name)
        cs_obj.buy_item(item_name, cost, additional_cps)
        build_clone.update_item(item_name)
    
    return cs_obj


def strategy_cursor_broken(cookies, cps, history, time_left, build_info):
    """
    Always pick Cursor!

    Note that this simplistic (and broken) strategy does not properly
    check whether it can actually buy a Cursor in the time left.  Your
    simulate_clicker function must be able to deal with such broken
    strategies.  Further, your strategy functions must correctly check
    if you can buy the item in the time left and return None if you
    can't.
    """
    return "Cursor"

def strategy_none(cookies, cps, history, time_left, build_info):
    """
    Always return None

    This is a pointless strategy that will never buy anything, but
    that you can use to help debug your simulate_clicker function.
    """
    return None

def strategy_cheap(cookies, cps, history, time_left, build_info):
    """
    Always buy the cheapest item you can afford in the time left.
    """
    
    cheapest_item = None
    min_cost = float('inf')
    max_cookies = cps*time_left + cookies
    
    for item in build_info.build_items():
        if build_info.get_cost(item) < min_cost and build_info.get_cost(item) <= max_cookies:
            cheapest_item = item
            min_cost = build_info.get_cost(item)
                
    return cheapest_item

def strategy_expensive(cookies, cps, history, time_left, build_info):
    """
    Always buy the most expensive item you can afford in the time left.
    """
    expensive_item = None
    max_cost = 0.0
    max_cookies = cps*time_left + cookies
    
    for item in build_info.build_items():
        if build_info.get_cost(item) > max_cost and build_info.get_cost(item) <= max_cookies:
            expensive_item = item
            max_cost = build_info.get_cost(item)
                
    return expensive_item

def strategy_best(cookies, cps, history, time_left, build_info):
    """
    The best strategy that you are able to implement.
    """
    # Try buying the highest CPS/cost ratio
    best_item = None
    max_cps_cost_ratio = 0.0
    max_cookies = cps*time_left + cookies
    
    for item in build_info.build_items():
        cps_cost_ratio = build_info.get_cps(item)/build_info.get_cost(item)
        if cps_cost_ratio > max_cps_cost_ratio and build_info.get_cost(item) <= max_cookies:
            best_item = item
            max_cps_cost_ratio = cps_cost_ratio
                
    return best_item
        
def run_strategy(strategy_name, time, strategy):
    """
    Run a simulation for the given time with one strategy.
    """
    state = simulate_clicker(provided.BuildInfo(), time, strategy)
    print strategy_name, ":", state

    # Plot total cookies over time

    # Uncomment out the lines below to see a plot of total cookies vs. time
    # Be sure to allow popups, if you do want to see it

    # history = state.get_history()
    # history = [(item[0], item[3]) for item in history]
    # simpleplot.plot_lines(strategy_name, 1000, 400, 'Time', 'Total Cookies', [history], True)

def run():
    """
    Run the simulator.
    """    
#    run_strategy("Cursor", SIM_TIME, strategy_cursor_broken)

    # Add calls to run_strategy to run additional strategies
#    run_strategy("Cheap", SIM_TIME, strategy_cheap)
#    run_strategy("Expensive", SIM_TIME, strategy_expensive)
    run_strategy("Best", SIM_TIME, strategy_best)
    
def test():
    """
    Run tests.
    """
    item = strategy_cheap(2.0, 1.0, [(0.0, None, 0.0, 0.0)], 1.0, \
                   provided.BuildInfo({'A': [5.0, 1.0], 'C': [50000.0, 3.0], 'B': [500.0, 2.0]}, 1.15))
    assert(item is None)
#     expected None but received "(Exception: Returned Type Mismatch) Expected type 'NoneType' but returned type 'str'."

run()
#test()


    

