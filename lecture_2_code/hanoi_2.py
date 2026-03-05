#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 15:15:46 2026

@author: geo
"""

def init_pegs(n):
    # Pegs stored as stacks (largest disk = largest number)
    return {
        1: list(range(n, 0, -1)),
        2: [],
        3: []
    }


def print_pegs(pegs, n):
    print("\nCurrent state:")
    
    # Maximum disk width for formatting
    max_width = n * 2 + 1
    
    # Print from top level down
    for level in range(n - 1, -1, -1):
        row = ""
        for peg in (1, 2, 3):
            if level < len(pegs[peg]):
                disk = pegs[peg][level]
                width = disk * 2 + 1
                row += f"{('#' * width).center(max_width)} "
            else:
                row += f"{'|'.center(max_width)} "
        print(row)
    
    print("-" * (max_width * 3 + 3))


def displayMove(fro, to, pegs, n):
    disk = pegs[fro].pop()
    pegs[to].append(disk)
    
    print(f"\nMove disk {disk} from {fro} to {to}")
    print_pegs(pegs, n)


def Towers(n, fro, to, spare, pegs, total_n):
    if n == 1:
        displayMove(fro, to, pegs, total_n)
    else:
        Towers(n - 1, fro, spare, to, pegs, total_n)
        Towers(1, fro, to, spare, pegs, total_n)
        Towers(n - 1, spare, to, fro, pegs, total_n)


# Run example
n = 10
pegs = init_pegs(n)

print_pegs(pegs, n)
Towers(n, 1, 2, 3, pegs, n)
