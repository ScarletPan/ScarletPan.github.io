---
layout: post
title: Leetcode 654 - Maximum Binary Tree
categories: Algorithm
comments: true
description: leetcode
keywords: stack
---

本文重点强调辅助栈对构建二叉树的作用。

<script type="text/javascript" async
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-MML-AM_CHTML">
</script>


## 1. 题目
Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

1. The root is the maximum number in the array.
2. The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
3. The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
Construct the maximum tree by the given array and output the root node of this tree.

<b> Example 1 </b> : 

```
Input: [3,2,1,6,0,5]
Output: return the tree root node representing the following tree:

      6
    /   \
   3     5
    \    / 
     2  0   
       \
        1
```

<b> Note </b>: 

1. The size of the given array will be in the range [1,1000].


## 2. 递归解法
拿到题目一看，第一思路就是先找数组最大，然后对最大值左侧右侧递归建树。找最大需要$O(N)$复杂度，整个复杂度取决于树的高度：
  * 最好的情况下树高为$O(logN)$，总时间复杂度 $O(NlogN)$;
  * 最坏情况为输入有序数组，树高为$O(N)$，总时间复杂度 $O(N^2)$;

代码如下：

```cpp
class Solution {
public:
    TreeNode* constructMaximumBinaryTree(vector<int>& nums) {
        int max_num = -5000, root_idx;
        if (nums.size() == 0)
            return NULL;
        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] > max_num) {
                max_num = nums[i];
                root_idx = i;
            }
        }
        struct TreeNode* root = new TreeNode(max_num);
        vector<int> left_nums, right_nums;
        for (int i = 0; i < root_idx; ++i)
            left_nums.push_back(nums[i]);
        for (int i = root_idx + 1; i < nums.size(); ++i)
            right_nums.push_back(nums[i]);
        root->left = constructMaximumBinaryTree(left_nums);
        root->right = constructMaximumBinaryTree(right_nums);
        return root;
    }
};
```

## 3. 非递归解法
众所周知，递归会影响程序的效率，针对这个题目，我们可以用一个辅助栈(Stack)来帮助迭代法构建最大二叉树。

### 3.1. 观测建树过程
假设我们此时已经迭代过程中构建好了位置 $ i $ 前的树如下所示，其中E为 $ i $ 的节点，A, B, C, D均为 $ index < i $ 的节点：

<img src="/images/post/post_18_09_05-1.png" width="80%">

我们可以注意到左数的最右侧路径(Path）为递减顺序，即 A > B > C > D。当E为不同值的时候，插入的结果如下：

<img src="/images/post/post_18_09_05-2.png" width="100%">

可以看到当E为不同值的时候，它的插入只会影响A, B, C, D右子树，而不会影响左子树，所以实际上我们只需要维护一个最右侧的路径即可。当知晓最右侧路径之后，我们可以从最底端开始比较，如果新插入的节点大于某个节点，则将该节点进行插入。

### 3.2. 辅助栈建树
我们可以用一个辅助栈来维护最右侧路径，同时不破坏当前树的结构。我们以一个实例来演示辅助栈是如何工作的。假设输入为 {3, 2, 6, 4, 5, 1, 8, 7}

<img src="/images/post/post_18_09_05-3.png" width="100%">

### 3.3. 非递归解法代码

```cpp
class Solution {
public:
    TreeNode* constructMaximumBinaryTree(vector<int>& nums) {
        vector<TreeNode*> stack;
        stack.push_back(new TreeNode(INT_MAX));
        for (auto num: nums) {
            TreeNode* tmp = new TreeNode(num);
            while (num > stack.back()->val) {
                stack.pop_back();
            }
            tmp->left = stack.back()->right;
            stack.back()->right = tmp;
            stack.push_back(tmp);
        }
        return stack.front()->right;
        
    }
};
```

### 3.4. 复杂度
我们可以看到，最好的情况为增序或降序序列输入，即while循环只判断一次，复杂度为$O(N)$。最差为$O(NlogN)$.







