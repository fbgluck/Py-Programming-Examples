# # Sample Code for list methods

line_sep = '*'*30 #This is a global variable known to all functions
def fn_line_seperator():
   print(f"\n{line_sep}\n")
# ------------------------------
      
#*********** .append method *****************
#.append = appends a value to a list
shopping_list=['apples','bacon','carrots','doughnuts']
new_list = shopping_list.append('eggs')
#new_list is empty because .append method modifies in place -- a new list is not created.
print(f'new_list is now: {new_list}')
print(f'shopping_list is now: {shopping_list}')
fn_line_seperator()

# We can assign one list to another variable to make a copy of it
new_list = shopping_list
print(f'shopping_list is: {shopping_list}')
print(f'new_list is now: {new_list}')
fn_line_seperator()

#**** .insert METHOD *********************
# INSERT Item in list using Index
# .insert(<at_index>,<item>)
shopping_list.insert(2,'spaghetti')
print(f'modified shopping_list is now: {shopping_list}')
fn_line_seperator()

# ********* .extend Method *******************
#.extend method -- extends a list from the print
# This is an 'iterable' meaning it will do the
#.extend over the list of items 
shopping_list.extend(['flour','grapes','iodine'])
print ('fExtended shopping_list is now: {shopping_list}')
fn_line_seperator()

# # ************** .pop Method *******************
# ## removing (.pop) -- takes the index of the item. Returns the item that was removed.
shopping_list.pop() #no arguments, removes the last item
print ('The list is shorter now ....', shopping_list,'\n',30*'-','\n')
## .pop with an index of 0
shopping_list.pop(0)
print ('The item at index 0 is gone', shopping_list,'\n',30*'-','\n')

# # ***** Remove Method *************
# ## .remove - removes the item with a specified value from the list. Works in place
shopping_list.remove('carrots')
print('Our shopping list is shorter..', shopping_list,'\n',30*'-','\n')
## EXPERIMENT -- what happens if we remove an item not in the list
# shopping_list.remove('zzyzx')

# # ***********. clear method *****************
# ## clear removes whatever is in the list
shopping_list.clear()
print('The list is now empty... see...', shopping_list,'\n',30*'-','\n')

# ## Reset the list
shopping_list=['apples','bacon','carrots','doughnuts']
print(shopping_list,'\n',30*'-','\n')
# # Find what index a particular item is in a list
print('The item you are looking for is index ...', shopping_list.index('carrots'),'\n',30*'-','\n')
# You can also supply start and Stop
# print('We can search from start to stop..', shopping_list.index('carrots',0,2),'\n',30*'-','\n')

# ## IN keyword -- returns true or false
print('carrots' in shopping_list,'\n',30*'-','\n') #used with list
print ('hello' in 'hello world','\n',30*'-','\n') #used in string
print('Are Carrots in the list?..',
   'carrots' in shopping_list[0:2],
   '\n',30*'-','\n')

# ## Count how many times an item occurs
target = 'carrots'
print(target.title(),
 'occurs '
 ,shopping_list.count(target),
 ' times',
 '\n',30*'-','\n' )

# This will not work.... why??
target = 'r'
print(f'{target} occurs {shopping_list.count(target)}times')
fn_line_seperator

# use count with strings
target_string = 'carrots'
find_string="r"
print(find_string,
 'occurs',
 target_string.count(find_string),
 'times in',
 target_string,
 '\n',30*'-','\n')

# #sort method
test_list=['Zane','Jean','Wally','Phil','Fred','Stacey','Albert']
print('The list is...',test_list,'\n',30*'-','\n')
test_list.sort() #modifies in place. No new list created
print('The sorted list is now:',test_list,'\n',30*'-','\n')
test_list.sort()

# # Buit in function sorted()
test_list=['Zane','Jean','Wally','Phil','Fred','Stacey','Albert']
new_list=test_list.sort()
print('New_list is now:',new_list,'\n',30*'-','\n')
test_list=['Zane','Jean','Wally','Phil','Fred','Stacey','Albert']
print('We have reset the list',test_list,'\n',30*'-','\n')
print('But if we use the sorted() function the list is sorted ...', sorted(test_list),'\n',30*'-','\n')
print('...and the original list is not touched',test_list,'\n',30*'-','\n')

# # .copy method -- copies the list and returns a new list
new_list=test_list.copy()
print('I just made new copy... here it is:',new_list,'\n',30*'-','\n')

# # reverse the list in place
test_list = ['c','g','a','w']
print('Our new list is:',test_list,'\n',30*'-','\n')
test_list.reverse()
print('Reverse The List:', test_list,'\n',30*'-','\n')

# # you can use a sorted, reversed basket
test_list = ['c','g','a','w']
test_list.sort()
test_list.reverse()
print('The sorted, reverse list is: ',test_list,'\n',30*'-','\n')