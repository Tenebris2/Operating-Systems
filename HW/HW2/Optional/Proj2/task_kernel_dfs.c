#include <linux/sched/signal.h> 
#include <linux/init.h>
#include <linux/kernel.h>
#include <linux/module.h>

///< The license type -- this affects runtime behavior 
MODULE_LICENSE("GPL"); 

///< The author -- visible when you use modinfo 
MODULE_AUTHOR("Bui Duc Anh"); 

///< The description -- see modinfo 
MODULE_DESCRIPTION("A Linux Kernel Module for Listing Tasks"); 

///< The version of the module 
MODULE_VERSION("0.1"); 


void dfs(struct task_struct *task) {
    struct list_head *list;
    struct task_struct *child;

    pr_info("Name: %s - State: %c - PID: %d\n", task->comm, task_state_to_char(task), task->pid);

    list_for_each(list, &task->children) {
        child = list_entry(list, struct task_struct, sibling);
        /* task points to the next child in the list */
        dfs(child);
    }
    
}
static int __init hello_start(void) 
{ 
	printk(KERN_INFO "Loading module...\n"); 
	printk(KERN_INFO "Listing tasks...\n"); 

    dfs(&init_task);

	return 0; 
} 

static void __exit hello_end(void) 
{ 
	printk(KERN_INFO "Unloading Module...\n"); 
} 

module_init(hello_start); 
module_exit(hello_end); 