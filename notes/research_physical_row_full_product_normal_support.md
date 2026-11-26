# Full physical-row products and strictly signed normal support

Private written proof, 17 November 2026.

The missing normal sector in an ordinary product of physical rows
has a particularly simple support and sign. Its coefficient at the
double node \(c_\ell\) is \((-1)^{N-1}\) times a strictly positive
quantity exactly when \(j+k+\ell\ge N-1\). That quantity is a
symmetric triple trace with an explicit positive sine-factorial
sum. This holds for every physical pair \(j,k\), including products
above the value-row degree range.

The positive Newton multiplication table and the general confluent
coordinate formula are prior results. We use them to obtain this
strict support statement and explicit coefficients; we do not
present coordinate inversion as a new theorem. The value coefficients
retain a separate alternating derivative tail. No scalar lower bound
after crossing phases is inferred.

## 1. Original basis and the finite reciprocal calculation

Set
\[
 N\ge2,\quad D=N-1,\quad J=\lfloor D/2\rfloor,\quad
 \theta=\pi/N,\quad q=e^{i\theta},\quad \eta=(-1)^D,
 \quad\kappa=q^{D^2/2},
\]
\[
 s_r=2\sin(r\theta),\quad S_r=\prod_{a=1}^r s_a,\quad S_0=1,
 \quad c_j=2\cos((2j+1)\theta),
\]
\[
 P_N(Z)=2T_N(Z/2)+2,\quad
 e_r(Z)=S_r^{-2}\prod_{a<r}(c_a-Z),\qquad
 \phi(f)=\eta N^2[Z^D]\operatorname{rem}_{P_N}f .
 \tag{1}
\]
Use the original turn \(Te_r=e_{D-r}\) in
\(\mathcal A_N=\mathbb C[Z]/(P_N)\). The physical rows and
normal rows are
\[
 F_j(Z)=K_N(c_j,Z),\quad 0\le j\le J,\qquad
 G_\ell(Z)=\partial_wK_N(c_\ell,Z),\quad \ell\in\mathcal D_N,
\]
\[
 K_N(w,Z)=\sum_{r=0}^D e_r(w)e_r(Z),\qquad
 \mathcal D_N=\{0,\ldots,\lfloor N/2\rfloor-1\}.
 \tag{2}
\]
At odd \(N\) the additional simple node has index
\(*=J\) and value \(c_*=-2\). The full basis is
\(\{F_j\}_{j=0}^J\cup\{G_\ell\}_{\ell\in\mathcal D_N}\).
There is no \(G_*\).

Write
\[
 f_{j,a}=e_a(c_j)
       =\frac{S_{j+a}}{S_{j-a}S_a^2}>0
       \quad(0\le a\le j),\qquad f_{j,a}=0\quad(a>j).
 \tag{3}
\]
The exact formula follows from
\(c_r-c_j=s_{j+r+1}s_{j-r}\).
All factorial indices in (3) are below \(N\).
The archived positive Newton table is
\[
 e_a e_b=\sum_{r=\max(a,b)}^{a+b}\mu_{ab,r}e_r,\qquad
 \mu_{ab,r}=
 \frac{S_{a+b}S_r}
 {S_aS_bS_{r-a}S_{r-b}S_{a+b-r}}>0
                      \quad(a+b\le D).
 \tag{4}
\]
If \(a+b\ge N\), the product is zero in the full algebra.
Both assertions retain all repeated-root normals.

Fix any \(0\le j,k\le J\), and put \(s=j+k\le D\).
For \(0\le r\le s\), define the explicit positive sum
\[
 u_r=
 \sum_{\substack{0\le a\le j,\ 0\le b\le k\\
                 \max(a,b)\le r\le a+b}}
     f_{j,a}f_{k,b}\,
     \frac{S_{a+b}S_r}
      {S_aS_bS_{r-a}S_{r-b}S_{a+b-r}},
 \qquad u_r=0\quad(r>s).
 \tag{5}
\]
Every \(u_r\) in \(0\le r\le s\) is strictly positive:
choose \(a+b=r\) with \(a\le j,b\le k\).
Thus, exactly as ordinary polynomials,
\[
 F_jF_k=\sum_{r=0}^{s}u_re_r,\qquad
 T(F_jF_k)=\sum_{m=0}^D h_me_m,\qquad h_m=u_{D-m}.
 \tag{6}
\]
In particular
\[
 h_m>0\ \Longleftrightarrow\ D-j-k\le m\le D.
 \tag{7}
\]
This is a finite factorial calculation followed by coefficient
reversal under the original turn. No triangular basis solve or
generic-root specialization is required.

## 2. The normal coefficients and their exact threshold

Expand uniquely in the full basis:
\[
 F_jF_k=\sum_{\ell\in\mathcal D_N}
          (A_{jk;\ell}F_\ell+B_{jk;\ell}G_\ell)
          +\mathbf1_{N\ {\rm odd}}A_{jk;*}F_* .
 \tag{8}
\]
Put \(\Delta_\ell=4-c_\ell^2>0\) at a double node.
The prior confluent Gram formula gives, for any canonical \(f\),
\[
 B_\ell(f)=\eta\Delta_\ell(Tf)(c_\ell),\qquad
 A_\ell(f)=\eta\{\Delta_\ell(Tf)'(c_\ell)-c_\ell(Tf)(c_\ell)\},
\]
\[
 A_*(f)=(Tf)(-2).
 \tag{9}
\]
These are full original values and spectral first normals.

**Theorem 1.** Define
\[
 \Gamma_{jk\ell}=\sum_{m=0}^{\ell}h_m f_{\ell,m}.
 \tag{10}
\]
It is symmetric in its three physical indices and satisfies
\[
 \Gamma_{jk\ell}=\phi(F_jF_kF_\ell),\qquad
 \Gamma_{jk\ell}>0\ \Longleftrightarrow\ j+k+\ell\ge D;
 \tag{11}
\]
it is zero otherwise. For every double node,
\[
 \boxed{\quad B_{jk;\ell}=\eta\Delta_\ell\Gamma_{jk\ell}.\quad}
 \tag{12}
\]
At the odd simple node,
\[
              A_{jk;*}=\Gamma_{jk*}>0
                       \ \Longleftrightarrow\ j+k\ge J .
 \tag{13}
\]
Equations (3), (5), and (10) are an explicit finite positive
sine-factorial sum for \(\Gamma\). On its first nonzero boundary,
\[
 j+k+\ell=D
 \quad\Longrightarrow\quad
 \Gamma_{jk\ell}=\frac{N^2}{H_jH_kH_\ell},\qquad
 H_a=\frac{S_a^4}{S_{2a}} .
 \tag{14}
\]

**Proof.** Evaluation of (6) at \(c_\ell\) gives (10).
The exact reproducing identity
\((Tf)(c_\ell)=\phi(F_\ell f)\) proves the triple-trace
identity and symmetry. Equations (3) and (7) show that the
sum is nonempty precisely when \(D-j-k\le\ell\); all its
nonzero terms are positive. Apply (9) to obtain (12) and
(13).

For (14), the ordinary product has degree exactly \(D\);
there is no reduction. Its leading coefficient is
\((-1)^{j+k+\ell}/(H_jH_kH_\ell)\), because
\((-1)^aH_aF_a\) is monic. Formula (1) and
\(\eta(-1)^D=1\) give (14). \(\square\)

Consequently the missing normal coefficients are not arbitrary
signed data. They all have sign \(\eta\) on a precisely known
terminal interval of double-node indices. At even levels this
interval is nonempty exactly when \(j+k\ge J+1\). At odd
levels it is nonempty exactly when \(j+k\ge J+1\) as well.
This agrees with the exact degree obstruction to an \(F\)-only
expansion above \(J\).

The simple coefficient also proves that the low-degree
alternating rule cannot be extended unchanged to all value
coefficients. At odd \(N\ge5\), choose physical indices with
\(j+k=J+1\). Equation (13) gives \(A_{jk;*}>0\), whereas
the extrapolated sign \((-1)^{j+k-J}\) would be negative.
No claim about the remaining \(A\)-signs is needed.

## 3. Every value coefficient, with its derivative tail retained

For a double node \(\ell\), the derivative of each Newton
polynomial is explicitly
\[
 e_m'(c_\ell)=
 \begin{cases}
 -f_{\ell,m}\displaystyle\sum_{a=0}^{m-1}
                        \frac1{c_a-c_\ell},&0\le m\le\ell,\\[2mm]
 (-1)^{m-\ell}
 \displaystyle\frac{S_{\ell+m}S_{m-\ell-1}}
                  {s_{2\ell+1}S_m^2},
                           &\ell<m\le D-\ell,\\[2mm]
 0,&m>D-\ell .
 \end{cases}
 \tag{15}
\]
The empty sum at \(m=0\) is zero. There are no zero
denominators in (15). Its middle line has the displayed
strictly alternating signs; the last line is a double-root
zero, not a value-only simplification.

To prove the middle line, differentiate the unique factor
\(c_\ell-Z\) in \(e_m\). The remaining factors split as
\[
 \prod_{\substack{0\le a<m\\a\ne\ell}}
       s_{\ell+a+1}
       =\frac{S_{\ell+m}}{S_\ell s_{2\ell+1}},\qquad
 \prod_{\substack{0\le a<m\\a\ne\ell}}
       s_{\ell-a}
       =(-1)^{m-\ell-1}S_\ell S_{m-\ell-1}.
\]
For \(m>D-\ell\), both occurrences of \(c_\ell\) are
present, so the derivative vanishes. The first line is
ordinary logarithmic differentiation away from zeros.

Combining (9), (10), and (15) gives every remaining coefficient:
\[
 \boxed{\quad
 A_{jk;\ell}
 =\eta\left\{\Delta_\ell\sum_{m=0}^Dh_m e_m'(c_\ell)
                   -c_\ell\Gamma_{jk\ell}\right\}.
 \quad}
 \tag{16}
\]
Equivalently, with \(L=D-j-k\), it is the finite formula
\[
 \begin{split}
 A_{jk;\ell}={}&-\eta\sum_{m=L}^{\ell}
 h_m f_{\ell,m}
       \left(c_\ell+\Delta_\ell
             \sum_{a=0}^{m-1}\frac1{c_a-c_\ell}\right)\\
 &+\eta\Delta_\ell
 \sum_{m=\max(L,\ell+1)}^{D-\ell}
 (-1)^{m-\ell}h_m
       \frac{S_{\ell+m}S_{m-\ell-1}}
            {s_{2\ell+1}S_m^2}.
 \end{split}
 \tag{17}
\]
An inverted summation range is empty. These formulas retain
all tail signs, without assigning a universal sign to their
sum. Together with (5), (12), and (13), they compute the
whole expansion (8) at both parities and every \(N\ge2\).
For example, \(N=2\) has \(j=k=\ell=0\); (15)--(17)
give \(A_{00;0}=1,B_{00;0}=0\), as required.

## 4. Exact turns, canonical collisions, and closing scope

Let
\[
 \lambda_{n,\ell}=(-1)^{n\ell}q^{-n\ell(\ell+1)},\qquad
 \alpha_\ell=\frac{R'(c_\ell)}{R(c_\ell)}
            =\frac{i(D-2\ell)}{4\sin((2\ell+1)\theta)} .
 \tag{18}
\]
The original signed turn \(V_n=\kappa^nTR^{-n}T\) acts on
(8), for every \(n\in\mathbb Z\), by
\[
 (A_{jk;\ell},B_{jk;\ell})
 \longmapsto
 \lambda_{n,\ell}
       (A_{jk;\ell}-n\alpha_\ell B_{jk;\ell},B_{jk;\ell}),
 \tag{19}
\]
with only the scalar factor on the odd simple coefficient.
Thus the normal coefficients have the definite amplitudes
(12) and the original quadratic phases, while their Jordan
contribution to the value coefficients is also retained.

The same support mechanism extends to any finite product
\(P=\operatorname{can}\prod_{i=1}^rF_{j_i}\). Put
\(s=\sum_i j_i\). Repeated use of (4), including its zero
rule when two Newton indices sum to at least \(N\), gives
\[
 P=\sum_{a=0}^{\min(D,s)}u_a e_a,\qquad u_a>0.
 \tag{20}
\]
For strictness at a prescribed \(a\le\min(D,s)\), choose
input indices \(a_i\le j_i\) summing to \(a\), and choose
the top output at every multiplication. Each partial sum
is at most \(D\), so this path survives with positive weight.
No other term is negative. Outputs above \(s\) cannot occur.
This proves (20) even when the ordinary degree exceeds \(D\).
The canonical zero rule is an identity modulo the full
\(P_N\), so all paired normals survive this argument.

Replacing \(h_m\) by \(u_{D-m}\) in (9), (15), and (16)
therefore gives the same all-channel formula for \(P\), with
\[
 \operatorname{sign}B_\ell(P)=\eta
       \quad\hbox{exactly when }s+\ell\ge D .
 \tag{21}
\]
The bare original closing has the exact elementary consequence
\[
             \phi(P)=u_D>0\quad\Longleftrightarrow\quad s\ge D.
 \tag{22}
\]
This is a positivity statement for the specified product
without inserted multiplication crossings. It is also
unchanged by one outer \(V_n\), since \(\lambda_{n,0}=1\)
and the closing extracts only the normal coefficient at zero.
For a pair \(j,k\), it is nonzero only at odd levels with
\(j=k=J\), where it equals one by the odd simple Gram block.
Thus the newly present normal
sector at other nodes does not by itself yield a bare closing.

After a multiplication crossing, the actual observation is
the coherent sum from the confluent closing source, involving
all \(A_\ell-(n+\sigma)\alpha_\ell B_\ell\) and their
quadratic phases. Neither positivity in (12) nor (22)
establishes noncancellation of that sum, an asymptotic lower
bound, or a general fixed-short-filling theorem.

## Complete direct sources

All three complete direct texts were read and their used
implications checked at these pins:

* [Positive Newton multiplication](actual_positive_newton_multiplication.md),
  SHA256 543b5be6035ecec349ce8e78ee47085345ceefe4fc51e5f2005b802d999805bb:
  the prior positive factorial table, full canonical zero rule,
  and physical-row Newton coefficients.
* [Alternating physical-row linearization](research_physical_row_alternating_linearization.md),
  SHA256 326c55623da9155b6f5a0be4ab3e3b2584bdf7c568cd288d1e69569473c36342:
  row degrees, monic factorial normalization, and full normal basis.
* [Confluent row closing](research_confluent_row_closing_and_positive_quotient.md),
  SHA256 daf5760f74dbd9d9c9646a1a18b95cdffc1f42ebc3cbcfc0a1b9f79b2ad77251:
  the prior coordinate formula, original Jordan phases, and
  prescribed bare and crossed observations.

Only written proof, source reads, and metadata hashes were used.
No mathematical programs, tests, numerics, or builds were run.
Adopted notes and public manuscripts were not edited.
