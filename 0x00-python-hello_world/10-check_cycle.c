#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "lists.h"


/**
 * check_cycle - check if listint_t *list has a cycle
 *
 * @list: listint_t pointer to head of the linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *tortoise;
	listint_t *hare;

	if (list == NULL)
	{
		return (0);
	}

	tortoise = list;
	hare = list;
	while (hare->next != NULL && hare->next->next != NULL)
	{
		tortoise = tortoise->next;
		hare = hare->next->next;
		if (tortoise == hare)
			return (1);
	}
	return (0);
}
