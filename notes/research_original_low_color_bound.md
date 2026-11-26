# A uniform bound for the first half of the original crossing coefficients

Research note, 3 November 2026.

The coefficients of an arbitrary integer power of the original crossing
are uniformly bounded on the first quarter of their Newton indices.
The bound is independent of the crossing power and of the quantum level.
On the rest of the distinct-node half, an explicit bound grows at most
linearly with the level. This is a statement about the original
coefficients, including negative powers. It does not follow from a
bound on a replacement positive model.

The reason is elementary. Each of these coefficients depends only on
distinct physical values of the crossing power, whose moduli are one.
The absolute weights in their divided-difference formula have a
telescoping sine identity. Later Newton coefficients also see the
derivatives at double roots and are not covered by this argument.

## 1. The original coefficient functional

Put \(N\ge2\), \(D=N-1\), \(\theta=\pi/N\),
\(q=e^{i\theta}\), and
\[
 s_m=2\sin(m\theta),\qquad S_m=\prod_{h=1}^m s_h,
 \qquad S_0=1,\qquad
 c_r=2\cos((2r+1)\theta).
 \tag{1}
\]
Use the original full algebra and Newton basis from the
[finite crossing formula](research_terminal_powers_qbinomial.md):
\[
 \mathcal A_N=\mathbb C[z]/(P_N(z)),\qquad
 e_j(z)=S_j^{-2}\prod_{r=0}^{j-1}(c_r-z).
 \tag{2}
\]
Here \(P_N(t+t^{-1})=t^N+t^{-N}+2\). Repeated roots of
\(P_N\) are retained. Let \(R\) be the original positive
crossing, \(M\) its multiplication matrix, and
\[
 \alpha_{p,j}=(M^p e_0)_j,
 \qquad p\in\mathbb Z,\qquad
 \kappa=\exp\frac{\pi i(N-1)^2}{2N}.
 \tag{3}
\]
The coordinate vector \(e_0\) in (3) represents the unit of
the algebra. At every distinct physical node under consideration,
\[
                R(c_r)=\kappa(-1)^r q^{r(r+1)},
                       \qquad |R(c_r)^p|=1.
 \tag{4}
\]
For example, (4) follows from the diagonal entry of the
original triangular multiplication matrix. Evaluation is an
algebra homomorphism, so it also gives every negative power.

If \(c_0,\ldots,c_j\) are distinct, ordinary Newton
interpolation gives the exact original coefficient
\[
 \alpha_{p,j}=(-1)^j S_j^2
       \sum_{r=0}^j\frac{R(c_r)^p}
                         {\prod_{0\le h\le j,\ h\ne r}(c_r-c_h)}.
 \tag{5}
\]
Every higher Newton basis element vanishes at these nodes.
Thus (5) recovers this coefficient from the full algebra,
without discarding a derivative needed by it.
The interpolation formula itself is classical; see
[DLMF, Sections 3.3(iii)--(iv)](https://dlmf.nist.gov/3.3#iii).
The estimates below use the particular original sine normalization
and the unit physical values in (4).

## 2. The absolute interpolation weights

Suppose first that \(2j+1<N\). All the nodes in (5) are
distinct and all the following sine factors are nonzero.
The difference of cosines gives
\[
 \left|\prod_{h\ne r}(c_r-c_h)\right|
      =\frac{S_{j+r+1}S_{j-r}}{s_{2r+1}},\qquad
 w_{j,r}:=\frac{S_j^2s_{2r+1}}{S_{j+r+1}S_{j-r}}>0.
 \tag{6}
\]
In particular \(|\alpha_{p,j}|\le\sum_{r=0}^j w_{j,r}\).
Define
\[
       A_r=\frac{S_j^2}{S_{j+r}S_{j-r}}\quad(0\le r\le j),
       \qquad A_{j+1}=0.
 \tag{7}
\]
One has \(A_0=1\) and, including \(r=j\),
\[
 A_{r+1}=A_r\frac{s_{j-r}}{s_{j+r+1}},\qquad s_0=0.
 \tag{8}
\]
The sine subtraction formula shows
\[
 s_{j+r+1}-s_{j-r}
   =4\cos((j+\tfrac12)\theta)\sin((r+\tfrac12)\theta)>0.
 \tag{9}
\]
Consequently the \(A_r\)'s decrease. More precisely,
\[
 \boxed{\quad
 w_{j,r}=(A_r-A_{r+1})
             \frac{\cos((r+\tfrac12)\theta)}
                  {\cos((j+\tfrac12)\theta)}.
 \quad}                                                       \tag{10}
\]
This identity also holds at \(r=j\). It follows by dividing
\(s_{2r+1}=4\sin((r+\tfrac12)\theta)
                   \cos((r+\tfrac12)\theta)\)
by the difference in (9). All differences \(A_r-A_{r+1}\)
are positive and sum to one.

**Theorem 1.** For every signed integer \(p\), every \(N\ge2\),
and every index with \(2j+1<N\),
\[
 \boxed{\qquad
 |\alpha_{p,j}|
       \le\sum_{r=0}^j w_{j,r}
       \le\frac{\cos(\pi/(2N))}
                    {\cos((2j+1)\pi/(2N))}.
 \qquad}                                                      \tag{11}
\]
In particular,
\[
 |\alpha_{p,j}|\le\sqrt2
       \quad\left(0\le j\le\left\lfloor\frac{N-2}{4}\right\rfloor\right).
 \tag{12}
\]
The integer \(p\) may depend on \(N\).

*Proof.* Apply (4) to (5), then sum (10). Each cosine in the
numerator of (10) is at most \(\cos(\theta/2)\).
The differences sum to one, proving (11).
In the range of (12), \((j+1/2)\theta\le\pi/4\),
so its denominator is at least \(1/\sqrt2\). \(\square\)

More generally, the same bound multiplied by
\(\max_{0\le r\le j}|F(c_r)|\) holds for the coefficient
of any \(F\in\mathcal A_N\). No condition on its higher
normal derivatives is needed for these indices.

## 3. The last distinct node at odd levels

If \(N=2m+1\), the node \(c_m=-2\) is still distinct
from \(c_0,\ldots,c_{m-1}\). Formula (5) therefore applies
at \(j=m\), but (6) has a removable zero in its last term.
Cancellation before evaluation gives
\[
 w_{m,m}=1,\qquad w_{m,r}=2\cos((m-r)\theta)\quad(0\le r<m).
 \tag{13}
\]
Indeed \(S_m^2=S_{N-1}=N\), and the factors paired about
\(m+1/2=N/2\) have equal sines. These facts give (13)
directly from the nonzero differences in (5).
Summing the finite cosine series yields
\[
 \sum_{r=0}^m w_{m,r}
        =1+2\sum_{h=1}^m\cos(h\theta)
        =\frac1{\sin(\theta/2)}.
 \tag{14}
\]
Thus all coefficients before the first repeated node satisfy
\[
 \boxed{\quad
       |\alpha_{p,j}|\le\csc\frac{\pi}{2N}=O(N),
       \qquad 0\le j\le\left\lfloor\frac{N-1}{2}\right\rfloor.
 \quad}                                                       \tag{15}
\]
For even \(N\), (15) follows directly from (11); its last
denominator is \(\sin(\pi/(2N))\). For odd \(N\), use
(11) before the last node and (14) at that node.

## 4. Consequence for the original reflected even source

Fix \(k\ge2\), and retain the original positive scalar
\[
 \mathcal E_{k,N}=\sum_{j=0}^{N-1}|\alpha_{2k,j}|^2
                =\phi_N(R^{-2k}T(R^{2k})).
 \tag{16}
\]
Use the constants and middle-color theorem from
[the backward-source estimate](research_even_run_backward_source_growth.md):
\[
 \begin{split}
 K_k&=k4^{k(k-1)/2+k-1},\qquad C_k=1+512k^2K_k^2,\\
 j_N&=N-\lceil N/4\rceil,\qquad
 \mathcal H_N=\{j_N-k+1,\ldots,N-1\},\\
 E^{\rm high}_{k,N}&=\sum_{j\in\mathcal H_N}|\alpha_{2k,j}|^2.
 \end{split}                                                  \tag{17}
\]
Here \(\mathcal H_N\) is the upper quarter of the original
Newton indices, enlarged by a fixed number of indices.

**Corollary 2.** For \(N\ge2048k^2\),
\[
 E^{\rm high}_{k,N}\le\mathcal E_{k,N}
             \le C_k\left(E^{\rm high}_{k,N}+\frac N2\right).
 \tag{18}
\]
The two quantities have the same logarithmic liminf and limsup
after division by \(N\). Negative even powers give the same
conclusion by conjugation.

*Proof.* The cited middle-color theorem bounds the full norm
by \(C_k\) times the sum on \(\mathcal H_N\) and
\(\{0,\ldots,N-2-\lfloor3N/4\rfloor\}\).
Every index in the latter set satisfies (12). There are at
most \(N/4\) of them, so their squared norm is at most
\(N/2\). This proves (18).
The cited actual endpoint-mode theorem gives a fixed positive
exponential lower bound on \(E^{\rm high}_{k,N}\): choose
its nonzero backward interval inside \((0,1/4)\).
Thus the additive \(N/2\) in (18) does not change either
logarithmic rate. \(\square\)

In particular the all-color backward envelope \(E_k\) in
that note now gives the simpler bound
\[
 \limsup_{N\to\infty}\frac1N\log\mathcal E_{k,N}
                  \le2\max_{0\le x\le1/4} E_k(x),
 \quad
 E_k(x)=\int_0^x\log\rho(H(2\pi t))\,dt-2J(x).
 \tag{19}
\]
The fixed enlargement in (17) does not change this maximum,
because \(E_k\) is continuous. There is no need to estimate
the forward product on the lower quarter for this bound.
Sharp equality still requires identifying the maximum in (19)
and proving that an actual nonzero mode attains it. It is not
inferred from a numerical ordering of the eigenvalues.

The conclusion is specific to an original crossing-power column.
An arbitrary input to a crossing or a turn need not have the unit
physical values in (4). Nor does this coefficient bound estimate
a subsequent signed pairing from below.

## 5. Reproducing the finite checks

The [checker](../experiments/check_original_low_color_bound.py)
compares literal powers of the original crossing matrix with (5),
then checks the sine weights, their telescoping identity, and both
bounds. It includes negative powers, powers depending on the level,
and the odd simple endpoint.

```sh
python3 experiments/check_original_low_color_bound.py --precision 150 --output repro/results/research-original-low-color-bound-root.json
```

The [saved record](../repro/results/research-original-low-color-bound-root.json)
checks 1,619 original coefficients at levels 2 through 20. The
maximum relative identity error is less than \(9.6\cdot10^{-147}\).
The all-power bounds follow from the exact proof, rather than these
finite samples.
