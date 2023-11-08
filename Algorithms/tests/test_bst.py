import pytest
import random

from Algorithms.python_solutions.bst import BinarySearchTree


def test_insert_and_search():
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(3)

    assert str(bst.search(10)) == '10'
    assert str(bst.search(15)) == '15'
    assert str(bst.search(3)) == '3'
    assert bst.search(8) is None


@pytest.fixture
def bst():
    tree = BinarySearchTree()
    tree.insert(5)
    tree.insert(3)
    tree.insert(7)
    tree.insert(2)
    tree.insert(4)
    tree.insert(6)
    tree.insert(8)
    return tree


def test_in_order_traversal(bst):
    assert bst.in_order_traversal() == [2, 3, 4, 5, 6, 7, 8]


def test_successor_predecessor(bst):
    assert bst.find_successor(5) == 6
    assert bst.find_predecessor(3) == 2
    assert bst.find_successor(8) is None
    assert bst.find_predecessor(2) is None


def test_delete(bst):
    bst.delete(4)
    assert bst.in_order_traversal() == [2, 3, 5, 6, 7, 8]
    bst.delete(5)
    assert bst.in_order_traversal() == [2, 3, 6, 7, 8]
    bst.delete(2)
    assert bst.in_order_traversal() == [3, 6, 7, 8]
    bst.delete(8)
    assert bst.in_order_traversal() == [3, 6, 7]


def test_delete_with_error(bst):
    bst_list = bst.in_order_traversal()
    for _ in range(7):
        elt_to_delete = random.choice(bst_list)
        bst.delete(elt_to_delete)
    with pytest.raises(IndexError):
        bst.delete(None)


def test_search(bst):
    assert bst._search(bst.root, 3) is not None
    assert bst._search(bst.root, 9) is None


def test_find_min_and_max():
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(3)

    assert bst.find_min() == 3
    assert bst.find_max() == 15


def test_random_length_and_elts():
    bst = BinarySearchTree()
    assert bst.is_empty() is True
    assert bst.find_max() is None
    assert bst.find_min() is None
    bst_length = random.randint(1000, 2000)
    for _ in range(bst_length):
        bst.insert(random.randint(-1000, 1000))
    assert bst.is_empty() is False
    list_bst = bst.in_order_traversal()
    assert bst.find_max() == max(list_bst)
    assert bst.find_min() == min(list_bst)
    assert len(list_bst) == bst_length
    assert sorted(list_bst) == list_bst
    for _ in range(bst_length):
        elt_to_delete = random.choice(list_bst)
        bst.delete(elt_to_delete)
        list_bst.remove(elt_to_delete)
        assert len(list_bst) == bst.size
        assert sorted(list_bst) == bst.in_order_traversal()
    assert len(bst.in_order_traversal()) == 0
