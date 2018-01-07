---
layout: post
title: Bayes Decision Rule
categories: Theory
comments: true
description: Bayes Decision Rule
keywords: Bayes
---
本文是对Bayes Decision Rule的理解

<script type="text/javascript" async
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-MML-AM_CHTML">
</script>
> 情景引入： 作为一个classificaton的问题，假设有sea bass 和 salmon两类鱼，而我们决策的目的是为了区分它们，用于区分我们将引入feature这个概念，大致意思就是可以用一系列特征来判断出某一条打捞上来的鱼是sea bass还是salmon，在这里我们只取一条鱼的lightness作为feature。


<p>&emsp;&emsp;</p>

### 1. 相关术语
* state of nature:
<p>&emsp;&emsp;在这个例子的前提下，我们可以断定自然状态下只有两种可能：sea bass和salmon. 如果我们用符号 $ w $ 来表示state of nature, 则 $ w = w_1 $ 为sea bass, $ w = w_2 $为salmon</p>

* priori probability(**prior**):
<p>&emsp;&emsp;$ P(w_1) $指打捞上来的下一条鱼为sea bass, $ P(w_2) $指打捞上来的下一条鱼为salmon，很显然, $ P(w_1) + P(w_2) = 1 $. 从上述陈述中我们可以将prior理解为我们事先知道的知识，比如我们知道我们要打捞的海域这两种鱼的比例为2:1。

* class-conditional probability density(**likelihood**): </p>
<p>&emsp;&emsp;$ P(x \space | w_j) $, 用概率论的知识我们可以这么理解它：假设feature $ x $在$ w_j $这一类中服从某种分布，那么在这一类鱼的lightness为某一直的概率越大，相应的$ P(x \space | w_j) $也就越大，比如说sea bass 的lightness 为10的可能性非常高，则$ P(x=10 \space | w_1) $也就非常大。 </p>

* evidence：
<p>&emsp;&emsp;$ p(x) $， 在这个例子中表示的就是某个lightness在打捞上来的鱼中出现的概率有多高。同事我们也可以将其当做一个scale因子，这可以保证posterior概率之和为1. </p>

* posterior：
<p>&emsp;&emsp;$ P(w_j \space | x) $， 在这个例子上即为当捞上一条鱼他的lightness为某一值时，它为sea bass和salmon的概率各自有多大</p>
<p>&emsp;&emsp;</p>

### 2. 似然值(likelihood)和似然函数([likelihood funciton](https://en.wikipedia.org/wiki/Likelihood_function))
&emsp;&emsp;我们假设likelihood:$ p(x \space | w_j) $遵循某种涉及到参数$ \theta $的分布（比如关于$ (\mu, \sigma^2) $的正态分布, 则likelihood就相当于参数确定的给定分布下$ x $发生的概率。
<p>&emsp;&emsp;从而似然函数即为对于$\space data \space x \in X, state \space w \in W $的一个条件概率分布$ p(x \space | w) \space $</p>
<p>&emsp;&emsp;</p>

### 3. MLE 和 MAP
#### 3.1. Maximum likelihood Estimator(MLE)
&emsp;&emsp;在捞到的一堆鱼里面，统计得出对于sea bass鱼中$ lightness = x $ 出现的概率为 $ p_1 $, 对于salmon鱼中$ lightness = x $ 出现的概率为$ p_2 $，假如$ p_1 \ge  p_2 $，则我们可以粗浅的认为这条鱼是sea bass的可能性大一点，极端点想如果这个$ x $在sea bass中出现频率最高，而在salmon中几乎不出现，肯定没有理由将其归为salmon了。用数学化的表示如下：
$$ w(x) = argmax_w(p(x \space | w))　$$
<p>&emsp;&emsp;特别的，对于二元问题我们经一系列不等式变换，再套个log函数可以列出下面的式子：</p>
$$ log\frac{p(x \space | w_0)}{p(x \space | w_1)} > 0 则 w(x) = w_0, 否则w(x) = w_１ $$
<p>&emsp;&emsp;我们将不等式右边log里的比值称作 <i>likelihood ratio</i>，这在下面的贝叶斯决策中也会涉及到。</p>


#### 3.2. The Maximum A Posteriori(MAP)
&emsp;&emsp;与上面的ML类似, MAP不过就是把最大化的概率换成了posterior的, 如下公式：
$$ w(x) = argmax_w(p(w \space | x))　$$


###  4. 贝叶斯公式
&emsp;&emsp;学过概率论的同学应该对下面这个式子并不陌生：&emsp;$ P(w_j  | x) = \frac{p(x \space | w_j) P(w_j)}{p(x)} $。&emsp;
有了上面的术语解释，我们可以用相关的术语来表达这个式子:

<center> $$ posterior = \frac{likelihood \times prior}{evidence} $$ </center>
这就是所谓的贝叶斯公式了。
<p>&emsp;&emsp;我们知道，概率论中贝叶斯公式的推导是从下面这个等式中来的:</p>
<center>  $$  P(w_j  | x)p(x) = p(x \space | w_j) P(w_j)  $$  </center>
我们可以左右求和一下
<center>  $$  \sum P(w_j  | x)p(x) = \sum p(x \space | w_j) P(w_j)  $$  </center>
而　$$ \sum P(w_j  | x) = 1 $$ ，所以有
<center>  $$  p(x) = \sum p(x \space | w_j) P(w_j)  $$  </center>
因此贝叶斯公式又可以写成：
<center>  $$  P(w_j  | x) = \frac{p(x \space | w_j) P(w_j)}{\sum p(x \space | w_j) P(w_j)}  $$  </center>
<p>&emsp;&emsp;</p>

### 5. The Decision rules and loss function
&emsp;&emsp;假设我们捞上来一条鱼，通过上面陈述的一些方法，你将会判断它是sea bass还是salmon, 但是如果决策发生了错误怎么办？你会受到一定的损失(loss/cost), 这时候我们需要引进一个损失函数来判断这个决策到底会带来多大的损失，这就是loss function. 
<p>&emsp;&emsp;在讲loss function前，我们先来引进一些符号，我们用$ \alpha(.) $来表示一个　*decision rule*。</p>
<p>&emsp;&emsp;如果我们进行了一个决策$ \alpha(x) $, 得到的结果是$w $，我们定义loss function 为$ \lambda(\alpha(x),w)　$。 </p>
<p>&emsp;&emsp;</p>

### 6. The Risk 
&emsp;&emsp; 假设我们观察到了一个$ x $，通过相应的决策我们得到了$ \alpha(x) = w_i $, 将这个决策记为$ \alpha_i $。再假设我们要分的总类数为c，那么它的state of nature为$ w_j $的可能性以posterior的方式表达就是: $ p(w_j \space | x) $。
<p>&emsp;&emsp;有了上述的假设，我们就可以自然地定义采取决策$ \alpha_i $所会造成的风险(Risk)为
$$ R(\alpha_i | x) = \sum_{j=1}^c \lambda(\alpha_i \space | w_j)P(w_j|x) $$ </p>

### 7. Bayes Decision Theory
&emsp;&emsp; 通过以上所说的我们就可以定义贝叶斯决策理论了: 即寻找一个决策$ \hat(\alpha) $来使得Risk　$ R(\alpha) $最小。即:
$$ \hat\alpha = arg_{\alpha \in A}min(R(\alpha)), \alpha \in A $$
<p>&emsp;&emsp;　$ \hat\alpha  $被称作贝叶斯决策(<i>Bayes Decision</i>), $ R(\hat\alpha) $被称作贝叶斯风险(<i>Bayes Risk</i>) </p>


