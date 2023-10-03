#!/usr/bin/python3

def canUnlockAll(boxes):
    n = len(boxes)
    visited = [False] * n
    visited[0] = True
    stack = [0]  # Start with the first box (box 0)

    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if key >= 0 and key < n and not visited[key]:
                visited[key] = True
                stack.append(key)

    return all(visited)

# You can add more code for testing the function or other functionality here

if __name__ == "__main__":
    # Example usage:
    boxes = [[1], [2], [3], []]
    result = canUnlockAll(boxes)
    print(result)

