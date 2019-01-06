---
layout: post
title: Tree Traversal Applications
categories: Algorithm
comments: true
description: leetcode
keywords: tree
---

本文介绍二叉树遍历的的几种情况，并将一些问题归化到二叉树遍历问题。

<script type="text/javascript" async
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-MML-AM_CHTML">
</script>


## 1. 二叉树遍历的几种形式
对于树来讲，从某个节点出发，可以有多个可以前往的节点，从而树的遍历形式多样。实际是通过推迟对某个节点的访问（输出）来控制遍历方式。一般来讲，树的遍历直观可以用递归的思路，如果要用到迭代法遍历，则需要一个辅助栈(stack)来维护这个顺序输出。
### 1.1 深度优先遍历
#### 1.1.1. 前序(Pre-order)遍历
遍历顺序为： 根节点->左子树->右子树
递归形式：

```c++
void pre_order_traversal(TreeNode* root) {
    visit(root->val); // can be any operation
    if (!root->left)
        pre_order_traversal(root->left);
    if (!root->right)
        pre_order_traversal(root->right);
}
```
迭代改写如下:

```c++
void pre_order_traversal(TreeNode* root) {
    stack<TreeNode* > stk;
    for (stk.push(root); !stk.empty();) {
        TreeNode* node = stk.top();
        visit(node);
        stk.pop()
        if (node->right) stk.push(node->right);
        if (node->left) stk.push(node->left);
    }
}
```

#### 1.1.2. 中序(In-order)遍历
遍历顺序为： 左子树->根节点->右子树
递归形式：

```c++
void in_order_traversal(TreeNode* root) {
    if (!root->left)
        in_order_traversal(root->left);
    visit(root->val); 
    if (!root->right)
        in_order_traversal(root->right);
}
```

迭代改写如下:

```c++
void in_order_traversal(TreeNode* root) {
    stack<TreeNode* > stk;
    TreeNode* curr = root;
    while (curr || !stk.empty()) {
        for (; curr; curr = curr->left)
            stk.push(curr);
        curr = stk.top();
        stk.pop();
        visit(curr);
        curr = curr->right;
    }
}
```

#### 1.1.3. 后序(Post-order)遍历
遍历顺序为： 左子树->右子树->根节点
递归形式：

```c++
void post_order_traversal(TreeNode* root) {
    if (!root->left)
        post_order_traversal(root->left);
    if (!root->right)
        post_order_traversal(root->right);
    visit(root->val); 
}
```
迭代改写如下:
```c++
void post_order_traversal(TreeNode* root) {
    stack<TreeNode* > stk;
    TreeNode* curr = root;
    while (curr || !stk.empty()) {
        if (!curr) {
            stk.push(curr);
            curr = curr->left;
        } else {
            TreeNode* tmp = stk.top()->right;
            if (tmp) {
                curr = tmp;
            } else {
                tmp = stk.top();
                stk.pop();
                visit(tmp->val);  // 左右子树都没了（即叶节点），则访问它
                while (!stk.empty() && tmp == stk.top()->right) {
                    // 如果pop出来的节点为栈顶节点的右儿子，则访问它
                    tmp = stk.top();
                    stk.pop();
                    visit(tmp->val);
                }   
            }
        }
        
    }

}
```
可以看到是非常麻烦的，但是换一种思路，假设我们能实现倒序的后序遍历，只要倒序之后再倒序就可以得到这样的后序序列了，代码如下。
```c++
void post_order_traversal(TreeNode* root) {
    if (!root) return;
    vector<TreeNode*> res;
    stack<TreeNode*> stk;
    stk.push(root);
    while (!stk.empty()) {
        TreeNode* tmp = stk.top();
        stk.pop();
        if (tmp->left) stk.push(tmp->val);
        if (tmp->right) stk.push(tmp->val);
        res.push_back(tmp);
    }
    for (int i = res.size() - 1; i >= 0; --i) {
        visit(res[i]);
    }
}
```


### 1.2. 广度优先遍历
#### 1.2.1 层序(Level-order)遍历

## 2. 通过若干遍历结果重构二叉树


## 3. 二叉树遍历归化问题
### 3.1 LeetCode 814 Binary Tree Pruning
