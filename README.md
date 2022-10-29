### Test Functions for Global Optimization

#### Uni-modal: unimodal_test_functions.py

| Name | Function                                                | Dimension | Range         | Global minima |
| ---- | ------------------------------------------------------- | --------- | ------------- | ------------- |
| f1   | $f(x)=\sum_{i=1}^nx_i^2$                                | 30        | [-100, 100]   | 0             |
| f2   | $f(x)=\sum_{i=1}^n|x_i|+\prod_{i=1}^n|x_i|$             | 30        | [-10, 10]     | 0             |
| f3   | $f(x)=\sum_{i=1}^n(\sum_{j=1}^ix_j)^2$                  | 30        | [-100, 100]   | 0             |
| f4   | $f(x)=\max_i\{|x_i|,1\leq i\leq n\}$                    | 30        | [-100, 100]   | 0             |
| f5   | $f(x)=\sum_{i=1}^{n-1}[100(x_{i+1}-x_i)^2+(x_i-1)^2]^2$ | 30        | [-30, 30]     | 0             |
| f6   | $f(x)=([x_i+0.5])^2$                                    | 30        | [-100, 100]   | 0             |
| f7   | $f(x)=\sum_{i=1}^nix_i^4+random[0,1)$                   | 30        | [-1.28, 1.28] | 0             |



------

#### Multi-modal: multimodal_test_functions.py

| Name                        | Function                                                     | Dimension | Range       | Global peaks |
| --------------------------- | ------------------------------------------------------------ | --------- | ----------- | ------------ |
| two-peak trap               | $f(x)=\left\{\begin{aligned}&\frac{160}{15}(15-x),0\leq x<15\\&\frac{200}{5}(x-15),15\leq x\leq 20\end{aligned}\right.$ | 1         | [0, 20]     | 1            |
| central two-peak trap       | $f(x)=\left\{\begin{aligned}x=1\\x=2\end{aligned}\right.$    | 1         | [0, 20]     | 1            |
| equal maxima                | $f(x)=\sin^6(5\pi x)$                                        | 1         | [0, 1]      | 5            |
| uneven maxima               | $f(x)=\sin^6(5\pi(x^{3/4}-0.05))$                            | 1         | [0, 1]      | 5            |
| inverted Shubert function   | $f(x)=-\prod_{i=1}^n\sum{j=1}^5j\times\cos[(j+1)x_i+j]$      | $n$       | [-10, 10]   | $n\times3^n$ |
| inverted Vincent function   | $f(x)=\frac{1}{n}\sum_{i=1}^n\sin(10\log(x_i))$              | $n$       | [0.25, 10]  | $6^n$        |
| inverted Rastrigin function | $f(x)=-\sum_{i=1}^n(x_i^2-10\cos(2\pi x_i)+10)$              | $n$       | [-1.5, 1.5] | 1            |

