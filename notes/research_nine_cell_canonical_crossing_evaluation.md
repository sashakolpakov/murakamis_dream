# Exact evaluation of the nine-cell crossing array

Private written proof, 17 November 2026. We evaluate the actual
six-variable source of [S], with all boundary indices. It is the
specified planar crossing tensor times one explicit nowhere-zero
scalar and the recorded charge phase. For every injective real vertex
decoration, with real odd roots, that scalar has modulus exactly
\(N^{-2}\). Its phase is retained. Neither the printed nine-cell
formula nor a pentagon assertion is a premise.

## 1. Source conventions and result

Use [S] unchanged: \(N>2\) is odd, \(q\) is primitive, \(d=N-1\),
and halves are modulo \(N\). For a sorted cell \(T=abcd\), put
\[
 \alpha_T=\frac{s_{ad}s_{bc}}{s_{ac}s_{bd}},\quad
 \beta_T=\frac{s_{ab}s_{cd}}{s_{ac}s_{bd}},\quad
 Z_T=s_{ac}s_{bd},\qquad \alpha_T^N+\beta_T^N=1.       \tag{1}
\]
The six vertex decorations are distinct. All roots and normalization
square roots remain on the same lifted regular domain. In the
notation \(W_T,\overline W_T\) of [S,(1)],
\[
 \frac{\overline W_T(j+1)}{\overline W_T(j)}
  =\frac{\beta_T}{1-\alpha_Tq^j},\qquad
 \frac{W_T(j)}{\overline W_T(j+1)}
  =\frac{1-\alpha_T}{\beta_T}.                         \tag{2}
\]
For five increasing labels define the literal finite sum
\[
 \mathfrak f_{abcde}
 =f\left(\alpha_{abcd},\alpha_{abce}/q
                      \,\middle|\,\beta_{abcd}/\beta_{abce}\right).
                                                               \tag{3}
\]
Here \(f\) is exactly [B,(4)]. With \(\mathfrak n\) exactly [S,(15)],
define
\[
\begin{split}
 J={}&\mathfrak n\,
  \mathfrak f_{01235}\mathfrak f_{01345}\mathfrak f_{12345}N^3
  \frac{1-\alpha_{1245}}{\beta_{1245}}
  \frac{1-\alpha_{2345}}{\beta_{2345}}
  \frac{1-\alpha_{0145}}{\beta_{0145}}
  \frac{\beta_{1345}}{1-\alpha_{1345}^{N}},\\
 C_N(\mathbf s)={}&\frac{J}{N^2}
 \left(\frac{s_{34}}{s_{01}s_{02}s_{03}s_{35}s_{45}^{\,2}}\right)^d .
\end{split}                                                     \tag{4}
\]
Then the recovered canonical array in [S,(18)] is
\[
 \boxed{\mathcal R^0_{\mathbf i}
   =C_N(\mathbf s)q^{\,3(h_1-1)/2}
                  R(\mathbf i\mid1,0,0,0).}                     \tag{5}
\]
The \(R\) on the right is the specified planar finite weight.
The scalar \(C_N\) is holomorphic and nowhere zero on the stated
lifted regular domain. For distinct real vertex decorations, real
odd roots \(s_{ij}\), and positive square roots of the real
divided-difference brackets in [B],
\[
                         |C_N(\mathbf s)|=N^{-2}.                \tag{6}
\]
No ordering of the real decorations is required.

## 2. Exact cyclic beta convolution

The cyclic summand \(a_j\) of \(f(x,y\mid z)\), with
\(z^N=(1-x^N)/(1-y^N)\), obeys
\((1-xq^{j+1})a_{j+1}=z(1-yq^{j+1})a_j\). Hence
\[
 (1-z)f(x,y\mid z)=(x-qyz)f(x,y\mid qz),             \tag{7}
\]
\[
 f(x,qy\mid z)
 =\frac{f(x,y\mid z)-qy f(x,y\mid qz)}{1-qy}
 =\frac{x-qy}{(1-qy)(x-qyz)}f(x,y\mid z).             \tag{8}
\]
These are finite-sum identities and do not divide by \(f\).
For any \(K,L\in\mathbb Z/N\), they imply
\[
 \boxed{\sum_r q^{Kr}
 \frac{W_{abcd}(r)}{\overline W_{abce}(r+L)}
 =\mathfrak f_{abcde}
   \frac{\overline W_{acde}(K+L)}
        {\overline W_{bcde}(K)\overline W_{abde}(L)}.} \tag{9}
\]
Indeed, set \(x=\alpha_{abcd}\), \(y=\alpha_{abce}/q\), and
\(z=\beta_{abcd}/\beta_{abce}=\alpha_{bcde}\).
The left side is
\(\overline W_{abce}(L)^{-1}f(x,q^Ly\mid q^Kz)\).
Its \(K,L\) steps from (7),(8) equal those of the right side, using
\[
 \alpha_{acde}=\alpha_{abce}z/x,\quad
 \alpha_{abde}=\alpha_{abce}/x,\quad
 \beta_{acde}/\beta_{bcde}=1/x,\quad
 \beta_{acde}/\beta_{abde}=1/\beta_{abce}.             \tag{10}
\]
At \(K=L=0\) both are (3). Every step multiplier is a unit: its
denominators reduce to nonzero roots and \(1-\alpha_Tq^j\), with
\(1-\alpha_T^N=\beta_T^N\ne0\). Periodicity retains the cyclic seam.
If \(\mathfrak f_{abcde}\) vanished, these unit steps would make the
left side zero for all \(K\) at \(L=0\). Fourier inversion would
annihilate its nonzero summand vector. Thus every scalar (3) is nonzero.

## 3. The actual six sums and their prefactor

Retain \(k_i=m_i-p_i+h_i\), \(\sum k_i=2\), and put
\[
 H=(3h_1-1)/2,\quad a=[-k_1],\quad m=[-k_2],\quad
 C=[k_3-1]+1\in\{1,\ldots,N\},\quad B=m-C.             \tag{11}
\]
Off \(\sum k_i=2\), the actual source is already zero. The capital
\(C\) is an integer representative, not \(C_N\). Define
\[
 (qX;q)_r=
 \begin{cases}
 \prod_{j=1}^{r}(1-q^jX),&r\ge0,\\
 \displaystyle\prod_{j=0}^{-r-1}(1-q^{-j}X)^{-1},&r<0.
 \end{cases}                                                    \tag{12}
\]

In [S,(16)], first sum \(r\) by (9) for \(01235\), with
\(K=u+v+1,\ L=1-k_1+s+z\). The remaining \(0235\) ratio is exactly
\[
 \frac{\overline W_{0235}(K+L)}
      {\overline W_{0235}(K+L-k_2)}
 =\beta_{0235}^{-m}
       \prod_{j=0}^{m-1}(1-\alpha_{0235}q^{K+L+j}).     \tag{13}
\]
Expand by degree \(\ell\), whose coefficient is
\(\beta_{0235}^{-m}(-\alpha_{0235})^\ell
 q^{\ell(\ell-1)/2}{m\brack\ell}_q\).
Then sum \(s\) by (9) for \(01345\) with
\(K=v+t+1+\ell,\ L=z+1-k_1\), and sum \(u\) for \(12345\) with
\(K=t+1+\ell,\ L=v+1\).
The remaining \(1345\) ratio is
\(\beta_{1345}/(1-\alpha_{1345}q^{v+t+1+\ell})\).
Equation (2) leaves the three linear ratios in (4), and the polynomials
\[
\begin{split}
 &\beta_{2345}^{-\ell}\prod_{j=1}^{\ell}
                         (1-\alpha_{2345}q^{t+j}),\\
 &\beta_{0145}^{-a}\prod_{j=1}^{a}
                         (1-\alpha_{0145}q^{z+j}),\\
 &\beta_{0345}^{-b_\ell}\prod_{j=0}^{b_\ell-1}
 (1-\alpha_{0345}q^{v+t+z+2-k_1+\ell+j}),\qquad b_\ell=[B-\ell].
\end{split}                                                     \tag{14}
\]
Their unexpanded phase is
\[
 q^{(1+\ell)v+t+(1+\ell)z+1-k_1+H+\ell(2-k_1)}.       \tag{15}
\]

Call the degree of the last polynomial \(j\), and let
\(r=[-1-\ell-j]\). The exact \(v\)-sum is
\[
 \sum_v\frac{q^{(1+\ell+j)v}}
              {1-\alpha_{1345}q^{v+t+1+\ell}}
 =\frac{N\alpha_{1345}^{r}}{1-\alpha_{1345}^N}
           q^{-(1+\ell+j)(t+1+\ell)}.                 \tag{16}
\]
The \(t\)-sum selects its polynomial's top degree \(\ell\), contributing
\(N(-\alpha_{2345})^\ell q^{\ell(\ell+1)/2}\beta_{2345}^{-\ell}\).
The \(z\)-sum selects degree \(r\le a\), or is zero, and contributes
the third \(N\). The collected phase and signs are
\[
 q^{H-k_1}q^{-k_1\ell}
 (-1)^j q^{j(j-1)/2+(1-k_1)j}
 (-1)^r q^{r(r-1)/2+r}.                              \tag{17}
\]
The root identities
\[
 \alpha_{0235}\alpha_{2345}/\beta_{2345}
       =\alpha_{0345}/\beta_{0345},\qquad
 \alpha_{1345}\alpha_{0145}=\alpha_{0345}              \tag{18}
\]
give the remaining factor
\(\alpha_{0345}^{\ell+j+r}\beta_{0345}^{-\ell-b_\ell}\).
The only ordinary totals congruent to \(d\) are \(d,2N-1\).
Thus all three \(N\)'s and all endpoint contributions in (4) are retained.

Define the rational function
\[
 F(X)=\sum_{\ell=0}^{m}{m\brack\ell}_q q^{a\ell}
                 X^\ell(qX;q)_{a+m-C-\ell}.                      \tag{19}
\]
All its Gaussian binomial denominators have order below \(N\).
Split \(F=L+U\) at \(\ell\le B\) and \(\ell>B\), with empty parts
zero. The first is polynomial of degree at most \(a+B<2N-1\).
For the second, the actual polynomial from (14) is \(1-X^N\)
times the corresponding rational term. Using
\(\beta_{0345}^N=1-\alpha_{0345}^N\), the precise result of
(13)--(18) is
\[
\begin{split}
 b(\mathbf k)={}&
 Jq^{H-k_1}\beta_{0235}^{-m}\beta_{0145}^{-a}
          \alpha_{0345}^d\beta_{0345}^{-B}\\
 &{}\cdot\left([X^d]F+
   \frac{\alpha_{0345}^N}{1-\alpha_{0345}^N}[X^{2N-1}]F\right).
\end{split}                                                     \tag{20}
\]
This equality comes from the original six sums, not a substituted
boundary representative.

## 4. Rational coefficient and exact triangular support

The finite binomial convolution gives the exact factorization
\[
 F(X)=(qX;q)_{a-C}
       \sum_{r=0}^{m}{m\brack r}_q q^{ar}
                                  (q^{1-C};q)_r X^r.             \tag{21}
\]
Indeed factor out \((qX;q)_{a-C}\) in (19), expand the remaining
\((q^{a-C+1}X;q)_{m-\ell}\), and use
\[
 {m\brack\ell}_q{m-\ell\brack r-\ell}_q
 ={m\brack r}_q{r\brack\ell}_q.
\]
The coefficient of \(X^r\), apart from
\({m\brack r}_q q^{ar}\), is exactly
\[
 \sum_{j=0}^{r}{r\brack j}_q(-1)^j
              q^{j(j-1)/2+(1-C)j}=(q^{1-C};q)_r.     \tag{22}
\]
All used factorial orders are below \(N\). The polynomial in (21)
has degree at most \(\min(m,C-1)\), because its displayed product
vanishes for \(r\ge C\). Hence \(F\) has degree at infinity at most
\(a-1\).

If \(C\le a\), \(F\) is polynomial, so both coefficients in (20)
vanish. If \(C>a\), its poles are simple and lie among
\(1,q,\ldots,q^{C-a-1}\), and its polynomial part has degree
at most \(a-1<d\). Partial fractions therefore give
\[
 [X^{2N-1}]F=[X^d]F=-[X^{-1}]_\infty F.               \tag{23}
\]
Consequently, with \(c(\mathbf k)=[X^d]F\), (20) becomes
\[
 b(\mathbf k)=Jq^{H-k_1}\beta_{0235}^{-m}\beta_{0145}^{-a}
     \alpha_{0345}^d\beta_{0345}^{C-m-N}c(\mathbf k)    \tag{24}
\]
when \(C>a\), and is zero otherwise.

Put \(n=a+m-C\), \(h=C-a-1\), and \(M=m-h=n+1\). If \(M<0\), every summand
is \(O(X^{-2})\) at infinity, so \(c=0\).
If \(M\ge0\), only \(\ell\ge M\) contribute a \(1/X\) term and
\[
 -[X^{-1}]_\infty X^\ell(qX;q)_{n-\ell}
 =(-1)^{\ell-M}q^{(\ell-M)(\ell-M+1)/2}{\ell\brack M}_q.
                                                               \tag{25}
\]
Indeed, expansion of the reciprocal product at infinity leaves the
complete homogeneous coefficient \({\ell\brack M}_q\).
Use \({m\brack\ell}_q{\ell\brack M}_q
 ={m\brack M}_q{m-M\brack\ell-M}_q\) and the finite binomial identity:
\[
 \boxed{c(\mathbf k)=q^{aM}
       \frac{p_m p_{C-1}}{p_Mp_hp_a},\qquad
       p_j=\prod_{r=1}^{j}(1-q^r).}                  \tag{26}
\]
All these indices lie in \(0,\ldots,d\). The exact nonzero support
is \(C>a,\ M\ge0\); there are no undeclared cyclic carries.

## 5. Comparison with the specified planar weight

Let \(\Phi(\mathbf k)=\sum_{\mathbf i}
 R(\mathbf i\mid1,0,0,0)q^{\sum i_jk_j}\).
The literal composition of \(d\) in [S, Section 6] gives zero
unless \(\sum k_i=2\). On that support the same direct substitution gives
\[
 \Phi=N^2q^{1-k_1}\sum_{z=0}^{d}q^{-z(k_1+k_2+z)}
 S_{d-z}(q^{-k_1-z})S_z(q^{1+z-k_3}),\quad
 S_j(X)=\frac{\prod_{r=1}^{j}(X-q^r)}{p_j}.            \tag{27}
\]
The two factors restrict \(a\le z\le C-1\). When \(C>a\), put
\(z=a+j\), \(h=C-a-1\), and \(M=m-h\).
Substitute the products \(S\) and the exact reflection identity
\(p_{d-r}p_r=N(-1)^r q^{r(r+1)/2}\). The remaining sum is
\[
 \frac{\Phi}{N^2q^{1-k_1}}
 =q^{aM}\frac{p_{C-1}}{p_a p_h}
   \sum_{j=0}^{h}{h\brack j}_q(-1)^j
                   q^{j(j-1)/2+(M+1)j}
 =q^{aM}\frac{p_{C-1}}{p_a p_h}(q^{M+1};q)_h .
                                                               \tag{28}
\]
This is the elementary finite binomial formula already proved in
[S,(31)]. If \(M<0\), the product contains \(1-q^0\);
otherwise it is \(p_m/p_M\), since \(M+h=m\le d\).
Equations (26),(28), including every zero, prove
\[
                   \Phi(\mathbf k)=N^2q^{1-k_1}c(\mathbf k).
                                                               \tag{29}
\]

On this support set \(a_i=[-k_i]\). We have
\(a_3=N-C\) and \(a_4=d-M\), the latter because
\(k_4\equiv M+1\) and \(0\le M\le d\).
Together with \(M=m-C+a+1\), this gives \(\sum_i a_i=2d\). Since
\(f_i(k_i)=s_{0i}^{d-a_i}s_{i5}^{a_i}\), direct cancellation yields
\[
 \frac{\beta_{0235}^{-m}\beta_{0145}^{-a}
       \alpha_{0345}^d\beta_{0345}^{C-m-N}}
      {\prod_i f_i(k_i)}
 =\left(\frac{s_{05}s_{34}}
                {s_{01}s_{02}s_{03}s_{35}s_{45}^{\,2}}\right)^d .
                                                               \tag{30}
\]
For example,
\(\beta_{0145}=s_{01}s_{45}/(s_{04}s_{15})\),
\(\beta_{0235}\beta_{0345}=s_{02}s_{45}/(s_{04}s_{25})\), and
\(\beta_{0345}=s_{03}s_{45}/(s_{04}s_{35})\); the fourth exponent
is fixed by \(\sum a_i=2d\).
Equations (24),(29),(30) prove the all-boundary identity
\[
 b(\mathbf k)=C_N(\mathbf s)q^{3(h_1-1)/2}s_{05}^d
                          \Phi(\mathbf k)\prod_i f_i(k_i).
                                                               \tag{31}
\]
Both sides also vanish off their common support. The exact inverse
adapter of [S] proves (5). Every factor in (4) is a unit by [B],
(1), and the argument following (10).

## 6. Exact modulus for all distinct real decorations

Now every vertex decoration is real and distinct, and every odd root
is chosen real. Their order can be arbitrary. The function \(t^N\)
is strictly increasing, so every divided-difference bracket
\((U^N-V^N)/(N(U-V))\) in [B] is positive. Choose its square roots
positive, consistently in each normalization.
Conjugating a finite sum and replacing its cyclic index by its
negative gives
\[
 f_q(x,y\mid z)^*
       =f_q(\bar y/q,\bar x/q\mid\bar z^{-1}).          \tag{32}
\]
The summand is periodic, so this also holds for negative real \(z\).
Applied to [B], it gives \(\bar\rho_T=\rho_T^*\) and
\[
 |\rho_T|^2=|\bar\rho_T|^2
       =\frac{Z_T^d\beta_T^N}{N(1-\alpha_T)}.          \tag{33}
\]
This is positive: \(d\) is even and
\((1-\alpha_T^N)/(1-\alpha_T)>0\) for real \(\alpha_T\ne1\).

Only within the following formula let
\(A=abcd,B=abce,C=acde,D=bcde,E=abde\).
The conjugate of (3) is its paired sum in [B,(11)].
That proved finite product and (10) give
\[
 |\mathfrak f_{abcde}|^2
 =N\frac{(1-\alpha_A)(1-\alpha_B)(1-\alpha_C)\beta_D^N}
          {\beta_A^N(1-\alpha_D)(1-\alpha_E)}.         \tag{34}
\]
This is a signed rational identity valid on every real component;
no continuation across a collision is used.

Multiply (33) for the nine cells and (34) for the three beta sums.
Six linear factors cancel immediately. The other three are canceled
by the squared linear ratios explicitly retained in (4).
The powers of \(N\) are \(N^{-9}N^3N^6=1\).
Using
\[
 \beta_{0125}\beta_{0235}\beta_{0345}=\beta_{0145},\qquad
 \beta_{1235}\beta_{1345}=\beta_{1245},
 \tag{35}
\]
all remaining factors reduce to
\[
 |J|^2=\mathfrak e^{\,2}\!
     \left(\prod_{\text{nine }T}Z_T\right)^d
     \left(\frac{\beta_{1245}\beta_{2345}\beta_{0145}}
                      {\beta_{1345}}\right)^{2d},\quad
 \mathfrak e=(s_{12}s_{23}s_{34}s_{14})^{-d}.           \tag{36}
\]
This retains the original edge weights. Finally
\[
 \prod_{\text{nine }T}Z_T
 =(s_{02}s_{03}s_{04}s_{13}s_{14}s_{15}s_{24}s_{25}s_{35})^2,
\]
so substitution in (36) proves
\[
 |J|=\left|\frac{s_{01}s_{02}s_{03}s_{35}s_{45}^{\,2}}{s_{34}}\right|^d .
                                                               \tag{37}
\]
Equation (6) now follows from (4), at every allowed odd level.
This proves a modulus, not constancy of the holomorphic phase.

## 7. Charge and source scope

For the full charge table of [S], its exact sector transport gives
\[
 \mathcal R^\chi_{\mathbf i}
 =C_N(\mathbf s)q^{3(h_1-1)/2+d_\chi+\zeta+w}
                      R(\mathbf i\mid x,y,\zeta,w).   \tag{38}
\]
Here \(d_\chi\) is exactly [S,(17b)], not a discarded charge gauge.
All boundary indices and both sides of each paired face remain.
The identities are holomorphic on the same lifted regular domain;
fixed-order decoration derivatives retain \(C_N\) and its derivatives.

Thus the previously unresolved array comparison is evaluated, with
an explicit scalar whose modulus is known for arbitrary distinct real
decorations. No globally canonical sector, new cut, or identity
wire pairing is substituted. Global contractions must retain the
original paired-face wire, charge, vertex, and edge factors.
This proves no even-level tetrahedral extension, off-root quantum
derivative, free-vertex source adapter, or selected geometric-period
lower bound. The residual phase is not asserted to be constant or
a root of unity.

## Complete direct sources

- [S] [Literal nine-cell source reduction](research_nine_tetrahedron_boundary_source_reduction.md),
  SHA256 5aeecb0c174f33baa1264bc34c7419d4ccae007e84f4410b3dcb47c6c81c554c.
  The entire proof and its complete primary definition were read.
- [B] [Literal charged tetrahedron inverse and bubble](research_literal_charged_tetrahedron_bubble.md),
  SHA256 1dfe35f26137572235b1c3af66dcf410e0af758836baddaa8dd6d958c0f61d9b.
  The entire proof was read; only its proved finite normalization
  identities are used.

No mathematical program, numerical experiment, or knot example was used.
