---
layout: post
title: Tree Traversal
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
对于树来讲，从某个节点出发，可以有多个可以前往的节点，从而树的遍历形式多样。实际是通过推迟对某个节点的访问（输出）来控制遍历方式。一般来讲，树的遍历直观可以用递归的思路，如果要用到迭代法遍历，则需要一个辅助栈(stack)来维护这个顺序输出。而辅助栈的作用实际是维护当前访问节点的一个successor，因此可以用threading binary tree的概念来减少这个开支。
### 1.1. 中序(In-order)遍历
#### 1.1.1 过程不可变更原树的结构
遍历顺序为： 左子树->根节点->右子树，时间复杂度为$O(N)$，空间复杂度为$O(N)$。
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
    while (!stk.empty() || curr) {
        if (curr) {
            stk.push(curr);
            curr = curr->left;
        } else {
            curr = stk.top();
            stk.pop();
            visit(curr);
            curr = curr->right;
        }
    }
}
```
#### 1.1.2 过程可变更原树的结构(Morris Traversal)

```c++
void inorderTraversal(TreeNode* root) {
    TreeNode* curr = root;
    while (curr) {
        // 如果是叶节点，则访问它，并通过之前建立的
        // threading链接到它的successor。
        if (!curr->left) {
            visit(curr);
            curr = curr->right;
        } else {
            // 如果当前节点不是叶节点，则寻找其在左子树中的precessor。
            TreeNode* prev = curr->left;
            while (prev->right && prev->right != curr)
                prev = prev->right;
            // 如果其precessor还没有与其建立threading，则建立
            if (!prev->right) {
                prev->right = curr;
                curr = curr->left;
            } else {
            // 如果已经建立了threading，说明访问是从其precessor过来的，
            // 其precessor已经被访问过，将threading删除，访问当前节点，
            // 将最右节点置为当前节点
                prev->right = NULL;
                visit(curr);
                curr = curr->right;
            }
        }
    }
    return res;
}
```
首先由于只维护了curr指针与prev指针，因此空间复杂度为$O(1)$。对于时间复杂度，对每个节点进行输出，因此复杂度必有$O(N)$，接下来就是探讨每次搜索precessor的时间开销。实际上，每个节点找precessor的路径不会重叠（每个节点都是从其左子树的右侧路径找），因此开销只有两倍的edge的数量，最右侧的节点不是任何一个节点的precessor，即访问的边数```2(N-1) - rightmost path length```，因此算上visit的```N```开销，总的时间复杂度仍然是$O(N)$。


### 1.2 前序(Pre-order)遍历
#### 1.2.1 过程不可变更原树的结构
遍历顺序为： 根节点->左子树->右子树，时间复杂度为$O(N)$，空间复杂度为$O(N)$。
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
    if (!root) return;
    stack<TreeNode*> stk;
    stk.push(root);
    while (!stk.empty()) {
        TreeNode* node = stk.top();
        stk.pop();
        visit(node);
        if (node->right) stk.push(node->right);
        if (node->left) stk.push(node->left);
    }
    return res;
    }
}
```

#### 1.2.2 过程可变更原树的结构(Morris Traversal)

#### 1.2.3 相关问题
* [多叉树前序遍历](https://leetcode.com/problems/n-ary-tree-preorder-traversal/description/)


### 1.3. 后序(Post-order)遍历
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
    TreeNode* curr = root, *prev = NULL;
    while (!stk.empty() || curr) {
        if (curr) {
            stk.push(curr);
            curr = curr->left;
        } else {
            TreeNode* node = stk.top();
            # stk.top() 的左节点为NULL或者访问过得，因此
            # 只有两种情况可以访问该节点
            # (1) 该节点没有右节点。
            # (2) 该节点的右节点被访问过。且根据访问顺序，如果该右节点
            # 正好是上一个被访问的节点。
            if (node->right && node->right != prev) {
                curr = node->right;
            } else {
                visit(node);
                stk.pop();
                prev = node;
                curr = NULL;
            }
        }
    }
}
```
我们也换一种思路，假设我们能实现倒序的后序遍历，只要倒序之后再倒序就可以得到这样的后序序列了，代码如下。
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
相关问题
* [多叉树后序遍历](https://leetcode.com/problems/n-ary-tree-postorder-traversal/description/)


### 1.4 层序(Level-order)遍历
```c++
void level_order_traversal(TreeNode* root) {
    if (!root) return;
    queue<TreeNode* > q;
    q.push(root);
    while (!q.empty()) {
        int n = q.size();
        vector<int> tmp;
        for (int i = 0; i < n; ++i) {
            TreeNode* node = q.front();
            q.pop();
            visit(node);
            if (node->left) q.push(node->left);
            if (node->right) q.push(node->right);
        }
    }
    return res;
}
```

相关变体问题如下：
* [多叉树层序遍历](https://leetcode.com/problems/n-ary-tree-level-order-traversal/description/)
* [ZigZag层序遍历（蛇形遍历）](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/)
    * 主要思路是维护一个zig的bool value，通过zig来判断每层遍历的方向，idx = i 或者 idx = n - i - 1;
* [自底向上层序遍历](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/)
    * 标准层序遍历后相反地输出。

<br>
<br>

## 2. 通过若干遍历结果重构二叉树
### 2.1 前序和中序遍历结果重构二叉树
```
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

    3
   / \
  9  20
    /  \
   15   7
```
* **思考**
<br> preorder的第一个元素为子树的root，然后我们可以去inorder寻找根节点i，从而得到左子树的元素个数i - st，则preorder[pre_st + 1: pre_st + n] 为左子树的preorder，preorder[pre_st+n+1:pre_end]为右子树的preorder，inorder[in_st, i - 1]为左子树的inorder，inorder[i + 1, in_end]为右子树的inorder，递归往下即可
```
[[3], [9], [20, 15, 7]]
[[9], [3], [15, 20, 7]]
...
```
* **解决思路1: 递归**
<br> 每一次递归时，首先先搜索root在inorder的位置，再将preorder, inorder分成左右子树进行递归，搜索的复杂度为$O(N)$，因此总时间复杂度为$O(N^2)$，空间复杂度为$O(N)$。
    ```c++
    class Solution {
    public:
        TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
            return helper(preorder, 0, preorder.size() - 1, inorder, 0, inorder.size() - 1);
        }
        
        TreeNode* helper(vector<int>& preorder, int pre_st, int pre_end, vector<int>& inorder, int in_st, int in_end) {
            if (pre_st > pre_end || pre_end >= preorder.size() || in_end >= inorder.size()) return NULL;
            int root_idx = -1;
            for (int i = in_st; i <= in_end; ++i)
                if (inorder[i] == preorder[pre_st])
                    root_idx = i;
            TreeNode* node = new TreeNode(preorder[pre_st]);
            node->left = helper(preorder, pre_st + 1, pre_st + root_idx - in_st, inorder, in_st, root_idx - 1);
            node->right = helper(preorder, pre_st + root_idx - in_st + 1, pre_end, inorder, root_idx + 1, in_end);
            return node;
        }
    };
    ```
<br>通过对程序分析可以发现在遍历过程中pre_st为1，2，3，...的增序序列，而在每次递归的时候只会访问pre_st，因此pre_end是多余的。改写如下：
```c++
class Solution {
public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        int pre_st = 0;
        return helper(preorder, inorder, pre_st, 0, inorder.size() - 1);
    }
    TreeNode* helper(vector<int>& preorder, vector<int>& inorder, 
                    int &pre_st, int in_st, int in_end) {
        if (in_st > in_end || in_end >= inorder.size()) return NULL;
        TreeNode* node = new TreeNode(preorder[pre_st++]);
        if (in_st == in_end) return node;
        int root_idx = -1;
        for (int i = in_st; i <= in_end; ++i)
            if (inorder[i] == node->val)
                root_idx = i;
        node->left = helper(preorder, inorder, pre_st, in_st, root_idx - 1);
        node->right = helper(preorder, inorder, pre_st, root_idx + 1, in_end);
        return node;
    }
};
```

* **解决思路2: hash表保存root的在中序表中的位置**
<br> 如法一，我们每次都需要搜索某个root_value在inorder的位置，因此可以用hash来加快搜索速度使得搜索复杂度为$O(1)$，总的时间复杂度为$O(N)$，空间复杂度为$O(N)$
    ```c++
    class Solution {
    public:
        TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
            int pre_st = 0;
            map<int, int> m;
            for (int i = 0; i < inorder.size(); ++i)
                m[inorder[i]] = i;
            return helper(preorder, inorder, pre_st, 0, inorder.size() - 1, m);
        }
        
        TreeNode* helper(vector<int>& preorder, vector<int>& inorder, 
                        int &pre_st, int in_st, int in_end,
                        map<int, int>& m) {
            if (in_st > in_end || in_end >= inorder.size()) return NULL;
            TreeNode* node = new TreeNode(preorder[pre_st++]);
            if (in_st == in_end) return node;
            int root_idx = m[node->val];
            node->left = helper(preorder, inorder, pre_st, in_st, root_idx - 1, m);
            node->right = helper(preorder, inorder, pre_st, root_idx + 1, in_end, m);
            return node;
        }
    };
    ```
* **解决思路3: 使用辅助栈迭代**
<br> 遍历preorder数组一次，inorder数组一次，因此总的时间复杂度为 $O(N)$，最差空间复杂度为$O(N)$
    ```c++
    class Solution {
    public:
        TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
            if (preorder.empty()) return NULL;
            TreeNode *p = NULL, *root = new TreeNode(preorder[0]);
            stack<TreeNode* > stk;
            stk.push(root);
            for (int pre = 1, in = 0; pre < preorder.size(); ++pre) {
                # 中序最前的元素为子树的最左节点，如果与当前遍历的前序元素不等，
                # 则是路径中的元素，构建最左侧路径并压入栈。
                if (stk.empty() || stk.top()->val != inorder[in]) {
                    stk.top()->left = new TreeNode(preorder[pre]);
                    stk.push(stk.top()->left);
                } else {
                    # 如果路径中的节点都没有右侧节点，则该路径中序与前序相反（即和栈里顺序相同），出栈即可。
                    # 如果有右侧节点，则preorder的最前元素即为栈顶节点的右侧节点，连上边后对其重新开始递归
                    while (!stk.empty() && stk.top()->val == inorder[in]) {
                        p = stk.top();
                        stk.pop();
                        in++;
                    }
                    p->right = new TreeNode(preorder[pre]);
                    stk.push(p->right);
                }
            }
            return root;
        }
    };
    ```

### 2.2 中序和后序遍历结果重构二叉树
```
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]

   3
   / \
  9  20
    /  \
   15   7

```

* **思考**
<br> 解决思路基本很中序与前序生成二叉树一致，我们只要从inorder和postorder的最后开始，先右子树，后左子树即可

* **解决思路1：递归法**
    ```c++
    class Solution {
    public:
        TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
            int post_end = postorder.size() - 1;
            return helper(inorder, postorder, 0, inorder.size() - 1, post_end);
        }

        TreeNode* helper(vector<int>& inorder, vector<int>& postorder, int st, int end, int &post_end) {
            if (st > end || end >= inorder.size() || post_end < 0) {
                return NULL;
            }
            TreeNode* node = new TreeNode(postorder[post_end--]);
            if (st == end) return node;
            int root_idx = -1;
            for (int i = st; i <= end; ++i) {
                if (inorder[i] == node->val)
                    root_idx = i;
            }
            node->right = helper(inorder, postorder, root_idx + 1, end, post_end);
            node->left = helper(inorder, postorder, st, root_idx - 1, post_end);
            return node;
        }
    };
    ```
* **解决思路2：迭代法**
    ```c++
    class Solution {
    public:
        TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
            if (postorder.empty()) return NULL;
            TreeNode* p = NULL, *root = new TreeNode(postorder[postorder.size() - 1]);
            stack<TreeNode* > stk;
            stk.push(root);
            for (int post = postorder.size() - 2, in = inorder.size() - 1; post >= 0; post--) {
                if (stk.empty() || stk.top()->val != inorder[in]) {
                    stk.top()->right = new TreeNode(postorder[post]);
                    stk.push(stk.top()->right);
                } else {
                    while (!stk.empty() && stk.top()->val == inorder[in]) {
                        p = stk.top();
                        stk.pop();
                        in--;
                    }
                    p->left = new TreeNode(postorder[post]);
                    stk.push(p->left);
                }
            }
            return root;
        }
    };
    ```

### 2.2 前序和后序遍历结果重构二叉树（无唯一解）
* **解决思路1：递归法**
```c++
class Solution {
public:
    TreeNode* constructFromPrePost(vector<int>& pre, vector<int>& post) {
        if (pre.empty()) return NULL;
        return helper(pre, post, 0, pre.size() - 1, 0, post.size() - 1);
    }

    TreeNode* helper(vector<int>& pre, vector<int>& post, int pre_st, int pre_end, int post_st, int post_end) {
        if (post_st > post_end || pre_st > pre_end ||
            pre_end >= post.size() || post_end >= post.size()) 
            return NULL;
        TreeNode* root = new TreeNode(pre[pre_st]);
        if (pre_st == pre_end) return root;
        int left_root_idx = -1, pre_st_1 = pre_st + 1, pre_st_2 = pre_st + 2;
        for (int i = post_st; i <= post_end; ++i)
            if (post[i] == pre[pre_st_1])
                left_root_idx = i;
        for (int i = pre_st; i <= pre_end; ++i)
            if (pre[i] == post[post_end - 1])
                pre_st_2 = i;
        root->left = helper(pre, post, pre_st_1, pre_st_1 + left_root_idx - post_st, post_st, left_root_idx);  
        root->right = helper(pre, post, pre_st_2, pre_end, left_root_idx + 1, post_end - 1);
        return root; 
    }
};
```
* **解决思路2：迭代法**

```c++
class Solution {
public:
    TreeNode* constructFromPrePost(vector<int>& pre, vector<int>& post) {
        if (pre.empty()) return NULL;
        stack<TreeNode* > stk;
        TreeNode* root = new TreeNode(pre[0]);
        stk.push(root);
        for (int i = 1, j = 0; i < pre.size(); ++i) {
            TreeNode* node = new TreeNode(pre[i]);
            while (stk.top()->val == post[j]) {
                stk.pop();
                ++j;
            }
            if (stk.top()->left) {
                stk.top()->right = node;
            } else {
                stk.top()->left = node;
            }
            stk.push(node);
        }
        return root;
    }
};
```