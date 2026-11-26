# Uniform pressure and a nonzero amplitude for the original triple-row trace

Private written proof, 17 November 2026.

The positive original scalar
\(\Gamma_{jk\ell}=\phi_N(F_jF_kF_\ell)\) has a uniform
variational rate on its entire nonzero physical support.
On compact subsets of strict macroscopic support, its exact
normalization is \(N^{-3}\) times a positive analytic amplitude
and its exponential action. The optimization is a strictly
concave sum of nine ideal-tetrahedron actions.

This controls the actual normal coefficients in the full
\(F/G\) product basis. An inserted \(G\) row is a different
derivative observable with a retained alternating tail; no
estimate of that tail or of a subsequent signed closing is
inferred by differentiating a continuous degree label.

## 1. Exact positive source and its symmetric sum

Use
\[
 N\ge2,\quad D=N-1,\quad J_N=\lfloor D/2\rfloor,\quad
 \eta=(-1)^D,\quad s_r=2\sin(\pi r/N),\quad
 S_r=\prod_{a=1}^r s_a,\quad S_0=1,
\]
\[
 c_j=2\cos((2j+1)\pi/N),\qquad
 e_r(Z)=S_r^{-2}\prod_{a<r}(c_a-Z),
\]
\[
 P_N(Z)=2T_N(Z/2)+2,\quad
 \phi_N(f)=\eta N^2[Z^D]\operatorname{rem}_{P_N}f,\quad
 F_j(Z)=\sum_{a=0}^j f_{j,a}e_a(Z),\quad
 f_{j,a}=\frac{S_{j+a}}{S_{j-a}S_a^2}.
 \tag{1}
\]
All \(j,k,\ell\) below are physical indices in
\(\{0,\ldots,J_N\}\).
The full normal row at a double node is
\(G_j(Z)=\partial_wK_N(c_j,Z)\), where
\(K_N(w,Z)=\sum_{r=0}^D e_r(w)e_r(Z)\).
At the odd simple node \(c_{J_N}=-2\) there is no normal row.
The full-product source proves
\[
 \Gamma_{jk\ell}:=\phi_N(F_jF_kF_\ell)>0
       \quad\Longleftrightarrow\quad j+k+\ell\ge D,
 \tag{2}
\]
and it is zero otherwise, with full canonical reduction and
every repeated-root normal retained.

Its positive sum can be made symmetric term by term.
The original Newton multiplication and Frobenius pairing give
\[
 \phi_N(e_a e_b e_c)
   =\frac{S_{a+b}S_{a+c}S_{b+c}}
          {N S_aS_bS_cS_{a+b+c-D}}
       \quad(a+b+c\ge D,\quad a,b,c\le J_N),
 \tag{3}
\]
and zero below that threshold.
Indeed it is the coefficient \(\mu_{ab,D-c}\) of the
original product \(e_ae_b\). All pair sums are at most \(D\).
Substitute its factorial formula and
\(S_{D-r}=N/S_r\) to obtain (3).
Thus, writing \(j_1=j,j_2=k,j_3=\ell\),
\[
 \boxed{\quad
 \Gamma_{\mathbf j}
 =\frac1N\!
 \sum_{\substack{0\le r_i\le j_i\\r_1+r_2+r_3\ge D}}
 \frac{\displaystyle
       \prod_i S_{j_i+r_i}
       \prod_{i<h}S_{r_i+r_h}}
      {\displaystyle
       \prod_i S_{j_i-r_i}
       \prod_i S_{r_i}^{\,3}
       S_{r_1+r_2+r_3-D}} .
 \quad}
 \tag{4}
\]
Every factorial index lies in \(0,\ldots,D\).
No signed term has been replaced by its modulus.

## 2. The variational action on the whole physical support

Set
\[
 \mathcal J(x)=\int_0^x\log(2\sin\pi u)\,du,\qquad0\le x\le1,
\]
\[
 f(x,t)=\mathcal J(x+t)-\mathcal J(x-t)-2\mathcal J(t),
\]
\[
 \mathfrak t(t_1,t_2,t_3)=
     \sum_{i<h}\mathcal J(t_i+t_h)
       -\sum_i\mathcal J(t_i)
       -\mathcal J(t_1+t_2+t_3-1).
 \tag{5}
\]
The continuous endpoint values are used.
Define
\[
 \mathcal X=\{\mathbf x\in[0,1/2]^3:\ \sum_i x_i\ge1\},
\quad
 \mathcal P(\mathbf x)=
       \{\mathbf t:\ 0\le t_i\le x_i,\ \sum_i t_i\ge1\},
\]
\[
 \Phi(\mathbf x,\mathbf t)
       =\sum_i f(x_i,t_i)+\mathfrak t(\mathbf t),\qquad
 \mathcal G(\mathbf x)
       =\max_{\mathbf t\in\mathcal P(\mathbf x)}
                                      \Phi(\mathbf x,\mathbf t).
 \tag{6}
\]
All arguments of \(\mathcal J\) in (5) lie in \([0,1]\)
on this compact feasible set.

**Theorem 1.** Uniformly over every nonzero physical triple,
at both level parities,
\[
 \boxed{\quad
 \log\Gamma_{\mathbf j}
       =N\mathcal G(j_1/D,j_2/D,j_3/D)+O(\log N).
 \quad}
 \tag{7}
\]
The constant is independent of the physical indices.
The function \(\mathcal G\) is continuous and concave on
\(\mathcal X\). Consequently every admissible sequence
\(\mathbf j_N/D\to\mathbf x\in\mathcal X\) has limiting
rate \(\mathcal G(\mathbf x)\).
The exact zero region in (2) is excluded from (7).

**Proof of the uniform estimate.** The uniform factorial bound is
\[
              \log S_r=N\mathcal J(r/N)+O(\log N)
                         \quad(0\le r<N).
 \tag{8}
\]
Moreover \(\mathcal J\) has modulus of continuity
\(O(\varepsilon(1+|\log\varepsilon|))\).
For a summand of (4) put \(x_i=j_i/D\), \(t_i=r_i/D\).
Replacing every factorial argument divided by \(N\) by its
corresponding argument in (5) changes it by \(O(N^{-1})\).
This includes \(r_1+r_2+r_3-D\).
There is a fixed number of factors, so the logarithm of
the summand is
\[
                      N\Phi(\mathbf x,\mathbf t)+O(\log N)
 \tag{9}
\]
uniformly through all endpoints. There are at most \(N^3\)
terms, giving the upper bound in (7).

For the lower bound choose a maximizing \(\mathbf t\)
and take \(r_i=\lceil Dt_i\rceil\).
Since \(j_i\) are integers, \(r_i\le j_i\).
Their sum is at least \(D\), so this is an actual supported
term at both parities. Its distance from the maximizing
state is \(O(N^{-1})\). The same modulus of continuity
and (9) give the lower bound.

Continuity of \(\mathcal G\) follows directly from continuity
of \(\Phi\) and continuity of these feasible polytopes.
For the latter point, if \(\mathbf x_n\to\mathbf x\) and
\(\mathbf t\in\mathcal P(\mathbf x)\), first replace \(t_i\)
by \(\min(t_i,x_{n,i})\). If their sum drops below one,
restore the missing \(o(1)\) using the remaining box
capacity; \(\sum_i x_{n,i}\ge1\) ensures enough capacity.
This constructs feasible \(\mathbf t_n\to\mathbf t\).
The reverse limiting assertion is compactness.
Concavity is proved next. \(\square\)

## 3. Nine positive atoms and the unique strict optimizer

For \(a+b+c=1\), let
\[
                 V(a,b,c)=-\pi\{\mathcal J(a)+\mathcal J(b)
                                             +\mathcal J(c)\}.
 \tag{10}
\]
This is the usual ideal-tetrahedron action on the closed
angle simplex. Its interior Hessian is negative definite;
the elementary cotangent proof and its boundary derivatives
are given in the variational source.
Using \(\mathcal J(1-x)=-\mathcal J(x)\), one has exactly
\[
 \pi f(x,t)
      =V(x-t,t,1-x)+V(x,t,1-x-t).
 \tag{11}
\]
All angles are nonnegative on \(0\le t\le x\le1/2\).
Also
\(\mathfrak t(a,b,c)=m(a,b,1-c)\), where \(m\) is the
original Newton product action. Its three-atom expression is
\[
 \begin{split}
 \pi\mathfrak t(a,b,c)={}&V(b,a,1-a-b)\\
 &+V(1-c-a,1-c-b,a+b+2c-1)\\
 &+V(2-a-b-2c,a+b+c-1,c).
 \end{split}
 \tag{12}
\]
These are exactly the three atoms of the original gate,
with its output set to \(1-c\). They are nonnegative
angles on the gate domain, which includes (6).
Thus \(\Phi\) is a jointly concave nine-atom action.
Maximization over the convex shared-label domain proves
the concavity asserted in Theorem 1.

Write
\[
 \mathcal X^\circ
       =\{\mathbf x:\ 0<x_i<1/2,\ \sum_i x_i>1\}.
 \tag{13}
\]
For every \(\mathbf x\) in (13), the maximum has
\[
             0<t_i^*(\mathbf x)<x_i,\qquad
                         \sum_i t_i^*(\mathbf x)>1.
 \tag{14}
\]
To prove this, choose a strict feasible state, which exists
because \(\sum_i x_i>1\), and join any boundary state to
it. A coordinate \(t_i=0\) is impossible on this polytope:
the other two are bounded by numbers whose sum is less
than one. If \(t_i=x_i\), the first atom of (11) is
\(V(0,x_i,1-x_i)\), a nonvertex-flat atom. Its inward
directional derivative is \(+\infty\).
If \(\sum_i t_i=1\), the last atom of (12) is
\(V(1-c,0,c)\), also nonvertex-flat.
Every other atom has either finite or positive infinite
inward derivative, never negative infinite derivative.
This argument includes simultaneous intersections of
these faces. No boundary point can maximize.

Strictness and nondegeneracy can also be checked directly.
For \(0<t<x<1/2\),
\[
 f_{xx}=\pi\{\cot\pi(x+t)-\cot\pi(x-t)\}<0,
\]
\[
 \det\operatorname{Hess}_{(x,t)}f
       =\frac{4\pi^2\sin^2\pi x}
                   {\sin\pi(x-t)\sin\pi(x+t)}>0 .
 \tag{15}
\]
Thus every row action has a negative definite joint Hessian.
The gate Hessian is nonpositive, and is itself negative
definite in the strict gate domain. Hence \(\Phi\) has
negative definite Hessian in all six variables at (14).
There is a unique maximizing state, analytic in \(\mathbf x\),
and
\[
 \mathcal H(\mathbf x)
       =-\Phi_{\mathbf t\mathbf t}(\mathbf x,\mathbf t^*)>0.
 \tag{16}
\]
The profile is real analytic and strictly concave on (13),
by the negative Schur complement of the full Hessian.
In particular its actual derivative in the continuous
degree parameter is
\[
 \partial_{x_i}\mathcal G(\mathbf x)
       =\log\frac{\sin\pi(x_i+t_i^*)}
                         {\sin\pi(x_i-t_i^*)}.
 \tag{17}
\]
This is not identified with an original spectral first normal.

## 4. Uniform nonzero amplitude on strict macroscopic support

For the amplitude use the exact parameters
\(\mathbf x_N=(j_1/N,j_2/N,j_3/N)\).
This differs from the convention in the uniform rate (7):
the \(D=N-1\) shift must now be retained in the amplitude.
For a strict state set \(d=t_1+t_2+t_3-1>0\) and
\[
 \mathcal R(\mathbf x,\mathbf t)=
 \frac{\displaystyle
       \prod_i\sin\pi(x_i+t_i)
       \prod_{i<h}\sin\pi(t_i+t_h)}
      {\displaystyle
       \prod_i\sin\pi(x_i-t_i)
       \prod_i\sin^3\pi t_i\ \sin\pi d}.
 \tag{18}
\]
All displayed factors are strictly positive.

**Theorem 2.** For any compact \(K\subset\mathcal X^\circ\),
uniformly over physical triples with \(\mathbf x_N\in K\),
\[
 \boxed{\quad
 \Gamma_{\mathbf j}
       =N^{-3}\mathcal A(\mathbf x_N)
                  e^{N\mathcal G(\mathbf x_N)}
                     \bigl(1+O_K(N^{-1})\bigr),
 \quad}
 \tag{19}
\]
where the positive real analytic amplitude is
\[
 \mathcal A(\mathbf x)=
       \frac{\pi^{3/2}}{8\sin(\pi d^*)}\,
       \frac{\sqrt{\mathcal R(\mathbf x,\mathbf t^*)}}
                            {\sqrt{\det\mathcal H(\mathbf x)}},
 \qquad d^*=\sum_i t_i^*-1.
 \tag{20}
\]
In particular it is bounded above and below by positive
constants on \(K\).

**Proof.** Strictness, uniqueness, and compactness provide
uniform buffered neighborhoods of all the selected saddles.
On them the bulk sine-factorial expansion is
\[
 S_{N\alpha+c}
  =\sqrt{2N\sin\pi\alpha}\ e^{N\mathcal J(\alpha)}
        (2\sin\pi\alpha)^c\bigl(1+O(N^{-1})\bigr),
 \tag{21}
\]
with uniform analytic derivatives on smaller bulk domains.
This formula is used for integral factorial arguments;
the canonical interpolation in the cited Laplace source
also supplies the corresponding holomorphic summand.

In (4) there are six numerator factorials and thirteen
denominator factorials, counting multiplicities. There is
also the displayed \(N^{-1}\).
Only the final denominator has a nonzero offset:
\[
                 r_1+r_2+r_3-D=Nd+1.
 \tag{22}
\]
Consequently each summand near the saddle equals
\[
 N^{-9/2}\mathfrak b(\mathbf x,\mathbf t)
               e^{N\Phi(\mathbf x,\mathbf t)}
                  \bigl(1+O_K(N^{-1})\bigr),\qquad
 \mathfrak b=
       \frac{2^{-9/2}\sqrt{\mathcal R(\mathbf x,\mathbf t)}}
                                      {\sin\pi d}.
 \tag{23}
\]
The factor \(1/(2\sin\pi d)\) from (22) is essential.

The whole complement of a sufficiently small saddle
neighborhood has a uniform strict action gap. To apply
this to the exact finite sum, its possible strip
\(\sum_i r_i/N\in[1-N^{-1},1)\) can be moved into the
limiting polytope by increasing coordinates by a total
at most \(N^{-1}\), without leaving their upper box.
The strict parameter margin supplies that capacity.
The uniform factorial estimate and modulus of continuity
then change the rate by only \(O(\log N)\).
Thus all these terms, and every other nonsaddle term,
are exponentially smaller than (19).

The remaining lattice has three independent integer
coordinates, with no congruence or parity restriction.
The finite-window lattice Laplace lemma applies to (23),
or equivalently follows by its midpoint cotangent contour
proof with all endpoint and nonconstant-mode terms
exponentially smaller. Its Gaussian factor is
\[
            N^{3/2}\frac{(2\pi)^{3/2}}
                                   {\sqrt{\det\mathcal H}}.
 \tag{24}
\]
Combining (23) and (24) yields \(N^{-3}\) and exactly
(20). The relative error is \(O_K(N^{-1})\), uniformly
over a finite cover of the compact parameter set.
Both parities use the same primitive lattice and the same
offset (22). \(\square\)

## 5. Actual normal coefficients and the remaining signed observable

The result applies directly to the normal sector of the
original full product. For a double node \(c_\ell\), the
exact coefficient of \(G_\ell\) in \(F_jF_k\) is
\[
           B_{jk;\ell}
                 =\eta(4-c_\ell^2)\Gamma_{jk\ell}.
 \tag{25}
\]
Therefore (7) controls its entire nonzero macroscopic
rate, with only polynomial endpoint factors. On every
strict compact of Theorem 2, its full asymptotic is
\[
 B_{jk;\ell}
   =\eta(4-c_\ell^2)N^{-3}\mathcal A(\mathbf x_N)
          e^{N\mathcal G(\mathbf x_N)}
                     (1+O_K(N^{-1})).
 \tag{26}
\]
Here the factor \(4-c_\ell^2\) is left exact.
At the odd simple node there is no normal coefficient;
its value coefficient is the same exact triple trace.
Theorem 1 covers that row, while the bulk amplitude theorem
does not assert a uniform fold or support-boundary expansion.

The inserted first normal
\(\phi_N(G_jF_kF_\ell)\), with \(c_j\) double, is a separate observable.
For precision, if
\[
              T(F_kF_\ell)=\sum_{m=0}^D h_m e_m,\qquad
              h_m\ge0,
 \tag{27}
\]
with the explicit factorial coefficients of the full-product
source, then the original identity is
\[
             \phi_N(G_jF_kF_\ell)
                         =\sum_{m=0}^D h_m e_m'(c_j).
 \tag{28}
\]
For \(m\le j\), logarithmic differentiation gives
\[
 e_m'(c_j)=-f_{j,m}\sum_{a=0}^{m-1}(c_a-c_j)^{-1},
\]
with the empty sum zero.
For \(j<m\le D-j\) they instead equal
\[
 e_m'(c_j)=(-1)^{m-j}
      \frac{S_{j+m}S_{m-j-1}}{s_{2j+1}S_m^2}.
 \tag{29}
\]
For \(m>D-j\) they vanish.
The alternating tail (29) is retained; it is not present
in the positive sum (4). No bound for it follows from
Theorem 2 by differentiating (17).
The same caution applies to mixed original first normals.

Thus the new estimate gives the actual size and nonzero
amplitude of the signed normal coefficient (25), not a
positivity replacement for the complete \(F/G\) packet.
Its subsequent \(V_n\) action retains the original phase
and the value-channel shear
\((A_\ell,B_\ell)\mapsto
\lambda_{n,\ell}(A_\ell-n\alpha_\ell B_\ell,B_\ell)\).
Here
\(\lambda_{n,\ell}=(-1)^{n\ell}e^{-i\pi n\ell(\ell+1)/N}\)
and
\(\alpha_\ell=i(D-2\ell)/(4\sin((2\ell+1)\pi/N))\)
are the original coefficients from the full-product source.
The prescribed crossed closing still includes both channels
and their coherent quadratic phases.
No lower bound for that sum is asserted.

The nine-atom expression provides a concrete positive
variational problem with original integer labels. Identifying
its external derivatives or internal stationary equations
with a supplied parent triangulation requires its actual
charge and gluing equations; no geometric volume equality
is inferred from the atom decomposition alone.

## Complete direct sources

All three complete texts were read and their used implications
checked at the following pins:

* [Full physical-row product support](research_physical_row_full_product_normal_support.md),
  SHA256 708d22248526c75b0d8b26cc9a07c63d8471b07d200b9e9947059ca8145b2efd:
  exact positive triple trace, all-index normal coefficients,
  and the retained original derivative tail.
* [Primitive action and variation](../papers/newton-calculus/variation.tex),
  SHA256 0e92ea26937bff27b0b813d6289ae917113c2d567e843ec07f883b23d1124296:
  uniform factorial rate, the original three-atom gate,
  strict concavity, and boundary derivative facts.
* [Uniform finite-window lattice Laplace proof](../papers/conway-asymptotics/README.md),
  SHA256 9bcd5f82e8de2be34e6a6428d9a6fb07049f06884f8febe111a4628719253cba:
  bulk factorial normalization with integer offsets and
  the uniform finite-lattice Gaussian amplitude.

Only written mathematics, source-text reads, and metadata
hashes were used. No programs, numerical evaluations, tests,
builds, or compilations were run. Frozen notes and public
manuscripts are unchanged.
