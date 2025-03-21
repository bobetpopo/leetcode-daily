# Problem: 2115. Find All Possible Recipes from Given Supplies (Medium)

# Solution 1: Topological Sort (Kahn's Algorithm)

# Time: O(n + m + s)
# Space: O(n + m + s)
# Notes: Essentially a BFS starting from nodes with indegree 0 to create recipes in dependency order.
#        Uses a dependency_graph mapping each recipe to the recipes which require it, used for updating 
#          each dependent recipe's indegree after the necessary recipe is made.
#        Whenever the indegree of a dependency reaches 0, we can make it and so we add it to the queue.

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supplies_set = set(supplies)
        recipe_to_index = {recipe: idx for idx, recipe in enumerate(recipes)}
        dependency_graph = defaultdict(list)
        in_degree = [0] * len(recipes)

        for recipe_idx, ingredient_list in enumerate(ingredients):
            for ingredient in ingredient_list:
                if ingredient not in supplies_set:
                    dependency_graph[ingredient].append(recipes[recipe_idx])
                    in_degree[recipe_idx] += 1
            
        queue = deque(idx for idx, count in enumerate(in_degree) if count == 0)
        created_recipes = []

        while queue:
            recipe_idx = queue.popleft()
            recipe = recipes[recipe_idx]
            created_recipes.append(recipe)

            for dependent_recipe in dependency_graph[recipe]:
                in_degree[recipe_to_index[dependent_recipe]] -= 1
                if in_degree[recipe_to_index[dependent_recipe]] == 0:
                    queue.append(recipe_to_index[dependent_recipe])

        return created_recipes
        
