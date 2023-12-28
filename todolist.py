# defining the function to add tasks to the list  
def add_task():  
      
    task_string = task_field.get()  
     
    if len(task_string) == 0:  
         
        messagebox.showinfo('Error', 'Field is Empty.')  
    else:  
         
        the_cursor.execute('insert into tasks values (?)', (task_string,))  
        
        list_update()  
          
        tasks.append(task_string)  
         
        task_field.delete(0, 'end')  
