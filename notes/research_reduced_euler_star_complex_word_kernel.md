# The lower-donor Euler star as a complex word kernel

Private written proof, 18 November 2026.

After the actual factorial normalization, a full reduced Euler
star is a finite word polynomial with an explicit inversion
weight. Its inverse has one additional bounded pair interaction.
On a compact chart where the ordinary linear characteristic is
nonzero, an elementary connected-graph argument proves that
both unprojected kernels are nonzero for a small normalized
lower-donor interval. On the \(a=O(\sqrt N)\) scale it gives a
relative quadratic-exponential approximation with error
\(O(N^{-1/2})\), not an absolute multinomial majorant.

The exact upper projectors remain. The result concerns the
lower donor, not its opposite endpoint or a closed contraction.
The sole complete proof direct is G, the actual reduced
correspondence. All finite-word and analytic estimates are
proved below.

## 1. The literal star and its capacity projectors

Use \(r\ge2\) heads, donor occupation \(a\), recipient
occupations \(b=(b_2,\ldots,b_r)\), and
\[
 d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad
 h=2\pi i/N,\quad x=-M/q,\quad
 f_k=\prod_{\ell=1}^k(1-Q^\ell),\quad f_0=1.
 \tag{1}
\]
All indices initially lie in \(\{0,\ldots,d\}\), and \(M\ne0\).
Let \(\mathcal G=G_F^{\otimes r}\), \(G_Fw_k=f_kw_k\).
G's exact positive \(S_r\) coefficient, after this conjugation,
is
\[
 \frac{f_a}{f_{a-n}\prod_{j=2}^rf_{n_j}}\,
 \prod_{j=2}^r
       x^{-(j-1)n_j}Q^{n_j\sum_{2\le i<j}b_i},
 \qquad n=\sum_{j=2}^r n_j,
 \tag{2}
\]
with \(0\le n\le a\) and \(b_j+n_j\le d\).
For \(S_r^{-1}\), multiply (2) by
\((-1)^nQ^{n(n-1)/2}\). No chirp is used in this note.
The factorial basis has not been assumed uniformly conditioned.

Identify the normalized basis with monomials in
\(z_0,z_2,\ldots,z_r\), where \(0\) labels the donor.
Put
\[
 c_0=z_0,\qquad
 c_j=x^{-(j-1)}Q^{\sum_{2\le i<j}b_i}z_j\quad(2\le j\le r).
 \tag{3}
\]
Let \(\Pi_b\) delete monomials for which any recipient
degree exceeds \(d\). There are polynomials \(K_a^\pm\)
such that the exact finite kernels are
\[
 \mathcal G^{-1}S_r^{\pm1}\mathcal G
       \left(z_0^a\prod_{j=2}^rz_j^{b_j}\right)
       =\Pi_b\left[\left(\prod_{j=2}^rz_j^{b_j}\right)K_a^\pm\right].
 \tag{4}
\]
The notation \(\Pi_b\) indicates its use on this displayed
input-dependent polynomial, not a change of the upper wall.
A sufficient condition for no truncation is
\[
                         a+\max_{j\ge2}b_j\le d.
 \tag{5}
\]
All intermediate masks are then satisfied as well: the donor
decreases monotonically and each recipient only increases.
Outside (5) the exact projector in (4) remains.

## 2. An exact word formula and a scalar difference recursion

Order the alphabet \(\mathcal J=\{0,2,\ldots,r\}\) naturally.
For a word \(\ell=(\ell_1,\ldots,\ell_a)\), let
\[
 \operatorname{inv}(\ell)=
       \#\{i<j:\ell_i>\ell_j\},\qquad
 n(\ell)=\#\{i:\ell_i\ne0\}.
 \tag{6}
\]
Then the exact unprojected kernels are
\[
 K_a^+=\sum_{\ell\in\mathcal J^a}
                  \prod_{i=1}^ac_{\ell_i}\,
                         Q^{\operatorname{inv}(\ell)},
 \tag{7}
\]
\[
 K_a^-=\sum_{\ell\in\mathcal J^a}
        (-1)^{n(\ell)}\prod_{i=1}^ac_{\ell_i}\,
        Q^{\operatorname{inv}(\ell)+n(\ell)(n(\ell)-1)/2}.
 \tag{8}
\]
Both vacuum polynomials \(K_0^\pm\) are one.

Here is a direct coefficient proof. For fixed letter counts
\((n_0,n_2,\ldots,n_r)\) summing to \(a\), the inversion sum is
\[
 \sum_{\text{words with these counts}}Q^{\operatorname{inv}}
                         =\frac{f_a}{\prod_j f_{n_j}}.
 \tag{9}
\]
Indeed choosing the first letter \(j\) contributes
\(Q^{\sum_{k<j}n_k}\). If the right side of (9) is inserted
in that recursion, the required numerator identity is
\[
 \sum_j Q^{\sum_{k<j}n_k}(1-Q^{n_j})=1-Q^a.
 \tag{10}
\]
It telescopes. Starting from the empty word proves (9),
including zero counts. Equations (2), (7), and (8) follow
with \(n_0=a-n\).

For a uniform notation define
\[
 c_j^+=c_j,\qquad c_0^-=c_0,\quad c_j^-=-c_j\ (j\ne0),
\]
\[
 B_+(j,k)=\boldsymbol1_{\{j>k\}},\qquad
 B_-(j,k)=\boldsymbol1_{\{j>k\}}
                      +\boldsymbol1_{\{j\ne0,\ k\ne0\}} .
 \tag{11}
\]
Both pair energies lie between zero and two.
Let \(T_j^\pm\) replace every \(z_k\) by
\(Q^{B_\pm(j,k)}z_k\), keeping the fixed input \(b\) unchanged.
Choosing the first letter of a word proves the exact recursion
\[
                 K_{a+1}^\pm
                      =\sum_{j\in\mathcal J}c_j^\pm T_j^\pm K_a^\pm,
             \qquad K_0^\pm=1.
 \tag{12}
\]
For example the positive \(j\ne0\) term shifts \(z_0\) and
the recipient variables with index less than \(j\) by \(Q\).
Thus (12) is a scalar finite difference evolution in coherent
variables. It is not an estimate obtained by replacing its
complex coefficients by positive ones.

## 3. A zero-free estimate for complex normalized weights

We prove a finite statement that applies to both signs.
Let complex numbers \(p_j\) satisfy
\[
             \sum_jp_j=1,\qquad \sum_j|p_j|\le R,\qquad R\ge1,
 \tag{13}
\]
and let \(B(j,k)\) be either pair energy in (11).
With an auxiliary complex parameter \(\zeta\), define
\[
 Z_a(\zeta;p)=
  \sum_{\ell\in\mathcal J^a}\prod_i p_{\ell_i}
     \exp\!\left(\zeta\sum_{i<j}B(\ell_i,\ell_j)\right).
 \tag{14}
\]
The \(p_j\)'s are held fixed when varying \(\zeta\).
Put
\[
                         \gamma=\frac1{128e^4R^2}.
 \tag{15}
\]
For \(a\ge2\), \(Z_a\) is nonzero on \(|\zeta|a\le\gamma\).
It has the holomorphic logarithm normalized by
\(\log Z_a(0;p)=0\), and
\[
                       |\log Z_a(\zeta;p)|\le a\log2.
 \tag{16}
\]
The same conclusions are immediate for \(a=0,1\), when \(Z_a=1\).

We give the full zero-free proof. On an ordered subset
\(\Lambda\subseteq\{1,\ldots,a\}\), write every pair factor as
\[
 e^{\zeta B(\ell_i,\ell_j)}
             =1+u_{ij}(\ell_i,\ell_j),\qquad
 |u_{ij}|\le v:=e^{2|\zeta|}-1.
 \tag{17}
\]
Expanding the product gives a sum over graphs on \(\Lambda\).
Group each graph into its connected components of size at least
two; its isolated vertices contribute \(\sum p_j=1\).
For a subset \(S\) of size \(s\ge2\), let \(w(S)\) be the
sum over its connected graphs, followed by the finite label
sum with weight \(\prod_{i\in S}p_{\ell_i}\).
The result is exactly
\[
 Z_\Lambda=\sum_{\substack{\mathcal A\text{ a family of}\\
                    \text{pairwise disjoint }S\subseteq\Lambda,\ |S|\ge2}}
                                    \prod_{S\in\mathcal A}w(S).
 \tag{18}
\]
This finite identity holds for complex weights.

Every connected graph contains a spanning tree. With one vertex
chosen as root, assigning a parent to every other vertex gives
at most \(s^{s-1}\) rooted trees. This upper bound needs no
tree-counting formula. Sum the possible extra graph edges after
each tree. Together with (13), this gives
\[
 |w(S)|\le R^s s^{s-1}v^{s-1}(1+v)^{s(s-1)/2}
                 \le R^s s^{s-1}v^{s-1}e^{vs^2/2}.
 \tag{19}
\]
Overcounting graphs with several spanning trees is harmless.

Under \(|\zeta|a\le\gamma\), one has \(v\le4|\zeta|\) and
\(e^{vs^2/2}\le e^s\). Also
\[
 \frac{s^{s-1}}{(s-1)!}\le e^s.
 \tag{20}
\]
For (20), integrate \(\log t\) from \(1\) to \(s-1\) to
bound \(\log((s-1)!)\) below, then use
\((1+1/(s-1))^{s-1}\le e\). The case \(s=2\) is included.
Consequently, for every vertex \(i\),
\[
 \begin{split}
 \sum_{S\ni i}|w(S)|2^{|S|-1}
 &\le \sum_{s=2}^a
    \binom{a-1}{s-1}R^ss^{s-1}(8|\zeta|)^{s-1}e^s\\
 &\le Re^2\sum_{s=2}^\infty
                  (8a|\zeta|Re^2)^{s-1}<\frac12 .
 \end{split}
 \tag{21}
\]
The explicit constant (15) suffices: the last geometric ratio
is at most \(1/(16Re^2)\), and its whole sum is less than \(1/2\).
The same bound holds on every subset \(\Lambda\).

We now induct on \(|\Lambda|\), proving both nonvanishing and
\[
 \left|\frac{Z_\Lambda}{Z_{\Lambda\setminus\{i\}}}-1\right|
                              \le\frac12\quad(i\in\Lambda).
 \tag{22}
\]
The empty and singleton cases are one. In (18), either \(i\)
is isolated or belongs to its unique set \(S\). Hence
\[
 \frac{Z_\Lambda}{Z_{\Lambda\setminus\{i\}}}
  =1+\sum_{\substack{S\subseteq\Lambda\\i\in S,\ |S|\ge2}}
           w(S)\frac{Z_{\Lambda\setminus S}}
                        {Z_{\Lambda\setminus\{i\}}}.
 \tag{23}
\]
Delete the other \(|S|-1\) vertices one at a time. The induction
hypothesis bounds every inverse ratio by two, so the last
quotient has modulus at most \(2^{|S|-1}\).
Equation (21) proves (22), and its disk excludes zero.
This induction proves the assertion for all subsets, not
only for an initial segment of the ordered sites.

Each ratio in (22) has the holomorphic logarithm of \(1+z\),
\(|z|\le1/2\), of modulus at most \(\log2\).
Multiply the ratios along any fixed sequence adding the
vertices. Their logarithms sum to the logarithm normalized
at \(\zeta=0\), proving (16). The construction is holomorphic
also in the normalized weights on every neighborhood with
the uniform bound (13).

## 4. The relative quadratic kernel

Let
\[
                     \mu=\sum_{j,k}p_jp_k B(j,k).
 \tag{24}
\]
Differentiating the finite sum (14) at zero gives
\((\log Z_a)'(0)=\binom a2\mu\).
Apply Cauchy's coefficient estimate to (16) on the disk
of radius \(\gamma/a\). For \(|\zeta|a\le\gamma/2\),
\[
 \boxed{\quad
 \log Z_a(\zeta;p)
       =\zeta\binom a2\mu+O_R(a^3|\zeta|^2).
 \quad}
 \tag{25}
\]
More explicitly the remainder is at most
\(2(\log2)a^3|\zeta|^2/\gamma^2\).
Indeed sum the geometric tail of the Taylor series from
degree two. This proves a bound for the canonical logarithm,
not a logarithm chosen separately at individual sample points.

Apply this to the actual coefficients (3), with
\[
 H_\pm=\sum_j c_j^\pm,\qquad p_j^\pm=c_j^\pm/H_\pm.
 \tag{26}
\]
Choose a compact coherent-variable and meridian neighborhood
where \(H_\pm\) is a unit and \(\sum|p_j^\pm|\le R\) on a
slightly larger neighborhood. Keep every \(N\)-dependent
\(x=-M/q\) and \(Q\)-prefix factor in (3). Then exactly
\[
                  K_a^\pm=H_\pm^a Z_a(h;p^\pm).
 \tag{27}
\]
In particular the unprojected kernel is nonzero when
\(a|h|\le\gamma\). Its normalized factor has the two-sided
bound \(2^{-a}\le|Z_a|\le2^a\).
For the lower-donor range \(0\le a\le C\sqrt N\), (25) gives
\[
 K_a^\pm
   =H_\pm^a
       \exp\!\left(h\binom a2\mu_\pm\right)
                  \bigl(1+O_{C,R}(N^{-1/2})\bigr),
 \tag{28}
\]
\[
 \mu_+=\sum_{j>k}p_j^+p_k^+,\qquad
 \mu_-=\sum_{j>k}p_j^-p_k^-
                       +\left(\sum_{j\ne0}p_j^-\right)^2.
 \tag{29}
\]
Every fixed coherent-variable and fixed-\(q\) meridian
derivative of the normalized error in (28) has the same
bound on the smaller compact set, by the holomorphy and
uniform bounds just proved. The vacuum \(a=0\) remains one.

In applying Cauchy in (25), \(\zeta\) was an auxiliary
interaction variable while the actual \(p^\pm\) were
held fixed. No \(N\)-dependent coefficient or half-shift
has been differentiated away. Their full values remain
in \(H_\pm,\mu_\pm\) in (28).

## 5. The physical characteristic at the resolved row

At G's resolved row endpoint the donor has \(A_{\rm d}=1\),
\(p_{\rm d}=0\), and physical \(f_{\rm d}\ne0\). In the
all-factorial polynomial model the unprojected physical
lowering symbols on the outputs are \(z_0,z_2,\ldots,z_r\).
G's \(S_r\) equations at \(p_{\rm d}=0\) give all partial
\(T_j=1\), unchanged recipient clocks \(B_j\), and
\[
 f'_{\rm r,j}=f_{\rm r,j},\qquad
 f'_{\rm d}=f_{\rm d}-x_0^{-1}F_{\rm r},
 \quad
 F_{\rm r}=\sum_{j=2}^r
       x_0^{-(j-2)}\left(\prod_{2\le i<j}B_i\right) f_{\rm r,j},
 \qquad x_0=-1.
 \tag{30}
\]
One can obtain the donor equality without division by its
vanishing flag: substitute \(A_{\rm d}=1-p_{\rm d}f_{\rm d}\)
and \(C=1-p_{\rm d}F_{\rm r}/x_0\) in
\(A'_{\rm d}=A_{\rm d}/C\), then take \(p_{\rm d}=0\).
Thus the principal linear characteristic is exactly
\[
                        H_+=f'_{\rm d}+x_0^{-1}F_{\rm r}
                                      =f_{\rm d}.
 \tag{31}
\]
For the inverse, the sign changes and
\[
                        H_-=f'_{\rm d}-x_0^{-1}F_{\rm r}
                                      =f_{\rm d}.
 \tag{32}
\]
Consequently the physical input donor unit supplies the
nonzero characteristic. This requires no assertion that
each intermediate donor in a chosen factorization has
nonzero \(f\). A compact neighborhood of that point has
bounded \(R\). It supplies the parameter chart in (26);
it does not supply a physical integer state at that point.

## 6. Capacity, normal, and source scope

Equations (7)--(12) are exact finite polynomial identities.
The actual kernel is still (4). Formula (28) is therefore
an actual kernel estimate in the untruncated capacity region
(5); elsewhere it is an estimate before the original upper
projectors. Those projectors can change its value and cannot
be estimated by the nonzero unprojected factor.

The result is explicitly a lower-donor theorem. It does
not apply when \(a\) is near \(d\). Even a two-head full-circle
product retains a factor of the form \(1-u^N\), which can
vanish or grow exponentially. No such factor is replaced
by a unit here.

The recipient clocks in the original integer source are
\(B_j=Q^{b_j}\). Allowing their coefficients in (3) to vary
holomorphically is useful for uniform estimates, but does
not construct an exact interpolation in complex occupations.
Neither does the auxiliary variable \(\zeta\) transport an
original contour or a root carry. Fixed-\(q\) meridian
derivatives in (28) are of the exact retained finite family;
no closed ordinary-color quantum-normal identity is inferred.

All factorial changes of basis, neighboring coupons,
Cartan lines, pivots, scalar normalizations and final
first-jet source functional must remain in a closed word.
The original flow propagation may force additional boundary
sectors outside (5). This theorem does not cancel them,
prove an endpoint-to-interior source propagation, or infer
noncancellation of a cyclic trace. It supplies the stated
relative local kernel estimate only.

## Coverage and complete proof source

Abstract polymer expansions and inductive zero-free arguments
are established techniques: see the primary papers by
[Kotecký--Preiss](https://doi.org/10.1007/BF01211762) and
[Scott--Sokal](https://arxiv.org/abs/cond-mat/0309352).
Their primary abstract pages were checked for coverage.
No theorem or proof from them is a premise above.
The specific content here is the actual finite Euler-star
word, its inverse pair energy, and its source-calibrated
lower-donor estimate.

* G: notes/research_actual_reduced_braid_critical_scheme.md,
  SHA256 ddddcd9bf75f35afdf3e5de0c03323acee2c66e624db36142c2344ef729a977a.

The complete source was freshly read nontruncated in this
active sequence and retained unchanged. Every used implication
was checked. Only written mathematics and text/hash operations
were used. Frozen and public files were not edited.
