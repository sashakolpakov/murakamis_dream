# A polynomial bound for every original face coefficient at the positive spectral endpoint

At the real spectral endpoint \(+2\), every coefficient of the full original resolvent face polynomial is bounded by \(2N^3\). This includes the interior entries, both one-sided parts and the CROSS part, at both level parities. The proof retains the cancellation between one-step and two-step paths. It does not replace their signed continuant by its absolute path expansion.

Consequently, for any fixed marked diagram with \(r\) such boxes, the full shared source, its CROSS part, and their difference are polynomially bounded at the single spectral tuple \((2,\ldots,2)\). This is an endpoint statement, not a uniform bound on the spectral cube and not a filling-volume theorem.

## 1. The original interval continuant

Put \(N\ge2\), \(d=N-1\), \(\theta=\pi/N\), and
\[
 c_j=2\cos((2j+1)\theta),\quad s_j=2\sin(j\theta),\quad
 \gamma_j=2-c_j=4\sin^2((j+\tfrac12)\theta).
 \tag{1}
\]
The actual homogeneous face operator at outer variables \(x,y\) is
\[
 C(x,y)z^j=c_jz^j-s_j^2(x+y)z^{j-1}
                         -s_js_{j-1}xy z^{j-2}.
 \tag{2}
\]
The matrix acts by columns on \(1,z,\ldots,z^d\). The source polynomial is defined from the full numerator
\[
 V_N(\sigma;C)=\chi_N(\sigma)(\sigma I-C)^{-1},
 \qquad \chi_N(\sigma)=2T_N(\sigma/2)+2.
 \tag{3}
\]
All repeated-root information is retained. At \(\sigma=2\), \(\chi_N(2)=4\) and every \(\gamma_j>0\).

Fix an interval \(0\le i\le j\le d\). Set \(x=S,y=1\). Its cleared signed continuant satisfies
\[
 \begin{split}
 P_{i,i}&=1,\qquad P_{i,i+1}=-s_{i+1}^2(1+S),\\
 P_{i,j}&=-s_j^2(1+S)P_{i,j-1}
             -s_js_{j-1}\gamma_{j-1}S P_{i,j-2}.
 \end{split}
 \tag{4}
\]
Indeed a decreasing path enters its final interval by a one-step arrow or a two-step arrow. In the second case the skipped row contributes its unused factor \(\gamma_{j-1}\). Both arrows of \(C\) are negative, giving the two signs in (4). Thus the full original numerator entry is exactly
\[
 [V_N(2;C(S,1))]_{i,j}
   =P_{i,j}(S)
       \prod_{\substack{0\le r<i\\\text{or }j<r\le d}}\gamma_r.
 \tag{5}
\]
There is no sum over omitted normal channels in (5).

Normalize only the continuant:
\[
 P_{i,j}(S)
   =(-1)^{j-i}\left(\prod_{r=i+1}^j s_r^2\right)
                                  h_{i,j}(S).
 \tag{6}
\]
Then \(h_{i,i}=1\), \(h_{i,i+1}=1+S\), and
\[
 h_{i,j}=(1+S)h_{i,j-1}-\rho_jS h_{i,j-2},
 \qquad
 \rho_j=\frac{\gamma_{j-1}}{s_js_{j-1}}=1+\varepsilon_j,
 \tag{7}
\]
\[
 \varepsilon_j=
 \frac{\sin^2(\theta/2)}{\sin(j\theta)\sin((j-1)\theta)}
 \quad(2\le j\le d).
 \tag{8}
\]
The identity behind the final equality is
\(c_0-c_{j-1}=s_js_{j-1}\).

## 2. Three elementary bounds on the recurrence

For \(N\ge3\), the positive sequence \(\varepsilon_j\) decreases and then increases. This follows from
\[
 \sin(j\theta)\sin((j-1)\theta)
     =\frac{\cos\theta-\cos((2j-1)\theta)}2.
 \tag{9}
\]
Its maximum occurs at \(j=2\) or \(j=d\), and
\[
 0<\varepsilon_j\le
 \frac{1}{8\cos^2(\theta/2)\cos\theta}\le\frac13,
 \qquad
 \varepsilon_j\ge\sin^2(\theta/2)\ge N^{-2}.
 \tag{10}
\]
The first endpoint bound uses \(\theta\le\pi/3\); the last is the sine chord inequality on \([0,\pi/2]\).

The total perturbation is bounded independently of the interval and the level. The exact telescoping formula is
\[
 \begin{split}
 \sum_{j=2}^{d}\varepsilon_j
 &=\frac{\sin^2(\theta/2)}{\sin\theta}
             \bigl(\cot\theta-\cot(d\theta)\bigr)\\
 &=\frac{\cos\theta}{1+\cos\theta}<\frac12.
 \end{split}
 \tag{11}
\]
In particular every interval product obeys
\[
                    \prod \rho_j<e^{1/2}<2.
 \tag{12}
\]

## 3. A positive energy for the signed continuant

Write \(S=e^{2it}\), \(c=\cos t\), and for \(k=0,\ldots,j-i\) define
\[
                  y_k=e^{-ikt}h_{i,i+k}(e^{2it}).
 \tag{13}
\]
The recurrence makes every \(y_k\) real:
\[
 y_0=1,\qquad y_1=2c,\qquad
 y_k=2cy_{k-1}-\rho_{i+k}y_{k-2}.
 \tag{14}
\]
For \(\rho>1\) use the positive quadratic form
\[
 Q_\rho(u,v)=u^2+\rho v^2-2cuv
            =(u-cv)^2+(\rho-c^2)v^2.
 \tag{15}
\]
The exact step identity is
\[
 Q_\rho(2cu-\rho v,u)=\rho Q_\rho(u,v).
 \tag{16}
\]
If \(\rho'\le\rho\), then \(Q_{\rho'}\le Q_\rho\). If \(\rho'\ge\rho\), completion of the square gives
\[
 Q_{\rho'}\le
       \frac{\rho'-c^2}{\rho-c^2}Q_\rho.
 \tag{17}
\]
The increase factors in (17) telescope because the sequence decreases and then increases. Let \(\rho_*\) be the minimum over the recurrence steps of the chosen interval, and \(\rho_{\mathrm{end}}\) its last coefficient. Starting from
\(Q_{\rho_{\mathrm{start}}}(2c,1)=\rho_{\mathrm{start}}\),
(12), (16), and (17) give
\[
 Q_{\rho_{\mathrm{end}}}(y_k,y_{k-1})
 \le
 2\rho_{\mathrm{start}}
       \frac{\rho_{\mathrm{end}}-c^2}{\rho_*-c^2}.
 \tag{18}
\]
If the interval ends before the minimum of the full sequence, its own minimum is its last coefficient and the ratio in (18) is one. Thus the displayed formula also covers monotone subintervals.

Minimizing (15) in its second variable shows
\[
 Q_\rho(u,v)\ge\frac{\rho-c^2}{\rho}u^2.
 \tag{19}
\]
Since \(\rho_{\mathrm{start}},\rho_{\mathrm{end}}\le4/3\) and
\(\rho_*-c^2\ge\rho_*-1\ge N^{-2}\), equations (18)–(19) imply
\[
                 |h_{i,j}(S)|<2N\qquad(|S|=1).
 \tag{20}
\]
Intervals of length zero or one satisfy the same bound directly. At \(N=2\) there are only those intervals. Cauchy's coefficient formula therefore gives
\[
                  |[S^p]h_{i,j}(S)|\le2N.
 \tag{21}
\]
This energy argument controls the original alternating recurrence. Taking absolute values in (7) before its negative second term has been combined would not give (20).

## 4. The exact unused-row factor is polynomial

Let \(w_{i,j}\) be the positive monomer prefactor in (5)–(6):
\[
 w_{i,j}
   =\left(\prod_{r=i+1}^j s_r^2\right)
       \prod_{r<i\ \text{or}\ r>j}\gamma_r
   =\frac4{\gamma_i}
       \prod_{r=i+1}^j\frac{s_r^2}{\gamma_r}.
 \tag{22}
\]
The last equality uses the exact shifted sine product
\(\prod_{r=0}^d\gamma_r=4\).
Define the full-index cap weights
\[
 U_j=\frac4{\gamma_0}
       \prod_{r=1}^j\frac{s_r^2}{\gamma_r},
 \qquad
 V_j=\frac{\gamma_jU_j}{4}
       =\prod_{r=1}^j
          \frac{\sin^2(r\theta)}{\sin^2((r-\tfrac12)\theta)}.
 \tag{23}
\]
The sequence \(U_j\) decreases and then increases, because its adjacent ratio is
\(\sin^2(j\theta)/\sin^2((j+\tfrac12)\theta)\).
Its endpoint values are
\[
 U_0=\csc^2(\theta/2)\le N^2,\qquad U_d=N^2.
 \tag{24}
\]
Hence \(U_j\le N^2\) everywhere. The sequence \(V_j\) increases and then decreases. Its endpoint values are \(V_0=1\) and
\(V_d=N^2\sin^2(\theta/2)\ge1\), so \(V_j\ge1\) everywhere. These monotonicity statements follow by comparing the two sine arguments and their reflections about \(\pi/2\); they include the possible central equality.

Consequently
\[
                         w_{i,j}=\frac{U_j}{V_i}\le N^2.
 \tag{25}
\]
Combining (5), (6), (21), and (25) proves the uniform finite coefficient estimate
\[
 \boxed{\quad
  \left|[x^p y^{j-i-p}]
            [V_N(2;C(x,y))]_{i,j}\right|
                   \le2N^3 .
 \quad}
 \tag{26}
\]
Homogeneity identifies the coefficient in (26) with \([S^p]\) after \(x=S,y=1\). Thus every monomial coefficient of the original four-face homogeneous \(H_{V_N(2)}\) has the same bound. The original input/output middle degrees are \(i,d-j\), so no further normalization occurs.

## 5. Endpoint calibration and a shrinking spectral interval

At \(\sigma=c_0\), the normalized interval recurrence (7) has \(\rho_j=1\). Therefore
\[
 h_{i,j}(S)=1+S+\cdots+S^{j-i}.
 \tag{27}
\]
For the full interval \(0,\ldots,d\) there are no unused rows. Since \(\prod_{r=1}^d s_r^2=N^2\),
\[
 [V_N(c_0;C(S,1))]_{0,d}
       =(-1)^dN^2(1+S+\cdots+S^d).
 \tag{28}
\]
This is an exact root-normal calibration of every south-degree coefficient, not an endpoint asymptotic.

There is also a uniform polynomial estimate on the entire interval
\[
                    c_0\le\sigma\le2,
 \qquad 2-c_0=O(N^{-2}).
 \tag{28a}
\]
Write \(\sigma=c_0+\lambda(2-c_0)\), \(0\le\lambda\le1\). The normalized recurrence (7) has \(\rho_j=1+\lambda\varepsilon_j\). If \(\lambda\ge N^{-2}\), the same energy argument gives
\(\rho_*-c^2\ge\lambda N^{-2}\ge N^{-4}\), hence
\(|h_{i,j}(S)|\le2N^2\) on \(|S|=1\).

If \(0\le\lambda<N^{-2}\), compare (14) with the free Chebyshev recurrence. For an interval of length \(k\), the exact forced solution is
\[
 y_k=U_k(c)
       -\lambda\sum_{r=2}^k
             \varepsilon_{i+r}U_{k-r}(c)y_{r-2},
 \tag{28b}
\]
where \(U_0=1,U_1=2c\). Since \(|U_\ell(c)|\le\ell+1\le N\), the maximum \(M\) of the finitely many \(|y_k|\) on the interval satisfies
\[
 M\le N+\frac{N\lambda}{2}M,\qquad M\le2N.
 \tag{28c}
\]
The unused-row monomer prefactor is nonnegative throughout (28a), because \(c_0\) is the largest node. Each unused factor \(\sigma-c_r\) is at most \(2-c_r\), so that prefactor is bounded by the \(N^2\) from (25), without division at \(\sigma=c_0\). Therefore
\[
 \boxed{\quad
 \sup_{c_0\le\sigma\le2}
 \left|[x^p y^{j-i-p}]
           [V_N(\sigma;C(x,y))]_{i,j}\right|
                         \le2N^4.
 \quad}
 \tag{28d}
\]
For \(N=2\) the absence of length-two intervals proves the same statement directly. This shrinking interval is not a fixed spectral neighborhood.

## 6. Whole shared contractions and scope

For a fixed marked source with \(r\) original boxes, there are at most \(N^3\) monomials in each local homogeneous polynomial of degree \(d\) in four faces. The full original shared coefficient is a sum of at most \(N^{3r}\) monomial selections. Equation (26) therefore yields
\[
 \begin{split}
 |S_N^{\mathrm{full}}(2,\ldots,2)|
       &\le2^rN^{6r},\\
 |S_N^{\mathrm{CROSS}}(2,\ldots,2)|
       &\le2^rN^{6r},\\
 |D_N(2,\ldots,2)|&\le2^{r+1}N^{6r}.
 \end{split}
 \tag{29}
\]
The CROSS projection, or any fixed LEFT/CROSS/RIGHT assignment, selects original input/output intervals, hence a subset of these monomial coefficients. This justifies the same estimate without introducing absolute values inside the local continuants.

The same argument using (28d) gives
\[
 \sup_{\boldsymbol\sigma\in[c_0,2]^r}|D_N(\boldsymbol\sigma)|
                         \le2^{r+1}N^{7r},
 \tag{30}
\]
and half that displayed bound for the full or CROSS source separately. All protected targets, shared ordinary targets, and the original mark are imposed before these estimates are used. They add no quantum dimension or Cartan correction. They do not estimate mixed tuples elsewhere in the fixed spectral cube, a neighborhood uniformly large enough for filling, or the supremum required for the undecorated bipyramid theorem.
