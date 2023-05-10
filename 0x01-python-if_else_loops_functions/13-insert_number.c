#include "lists.h"


/**
 * insert_node - insert a new node to the beginning of a sorted
 *	singly linked list.
 *
 * @head: head of the linked list
 * @number: number to add
 *
 * Return: listint_t address pointer to the new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head;
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	if (node == NULL || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	new->next = node->next;
	node->next = new;

	return (new);
}
