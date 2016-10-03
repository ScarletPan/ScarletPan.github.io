---
layout: post
title: Bayes Decision Rule
tags: Pattern_Classification
comments: true
modifed: 2016-10-04
---

> 情景引入： 作为一个classificaton的问题，假设有sea bass 和 salmon两类鱼，而我们决策的目的是为了区分它们，用于区分我们将引入feature这个概念，大致意思就是可以用一系列特征来判断出某一条打捞上来的鱼是sea bass还是salmon，在这里我们只取一条鱼的lightness作为feature。

#### 相关术语
* state of nature:
<p>&emsp;&emsp;在这个例子的前提下，我们可以断定自然状态下只有两种可能：sea bass和salmon. 如果我们用符号\\( w \\)来表示state of nature, 则\\( w = w\_1 \\)为sea bass, \\( w = w\_2 \\)为salmon</p>
* priori probability(**prior**):
<p>&emsp;&emsp;\\( P(w\_1) \\)指打捞上来的下一条鱼为sea bass, \\( P(w\_2) \\)指打捞上来的下一条鱼为salmon，很显然, \\( P(w\_1) + P(w\_2) = 1 \\). 从上述陈述中我们可以将prior理解为我们事先知道的知识，比如我们知道我们要打捞的海域这两种鱼的比例为2:1。
* class-conditional probability density(**likelihood**):
<p>&emsp;&emsp;\\( P(x \space | w\_j) \\), 用概率论的知识我们可以这么理解它：假设feature \\( x \\)在\\( w\_j \\)这一类中服从某种分布，那么在这一类鱼的lightness为某一直的概率越大，相应的\\( P(x \space | w\_j) \\)也就越大，比如说sea bass 的lightness 为10的可能性非常高，则\\( P(x=10 \space | w\_1) \\)也就非常大。
* evidence：
<p>&emsp;&emsp;\\( p(x) \\)， 在这个例子中表示的就是某个lightness在打捞上来的鱼中出现的概率有多高。同事我们也可以将其当做一个scale因子，这可以保证posterior概率之和为1.
* posterior：
<p>&emsp;&emsp;\\( P(w\_j \space | x) \\)， 在这个例子上即为当捞上一条鱼他的lightness为某一值时，它为sea bass和salmon的概率各自有多大

#### 贝叶斯公式
&emsp;&emsp;学过概率论的同学应该对下面这个式子并不陌生：
<center> \\[ P(w\_j  | x) = \frac{p(x \space | w\_j) P(w\_j)}{p(x)} \\] </center>
&emsp;&emsp;有了上面的术语解释，我们可以用相关的术语来表达这个式子:
<center> \\[ posterior = \frac{likelihood \times prior}{evidence} \\]</center>
&emsp;&emsp;这就是所谓的贝叶斯公式了
