#include "lists.h"
#include <stdlib.h>
#include <stdint.h>
/**
 * insert_nodeint_at_index - inserts a node at point specified by index
 * @head: pointer to address of list
 * @idx: point which node is to be inserted
 * @n: node's data
 * Return: pointer to modified node
*/
listint_t *insert_nodeint_at_index(listint_t **head, unsigned int idx, int n)
{
	unsigned int  i = 0;
	listint_t *node, *ptr = *head, *preptr = *head;

	node = malloc(sizeof(listint_t));
	if (!node)
		return (NULL);
	node->n = n;
	node->next = NULL;

	if (!ptr && !idx)
	{
		*head = node;
		return (*head);
	}
	if (ptr && !idx)
	{
		node->next = *head;
		*head = node;
		return (*head);
	}
	if (!ptr && idx)
		return (NULL);
	while (i != idx && ptr)
	{
		i++;
		preptr = ptr;
		ptr = ptr->next;
	}
	if (i != idx)
		return (ptr);
	preptr->next = node;
	node->next = ptr;
	return (*head);
}
/**
 * insert_node - inserts a node in a sorted list
 * @head: pointer to node head
 * @number: value to be inserted to list
 * Return: inserted node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head;
	unsigned int i = 0;

	while (node)
	{
		if (node->n >= number)
			break;
		i++;
		node = node->next;
	}
	return (insert_nodeint_at_index(head, i, number));
}
